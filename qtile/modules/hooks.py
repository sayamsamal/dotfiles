from libqtile import hook
import subprocess
import os

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])

# @hook.subscribe.client_focus
# def notion_tiled(window):
#     wm_class = window.window.get_wm_class()
#     if "notion" in wm_class:
#         window.floating = False


# def openrgb(window):
#    wm_class = window.window.get_wm_class()[0]
#    windowFocus = os.path.expanduser("~/.config/OpenRGB/scripts/windowFocus.sh")
#    subprocess.call([windowFocus, wm_class])
