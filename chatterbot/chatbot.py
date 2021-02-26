import logging
from py_imessage import imessage
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import UbuntuCorpusTrainer 
from chatterbot.trainers import TwitterTrainer

lillyphone = "13039292119"
andyiphone = "13032534350"
def main():
#    if not imessage.check_compatibility(andyiphone):
#        print("Not an Iphone, quitting chatbot")

    bot = ChatBot(name = 'Andy',
                  read_only = False,
                  logic_adapters = ['chatterbot.logic.BestMatch',
                                    'chatterbot.logic.MathematicalEvaluation'],
                  storage_adapter='chatterbot.storage.SQLStorageAdapter',
                  database_uri='sqlite:///database.sqlite3')

#        conversation = [
#    logging.basicConfig(level=logging.INFO)
    #bot = ChatBot('Example Bot')
#    trainer = UbuntuCorpusTrainer(chatbot)
#    trainer.train()
#    "Hello",
#    "Hi there!",
#    "How are you doing?",
#    "I'm doing great.",
#    "That is good to hear",
#    "Thank you.",
#    "You're welcome."
#    ]
    #trainer = ListTrainer(bot)
    #trainer.train(conversation)

    #ubuntu_trainer = UbuntuCorpusTrainer(bot)
    #ubuntu_trainer.train()
    corpus_trainer = ChatterBotCorpusTrainer(bot)
    corpus_trainer.train("chatterbot.corpus.english")

    run(bot)

#def readDataSet() -> list:
#    with open ('conversation.txt', 'r') as myfile:
#        conversation = myfile.readlines()
#    
#    for i in range(5):
#        print(conversation)
#        
#    return conversation

def run(bot):
    while(True):
        user_input = input()
        if (user_input == "q"):
            break
        elif(user_input == "\n"):
            continue
        response = bot.get_response(user_input)
        print(response)

if __name__ == "__main__":
    main()
