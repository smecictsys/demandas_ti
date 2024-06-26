from modules.autenticador import Autenticador
from modules.gplanilhas_man import GSheetManager
from flask import render_template, request, flash, redirect, url_for
from datetime import datetime

from flask import Blueprint
auth = Autenticador()
bp_gerir = Blueprint('gerir', __name__, template_folder='templates', url_prefix='/gerir', static_folder='static')

@bp_gerir.route('/cadastro', methods=["GET"])
def cadastro_colab():
    return render_template("cadastro_colabs.html")

@bp_gerir.route('/registrar_colab', methods=["POST"])
def registrar_colab():
    cliente_gspread = auth.obter_cliente()
    gsheetman = GSheetManager('controle_demandas', 'colab', cliente_gspread)
    nome = request.form['nome']
    email = request.form['email']
    sala = request.form['sala']
    numero_demandas = 0

    dados = [nome, email, sala, numero_demandas]
    res = gsheetman.inserir_dados(dados)
    if res:
        return redirect(url_for('colabs.gerir.cadastro_colab'))