class AC:
    company = "Voltas"
    def turnOn(self):
        print("AC turned on!")

    def turnOff(self):
        print("AC turned off!")

class Remote(AC):
    def turnOn(self):
        super().turnOff()
        print("Remote turned on!")

    def turnOff(self):
        print("Remote turned off!")
    buttons = 14
    battery = "AA"

p = AC()
q = Remote()

# p.turnOn()
q.turnOn()
q.turnOff()