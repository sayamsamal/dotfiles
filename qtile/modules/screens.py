from libqtile import bar
from .widgets import *
from libqtile.config import Screen
from modules.keys import terminal
import os

def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2                 # Monitor 2 will display all widgets in widgets_list

screens = [
    Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=1.0, size=25, background='#282c34')),
    Screen(top=bar.Bar(widgets=init_widgets_screen2(), opacity=1.0, size=25))
]