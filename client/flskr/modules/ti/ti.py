from flask import Blueprint, url_for, request, jsonify
from .bp_demandas import bp_demandas
import qrcode

bp_ti = Blueprint('ti', __name__, url_prefix='/ti')

bp_ti.register_blueprint(bp_demandas)

@bp_ti.route('/gerar_qrcodes')
def criar_qrs():
    url = request.host_url + url_for('ti.demandas.criar_demanda')[1:]
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill="black", black_color="white")
    img.save("client/flskr/modules/ti/static/images/qrcode_demanda_ti.png")
    return jsonify({
        'request_url':url
    })