from datetime import time,datetime
import settings

##variables
current = datetime.now()
growtime = current + timedelta(minutes=60)

class field:
    def __init__(self,name,cost,value):
        self.cost = cost
        self.name = name
        self.value = value

    def grow(self):
        if growtime > current:
            settings.unharvested_field.add(self.name)

    def buy(self):
        if self.cost < player.gold(1000):
            settings.fields.add(self.name)

    def grown(self):
        if growtime < current:
            settings.ready_to_harvest.add(self.name)

    def harvest(self):
        settings.playermoney += self.value
        print("Field has been harvested")
        print(f"Your account hass been increased to {settings.playermoney}")