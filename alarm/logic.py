import _tkinter
import time 
from datetime import datetime
from playsound import playsound

class Timer:
    def __init__(self):
        self.seconds = 0
        self.running = False

    def start(self, seconds):
        self.seconds = seconds
        self.running = True
    
    def reset(self):
        self.seconds = 0
        self.running = False
        
    
    def tick(self):
        if self.running and self.seconds > 0:
            self.seconds -= 1

class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.running = False
    
    def start(self):
        self.running = True
    
    def stop(self):
        self.running = False


    def tick(self):
        if self.running:
            self.seconds += 1


class Clock:
    def get_time(self):
        return datetime.now().strftime("%H:%M:%S")
    

