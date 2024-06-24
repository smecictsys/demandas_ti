from modules.autenticador import Autenticador
from modules.gplanilhas_man import GSheetManager
from flask import render_template, request, flash, redirect, url_for
from datetime import datetime

from flask import Blueprint
auth = Autenticador()
bp_demandas = Blueprint('demandas', __name__, template_folder='templates', url_prefix='/demandas', static_folder='static')

@bp_demandas.route('/criar_demanda', methods=["GET"])
def criar_demanda():
    cliente_gspread = auth.obter_cliente()
    gsheetman = GSheetManager('controle_demandas', 'cadastros', cliente_gspread)
    dados = gsheetman.obter_dados()
    
    del dados[0]
    return render_template("criar_demanda.html", dados=dados)

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
    print(novos_dados)
    res = gsheetman.inserir_dados(novos_dados)
    if res:
        flash('Demanda registrada. Atualize a pagina para enviar outra demanda.')
        return redirect(url_for('ti.demandas.criar_demanda'))