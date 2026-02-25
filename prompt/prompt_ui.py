import streamlit as st
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import load_prompt

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.3-70B-Instruct",
    task="text-generation",
)
model = ChatHuggingFace(llm=llm)

template = load_prompt("template.json")

st.header("Research Tool")

user_input = st.text_input("Enter topic to get summary")


if st.button("Send"):
    chain = template | model
    result = chain.invoke({
    "topic":user_input
    })
    st.text(result.content)