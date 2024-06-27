from modules.autenticador import Autenticador
from modules.gplanilhas_man import GSheetManager
from modules.tools import hash_do_token, checar_token, colab_format, auth_error
from flask import render_template, request, flash, redirect, url_for, session
from datetime import datetime

from flask import Blueprint
auth = Autenticador()
bp_gerir = Blueprint('gerir', __name__, template_folder='templates', url_prefix='/gerir', static_folder='static')

@bp_gerir.route('/cadastro', methods=["GET"])
def cadastro_colab():
    if 'user' in session:
        return render_template("cadastro_colabs.html")
    return auth_error()

@bp_gerir.route('/registrar_colab', methods=["POST"])
def registrar_colab():
    if 'user' in session:
        hoje = datetime.now().strftime("%d/%m/%Y")
        cliente_gspread = auth.obter_cliente()
        gsheetman = GSheetManager('controle_demandas', 'colab', cliente_gspread)
        nome = request.form['nome']
        email = request.form['email']
        sala = request.form['sala']
        numero_demandas = 0
        token = str(hash_do_token(sala + nome))

        dados = [hoje, nome, email, sala, numero_demandas, token]
        res = gsheetman.inserir_dados(dados)
        if res:
            return redirect(url_for('colabs.gerir.cadastro_colab'))
    return auth_error()
    
@bp_gerir.route('/login', methods=['GET'])
def login_colab():
    return render_template('login.html')

@bp_gerir.route('/autenticar', methods=['POST'])
def auth_colab():
    cliente_gspread = auth.obter_cliente()
    gsheetman = GSheetManager('controle_demandas', 'colab', cliente_gspread)
    usuario = request.form['usuario']
    senha = request.form['senha']

    res = None
    data = gsheetman.obter_dados()
    del data[0]
    for item in data:
        usuario_check = item[1]
        if usuario_check == usuario:
            byte = eval(item[5])
            res = checar_token(byte, senha)
            if res:
                user = colab_format(item)
                session['user'] = user
                return redirect(url_for('ti.ti_menu'))
            else:
                flash('Senha inválida')
                return redirect(url_for('colabs.gerir.login_colab'))
        else:
            flash('Usuário inválido')
            return redirect(url_for('colabs.gerir.login_colab'))
        
@bp_gerir.route('/logout', methods=['GET'])
def logout_colab():
    if 'user' in session:
        session.pop('user', None)
        return redirect(url_for('colabs.gerir.login_colab'))
    return auth_error()