"""Devices classes
"""
from abc import ABC, abstractmethod

class Device:
    """Class representing a device"""

    def __init__(self, name:str, id:str, device_type:str = None) -> None:
        self.name = name
        self.id = id
        self.device_type = device_type

class Light(ABC, Device):
    """Class representing a light device"""

    def __init__(self, name: str, id: str, device_type:str = "light") -> None:
        super().__init__(name, id, device_type)

    @abstractmethod
    def turn_on(self) -> None:
        pass

    @abstractmethod
    def turn_off(self) -> None:
        pass

class RGBLight(Light):
    """Class representing a RGB light device"""

    def __init__(self, name: str, id: str) -> None:
        super().__init__(name, id, "RGB light")

    @abstractmethod
    def set_color(self, r:int, g:int, b:int) -> None:
        pass

    @abstractmethod
    def set_intensity(self, k:int) -> None:
        pass

class Shutters(ABC, Device):
    """Class representing shutters device"""

    def __init__(self, name: str, id: str) -> None:
        super().__init__(name, id, "shutters")

    @abstractmethod
    def open(self) -> None:
        pass

    @abstractmethod
    def close(self) -> None:
        pass

    @abstractmethod
    def stop(self) -> None:
        pass