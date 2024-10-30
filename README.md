# get dexcom blood glucose - gdbg

TODO:
* [ ] create py2app
  * [ ] have it start as login item
  * [ ] use resources properly
    * https://github.com/dante-biase/py2app?tab=readme-ov-file#resources 
* [ ] logic for time interval (rumps has thing, but luka-mini has dynamic approach)
  * [ ] will need to fallback to 10 min if no timestamp available
* [ ] show how many minutes since last retrieved
* [ ] handle errors? (pydexcom if any)
  * [ ] icon for no recent readings
  * [ ] icon for retrying in 10 min
* [ ] git and gi repo

## overview

a python app that displays blood glucose in the macos menu bar. retrieves blood glucose from dexcom via the [pydexcom](https://github.com/gagebenne/pydexcom) library. it also writes the blood glucose and arrow (with terminal colors) to a state file that can be used for displaying data in your terminal.

this app was inspire by [kylebshr/luka-mini](https://github.com/kylebshr/luka-mini/tree/main). i wanted to be able to access the blood glucose data outside of the app for other uses.

## how to use

NOTE: this is configured to work with a conda environment (see [development](#development))

### file resources

all resources are in the directory: `$HOME/.dexcom`

*secrets*

* dexcom_credentials.json

```json
{
  "username" : "dexcom_username",
  "password": "dexcom_password"
}
```

*blood glucose state files*

* bg_status.txt
* bg_color_status.txt

### build app

`python setup.py py2app -r $HOME/.dexcom`

### add to login items

TODO:

## development

```sh
conda create --name gdbg python=3.12

conda activate gdbg  

pip install -r requirements.txt
```

## using in zsh $PROMPT

to use in zsh prompt, update `$PROMPT` in `$HOME/.zshrc`. the backslash when setting `$PROMPT` to execute the function to read the bg text file is __critical__ (will not work otherwise).

```sh
# ~/.zshrc

function get_bg() {
    cat $HOME/.dexcom/bg_status.txt
}

export PROMPT="$PROMPT\$(get_bg)"
```

## references

*packages*

* [gagebenne/pydexacom](https://github.com/gagebenne/pydexcom)
* [jaredks/rumps](https://github.com/jaredks/rumps)
* [dante-biase/py2app](https://github.com/dante-biase/py2app)
  * [pypa/setuptools](https://github.com/pypa/setuptools)

*articles*

* [Create a macOS Menu Bar App with Python (Pomodoro Timer) - Camillo Visini](https://camillovisini.com/coding/create-macos-menu-bar-app-pomodoro)
* [Glucose Readings in a Terminal Prompt - Hart Hoover](https://harthoover.com/glucose-readings-in-a-terminal-prompt/)
