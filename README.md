# Site CLI

A simple command-line tool to open websites directly from your terminal.

---

## Installation

### Option 1 — Installer (recommended)
1. Download `SiteCLI_Setup.exe` from [Releases](../../releases)
2. Run it and follow the instructions
3. Done ! `site` is now available in your terminal 

### Option 2 — Manual
1. Requires **Python 3** and **Git for Windows**
2. Clone the repo :
```
git clone https://github.com/zedka450/site-CLI.git
```
3. Copy `site.py` and `site.bat` to `C:\tools\`
4. Add `C:\tools\` to your PATH

---

## Usage

```
site launch <url> [--browser-use]
site settings <browser>
site settings view
site help
```

### Examples

```
site launch https://google.com
site launch https://youtube.com --firefox-use
site launch https://github.com --bing-use
site settings firefox
site settings view
```

---

## Supported Browsers

| Flag | Browser |
|------|---------|
| `--firefox-use` | Firefox |
| `--google-chrome-use` | Google Chrome |
| `--bing-use` | Microsoft Edge |

---

## Commands

| Command | Description |
|---------|-------------|
| `site launch <url>` | Open a URL in the default browser |
| `site launch <url> --firefox-use` | Open with Firefox |
| `site settings firefox` | Set Firefox as default |
| `site settings view` | Show current default browser |
| `site help` | Show help |

---

## Requirements

- Windows 10 / 11
- Python 3.x — [download](https://python.org)
- Git for Windows — [download](https://git-scm.com)

---

## Files

```
site.py          → main script
site.bat         → Windows wrapper to run from terminal
install.iss      → Inno Setup source (to rebuild the installer)
Output/
└── SiteCLI_Setup.exe  → Windows installer
```

---

## License

MIT
