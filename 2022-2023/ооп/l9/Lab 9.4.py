from dataclasses import dataclass

@dataclass

class Location:
    name : str
    longitude : float = 0
    latitude : float = 11.5

stonehenge = Location(latitude=1.5, name='Stonehenge',  longitude=51)

print(stonehenge)