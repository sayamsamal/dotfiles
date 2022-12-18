from libqtile import widget
from libqtile import qtile

colors = [
	      ["#282c34", "#282c34"], # panel background
          ["#3d3f4b", "#434758"], # background for current screen tab
          ["#ffffff", "#ffffff"], # font color for group names
          ["#ff5555", "#ff5555"], # border line color for current tab
          ["#74438f", "#74438f"], # border line color for 'other tabs' and color for 'odd widgets'
          ["#4f76c7", "#4f76c7"], # color for the 'even widgets'
          ["#e1acff", "#e1acff"], # window name
          ["#ecbbfb", "#ecbbfb"]  # backbround for inactive screens
]

class MyVolume(widget.Volume):
    def _configure(self, qtile, bar):
        widget.Volume._configure(self, qtile, bar)
        self.volume = self.get_volume()
        if self.volume <= 0:
            self.text = 'ﱝ'
        elif self.volume <= 15:
            self.text = ''
        elif self.volume < 50:
            self.text = '奔'
        else:
            self.text = '墳'
        # drawing here crashes Wayland

    def _update_drawer(self, wob=False):
        if self.volume <= 0:
            self.text = 'ﱝ'
        elif self.volume <= 15:
            self.text = ''
        elif self.volume < 50:
            self.text = '奔'
        else:
            self.text = '墳'
        self.draw()

        if wob:
            with open(self.wob, 'a') as f:
                f.write(str(self.volume) + "\n")

volume = MyVolume(
    fontsize=18,
    font='SauceCodePro Nerd Font',
    foreground=colors[4],
    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn("pavucontrol")}
)

widget_defaults = dict(
    font='SauceCodePro Nerd Font',
    fontsize=15,
    padding=0,
    background="#000000"
)

def init_widgets_list():
    widgets_list = [
        widget.Sep(padding=3, linewidth=0),
        widget.Image(filename='~/.config/qtile/eos-c.png', margin=3, mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("rofi -show combi")}),
        widget.Sep(padding=4, linewidth=0), 
        widget.GroupBox(
                        highlight_method='line',
                        this_screen_border="#5294e2",
                        this_current_screen_border="#5294e2",
                        active="#ffffff",
                        inactive="#848e96"),
        widget.Spacer(),
        volume,
    ]
    return widgets_list