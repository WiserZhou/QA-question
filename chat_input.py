import streamlit as st
from src import init, produce_res
from langchain_core.messages import AIMessage, HumanMessage
# 对模型等进行初始化
init()
chat_history = []
# histroy 属性
if "history" not in st.session_state:
    st.session_state.history = []
for message in st.session_state.history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


with st.sidebar:
    st.markdown(':rose: :green[**检索内容：**] :rose:')
messages = st.container(height=300)

if prompt := st.chat_input("Say something"):
    with st.chat_message("user"):
        st.markdown(prompt)
    # response, material = get_response_material(prompt, st.session_state.history)
    # 使用左侧框，展示检索到的信息
    docs, response = produce_res(prompt, chat_history)
    chat_history.append(
        HumanMessage(content=prompt),
        AIMessage(content=response),
    )
    print(chat_history)
    with st.sidebar:
        st.markdown(':rose: :green[**检索内容：**] :rose:')
        st.text(docs)
    st.session_state.history.append({"role": "user", "content": prompt})

    # 在页面上显示回复
    response = response
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.history.append({"role": "assistant", "content": response})

    if len(st.session_state.history) > 20:
        st.session_state.messages = st.session_state.messages[-20:]

