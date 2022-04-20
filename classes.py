class Television:
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self):
        self.channel = Television.MIN_CHANNEL
        self.volume = Television.MIN_VOLUME
        self.tv_power = False

    def power(self):
        if self.tv_power == False:
            self.tv_power = True
        elif self.tv_power == True:
            self.tv_power = False

    def channel_up(self):
        if self.tv_power == True:
            if self.channel == Television.MAX_CHANNEL:
                self.channel = Television.MIN_CHANNEL
            elif self.channel != Television.MAX_CHANNEL:
                self.channel += 1

    def channel_down(self):
        if self.tv_power == True:
            if self.channel == Television.MIN_CHANNEL:
                self.channel = Television.MAX_CHANNEL
            elif self.channel != Television.MAX_CHANNEL:
                self.channel -= 1

    def volume_up(self):
        if self.tv_power == True:
            if self.volume == Television.MAX_VOLUME:
                self.volume = Television.MAX_VOLUME
            elif self.volume != Television.MAX_VOLUME:
                self.volume += 1

    def volume_down(self):
        if self.tv_power == True:
            if self.volume == Television.MIN_VOLUME:
                self.volume = Television.MIN_VOLUME
            elif self.volume != Television.MIN_VOLUME:
                self.volume -= 1

    def __str__(self):
        return f'TV status Is on = {self.tv_power}, Channel = {self.channel}, Volume = {self.volume}'

