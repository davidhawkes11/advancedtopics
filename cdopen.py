# open and close the CD tray door (Windows OS)
# tested with Python 3.1, works with Python 3.5
import ctypes
import time
# open the CD tray door
ctypes.windll.winmm.mciSendStringW("set cdaudio door open",
    None, 0, None)
# wait 3.5 seconds
time.sleep(3.5)
# close the CD tray (manual closing only with some notebooks)
ctypes.windll.winmm.mciSendStringW("set cdaudio door closed",
    None, 0, None)
