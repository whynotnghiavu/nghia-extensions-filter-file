from pydub import AudioSegment


def MyNoSound(time, file):
    if time != 0:
        silence = AudioSegment.silent(duration=time*1000)
        silence.export(file, format="wav")
