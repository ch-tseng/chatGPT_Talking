#coding=utf-8  
from libT2S import T2S
import openai
import os, random
from configparser import ConfigParser
import ast

cfg = ConfigParser()
cfg.read("config.ini",encoding="utf-8")

model_engine = cfg.get("OpenAI", "model_engine")
openai.api_key = cfg.get("OpenAI", "API")
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=cfg.get("Google", "GOOGLE_APPLICATION_CREDENTIALS_PATH").replace('\\','/')

gt2s = T2S()
persons = ast.literal_eval(cfg.get("Google", "voices"))
id_person = random.randint(0,len(persons)-1)
language_audio = persons[id_person]

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
        gt2s.speak(rtn_txt, language_audio)
        
        with open('history_t2s.txt', 'a', encoding='UTF-8') as f:
            f.write('\n' + query + '\n' + rtn_txt + '\n ----------------------------------------------- \n')
