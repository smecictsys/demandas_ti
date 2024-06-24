from flask import Blueprint, url_for, request, jsonify
from .bp_gerir import bp_gerir
import qrcode

bp_usuarios = Blueprint('usuarios', __name__, url_prefix='/usuarios')

bp_usuarios.register_blueprint(bp_gerir)

@bp_usuarios.route('/gerar_qrcodes')
def criar_qrs():
    url = request.host_url + url_for('usuarios.gerir.cadastro')[1:]
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill="black", black_color="white")
    img.save("client/flskr/modules/ti/static/images/qrcode_usuarios.png")
    return jsonify({
        'request_url':url
    })