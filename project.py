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

def delay():
  audio_path = 'audio2.wav'
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
  plt.figure(figsize=(14, 5))
  librosa.display.waveshow(y, sr=sr)
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
  board = Pedalboard([Reverb(room_size=0.25)])
  effected = board(audio, samplerate)
  with AudioFile('processed2-output.wav', 'w', samplerate, effected.shape[0]) as f:
    f.write(effected)
  Audio(effected[:20 * sr], rate=sr)
  audio_path2='processed2-output.wav'
  y , sr = librosa.load(audio_path2)
  plt.figure(figsize=(14, 5))
  librosa.display.waveshow(y, sr=sr)
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
      board = Pedalboard ([   PitchShift(semitones=12)])
      effected = board(audio, samplerate)
      with AudioFile('processed2-output.wav', 'w', samplerate, effected.shape[0]) as f:
       f.write(effected)
       Audio(effected[:20 * sr], rate=sr)
       audio_path2='processed2-output.wav'
      y , sr = librosa.load(audio_path2)
      plt.figure(figsize=(14, 5))
      librosa.display.waveshow(y, sr=sr)
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
      plt.figure(figsize=(14, 5))
      librosa.display.waveshow(y, sr=sr)
      plt.show()

###################################################

  #audio_path = 'audio2.wav'
  #playsound(audio_path)
 # x , sr = librosa.load(audio_path)
 # plt.figure(figsize=(14, 5))
 # librosa.display.waveshow(x, sr=sr)
  #plt.show()
ans=True
while ans:
    print ("""
    1.delay
    2.reverb
    3.convolution
    4.pitch_shift
    5.exit
    """)
    ans=input("What would you like to do? ") 
    if ans=="1": 
      delay()
    elif ans=="2":
      reverb()
    elif ans=="3":
      convolution()
    elif ans=="4":
      pitch_shift()
    elif ans=="5":
     print("\n Goodbye")
     break
    elif ans !="":
      print("\n Not Valid Choice Try again") 




      

########################################################
#another fun.
#Make a Pedalboard object, containing multiple plugins:
#board = Pedalboard([Chorus(), Reverb(room_size=0.25)])
#delay_longer_and_more_pitch_shift = Pedalboard([
 # Delay(delay_seconds=0.5, mix=1.0),
 # PitchShift(semitones=12),
  #Gain(gain_db=-6)]}

  #Convolution("./guitar.wav", 1.0),

##########################################################
# Run the audio through this pedalboard!
#effected = board(audio, samplerate)
# Write the audio back as a wav file:
#with AudioFile('processed2-output.wav', 'w', samplerate, effected.shape[0]) as f:
 # f.write(effected)
 # Audio(effected[:20 * sr], rate=sr)
  #audio_path2='processed2-output.wav'
#y , sr = librosa.load(audio_path2)
#plt.figure(figsize=(14, 5))
#librosa.display.waveshow(y, sr=sr)
#plt.show()


 