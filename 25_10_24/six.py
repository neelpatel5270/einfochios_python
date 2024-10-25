import json
class Vehicle:
    def __init__(self, name, engine, price):
                self.name = name
                self.engine = engine
                self.price = price

vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)
convertjshon=json.dumps(vehicle.__dict__, indent=4)
print(convertjshon)

            
            
    