from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import time
import pandas as pd
import googletrans

time.clock = time.time()

arquivo = pd.read_excel('chatbot.xlsx')

arquivo2 = arquivo.values.tolist()
conversa = list()
for lista in arquivo2:
    for pergunta in lista:
        conversa.append(pergunta)

chatbot = ChatBot("ArmanBot")

trainer = ListTrainer(chatbot)
trainer.train(conversa)

print(chatbot.get_response("oi"))