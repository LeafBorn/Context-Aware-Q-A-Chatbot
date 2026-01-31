import streamlit as st
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

#load the groq
load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
model = init_chat_model("groq:llama-3.1-8b-instant")

#streamlit UI
st.set_page_config(page_title="S E N S E I")
st.header("Hey, Let's Talk")



if 'flowmessages' not in st.session_state:
    st.session_state["flowmessages"] = [
        SystemMessage(
            content="You are assistant who explains concepts using jokes and simple example"
        )
    ]



def get_chatmodel_response(Question):

    st.session_state['flowmessages'].append(HumanMessage(content=Question))
    answer = model.invoke(st.session_state['flowmessages'])
    st.session_state['flowmessages'].append(AIMessage(content=answer.content))
    return answer.content

input = st.text_input("Your Question: ")

if st.button("Ask the question"):
    if input.strip() != "":
        response = get_chatmodel_response(input)
        st.subheader("Your answer is:")
        st.write(response)
    else:
        st.warning("Please enter a question first 😄")