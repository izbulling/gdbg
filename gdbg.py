import os
import json
import rumps

from py2x import Resources
from pydexcom import Dexcom

# TODO: resources correctly


# TODO: finish moving this to class
class DexcomAPI:
    def __init__(self, dexcom_dir):
        self.credentials = self.load_credentials(dexcom_dir + "dexcom_credentials.json")

        self.reading = {}
        self.value = 0
        self.status = ""
        self.color_status = ""

        self.colors = {
            "red": "\033[91m",
            "green": "\033[92m",
            "yellow": "\033[93m",
            "blue": "\033[94m",
            "end": "\033[0m",
        }

    def load_credentials(self, path):
        with open(Resources.get(path), "r") as f:
            return json.load(f)

    def login_dexcom(self):
        credentials = self.credentials

        self.dexcom = Dexcom(
            username=credentials["username"], password=credentials["password"]
        )

    def get_reading(self):
        self.reading = dexcom.get_current_glucose_reading()

    def create_status(self):
        bg = self.reading
        value = bg.value
        arrow = bg.trend_arrow

        self.value = value
        self.status = f"{value} {arrow}"

    def colorize_status(self):
        value = self.value
        colors = self.colors

        if 80 <= value <= 180:
            color = colors["green"]
        elif value >= 181:
            color = colors["red"]
        elif value <= 79:
            color = colors["yellow"]
        else:
            color = colors["blue"]

        self.color_status = f"{color}{self.status}{colors["end"]}"

    def get_reading(self):
        self.login_dexcom()
        self.get_reading()
        self.create_status()
        self.colorize_status()


class GDBG(object):
    def __init__(self):
        dexcom_dir = os.path.expanduser("~") + "/.dexcom/"

        self.app_name = "gdbg"
        self.dexcom = DexcomAPI(dexcom_dir)
        self.state_file = (dexcom_dir + "/bg_status.txt",)
        self.state_color_file = (dexcom_dir + "/bg_color_status.txt",)

        self.app = rumps.App(self.app_name)
        # TODO: menu

        # self.set_up_menu()
        # self.timer = rumps.Timer(self.on_tick, 1)
        # self.interval = self.config["interval"]
        # self.start_pause_button = rumps.MenuItem(
        #     title=self.config["start"], callback=self.start_timer
        # )
        # self.stop_button = rumps.MenuItem(title=self.config["stop"], callback=None)
        # self.app.menu = [self.start_pause_button, self.stop_button]

    def set_up_menu(self):
        self.app.title = self.app_name

    # TODO: called by timer
    def write_state(self):
        dexcom = self.dexcom

        with open(Resources.get(self.state_file), "w") as f:
            f.write(dexcom.status)

        with open(Resources.get(self.state_color_file), "w") as f:
            f.write(dexcom.color_status)

    def get_dexcom_reading(self):
        self.dexcom.get_reading()
        self.write_state()

    def run(self):
        self.app.run()


if __name__ == "__main__":
    app = GDBG()
    app.run()
