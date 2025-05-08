from dotenv import load_dotenv
from openai import OpenAI
import streamlit as st

load_dotenv()

client = OpenAI()

st.title("welcome to Plan Emarat!")
initial_message=[
        {"role": "system", "content": "You are a trip planner in UAE.you are an expert in UAE tourism, locations, food, events, hotels, etc.you are able to guide users to plan their vacations to UAE.you should respond professionally.your name is Plan emarat. short name is PG.response shouldn't exceed 200 words.always ask questions to user and help them plan their trip.finally give a daywise itenerary."},
        {
            "role": "assistant",
            "content": "Hello, I am Plan Emarat, your expert trip planner. how can i help you?"
        }]
#function to get response from llm
def get_response_from_llm(messages):
    completion =client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )
    return completion.choices[0].message.content
#-----------------------------------------------
#initiallise with initial message      
if "messages" not in st.session_state:
    st.session_state.messages=initial_message
#display prev message i ui
for message in st.session_state.messages:
    if message["role"]!="system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
user_message=st.chat_input("enter your message") 
if user_message:
    new_message={
            "role": "user",
            "content": user_message
        }
    st.session_state.messages.append(new_message)
    with st.chat_message(new_message["role"]):
        st.markdown(new_message["content"])
        
        
    response = get_response_from_llm(st.session_state.messages)
    
    if response:
        response_message={
            "role": "assistant",
            "content": response
        }
        st.session_state.messages.append(response_message)
        with st.chat_message(response_message["role"]):
            st.markdown(response_message["content"])
