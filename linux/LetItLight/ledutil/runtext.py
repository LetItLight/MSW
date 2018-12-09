#!/usr/bin/env python
# Display a runtext with double-buffering.
from samplebase import SampleBase
from rgbmatrix import graphics
import time


class RunText(SampleBase):
    def __init__(self, *args, **kwargs):
        print(args)
        super(RunText, self).__init__(*args, **kwargs)
        self.parser.add_argument("-t", "--text", help="The text to scroll on the RGB LED panel", default="Hello world!")
        self.parser.add_argument("-f", "--fix", help="Use this option when you want to not moving text", default=0, type=int)
        self.parser.add_argument("-l", "--color", help="Set color R G B like 128 122 255", default="255 255 255")

    def run(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("../fonts/nanumbarungothic10.bdf")
        color_list = [int(x)  for x in self.args.color.split(' ')]
        textColor = graphics.Color(color_list[0], color_list[1], color_list[2])
        pos = offscreen_canvas.width
        my_text = self.args.text
        fix = self.args.fix
        while True:
            offscreen_canvas.Clear()
            if fix == 1:
                pos = 0
            len = graphics.DrawText(offscreen_canvas, font, pos, 10, textColor, my_text.decode('utf-8'))
            if fix == 0:
                pos -= 1
            if (pos + len < 0):
                break

            time.sleep(0.05)
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)


# Main function
if __name__ == "__main__":
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()
