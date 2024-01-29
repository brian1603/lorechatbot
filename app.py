import os
from apikey import apikey

import streamlit as st
from langchain.llms import OpenAI

# make avaialle fto openai environment
os.environ['OPENAI_API_KEY'] = apikey

# app framework
st.title("lorebot")
prompt = st.text_input('Plug in your prompt here')