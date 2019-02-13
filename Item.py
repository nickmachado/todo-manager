import datetime

# I have my item Class here that I will use to time and complete tasks using the Manager module
class Item(object):

    # I am making sure i have variables as place holders so I can use them later
    def __init__ (self, date, complete, items):
        self.date = date
        self.complete = False
        self.items = []
    # I could not get this to work properly
