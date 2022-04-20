import pytest
from classes import *

def test_channel_up(self):
    self.tv1.channel_up()
    assert self.tv1.__str__() == 'TV statue: Is on = Flase, Channel = 0, Volume = 0'
    self.tv1.power()
    self.tv1.channel_up()
    assert self.tv1.__str__() == 'TV statue: Is on = Flase, Channel = 1, Volume = 0'
    self.tv1.channel_up()
    self.tv1.channel_up()
    assert self.tv1.__str__() == 'TV statue: Is on = Flase, Channel = 3, Volume = 0'


def test_volume_up(self):
    self.tv1.volume_up()
    assert self.tv1.__str__() == 'TV statue: Is on = Flase, Channel = 0, Volume = 0'
    self.tv1.power()
    self.tv1.volume_up()
    assert self.tv1.__str__() == 'TV statue: Is on = Flase, Channel = 0, Volume = 1'
    self.tv1.volume_up()
    self.tv1.volume_up()
    assert self.tv1.__str__() == 'TV statue: Is on = Flase, Channel = 0, Volume = 2'