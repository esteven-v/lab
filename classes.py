class Television:
    """
    Class to represent the Television objects
    """
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self) -> None:
        """
        Method to set the default state of the TV.
        """
        self.channel = Television.MIN_CHANNEL
        self.volume = Television.MIN_VOLUME
        self.tv_power = False

    def power(self) -> None:
        """
        Method to turn off and on the TV
        If tv is off then it will switch to on
        If tv is on then it will switch to off
        """
        if self.tv_power == False:
            self.tv_power = True
        elif self.tv_power == True:
            self.tv_power = False

    def channel_up(self) -> None:
        """
        Method to move the channel up
        It should only work for a TV that is on.
        If the method is called when one is on the MAX_CHANNEL, it should take the TV channel back to the MIN_CHANNEL.
        """
        if self.tv_power == True:
            if self.channel == Television.MAX_CHANNEL:
                self.channel = Television.MIN_CHANNEL
            elif self.channel != Television.MAX_CHANNEL:
                self.channel += 1

    def channel_down(self) -> None:
        """
        Method to move the tv channel down
        It should only work for a TV that is on.
        If the method is called when one is on the MIN_CHANNEL, it should take the TV channel back to the MAX_CHANNEL.
        """
        if self.tv_power == True:
            if self.channel == Television.MIN_CHANNEL:
                self.channel = Television.MAX_CHANNEL
            elif self.channel != Television.MAX_CHANNEL:
                self.channel -= 1

    def volume_up(self) -> None:
        """
        Method to move the tv volume up.
        It should only work for a TV that is on.
        If the method is called when one is on the MAX_VOLUME, the volume should not be adjusted.

        """
        if self.tv_power == True:
            if self.volume == Television.MAX_VOLUME:
                self.volume = Television.MAX_VOLUME
            elif self.volume != Television.MAX_VOLUME:
                self.volume += 1

    def volume_down(self) -> None:
        """
        Method to move the tv volume down
        It should only work for a TV that is on.
        If the method is called when one is on the MIN_VOLUME, the volume should not be adjusted.

        """
        if self.tv_power == True:
            if self.volume == Television.MIN_VOLUME:
                self.volume = Television.MIN_VOLUME
            elif self.volume != Television.MIN_VOLUME:
                self.volume -= 1

    def __str__(self) -> str:
        """
        This method should be used to return the TV status
        :return: String with tv_power tv_channel and tv_volume
        """
        return f'TV status Is on = {self.tv_power}, Channel = {self.channel}, Volume = {self.volume}'

