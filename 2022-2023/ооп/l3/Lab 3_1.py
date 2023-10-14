class Country:
    city ='Novosibirsk'
    street = 'Russian_street'
    building = 55
    def __init__(self, city, street, building):
        self.city = city
        self.street = street
        self.building = building


msc = Country('Moscow', 'Nikolskaya', 5)
spb = Country('St_Petersburg', 'Horse_lane', 12)

print(Country.city + ',', Country.street + ',', Country.building)
print(msc.city + ',', msc.street + ',', msc.building)
print(spb.city + ',', spb.street + ',', spb.building)