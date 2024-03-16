"""Room class
"""
from .device import *

class Room:
    """Class representing a room and its devices.
    """
    def __init__(self, name:str) -> None:
        self.name = name
        self.devices = set()

    def add_device(self, device: Device) -> None:
        self.devices.add(device)

    def remove_device(self, device: Device) -> None:
        try:
            self.devices.remove(device)
        except KeyError:
            print(f'Device ({device.id}) not found for {self.name} room.')

