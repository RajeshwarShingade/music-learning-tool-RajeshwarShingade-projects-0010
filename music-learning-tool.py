import tkinter as tk
from tkinter import ttk
import numpy as np
import simpleaudio as sa

# -----------------------------
# Musical Notes & Frequencies
# -----------------------------
notes_freq = {
    'C': 261, 'D': 294, 'E': 329, 'F': 349, 'G': 392, 'A': 440, 'B': 494
}

# Tips for beginners
tips = {
    'C': 'Start with your thumb on C.',
    'D': 'Use your index finger for D.',
    'E': 'Middle finger for E.',
    'F': 'Ring finger for F.',
    'G': 'Little finger for G.',
    'A': 'Thumb on A for next octave.',
    'B': 'Index finger for B.'
}

# Instruments - waveform multipliers for simple effect
instruments = {
    'Piano': 1,
    'Guitar': 0.7,
    'Flute': 0.5
}

current_instrument = 'Piano'

# -----------------------------
# Function to play note
# -----------------------------
def play_note(note):
    frequency = notes_freq[note] * instruments[current_instrument]
    duration = 0.5
    fs = 44100
    t = np.linspace(0, duration, int(fs * duration), False)
    wave = np.sin(frequency * t * 2 * np.pi)
    audio = wave * (2**15 - 1) / np.max(np.abs(wave))
    audio = audio.astype(np.int16)
    sa.play_buffer(audio, 1, 2, fs).wait_done()
    status_label.config(text=f"🎵 Playing {note} - Tip: {tips[note]}")

# -----------------------------
# Change Instrument
# -----------------------------
def change_instrument(event):
    global current_instrument
    current_instrument = instrument_combo.get()
    status_label.config(text=f"🎶 Instrument set to: {current_instrument}")

# -----------------------------
# GUI Setup
# -----------------------------
root = tk.Tk()
root.title("🎵 Music Learning App for Beginners 🎵")
root.geometry("600x400")

# Instrument selection
tk.Label(root, text="Select Instrument:", font=("Arial", 12)).pack(pady=10)
instrument_combo = ttk.Combobox(root, values=list(instruments.keys()))
instrument_combo.current(0)
instrument_combo.bind("<<ComboboxSelected>>", change_instrument)
instrument_combo.pack()

# Piano keys (note buttons)
frame_keys = tk.Frame(root)
frame_keys.pack(pady=20)

for note in notes_freq.keys():
    btn = tk.Button(frame_keys, text=note, width=6, height=3,
                    command=lambda n=note: play_note(n))
    btn.pack(side=tk.LEFT, padx=5)

# Status Label
status_label = tk.Label(root, text="Select an instrument and play notes!", font=("Arial", 12))
status_label.pack(pady=20)

# -----------------------------
# Preloaded Song Button
# -----------------------------
twinkle_twinkle = ['C', 'C', 'G', 'G', 'A', 'A', 'G',
                   'F', 'F', 'E', 'E', 'D', 'D', 'C']

def play_song():
    status_label.config(text="🎵 Playing 'Twinkle Twinkle Little Star' 🎵")
    root.update()
    for note in twinkle_twinkle:
        play_note(note)
        root.update()
    status_label.config(text="Song finished! Try playing it yourself!")

tk.Button(root, text="Play Twinkle Twinkle", command=play_song).pack(pady=10)

# -----------------------------
# Run GUI
# -----------------------------
root.mainloop()




#created by Mr.Rajeshwar Shingade
#GitHub : https://github.com/RajeshwarShingade
#LinkedIn : https://www.linkedin.com/in/rajeshwarshingade
#telegram : https://t.me/rajeshwarshingade



#Happy Coding
#© All Rights Reserved