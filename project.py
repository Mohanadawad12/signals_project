from fileinput import filename
from tabnanny import filename_only
from numpy import true_divide
from playsound import playsound
import librosa
import matplotlib.pyplot as plt
import librosa.display
from IPython.display import Audio
import pedalboard
import matplotlib.pyplot as plt
from pedalboard import Pedalboard, Chorus, Reverb,Delay,Convolution,PitchShift
from pedalboard.io import AudioFile
from cProfile import label
from tkinter import *
from tokenize import Number
from tkinter import messagebox
import tkinter as tk


#######################################################################################################################
def delay():
  audio_path ='audio2.wav'
  playsound(audio_path)
  x , sr = librosa.load(audio_path)
  plt.figure(figsize=(14, 5))
  librosa.display.waveshow(x, sr=sr)
  plt.show()
  with AudioFile('audio2.wav', 'r') as f:
    audio = f.read(f.frames)
    samplerate = f.samplerate
    board = Pedalboard([  Delay(delay_seconds=1, mix=1.0)])
    effected = board(audio, samplerate)
    with AudioFile('processed2-output.wav', 'w', samplerate, effected.shape[0]) as f:
      f.write(effected)
  Audio(effected[:20 * sr], rate=sr)
  audio_path2='processed2-output.wav'
  y , sr = librosa.load(audio_path2)
  plt.subplot(2,1,1)
  librosa.display.waveshow(x, sr=sr)
  plt.title('before')
  plt.subplot(2,1,2)
  librosa.display.waveshow(y, sr=sr)
  plt.title('after')
  plt.tight_layout()
  plt.show()


def reverb():
  audio_path = 'audio2.wav'
  playsound(audio_path)
  x , sr = librosa.load(audio_path)
  plt.figure(figsize=(14, 5))
  librosa.display.waveshow(x, sr=sr)
  plt.show()
  with AudioFile('audio2.wav', 'r') as f:
    audio = f.read(f.frames)
    samplerate = f.samplerate
    board = Pedalboard([  Reverb(room_size=1)])
    effected = board(audio, samplerate)
    with AudioFile('processed2-output.wav', 'w', samplerate, effected.shape[0]) as f:
      f.write(effected)
    Audio(effected[:20 * sr], rate=sr)
    audio_path2='processed2-output.wav'
    y , sr = librosa.load(audio_path2)
    plt.subplot(2,1,1)
    librosa.display.waveshow(x, sr=sr)
    plt.title('before')
    plt.subplot(2,1,2)
    librosa.display.waveshow(y, sr=sr)
    plt.title('after')
    plt.tight_layout()
    plt.show()

def pitch_shift():
  audio_path = 'audio2.wav'
  playsound(audio_path)
  x , sr = librosa.load(audio_path)
  plt.figure(figsize=(14, 5))
  librosa.display.waveshow(x, sr=sr)
  plt.show()
  with AudioFile('audio2.wav', 'r') as f:
      audio = f.read(f.frames)
      samplerate = f.samplerate
      board = Pedalboard ([   PitchShift(semitones=22)])
      effected = board(audio, samplerate)
      with AudioFile('processed2-output.wav', 'w', samplerate, effected.shape[0]) as f:
       f.write(effected)
       Audio(effected[:20 * sr], rate=sr)
       audio_path2='processed2-output.wav'
      y , sr = librosa.load(audio_path2)
      plt.subplot(2,1,1)
      librosa.display.waveshow(x, sr=sr)
      plt.title('before')
      plt.subplot(2,1,2)
      librosa.display.waveshow(y, sr=sr)
      plt.title('after')
      plt.tight_layout()
      plt.show()


      
def convolution():
  audio_path = 'audio2.wav'
  playsound(audio_path)
  x , sr = librosa.load(audio_path)
  plt.figure(figsize=(14, 5))
  librosa.display.waveshow(x, sr=sr)
  plt.show()
  with AudioFile('audio2.wav', 'r') as f:
      audio = f.read(f.frames)
      samplerate = f.samplerate
      board = Pedalboard ([   Convolution("./guitar.wav", 1.0)])
      effected = board(audio, samplerate)
      with AudioFile('processed2-output.wav', 'w', samplerate, effected.shape[0]) as f:
       f.write(effected)
       Audio(effected[:20 * sr], rate=sr)
       audio_path2='processed2-output.wav'
      y , sr = librosa.load(audio_path2)
      plt.subplot(2,1,1)
      librosa.display.waveshow(x, sr=sr)
      plt.title('before')
      plt.subplot(2,1,2)
      librosa.display.waveshow(y, sr=sr)
      plt.title('after')
      plt.tight_layout()
      plt.show()
###########################################################################
def printtext():
  ans=True
  while ans:
    ans=string = entry1.get() 
    if ans=="1": 
      delay()
      tk.messagebox.showinfo(title="Done", message="the effected audio saved successfully", )

    elif ans=="2":
      reverb()
      tk.messagebox.showinfo(title="Done", message="the effected audio saved successfully", )

    elif ans=="3":
      
      convolution()
      tk.messagebox.showinfo(title="Done", message="the effected audio saved successfully", )

    elif ans=="4":
      pitch_shift()
      tk.messagebox.showinfo(title="Done", message="the effected audio saved successfully", )
  
    elif ans !="":
      messagebox.showerror("Error ", "Not Valid Choice Try again")

      break
       
####################################################################
root= Tk()
canvas1 = tk.Canvas(root, width = 400, height = 600)
root['bg']='#3EB489'
root.title("signal project")
root.minsize(400,600)
the_text=Label(text="Choose one effect from menu", height=3 , font=('helvetica', 16, 'bold') ,background=('#3EB489'), fg=("black"))
the_text.pack()
the_text=Label(text="1.Delay",height=2 ,background=('#3EB489'), font=('helvetica',16, 'bold'), fg=("black") )
the_text.pack()
the_text=Label(text="2.Reverb", height=2 , font=('helvetica', 16, 'bold') ,background=('#3EB489'),fg=("black"))
the_text.pack()
the_text.pack()
the_text=Label(text="3.Convolution", height=2 , font=('helvetica', 16, 'bold') ,background=('#3EB489'),fg=("black"))
the_text.pack()
the_text=Label(text="4.Pitch shift", height=2 , font=('helvetica',16, 'bold'),background=('#3EB489'), fg=("black"))
the_text.pack()
#the_text=Label(text="For Exit Choose 5", height=5 , font=('helvetica', 16, 'bold'),background=('#3EB489'), fg=("black"))
#the_text.pack()
canvas1['bg']='#3EB489'
entry1 = tk.Entry (root) 
entry1.pack()
entry1.focus_set()
button1 = tk.Button(text='Enter the choice ', command=printtext, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
button1.pack()
root.mainloop()
