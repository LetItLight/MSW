import os
import sys
import subprocess
from param import *

class Controller:
    def __init__(self):
        self.cmd = ""
        self.brightness = "100"
        self.color = "255 255 255"
        self.fix = "0"
    def process_data(self, data):
        cmdData = paramPaser(self.brightness, self.color)
        cmdData.parse_data(data)
        if cmdData.cmdtype == CommandType.Param:
           self.brightness =  cmdData.brightness
           self.color =  cmdData.color
           print("Set Option")
           print("brightness :%s"%self.brightness)
           print("color :%s"%self.color)
           return None
        elif cmdData.cmdtype == CommandType.FixText:
           self.cmd = "./../ledutil/runtext.py"
           self.fix = "1"
           self.text = cmdData.text
        elif cmdData.cmdtype == CommandType.ScrollText:
           self.cmd = "./../ledutil/runtext.py"
           self.fix = "0"
           self.text = cmdData.text
#Need to add animation or other operation case
        else:
           print("Not supported command")
        cmd_op = self.cmd
        brightness_op = "-b=" + self.brightness
        color_op = "-l=" + self.color
        fix_op = "-f=" + self.fix
        text_op = "-t=" + self.text
        subprocess.call([cmd_op, brightness_op, color_op, fix_op, text_op])
        
