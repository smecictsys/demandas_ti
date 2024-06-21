from modules.autenticador import Autenticador
from flskr.create_app import create_app
from flask import render_template, request, flash, redirect, url_for
import qrcode

auth = Autenticador()
demandas_app = create_app()

@demandas_app.route('/criar_demanda', methods=["GET"])
def criar_demanda():
    url = "http://http://192.168.100.111:5000/criar_demanda"
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill="black", black_color="white")
    img.save("client/flskr/static/images/qrcode.png")
    return render_template("criar_demanda.html")

@demandas_app.route('/registrar_demanda', methods=["POST"])
def registrar_demanda():
    nome = request.form['nome']
    sala = request.form['sala']
    desc = request.form['descricao']
    tipo = "demanda do novo formulário"

    novos_dados = [nome, sala, desc, tipo]
    res = auth.inserir_dados(novos_dados)
    if res:
        flash('Demanda registrada. Atualize a pagina para enviar outra demanda.')
        return redirect(url_for('criar_demanda'))