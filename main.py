import time
from StopwatchController import *

time.sleep(0.1) # Wait for USB to become ready

print("Hello, Pi Pico!")

mystopwatch = StopwatchController()
mystopwatch.run()