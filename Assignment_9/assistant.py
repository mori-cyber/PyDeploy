# !pip install -q -U langchain langchain_core langchain_groq gradio

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
# import gradio as gr

groq_api_key = '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'


def fetch_response(user_input):
  chat = ChatGroq(
    api_key = groq_api_key,
    model_name = "mixtral-8x7b-32768"
  )
  system = "You are a helpful assistant."
  human = "{text}"

  prompt = ChatPromptTemplate.from_messages(
      [
          ("system", system), ("human", human)
      ]
  )
  chain = prompt | chat | StrOutputParser()
  output = chain.invoke({"text": user_input})
  return output

