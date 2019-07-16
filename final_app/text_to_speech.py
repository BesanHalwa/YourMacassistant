import os

def speak(text, delimeter='.'):
    # split the paragraph into sentences
    # or as according to the delimeter
    text = text.replace('\n','')
    text = text.replace('\t','')
    text = str(text).split(delimeter)

    for txt in text:
        txt = txt.rstrip()
        os.system("say " + txt)

    return 0
