import random
import time

import numpy as np
import pyaudio

# notes to frequencies

notes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'AA', 'BB', 'CC', 'DD', 'EE', 'FF', 'GG']
freqs = [220.00, 246.94, 261.63, 293.66, 329.63, 349.23, 392.00,
    440.00, 493.88, 523.25, 587.33, 659.26, 698.46, 783.99]

twinkle_twinkle = ['C', 'C', 'G', 'G', 'AA', 'AA', 'G',
                   'F', 'F', 'E', 'E', 'D', 'D', 'C',
                   'G', 'G', 'F', 'F', 'E', 'E', 'D',
                   'G', 'G', 'F', 'F', 'E', 'E', 'D',
                   'C', 'C', 'G', 'G', 'AA', 'AA', 'G',
                   'F', 'F', 'E', 'E', 'D', 'D', 'C']

mary_had_a_little_lamb = [
    'E', 'D', 'C', 'D', 'E', 'E', 'E',
    'D', 'D', 'D', 'E', 'G', 'G',
    'E', 'D', 'C', 'D', 'E', 'E', 'E',
    'E', 'D', 'D', 'E', 'D', 'C'
]

mario = ['E', 'E', 'E', 'C', 'E', 'G', 'GG', 'G', 
               'CC', 'G', 'E', 'A', 'AA', 'BB', 'B', 'A', 
               'G', 'E', 'G', 'C', 'D', 'E', 'E', 'D', 
               'C', 'G', 'C', 'G', 'E', 'A', 'A', 'B', 
               'B', 'A', 'G', 'E', 'G', 'C', 'D', 'E', 'E', 'D', 'C']

def modeSelect():
    melody = []
    while True:
        rifforno = input('Want to play a pre-programmed song?\nY to choose song, N to make your own:\n   ')
        if str.upper(rifforno) == 'Y':
            riffInput = int(input("Song options:\n 1. Mary Had a Little Lamb\n 2. Twinkle Twinkle Little Star \n 3. boring minor scale \n 4. Mario\nEnter song number: "))
            if riffInput == 1:
                melody = mary_had_a_little_lamb
                break
            elif riffInput == 2:
                melody = twinkle_twinkle
                break
            elif riffInput == 3:
                melody = notes
                break
            elif riffInput == 4:
                melody = mario
                break
        elif str.upper(rifforno) == 'N':
            melody = writeSong()
            break
        else:
            print("Invalid input. Try again.\n")
            continue

    return melody

def writeSong():
    melody = []
    allowedNotes = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'AA', 'BB', 'CC', 'DD', 'EE', 'FF', 'GG'}
    while True:
        note = str.upper(input("Add note to melody:\n "))
        if 1 <= len(note) <= 2 and note in allowedNotes:
            melody = melody + [note]
        elif note =='':
            break        
        else:
            print("Invalid input. Try again.\n")       
             
                    
    print("there are " + str(len(melody)) + " notes in this melody:")
    print(melody)
 
    note_to_freq = dict(zip(notes, freqs))
    #user_input_converted = [note_to_freq[note] for note in melody]

    user_note_to_freq = dict(zip(melody, [note_to_freq[note] for note in melody]))

    return user_note_to_freq

    return user_input_converted
    
def playMelody(melody):
    note_to_freq = dict(zip(notes, freqs))
    for note in melody:
        frequency = note_to_freq.get(note, 0.0)
        print(note)
        play_sine_wave(frequency, duration=.2)
        


def play_sine_wave(frequency, duration, volume=0.5):
    p = pyaudio.PyAudio()

    fs = 44100  # sampling rate, Hz, must be integer
    samples = np.sign(np.sin(2 * np.pi * np.arange(fs * duration) * frequency / fs)).astype(np.float32)
    output_bytes = (volume * samples).tobytes()

    stream = p.open(format=pyaudio.paFloat32, channels=1, rate=fs, output=True)

    stream.write(output_bytes)
   

    stream.stop_stream()
    stream.close()

    p.terminate()

#modeSelect()

if __name__ == "__main__":
    melody_to_play = modeSelect()
    playMelody(melody_to_play)
