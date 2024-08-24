import subprocess


def MyExecute(cmd):
    subprocess.Popen(cmd, shell=True).wait()
