#coding=utf-8  

import openai
import os
from configparser import ConfigParser
import ast

cfg = ConfigParser()
cfg.read("config.ini",encoding="utf-8")

model_engine = cfg.get("OpenAI", "model_engine")
openai.api_key = cfg.get("OpenAI", "API")
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=cfg.get("Google", "GOOGLE_APPLICATION_CREDENTIALS_PATH").replace('\\','/')

#---------------------------------
def GPT(query):
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=query,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    response = completion.choices[0].text
    with open('history_t2t.txt', 'a', encoding='UTF-8') as f:
        f.write('\n' + query + '\n' + response + '\n ----------------------------------------------- \n')

    return response

# Specify you exit condition
exit_conditions = (":q", "quit", "exit")


while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        rtn_txt = GPT(query)
        print ("ChatGPT: %s " % (rtn_txt))
