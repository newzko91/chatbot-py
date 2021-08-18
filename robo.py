# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, jsonify
import aiml
import os
import time

chatbot = Flask(__name__)

# Define rota para carregar a página web que está na pasta Templates
@chatbot.route("/")
def golive():
    return render_template('chat.html')

# Função criada para implementar uma parada na aplicação usando a nomenclatura em PT-BR
def sair():
    exit()

# Webhook - método que fica a espera de uma requisição do tipo POST
@chatbot.route("/atendimento", methods=['POST'])
def conversa():

    # Armazena o conteúdo do campo texto da mensagem, codificia e tira os espaços
    mensagem = request.form['messageText'].encode('utf-8').strip()

    ''' Declaração do objeto kernel de AIML que irá preparar o ambiente para 
        manipular as requisições e as mensagens '''
    kernel = aiml.Kernel()

    '''Laço que verifica se existe um arquivo "cérebro". Se existir ele é carregado com as
       linguagens armazenadas e caso não exista ele é criado e definido como "brainfile". 
       Esses arquivos permitem um carregamento mais veloz dos arquvios AIML sem a necessidade 
       de ter que 'aprender' a linguagem novamente.'''
    if os.path.isfile("adelaide.brn"):
        kernel.bootstrap(brainFile = "adelaide.brn")
    else:
        ''' Etapa que é carregado o XML que aponta para os arquivos da base de conhecimento
            em AIML. Note que no arquivo foi definiod uma frase para carregar esse aprendizado
            e que, no caso, é LOAD AIML B. '''
        kernel.bootstrap(
            learnFiles=os.path.abspath("aiml/std-vamosconversar.xml"),
            commands="load aiml b")
        # Em seguida esse conhecimento é armazenado no cérebro    
        kernel.saveBrain("adelaide.brn")


    # Prepara o kernel e o deixa pronto para receber as mensagens
    while True:
        resposta = kernel.respond(mensagem)

        '''' Imprime resposta do robô na tela, um atraso de 200 milésimo de segundo foi definido
        para apresentar "Adelaide está escrevendo..." na tela, simulando algo natural numa conversa
        com outros seres humanos, que é a espera para receber um retorno '''
        time.sleep(0.2)
        return jsonify({'status': 'OK', 'answer': resposta})

# Executa o aplicativo
if __name__ == "__main__":
    chatbot.run(debug=True)