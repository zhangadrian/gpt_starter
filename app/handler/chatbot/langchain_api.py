from flask import current_app, request
from app.common.log import logger
import app.proto.gpt_pb2 as gpt_proto
# from app.util.redis import Redis


# langchain引入的package 为了方便以后迁移 先集中写在一起
from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain, ConversationChain
from langchain.schema import messages_from_dict, messages_to_dict
from langchain.memory.chat_memory import ChatMessageHistory
from langchain.memory.chat_message_histories import RedisChatMessageHistory
from langchain.chains.conversation.memory import (ConversationBufferMemory, 
                                                  ConversationSummaryMemory, 
                                                  ConversationBufferWindowMemory,
                                                  ConversationKGMemory)
from langchain.callbacks import get_openai_callback

# 使用langchain构建bot
class LangChainGPTBot():
    def __init__(self):
        logger.debug("[{}] start init".format(self.__class__.__name__)) 
        super().__init__()
        self.openai_api_key = current_app.config.get("OPENAI_KEY", "")
        self.llm = ChatOpenAI(temperature=0, openai_api_key=self.openai_api_key, model_name='gpt-3.5-turbo')
        template = """You are a chatbot having a conversation with a human.

        {chat_history}
        Human: {human_input}
        Chatbot:"""

        prompt = PromptTemplate(
            input_variables=["chat_history", "human_input"], 
            template=template
        )
        message_history = RedisChatMessageHistory(url='redis://redis:6379/0', ttl=600, session_id='my-session')
        self.memory = ConversationBufferMemory(memory_key="chat_history", chat_memory=message_history)
        self.conversation_buf = LLMChain(llm=self.llm, prompt=prompt, verbose=False, memory=self.memory)
        
    def reply(self, query, context=None):
        logger.debug("[{}] start reply".format(self.__class__.__name__)) 
        if not context:
            # gpt_resp = self.normal_reply(query)
            gpt_resp = self.gpt_text(query)
            logger.info("[{}] reply_cont={}, completion_tokens={}".format(self.__class__.__name__, gpt_resp.reply, gpt_resp.token_count))
            return gpt_resp.reply
        else:
            logger.debug("[{}] here is context".format(self.__class__.__name__))

        
    def gpt_text(self, query) -> dict:
        gpt_resp = self.count_tokens(query)
        history = self.memory.chat_memory
        dicts = messages_to_dict(history.messages)
        logger.info("[{}] current history: {}".format(self.__class__.__name__, dicts))
        return gpt_resp
    
    def count_tokens(self, query):
        gpt_resp = gpt_proto.GPTResponse()
        with get_openai_callback() as cb:
            prompt = self.gen_prompt(query)
            # reply = self.conversation_buf.run(prompt)
            reply = self.conversation_buf.predict(human_input=prompt)
            logger.info("[{}] Spent a total of {} tokens".format(self.__class__.__name__, cb.total_tokens))

            gpt_resp.prompt = prompt
            gpt_resp.reply = reply
            gpt_resp.token_count = cb.total_tokens 
            return gpt_resp
    
    def normal_reply(self, query):
        gpt_resp = gpt_proto.GPTResponse()
        prompt = self.gen_prompt(query)
        reply = self.conversation_buf.predict(human_input=prompt)
        logger.info("[{}] the type of reply {}".format(self.__class__.__name__, type(reply)))

        gpt_resp.prompt = prompt
        gpt_resp.reply = reply 
        return gpt_resp
            
    
    def gen_prompt(self, query):
        return query

