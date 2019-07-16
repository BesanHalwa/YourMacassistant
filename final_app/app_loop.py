import captioning
import face_recognition
import image_to_text
import play
import send_mail
import speech_to_text
import text_to_speech
import decode_command
import capture_image
import wiki_search
import face_recognisation

import os
import glob
import cv2
import numpy as np
import json
import requests
import smtplib

import wikipediaapi
import face_recognition
import speech_recognition as sr
import pygame
from pygame import mixer
from mutagen.mp3 import MP3
import time

def startloop():
    intro = "hello, I am June. I can help you in reading books, sending mail."
    intro2 = "I can recognise people for you, identify objects near you and describe the location you are in"
    intro3 = "I can perfom web search for your assistance, read out news to you and play music from library"
    intro4 = "how I may help you?"
    #os.system("say " + intro)
    #os.system("say " + intro2)
    #os.system("say " + intro3)
    os.system("say " + intro4)

    while True:
        command = speech_to_text.get_text()
        operation = decode_command.decode(command)

        if (operation == -1):
            os.system("say 'I don't recognise the operation. Soory.")
            continue

        perform(operation)


def perform(operation):
    if operation == 1:
        # read from camera
        capture_image.start()
        text = image_to_text.text_from_image('temp/captureCropped.jpg')
        print(text)
        text_to_speech.speak(text)

    elif operation == 2:
        # send mail
        os.system("say 'waht is the mail id'")
        sendto = speech_to_text.get_text()
        sendto = sendto.replace(" ", "")

        os.system("say 'waht is the subject of the mail?'")
        subject = speech_to_text.get_text()

        os.system("say 'waht should i write in the mail?'")
        mailtext = speech_to_text.get_text()

        send_mail.mail(sendto,subject,mailtext)

    elif operation == 3:
        # what am i looking at => object identification
        capture_image.capture()
        captioning.dense_cap('temp/capture.jpg')

    elif operation == 4:
        # where am I? scene captionong
        capture_image.capture()
        captioning.scene_cap('temp/capture.jpg')

    elif operation == 5:
        # Wikipedia search
        os.system("say 'waht should i search about on the web'")
        subject = speech_to_text.get_text()
        subject = subject.rstrip()
        article = wiki_search.get_article(subject)
        article = article.rstrip()
        text_to_speech.speak(article)

    elif operation == 6:
        # who is in the frame
        face_recognisation.recognise()

    elif operation == 7:
        play.playmp3()

    # TODO add news apikey
    else:
        "do nothing, return to app loop"
