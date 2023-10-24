from dotenv import load_dotenv
import os
import streamlit as st
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate
from langchain.prompts import PromptTemplate 
from langchain.memory import ConversationBufferWindowMemory
import openai
from langchain import PromptTemplate
from langchain import FewShotPromptTemplate
from langchain.prompts.example_selector import LengthBasedExampleSelector
import random
from langchain.chat_models import ChatOpenAI
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
llm = OpenAI(model_name="gpt-3.5-turbo-16k-0613",openai_api_key=openai.api_key,temperature=1)
# f = open('ppython.txt','r')
# k=""
# with open('ppython.txt') as f:
#     contents = f.read()
#     k=k+contents
lis=['os','dbms','python','c','social network analysis','networks','deeplearning','machinelearning']
kk=random.randint(0, 7)
kf=lis[kk]

print(kf)

prompt = """generate only one interview questions on the topic {kfa} 

Answer: """
prompt_template = PromptTemplate(
    input_variables=["kfa"],
    template=prompt
)
if st.button('generate question on different topics in random oder'):
    for i in range(0,30):
        if i<8:
            kf=lis[i]
            st.write(llm(prompt_template.format(kfa=kf)))
        else:
            kk=random.randint(0, 7)
            kf=lis[kk]
            st.write(llm(prompt_template.format(kfa=kf)))

