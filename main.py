# make a simple mp3 player using pygame and tkinter

import os
import tkinter as tk
from tkinter import filedialog
import pygame

# initialize pygame mixer
pygame.mixer.init()

# create tkinter window
root = tk.Tk()
root.minsize(300, 300)

# function for adding music
def addMusic():
    directory = filedialog.askdirectory()
    os.chdir(directory)

    songList = os.listdir()
    for song in songList:
        pygame.mixer.music.load(song)
        pygame.mixer.music.play()

# button for adding music
addBtn = tk.Button(root, text = "Add Music", command = addMusic)
addBtn.pack(pady = 10)

# function for playing music
def playMusic():
    pygame.mixer.music.unpause()

# button for playing music
playBtn = tk.Button(root, text = "Play Music", command = playMusic)
playBtn.pack(pady = 10)

# function for pausing music
def pauseMusic():
    pygame.mixer.music.pause()

# button for pausing music
pauseBtn = tk.Button(root, text = "Pause Music", command = pauseMusic)
pauseBtn.pack(pady = 10)

# function for stopping music
def stopMusic():
    pygame.mixer.music.stop()

# button for stopping music
stopBtn = tk.Button(root, text = "Stop Music", command = stopMusic)
stopBtn.pack(pady = 10)

# function for exiting program
def exitMusic():
    pygame.mixer.music.stop()
    root.destroy()

# button for exiting program
exitBtn = tk.Button(root, text = "Exit Music", command = exitMusic)
exitBtn.pack(pady = 10)

# run tkinter window's mainloop
root.mainloop()

# Path: main.py
# make a simple mp3 player using pygame and tkinter