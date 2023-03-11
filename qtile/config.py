import os

from libqtile import qtile, bar, layout
from libqtile.config import (
    Click,
    Drag,
    DropDown,
    Group,
    Key,
    KeyChord,
    Match,
    ScratchPad,
    Screen,
)
from libqtile.lazy import lazy

from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration

from modules.hooks import *

# from modules.my_widget import GroupBox
from modules.custom_groupbox import CustomGroupBox


mod = "mod4"
myTerm = "alacritty"
myBrowser = "brave"

keys = [
    ### The essentials
    Key([mod], "Return", lazy.spawn(myTerm), desc="Launches My Terminal"),
    Key([mod, "shift"], "Return", lazy.spawn("dm-run"), desc="Run Launcher"),
    Key([mod], "b", lazy.spawn(myBrowser), desc="Brave"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle through layouts"),
    Key([mod, "shift"], "c", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "shift"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key(
        [mod, "shift"],
        "p",
        lazy.spawn(os.path.expanduser("~/.config/rofi/scripts/powermenu")),
        desc="Power Menu",
    ),
    Key(
        ["control", "shift"],
        "e",
        lazy.spawn("emacsclient -c -a emacs"),
        desc="Doom Emacs",
    ),
    Key(
        [mod],
        "r",
        lazy.spawn(os.path.expanduser("~/.config/rofi/scripts/launcher")),
        desc="Spawn a command using a prompt widget",
    ),
    ### Rofi Keychords
    KeyChord(
        [mod],
        "p",
        [
            Key(
                [],
                "n",
                lazy.spawn(
                    "firefox --new-window https://notion.so -P notion-profile --no-remote --class=notion --name=notion"
                ),
                desc="Spawn notion as native-like app",
            )
        ],
        name="D Menu Run",
    ),
    ### Switch focus to specific monitors
    Key([mod], "w", lazy.to_screen(0), desc="Keyboard focus to monitor 1"),
    Key([mod], "e", lazy.to_screen(1), desc="Keyboard focus to monitor 2"),
    # Switch focus of monitors
    Key([mod], "period", lazy.next_screen(), desc="Move focus to next monitor"),
    Key([mod], "comma", lazy.prev_screen(), desc="Move focus to prev monitor"),
    ### Window controls
    Key([mod], "j", lazy.layout.down(), desc="Move focus down in current stack pane"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up in current stack pane"),
    Key(
        [mod, "shift"],
        "j",
        lazy.layout.shuffle_down(),
        lazy.layout.section_down(),
        desc="Move windows down in current stack",
    ),
    Key(
        [mod, "shift"],
        "k",
        lazy.layout.shuffle_up(),
        lazy.layout.section_up(),
        desc="Move windows up in current stack",
    ),
    Key(
        [mod],
        "h",
        lazy.layout.shrink(),
        lazy.layout.decrease_nmaster(),
        desc="Shrink window (MonadTall), decrease number in master pane (Tile)",
    ),
    Key(
        [mod],
        "l",
        lazy.layout.grow(),
        lazy.layout.increase_nmaster(),
        desc="Expand window (MonadTall), increase number in master pane (Tile)",
    ),
    Key([mod], "n", lazy.layout.normalize(), desc="normalize window size ratios"),
    Key(
        [mod],
        "m",
        lazy.layout.maximize(),
        desc="toggle window between minimum and maximum sizes",
    ),
    Key([mod, "shift"], "f", lazy.window.toggle_floating(), desc="toggle floating"),
    # Full Screen Toggle
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="toggle fullscreen"),
    ### Stack controls
    Key(
        [mod, "shift"],
        "Tab",
        lazy.layout.rotate(),
        lazy.layout.flip(),
        desc="Switch which side main pane occupies (XmonadTall)",
    ),
    Key(
        [mod],
        "space",
        lazy.layout.next(),
        desc="Switch window focus to other pane(s) of stack",
    ),
    Key(
        [mod, "shift"],
        "space",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    ### Audio and Brightness keymapping
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer set Master 3%+")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer set Master 3%-")),
    Key([], "XF86AudioMute", lazy.spawn("amixer set Master toggle")),
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
    ### Scratchpads and stuff
    Key([mod], "Insert", lazy.group["scratchpad"].dropdown_toggle("term")),
    Key([mod], "Home", lazy.group["scratchpad"].dropdown_toggle("thunar")),
    Key([mod], "Delete", lazy.group["scratchpad"].dropdown_toggle("spotify")),
]

groups = [
    Group("1", label="", layout="monadtall"),
    Group("2", label="", layout="monadtall"),
    Group("3", label="", layout="monadtall"),
    Group("4", label="", layout="monadtall"),
    Group("5", label="", layout="monadtall"),
    Group("6", label="", layout="monadtall"),
    ScratchPad(
        "scratchpad",
        [
            DropDown(
                "term",
                "alacritty",
                x=0.2,
                y=0.1,
                width=0.6,
                height=0.8,
                opacity=1,
                on_focus_lost_hide=True,
            ),
            DropDown(
                "thunar",
                "thunar",
                x=0.2,
                y=0.1,
                width=0.6,
                height=0.8,
                opacity=1,
                on_focus_lost_hide=True,
            ),
            DropDown(
                "spotify",
                "spotify-launcher",
                x=0.2,
                y=0.1,
                width=0.6,
                height=0.8,
                opacity=1,
                on_focus_lost_hide=True,
            ),
        ],
    ),
]

from libqtile.dgroups import simple_key_binder

dgroups_key_binder = simple_key_binder("mod4")

layout_theme = {
    "border_width": 2,
    "margin": 8,
    "border_focus": "b7bdf8",
    "border_normal": "1D2330",
}

layouts = [
    # layout.MonadWide(**layout_theme),
    # layout.Bsp(**layout_theme),
    # layout.Stack(stacks=2, **layout_theme),
    # layout.Columns(**layout_theme),
    # layoHHut.RatioTile(**layout_theme),
    # layout.Tile(shift_windows=True, **layout_theme),
    # layout.VerticalTile(**layout_theme),
    # layout.Matrix(**layout_theme),
    # layout.Zoomy(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Stack(num_stacks=2),
    layout.RatioTile(**layout_theme),
    layout.TreeTab(
        font="Ubuntu",
        fontsize=10,
        sections=["FIRST", "SECOND", "THIRD", "FOURTH"],
        section_fontsize=10,
        border_width=2,
        bg_color="1c1f24",
        active_bg="c678dd",
        active_fg="000000",
        inactive_bg="a9a1e1",
        inactive_fg="1c1f24",
        padding_left=0,
        padding_x=0,
        padding_y=5,
        section_top=10,
        section_bottom=20,
        level_shift=8,
        vspace=3,
        panel_width=200,
    ),
    layout.Floating(margin=8, border_focus="#e1acff", border_normal="#1D2330"),
]

# Widgets

colors = [
    ["#282c34", "#282c34"],
    ["#1c1f24", "#1c1f24"],
    ["#dfdfdf", "#dfdfdf"],
    ["#ff6c6b", "#ff6c6b"],
    ["#98be65", "#98be65"],
    ["#da8548", "#da8548"],
    ["#51afef", "#51afef"],
    ["#c678dd", "#c678dd"],
    ["#46d9ff", "#46d9ff"],
    ["#a9a1e1", "#a9a1e1"],
]

bubble_colors = {
    "g1": "#bfbfbf",
    "g2": "#4c5958",
    "g3": "#8aa6a3",
    "g4": "#10403b",
    "g5": "#127369",
    "foreground": "#cad3f5",
    "background": "#363a4f",
}

widget_defaults = dict(
    font="SauceCodePro Nerd Font Medium",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

decoration_group = {
    "decorations": [
        RectDecoration(
            colour=bubble_colors["background"],
            radius=10,
            filled=True,
            clip=True,
        )
    ]
}


def init_widgets_list():
    return [
        widget.Spacer(length=5),
        widget.Image(
            filename="~/.config/qtile/assets/eos-c.png",
            margin=3,
            mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("rofi -show combi")},
        ),
        widget.Spacer(length=5),
        CustomGroupBox(
            fontsize=30,
            padding_y=0,
            padding_x=5,
            margin_x=0,
            margin_y=3,
            active="#a5adcb",
            inactive="#363a4f",
            this_current_screen_border="#a5adcb",
            other_current_screen_border="#494d64",
            highlight_method="text",
            disable_drag=True,
        ),
        widget.Spacer(length=5),
        widget.CurrentLayoutIcon(
            custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
            foreground=colors[2],
            padding=3,
            scale=0.5,
            **decoration_group
        ),
        widget.Spacer(length=5),
        widget.Prompt(),
        widget.Spacer(length=5),
        widget.WindowName(padding=0),
        widget.Spacer(length=5),
        widget.Chord(
            chords_colors={
                "launch": ("#ff0000", "#ffffff"),
            },
            name_transform=lambda name: name.upper(),
        ),
        # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
        # widget.StatusNotifier(),
        widget.Systray(icon_size=18),
        widget.Spacer(length=5),
        widget.Net(
            interface="wlan0",
            format="  {down} ↓↑ {up}",
            padding=10,
            foreground=bubble_colors["foreground"],
            **decoration_group
        ),
        widget.Spacer(length=5),
        widget.ThermalSensor(
            threshold=90,
            fmt=" {}",
            padding=10,
            foreground=bubble_colors["foreground"],
            **decoration_group
        ),
        widget.Spacer(length=5),
        widget.CheckUpdates(
            update_interval=1800,
            distro="Arch_checkupdates",
            display_format="{updates} ﮮ",
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn(myTerm + " -e sudo pacman -Syu")
            },
            padding=10,
            foreground=bubble_colors["foreground"],
            colour_have_updates=bubble_colors["foreground"],
            colour_no_updates=bubble_colors["foreground"],
            **decoration_group
        ),
        widget.Spacer(length=5),
        widget.Memory(
            mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(myTerm + " -e btop")},
            fmt=" {}",
            padding=10,
            foreground=bubble_colors["foreground"],
            **decoration_group
        ),
        widget.Spacer(length=5),
        widget.Volume(
            fmt="  {}",
            padding=10,
            foreground=bubble_colors["foreground"],
            **decoration_group
        ),
        widget.Spacer(length=5),
        widget.Battery(
            update_interval=10,
            padding=10,
            foreground=bubble_colors["foreground"],
            **decoration_group
        ),
        widget.Spacer(length=5),
        widget.Clock(
            padding=10,
            format="  %A, %B %d",
            foreground=bubble_colors["foreground"],
            **decoration_group
        ),
        widget.Spacer(length=5),
        widget.Clock(
            padding=10,
            format=" %H:%M",
            foreground=bubble_colors["foreground"],
            **decoration_group
        ),
        widget.Spacer(length=5),
        widget.TextBox(
            padding=10,
            text="襤",
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn(
                    os.path.expanduser("~/.config/rofi/scripts/powermenu-sidebar")
                )
            },
            foreground=bubble_colors["foreground"],
            **decoration_group
        ),
        widget.Spacer(length=5),
    ]


def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1


def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    del widgets_screen2[12:13]
    return widgets_screen2


# Screens
screens = [
    Screen(
        top=bar.Bar(
            widgets=init_widgets_screen1(), size=25, background="#00000000", margin=8
        ),
    ),
    Screen(
        top=bar.Bar(
            widgets=init_widgets_screen2(), size=25, background="#00000000", margin=8
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_app_rules = []  # type: list
follow_mouse_focus = False
bring_front_click = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(wm_class="zoom"),  # zoom
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
