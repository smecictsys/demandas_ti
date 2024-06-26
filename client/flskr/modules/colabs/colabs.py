from flask import Blueprint, url_for, request, jsonify
from .bp_gerir import bp_gerir
import qrcode

bp_colabs = Blueprint('colabs', __name__, url_prefix='/colabs')

bp_colabs.register_blueprint(bp_gerir)

@bp_colabs.route('/gerar_qrcodes')
def criar_qrs():
    url = request.host_url + url_for('colabs.gerir.cadastro_colab')[1:]
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill="black", black_color="white")
    img.save("client/flskr/modules/colabs/static/images/qrcode_colabs_cadastro.png")
    return jsonify({
        'request_url':url
    })