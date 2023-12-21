import sounddevice as sd
import numpy as np
import sys

#print(sd.query_devices())
sample_rate = 44100
channels = 2
duration = 5  # in seconds

def audio_stream(callback, channels=2, samplerate=44100):
    stream = sd.InputStream(callback=callback, channels=channels, samplerate=samplerate)
    with stream:
        print("Streaming audio. Press Ctrl+C to stop.")
        running = True
        while running:
            sd.sleep(100)
                   

# Callback function to process audio data (you can customize this function)
def audio_callback(indata, frames, time, status):
    global audio_data
    if status:
        print(status)
    # Process the audio data as needed
    # For example, you can save it, analyze it, or perform real-time processing



print(sd.query_devices())

# Start the audio stream with the callback function
asyncio.run(audio_stream(audio_callback))



print("PLAY BACK")
value = input("TEST")
sd.default.device = "default"
sd.play(audio_data, sample_rate)
sd.wait()


sys.exit()

#https://www.reddit.com/r/Ubuntu/comments/se4vl7/pulseaudio_audio_output_to_send_virtual/