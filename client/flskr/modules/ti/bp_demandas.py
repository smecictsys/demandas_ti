from modules.autenticador import Autenticador
from modules.gplanilhas_man import GSheetManager
from modules.msender import Msender
from modules.tools import compilar_dados, list_to_dict, list_format, auth_error
from flask import render_template, request, flash, redirect, url_for, session
from datetime import datetime

from flask import Blueprint
auth = Autenticador()
bp_demandas = Blueprint('demandas', __name__, template_folder='templates', url_prefix='/demandas', static_folder='static')

@bp_demandas.route('/listar_todas', methods=['GET'])
def listar_demandas():
    if 'user' in session:
        cliente_gspread = auth.obter_cliente()
        gsheetman = GSheetManager('controle_demandas', 'lancamento', cliente_gspread)
        lancamento_data = gsheetman.obter_dados()
        del lancamento_data[0]
        del lancamento_data[0]
        lancamento_data = list_to_dict(lancamento_data)
        lancamento_data.reverse()
        gsheetman.definir_pagina('colab')
        colab_data = gsheetman.obter_dados()
        del colab_data[0]
        hoje = datetime.now().strftime("%d/%m/%Y")
        return render_template('listar_demandas.html', data=lancamento_data, colab_data=colab_data, hoje=hoje)
    else:
        return auth_error()

@bp_demandas.route('/criar_demanda', methods=["GET"])
def criar_demanda():
    cliente_gspread = auth.obter_cliente()
    gsheetman = GSheetManager('controle_demandas', 'cadastros', cliente_gspread)
    dados = gsheetman.obter_dados()
    del dados[0]
    dados_compilados = compilar_dados(dados)
    return render_template("criar_demanda.html", dados=dados_compilados)

@bp_demandas.route('/registrar_demanda', methods=["POST"])
def registrar_demanda():
    cliente_gspread = auth.obter_cliente()
    gsheetman = GSheetManager('controle_demandas', 'lancamento', cliente_gspread)
    data_de_entrada = datetime.now().strftime("%d/%m/%Y")
    solicitante = request.form['nome'] + "/ " + request.form['sala']
    tipo = "Interna"
    direcionamento = "N/D"
    desc = request.form['descricao']
    status = "Nova demanda"

    novos_dados = [data_de_entrada, solicitante, tipo, direcionamento, desc, status]
    res = gsheetman.inserir_dados(novos_dados)
    if res:
        msender = Msender()
        gsheetman.definir_pagina('colab')
        colab_data = gsheetman.obter_dados()
        del colab_data[0]
        msender.setar_lista(colab_data)
        msender.setar_dados(list_format(novos_dados))
        msender.send_emails()
        flash('Demanda registrada. Atualize a pagina para enviar outra demanda.')
        return redirect(url_for('ti.demandas.criar_demanda'))
    
@bp_demandas.route('/buscar/<int:linha>')
def buscar_demanda(linha):
    cliente_gspread = auth.obter_cliente()
    gsheetman = GSheetManager('controle_demandas', 'lancamento', cliente_gspread)
    data = gsheetman.obter_dados()
    del data[0]
    del data[0]
    data = list_to_dict(data)
    for reg in data:
        if reg['id'] == linha:
            return render_template('demanda.html', reg=reg)