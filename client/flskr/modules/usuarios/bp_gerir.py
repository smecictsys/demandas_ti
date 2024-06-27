from modules.autenticador import Autenticador
from modules.gplanilhas_man import GSheetManager
from modules.tools import auth_error
from flask import render_template, request, redirect, url_for, session
from datetime import datetime

from flask import Blueprint
auth = Autenticador()
bp_gerir = Blueprint('gerir', __name__, template_folder='templates', url_prefix='/gerir', static_folder='static')

@bp_gerir.route('/cadastro', methods=["GET"])
def cadastro_usuario():
    if 'user' in session:
        return render_template("cadastro_usuario.html")
    return auth_error()

@bp_gerir.route('/registrar_usuario', methods=["POST"])
def registrar_usuario():
    if 'user' in session:
        cliente_gspread = auth.obter_cliente()
        gsheetman = GSheetManager('controle_demandas', 'cadastros', cliente_gspread)
        nome = request.form['nome']
        sala = request.form['sala']

        dados = [nome, sala]
        res = gsheetman.inserir_dados(dados)
        if res:
            return redirect(url_for('usuarios.gerir.cadastro_usuario'))
    return auth_error()