from .Environment import Environment


class Checker:

    def __init__(self):
        self.env = Environment()
        self.played = False

    def wavWasPlayed(self):
        self.played = True

    def resetWav(self):
        self.played = False

    def reminder(self):
        if self.env.getTime().hour >= 17:
            self.env.playWavFile("file")
            self.wavWasPlayed()
        else:
            self.resetWav()



