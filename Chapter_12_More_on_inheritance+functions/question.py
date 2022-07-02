
class Lock:
    key = "#L0cK"
    lockOpened = False

    def open(self, key):
        if(self.key == key):
            self.lockOpened = True
            print("Lock opened successfully!!")
        else:
            print("Incorrect password!... Please try again later.")
    
    def lock(self):
        if self.lockOpened == False:
            print("Already locked!")
        else: 
            print("Lock closed successfully")
    
    
l = Lock()
l.open("#L0cK")
l.lock()