import os

from .vector_base import MyPinecone
import pandas as pd
from langchain_core.prompts import ChatPromptTemplate
from operator import itemgetter
from langchain_core.output_parsers import StrOutputParser
from .baichuan2 import Baichuan2_LLM
import time
from langchain_core.messages import AIMessage, HumanMessage
# completion llm
pc = None


def init():
    global pc
    global model
    global chain
    print(os.getcwd())
    pc = MyPinecone("99cad44f-fb02-480d-9c18-76c938c44578", "test", "BAAI/bge-large-zh-v1.5", "text")
    model = Baichuan2_LLM("model")

    template = """你是一个小导游，请基于下面给出的背景用你自己的话来回答用户问题:
    背景：
    {context}
    
    历史记录：
    {chat_history}
    
    问题: 
    {question}
    
    历史记录是你之前与用户的交流，请在回答的时候考虑进去，不要重复回答。请只针对问题'{question}',用中文回答,背景并不一定都与问题相关，不相关的请忽视,回答时请注意句子与句子之间的衔接。
    """
    prompt = ChatPromptTemplate.from_template(template)
    question = '介绍一下恩江古城？'
    chain = (
        {
            "context": itemgetter("context"),
            "chat_history": itemgetter("chat_history"),
            "question": itemgetter("question"),
        }
        | prompt
        | model
        | StrOutputParser()
    )
def produce_res(question, chat_history):
    global pc
    docs = pc.get_similarity(question, 6)
    history = []
    print(question)
    print(chat_history)
    len_history = len(chat_history)
    for turn in range(0, len_history, 2):
        history.append(HumanMessage(content=chat_history[turn]))
        history.append(AIMessage(content=chat_history[turn + 1]))
    print("history=")
    print(history)
    response = chain.invoke({"context": docs, "question": question, "chat_history": history})
    chat_history.append((question, response))
    return response
# def produce_res(question, chat_history):
#     global pc
#     docs = pc.get_similarity(question, 6)
#     response = chain.invoke({"context": docs, "question": question, "chat_history": chat_history})
#     return response

def test():
    responses = []
    with open("test.txt", "r", encoding="utf-8") as f:
        for line in f:
            question = line.strip()
            docs = pc.get_similarity(question, 6)
            print(docs)
            time1 = time.time()
            # response, history = model.chat(tokenizer, question, history=[])
            response = chain.invoke({"context": docs, "question": question, "chat_history": chat_history})
            time2 = time.time()
            print(f'花费了 {time2 - time1} s')
            print(question)
            print(response)
            responses.append(response)
    dout = pd.DataFrame(responses)
    with pd.ExcelWriter('../src0/3.xlsx') as writer:
        print("start to write……")
        dout.to_excel(writer, sheet_name='Sheet2', index=False)

