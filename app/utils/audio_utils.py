import os
from pydub import AudioSegment

def convert_audio_to_wav(audio_file):
    audio = AudioSegment.from_file(audio_file)
    wav_file = os.path.splitext(audio_file)[0] + '.wav'
    audio.export(wav_file, format='wav')
    return wav_file
