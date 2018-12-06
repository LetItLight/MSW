import os
import sys
import subprocess
class Text:
    brightness = 100
    color = [255, 0, 0]

    def set_string(self, string):
        print("string : %s"%string)
        print("brightness : %d"%self.brightness)
        if string == '1':
            text="-t="+"Sorry. First trip"
            subprocess.call(["./../ledutil/runtext.py", text])
        elif string == '2':
            text="-t="+"Thank you. Have a nice day"
            subprocess.call(["./../ledutil/runtext.py", text])
        else:
            print("Not defined")
    def set_brightness(self, value):
        if (value < 0 | value > 100):
            print("Invalid value : %d"%d)
        else:
            print("brightness changed to %d"%d)
            self.brighntess = value
