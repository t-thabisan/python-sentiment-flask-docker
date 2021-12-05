from flask import Blueprint
from controller.sentimentController import sentiment_form, sentiment_sentence_check

# Blueprint definition
sentiment_bp = Blueprint('sentiment_bp', __name__)

# Routes definition
sentiment_bp.route('/', methods=['GET'])(sentiment_form)
sentiment_bp.route('/form', methods=['GET'])(sentiment_form)
sentiment_bp.route('/result', methods=['GET'])(sentiment_sentence_check)