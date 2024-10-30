from setuptools import setup

APP = ["gdbg.py"]
DATA_FILES = []  # TODO:
OPTIONS = {
    "argv_emulation": True,  # TODO:
    "iconfile": "icon.icns",  # TODO:
    "plist": {
        "CFBundleShortVersionString": "0.2.0",  # TODO:
        "LSUIElement": True,  # TODO:
    },
    "packages": ["pydexcom", "rumps"],  # TODO:
}

# TODO: use conda

setup(
    app=APP,
    name="gdbg",
    data_files=DATA_FILES,
    options={"py2app": OPTIONS},
    setup_requires=["py2app"],
    install_requires=["rumps"],  # TODO:
)
