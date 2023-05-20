from flask import Blueprint, request
from app.handler.chatbot.langchain_api import LangChainGPTBot

gpt_text_api = Blueprint("gpt_text", __name__)

@gpt_text_api.route('/normal_gpt', methods=['POST'])
def get_gpt_reply():
    print("start gpt reply test 1")
    # print(request.data)
    # print(request.json)
    req_json = request.json
    # print("req_json", req_json)
    gpt_reply_text = "no reply"
    gpt_bot = LangChainGPTBot()
    query = req_json["query"]
    print("gpt query:\t{}".format(query))
    gpt_reply_text = gpt_bot.reply(query=query)
    return {
        'msg': gpt_reply_text
    }
