import sys
import os
from tkinter import * 
import tkinter as tk
import imageio
import threading
import time
import subprocess
from PIL import ImageTk, Image
from pathlib import Path



dvideo_name = str(Path().absolute()) + '/samplefinal.mp4'
dvideo = imageio.get_reader(dvideo_name)
ddelay = int(1000 / dvideo.get_meta_data()['fps'])

bvideo_name = str(Path().absolute()) + '/bottlefinal.mp4'
bvideo = imageio.get_reader(bvideo_name)
bdelay = int(1000 / bvideo.get_meta_data()['fps'])


video_name1 = str(Path().absolute()) + '/../countfinal.mp4'
video1 = imageio.get_reader(video_name1)
delay1 = int(1000 / video1.get_meta_data()['fps'])

def stream(label):
    try:
      image = dvideo.get_next_data()
    except:
      dvideo.close()
      return
    label.after(ddelay, lambda: stream(label))
    frame_image = ImageTk.PhotoImage(Image.fromarray(image))
    label.config(image=frame_image)
    label.image = frame_image

def bstream(label):
    try:
      image = bvideo.get_next_data()
    except:
      bvideo.close()
      return
    label.after(bdelay, lambda: bstream(label))
    frame_image = ImageTk.PhotoImage(Image.fromarray(image))
    label.config(image=frame_image)
    label.image = frame_image


def stream1(label):
 
  try:
    image = video1.get_next_data()
  except:
    video1.close()
    return
  label.after(delay1, lambda: stream1(label))
  frame_image = ImageTk.PhotoImage(Image.fromarray(image))
  label.config(image=frame_image)
  label.image = frame_image


def ddrown():
    os.system('python drown_video.py -i samplefinal.mp4')

def bdrown():
    os.system('python drown_video.py -i bottlefinal.mp4')

def run():
    if(v.get() == 1):
      print("Sample")
      threading.Thread(target=ddrown).start()
    else:
      print("bottle")
      threading.Thread(target=bdrown).start()

def run1():
    threading.Thread(target=count).start()    

def count():
    os.system('python ss.py')
    os.system('python yolo_video.py --input data/frame1.jpg --output f1.mp4 --yolo yolo-coco')
   # ans=y.send()
    #my_label2= Label(top, text = str(ans)).place(x=1250, y=750)

def sel():
    print(v.get())
    if (v.get() == 1):
      print("you picked option1")      
      bmy_label.place_forget()
      dmy_label.place(x=30, y=220)
      dmy_label.after(ddelay, lambda: stream(dmy_label))
    else:
      print("you picked option2")
      dmy_label.place_forget()
      bmy_label.place(x=30, y=220)
      bmy_label.after(bdelay, lambda: bstream(bmy_label))
    



if __name__ == '__main__':
 
  top = Tk(className=" Real time drowning detector")
  top.geometry("1600x900")
  canvas = Canvas(top, width = 248, height = 165, borderwidth=0, bd=0, relief='ridge', highlightthickness = 0) 
  canvas.place(x=0, y=0)
  img = ImageTk.PhotoImage(Image.open("r3a.jpg"))     
  canvas.create_image(0,0, anchor=NW, image=img)

  canvas1 = Canvas(top, width = 250, height = 40, highlightthickness = 0) 
  canvas1.place(x=1300, y=5)
  img1 = ImageTk.PhotoImage(Image.open("change.jpeg"))     
  canvas1.create_image(0,0, anchor=NW, image=img1)

  canvas2 = Label(top, text = "Developed by Samskruthi and Poornachandra V sem Department of MCA RV College of Engineering Bengaluru") 
  canvas2.config(font=("Arial", 18), bg = "#66ccff", fg="#005c99")
  canvas2.place(x=150, y=700)
  
  top['background']='#66ccff'
  l1 = Label(top, text = "Real time drowning detection")
  l1.config(font=("Arial", 36), bg = "#005c99", fg="white")
  l1.place(x=440, y=30)

  dmy_label = Label(top, highlightthickness = 0, borderwidth=0)
  dmy_label.place(x=30, y=220)

  bmy_label = Label(top, highlightthickness = 0, borderwidth=0)
  bmy_label.place(x=30, y=220)

  dmy_label.after(ddelay, lambda: stream(dmy_label)) 
  btn = Button(top, text="Start Detection", bg="#005c99", fg="white",command=run, font=("Arial", 16)).place(x=250, y=600)

  my_label1 = Label(top, highlightthickness = 0, borderwidth=0)
  my_label1.place(x=850, y=220)
  my_label1.after(delay1, lambda: stream1(my_label1))
  btn1 = Button(top, text="Count", bg="#005c99", fg="white", command=run1, font=("Arial", 16)).place(x=1150, y=600)
  
  v = IntVar()
  r1 = Radiobutton(top, text="Camera 1", value=1, command=sel, variable=v, bg="#66ccff", fg="#005c99", font=("Arial", 12))
  r1.select()
  r1.place(x=720, y=220)
  r2 = Radiobutton(top, text="Camera 2", value=2, command=sel, variable=v, bg="#66ccff", fg="#005c99", font=("Arial", 12))
  r2.place(x=720, y=240)

  
  top.mainloop()