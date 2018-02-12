import os
from Xlib import display, X
import Xlib.xobject.drawable as drawable

from PIL import Image


class ScreenshotHelper:
    def __init__(self):
        self.display = display.Display()
        self.root = self.display.screen().root
        self.screen_width, self.screen_height = \
            self.display.screen().width_in_pixels, self.display.screen().height_in_pixels
        self.drawable = drawable.Drawable()

    def take_screenshot(self, type, width=0, height=0):
        if type == "screen":
            raw = self.root.get_image(0, 0, self.screen_width, self.screen_height, X.ZPixmap, 0xffffffff)
            image = Image.frombytes("RGB", (self.screen_width, self.screen_height), raw.data, "raw", "BGRX")
            return image
        elif type == "selection":
            # TODO: able to actually make a selection
            got_selection = False
            while not got_selection:
                events = self.display.next_event()

            raw = self.root.get_image(0, 0, width, height, X.ZPixmap, 0xffffffff)
            image = Image.frombytes("RGB", (width, height), raw.data, "raw", "BGRX")
            return image
        elif type == "window":
            # TODO: able to select what window to take a screenshot of
            pass

kaas = ScreenshotHelper()
kaas.take_screenshot("selection", 500, 500).show()
