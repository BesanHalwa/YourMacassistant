import pygame
from pygame import mixer
from mutagen.mp3 import MP3
import time
import glob
import os

def play_mp3():
    files = []
    for file in glob.iglob("music_lib/*.mp3"):
        files.append(file)
    files.sort()

    for file in files:
        print(file)


    for file in files:
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()

        # get track length in seconds
        weight_time = MP3(file).info.length

        print("playing file", file)
        print(weight_time)


        # weight for the file to play
        time.sleep(weight_time)
