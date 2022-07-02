class Founder1:
    name1 = "Steve Jobs"
    def dob(self):
        print(f"D-O-B of {self.name1} is: 24 February 1955")
class Founder2:
    name2 = "Steve Wozniak"
    def dob2(self):
        print(f"D-O-B of {self.name2} is: 11 August 1950")

class Apple(Founder1, Founder2):
    products = 27

watch = Apple()
print(watch.name2)
watch.dob()
watch.dob2()