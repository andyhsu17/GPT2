import logging
import os

def GetListOfTexts():
    output = []
    
    for root, dirs, files in os.walk("backup"):
        path = root.split(os.sep)
        for fil in files:
            if fil.endswith(".txt"):
                fullpath = os.path.join(root, fil)
                with open(fullpath, 'r') as myfile:
                    conversation = myfile.readlines()
                
                for line in conversation:
                    words = line.split()
                    for word in words:
                        if word == "Friend:" or word == "Me:":
                            words.remove(word)
                    sentence = ' '.join(words)
                    newsent = ""
                    for c in sentence:
                        if c.isalnum() or c == " " or c == "." or c == ',' or c == '!' or c == '/':
                            newsent += c
                    output.append(newsent)
                for message in output:
                    if not message or message.startswith('http'):
                        output.remove(message)
    return output
