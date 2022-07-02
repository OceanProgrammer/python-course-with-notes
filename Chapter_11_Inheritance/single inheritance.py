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

s7 = Apple()
new = Watch()
print(new.purpose)
print(s7.purpose)
s7.showTime()
new.showTime()
