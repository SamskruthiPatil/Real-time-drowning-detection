import pyglet
import tkinter as tk 
from tkinter import messagebox 
import multiprocessing
from playsound import playsound



#music = pyglet.resource.media('')

player = pyglet.media.Player()
def pla():
  
  music.play()

  pyglet.app.run()

def pause():
  music.pause()


player.queue(pyglet.resource.media('alarm_2.mp3'))
def play1():
  
  player.play()
  pyglet.app.run()

def pause1():
  print("hi")
  player.pause()

  


if __name__ == "__main__":
    play1()
