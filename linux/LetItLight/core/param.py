import os
import sys
import enum

class CommandType(enum.Enum):
    NoCmd, FixText, ScrollText, Param, Animation = range(5)  
    

class paramPaser:
    def __init__(self, old_b, old_c):
        self.brightness = old_b
        self.color = old_c
        self.cmdtype = CommandType.NoCmd
        self.text = ""
    def parse_data(self, data):
        checker = data[0:2]
        payload = data[3:]
        print("parse_data : %s"%data)
        if checker == "-f":
            self.cmdtype = CommandType.FixText
            self.text = payload
        elif checker == "-s":
            self.cmdtype = CommandType.ScrollText
            self.text = payload
        elif checker == "-b":
            self.cmdtype = CommandType.Param
            self.brightness = payload
        elif checker == "-c":
            self.cmdtype = CommandType.Param
            self.color = payload
        else:
            print("Not defined")
    def print_attr(self):
        print(self.text)
        print(self.cmdtype)
        print(self.color)
        print(self.brightness)
