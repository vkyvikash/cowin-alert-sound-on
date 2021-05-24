import time
import os
from sys import platform

# Speech dispatcher
speech_dispatcher = 'say' # for Mac
if 'linux' in platform:
    speech_dispatcher = 'spd-say'

while True:
    time.sleep(800)
    print (time.strftime('%Y-%m-%d %H:%M'))
    os.system('{} "{}"'.format(speech_dispatcher, 'Logout'))
