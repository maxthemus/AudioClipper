import sounddevice as sd
import numpy as np
import sys



def audio_stream(callback, channels=2, samplerate=44100):
    stream = sd.InputStream(callback=callback, channels=channels, samplerate=samplerate)
    with stream:
        print("Streaming audio. Press Ctrl+C to stop.")
        running = True
        while running:
            sd.sleep(100)
                   

# Callback function to process audio data (you can customize this function)
def audio_callback(indata, frames, time, status):
    print(indata)
    if status:
        print(status)
    # Process the audio data as needed
    # For example, you can save it, analyze it, or perform real-time processing



print(sd.query_devices())

# Start the audio stream with the callback function
audio_stream(audio_callback)

print("DONE")
sys.exit()