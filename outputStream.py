import sounddevice as sd
import numpy as np
import pygame
import sys
import tty
import termios


def audio_stream(callback, channels=2, samplerate=44100):
    stream = sd.InputStream(callback=callback, channels=channels, samplerate=samplerate)
    with stream:
        print("Streaming audio. Press Ctrl+C to stop.")
        running = True
        while running:
            sd.sleep(100)

            x = 0
            while x != chr(27): # ESC
                x=sys.stdin.read(1)[0]
                running = False
                print("You pressed", x)
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)              

# Callback function to process audio data (you can customize this function)
def audio_callback(indata, frames, time, status):
    print(indata)
    if status:
        print(status)
    # Process the audio data as needed
    # For example, you can save it, analyze it, or perform real-time processing

#INIT KEybaord
orig_settings = termios.tcgetattr(sys.stdin)
tty.setcbreak(sys.stdin)


# Start the audio stream with the callback function
audio_stream(audio_callback)

print("DONE")
sys.exit()