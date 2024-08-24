
def TinhGiay(time):
    return (time.hours * 3600) + (time.minutes * 60) + time.seconds + (time.milliseconds / 1000)
