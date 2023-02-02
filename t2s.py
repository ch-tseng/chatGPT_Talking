#coding=utf-8  
from libT2S import T2S
import openai
import os, random

model_engine = "text-davinci-003"
openai.api_key = "xxxxxxxxx"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="chatGPT.json"

gt2s = T2S()
persons = ['cmn-TW-Wavenet-A', 'cmn-TW-Wavenet-B', 'cmn-TW-Wavenet-C']
id_person = random.randint(0,2)
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
