import librosa
import numpy as np

sound_effects = ["Static", "Engine", "Radio"]

def get_bpm(loaded_audio, sr):
    tempo = librosa.beat.beat_track(y=loaded_audio[0], sr=sr)
    if isinstance(tempo[0], np.ndarray):
        return tempo[0][0]
    else:
        tempo[0]

def energetic_music(value):
    return 1 if value >= 80 else 0

def sound_effect(row, col_list):
    total = sum(row[col] for col in col_list)
    return 1 if total > 0.0 else 0

def include_sound(row, col_list):
    return 1 if row[col_list].gt(0).any() else 0