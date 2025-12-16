from litellm import completion
from typing import List,Dict
import os

def call_llm(model:str,temperature:float,messages:List[Dict],**kwargs):
    """calls the llm on the messages generated"""
    response = completion(model=model,
               messages=messages,
               temperature=temperature,
               api_key=os.getenv("OPENAI_API_KEY"))
    return response 
    