import wave
from pydub import AudioSegment


def LayDoDaiFileWAV(file_path):
    # with wave.open(file_path, 'rb') as wav_file:
    #     params = wav_file.getparams()
    #     duration = float(params.nframes) / params.framerate
    #     return duration
    audio = AudioSegment.from_wav(file_path)
    duration = len(audio)
    duration_seconds = duration / 1000.0
    return duration_seconds
