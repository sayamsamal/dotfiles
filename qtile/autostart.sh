#!/bin/sh

wallpaper='Wallpaper-1.png'

~/.screenlayout/monitorswitch.sh

feh --bg-fill ~/Pictures/wallpapers/$wallpaper --bg-fill ~/Pictures/wallpapers/$wallpaper & disown

picom -b --vsync & disown # --experimental-backends --vsync should prevent screen tearing on most setups if needed

# Low battery notifier
~/.config/qtile/scripts/check_battery.sh & disown

# Start welcome
# eos-welcome & disown

/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 & disown # start polkit agent from GNOME

nm-applet & disown
