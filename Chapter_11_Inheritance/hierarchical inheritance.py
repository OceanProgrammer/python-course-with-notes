from datetime import datetime
class Watch:
    # attributes
    purpose = "to show time"
    def showTime(self):
        time = datetime.now()
        print(time)

class Apple(Watch):
    purpose = "to show time in watch"
    type = "smartwatch"

class Rolex(Watch):
    type = "Luxury"

print(Apple.type)