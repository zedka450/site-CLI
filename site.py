

import sys
import os
import json
import webbrowser
import subprocess

CONFIG_FILE = os.path.join(os.path.expanduser("~"), ".site_config.json")

BROWSERS = {
    "--firefox-use": "firefox",
    "--google-chrome-use": "chrome",
    "--bing-use": r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
}

HELP = """site - launch websites from the terminal

USAGE:
  site launch <url> [--browser-use]
  OR
  site launch help

  site settings <browser>
  OR
  site settings view
  OR
  site settings help

  site help

COMMANDS:
  launch      Open a URL in a browser
  settings    Set the default browser
  help        Show this help message

BROWSER OPTIONS:
  --firefox-use         Open with Firefox
  --google-chrome-use   Open with Chrome
  --bing-use            Open with Edge
  (empty)               Use default browser from settings

EXAMPLE:
  site launch https://youtu.be/
  site launch https://youtu.be/ --firefox-use"""

LAUNCH_HELP = """site launch - open a URL in a browser
USAGE:
  site launch <url> [--browser-use]
  OR
  site launch help
  
BROWSER OPTIONS:
  --firefox-use         Open with Firefox
  --google-chrome-use   Open with Chrome
  --bing-use            Open with Edge
  (empty)               Use default browser from settings"""

SETTINGS_HELP = """site settings - set the default browser

USAGE:
  site settings <browser>
  OR
  site settings view
  OR
  site settings help

BROWSER OPTIONS:
  firefox       Set Firefox as default
  google-chrome Set Chrome as default
  bing          Set Edge as default

EXAMPLE:
  site settings firefox"""

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE) as f:
            return json.load(f)
    return {}

def save_config(config):
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f)

def launch(args):
    if not args or args[0] == "help":
        print(LAUNCH_HELP)
        return

    url = args[0] if args else ""
    flag = None
    for arg in args[1:]:
        if arg.startswith("--"):
            flag = arg
            break
    browser = None

    if flag:
        if flag in BROWSERS:
            browser = BROWSERS[flag]
        else:
            print(f"Unknown browser flag: {flag}")
            return
    else:
        config = load_config()
        browser = config.get("default_browser")

    if browser:
        try:
            subprocess.Popen([browser, url], shell=False)
        except FileNotFoundError:
            print(f"Browser '{browser}' not found, using system default.")
            webbrowser.open(url)
    else:
        webbrowser.open(url)

def settings(args):
    if not args or args[0] == "help":
        print(SETTINGS_HELP)
        return

    browser_map = {
        "firefox": "firefox",
        "google-chrome": "chrome",
        "bing": r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    }

    if args[0] == "view":
        config = load_config()
        current = config.get("default_browser")
        if current:
            reverse_map = {v: k for k, v in browser_map.items()}
            name = reverse_map.get(current, current)
            print(f"Current default browser: {name}")
        else:
            print("No default browser set.")
        return

    browser = args[0]
    if browser not in browser_map:
        print(f"Unknown browser: {browser}")
        return

    config = load_config()
    current = config.get("default_browser")
    
    if current == browser_map[browser]:
        print(f"{browser} is already the default/primary browser")
        return

    config["default_browser"] = browser_map[browser]
    save_config(config)
    print(f"Default browser set to: {browser}")

def main():
    args = sys.argv[1:]

    if not args or args[0] == "help":
        print(HELP)
        return

    command = args[0]
    rest = args[1:]

    if command == "launch":
        launch(rest)
    elif command == "settings":
        settings(rest)
    else:
        print(f"Unknown command: {command}")
        print(HELP)

if __name__ == "__main__":
    main()