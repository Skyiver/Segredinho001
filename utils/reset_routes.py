from flask import Blueprint, jsonify
from models import db

reset_bp = Blueprint('reset', __name__)

@reset_bp.route('/reseta', methods=['POST'])
def reset_sistema():
    try:
        db.drop_all()
        db.create_all()
        
        from models import Professor
        prof = Professor(nome="Professor Padrão", id=999)
        db.session.add(prof)
        db.session.commit()
        
        return jsonify({"status": "sistema resetado"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"erro": str(e)}), 500