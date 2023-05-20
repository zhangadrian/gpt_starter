from flask import Blueprint
from app.api.v1.model.prompt import Prompt

prompt_api = Blueprint("prompt", __name__)

@prompt_api.route('/get_normal', methods=['GET'])
def get_normal():
    return {
        'msg': 'You are a kind helpful assistant'
    }
