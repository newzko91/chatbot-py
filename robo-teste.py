# -*- coding: utf-8 -*-
import aiml
import os

k = aiml.Kernel()

if os.path.isfile("brain/adelaide.brn"):
    k.bootstrap(brainFile="brain/adelaide.brn")
else:
    k.bootstrap(learnFiles=os.path.abspath("aiml/std-vamosconversar.xml"),
                     commands="load aiml b")
    k.saveBrain("brain/adelaide.brn")


def sair():
    exit()

while True:
    message = raw_input("Sua mensagem ao robô: ")
    if message == "tchau":
        sair()
    elif message == "lembre-se":
        k.saveBrain("brain/adelaide.brn")
    else:
        bot_response = k.respond(message)
        print bot_response