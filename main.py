from chatbot import ChatBot
myChatBot = ChatBot()
#apenas carregar um modelo pronto
myChatBot.loadModel()

#criar o modelo
# myChatBot.createModel()




print("Bem vindo ao Chatbot")


pergunta = input("como posso te ajudar?\n")
resposta, intencao = myChatBot.chatbot_response(pergunta)
print(resposta + "   ["+intencao[0]['intent']+"]\n")


while (intencao[0]['intent']!="despedida"):
    pergunta = input("alguma dúvida?\n")
    resposta, intencao = myChatBot.chatbot_response(pergunta)
    print(resposta + "   [" + intencao[0]['intent'] + "]\n")

print("Foi um prazer atendê-lo")
