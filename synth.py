import numpy as np
import sounddevice as sd

class Synth:
    def __init__(self):
        self.sample_rate = 44100
        self.notes = [
            261.63, 277.18, 293.66, 311.13, 329.63,
            349.23, 369.99, 392.00, 415.30, 440.00,
            466.16, 493.88, 523.25, 554.37, 587.33, 622.25
        ]
        self.stream = sd.OutputStream(callback=self.audio_callback, samplerate=self.sample_rate, channels=1)
        self.stream.start()
        self.current_freq = 0
        self.phase = 0
        self.amplitude = 0.5

    def play(self, index):
        self.current_freq = self.notes[index]

    def stop(self):
        self.current_freq = 0

    def audio_callback(self, outdata, frames, time, status):
        t = (self.phase + np.arange(frames)) / self.sample_rate
        t = t.reshape(-1, 1)
        outdata[:] = self.amplitude * np.sin(2 * np.pi * self.current_freq * t)
        self.phase += frames
