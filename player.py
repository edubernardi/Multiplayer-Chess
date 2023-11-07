import time

class Player():
    def __init__(self, socket, address, color):
        self.color = color
        self.socket = socket
        self.address = address
        self.time = 0
        #timeout após 15 minutos
        self.timeLimit = 900

    def incrementTime(self, amount):
        self.time += amount

    def timeout(self):
        return self.time > self.timeLimit

    def updateConnection(self, socket, address):
        self.socket = socket
        self.address = address

    def getTime(self):
        return "\n" + str(time.strftime('%M:%S', time.gmtime(self.time))) + "\n"

