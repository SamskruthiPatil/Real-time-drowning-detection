import pyglet
import tkinter as tk 
from tkinter import messagebox 

def pla():
  music = pyglet.resource.media('alert_signal.mp3')
  music.play()

  pyglet.app.run()
  


if __name__ == "__main__":
    pla()