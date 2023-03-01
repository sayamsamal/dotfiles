#!/bin/sh

~/.screenlayout/monitorswitch.sh

picom -b & disown # --experimental-backends --vsync should prevent screen tearing on most setups if needed

# feh --bg-fill ~/Pictures/wallpapers/firewatch.png --bg-fill ~/Pictures/wallpapers/firewatch.png & disown

# Low battery notifier
# ~/.config/qtile/scripts/check_battery.sh & disown

# Start welcome
# eos-welcome & disown

/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 & disown # start polkit agent from GNOME

nm-applet & disown
