from flask import Blueprint

from app.api.v1 import prompt, gpt_text

def create_v1():
    bp_v1 = Blueprint("v1", __name__)
    bp_v1.register_blueprint(prompt.prompt_api, url_prefix="/prompt")
    bp_v1.register_blueprint(gpt_text.gpt_text_api, url_prefix="/gpt_text")
    return bp_v1