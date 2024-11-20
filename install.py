#!/usr/bin/env python3
import argparse
import json
from subprocess import CalledProcessError, check_output as run
from typing import Union
from urllib.request import urlopen

arg_parser = argparse.ArgumentParser(
    prog="Catppuccin Theme - Gnome-Terminal Installation",
    description="Installs the Catppuccin theme for gnome-terminal",
)
arg_parser.add_argument("-l", "--local", action="store")
args = arg_parser.parse_args()

if args.local is None:
    try:
        url = "https://raw.githubusercontent.com/catppuccin/palette/refs/tags/v1.7.1/palette.json"
        res = urlopen(url).read().decode("utf-8")
        palette = json.loads(res)
    except Exception as e:
        print(f"Error fetching the palette: {e}")
        exit(1)
else:
    try:
        with open(args.local) as local_palette:
            palette = json.load(local_palette)
    except Exception as e:
        print(f"Error fetching the palette: {e}")
        exit(1)

gsettings_path_base = (
    "org.gnome.Terminal.Legacy.Profile:/org/gnome/terminal/legacy/profiles:/"
)
gsettings_schema = "org.gnome.Terminal.ProfilesList"
# hardcoded uuids for each flavor
uuids = {
    "mocha": "95894cfd-82f7-430d-af6e-84d168bc34f5",
    "macchiato": "5083e06b-024e-46be-9cd2-892b814f1fc8",
    "frappe": "71a9971e-e829-43a9-9b2f-4565c855d664",
    "latte": "de8a9081-8352-4ce4-9519-5de655ad9361",
}

# New palette color definitions
new_palette = {
    "background": "#e5ff8f",
    "foreground": "#354000",
    "cursor": "#627400",
    "black": "#d1f600",
    "red": "#ffc9d8",
    "green": "#caed00",
    "yellow": "#ffd0aa",
    "blue": "#b7e0ff",
    "magenta": "#e0d1ff",
    "cyan": "#01fcde",
    "white": "#627400",
    "brightBlack": "#9eba00",
    "brightRed": "#ffebf0",
    "brightGreen": "#e5ff8f",
    "brightYellow": "#ffeddf",
    "brightBlue": "#e4f3ff",
    "brightMagenta": "#f3eeff",
    "brightCyan": "#c5fff2",
    "brightWhite": "#1f2600"
}

def gsettings_get(key: str):
    return json.loads(
        run(["gsettings", "get", gsettings_schema, key])
        .decode("utf-8")
        .replace("'", '"')
    )


def gsettings_set(
    key: str, value: Union[dict, list, str, bool], path: str = ""
) -> None:
    if type(value) in [dict, list]:
        value = json.dumps(value).replace('"', "'")
    elif type(value) is str:
        value = f"'{value}'"
    elif type(value) is bool:
        value = str(value).lower()

    if path:
        print(f"Setting {path}/ {key} to {value}")
        run(
            ["gsettings", "set", f"{gsettings_path_base}:{path}/", f"{key}", f"{value}"]
        )
    else:
        print(f"Setting {key} to {value}")
        run(["gsettings", "set", f"{gsettings_schema}", f"{key}", f"{value}"])


# handle the case where there are no profiles
try:
    profiles = gsettings_get("list")
except CalledProcessError:
    profiles = []

# Iterate over each flavor and apply the new colors
for flavor, color_obj in palette.items():
    uuid = uuids.get(flavor)
    
    if not uuid:
        continue
    
    colors = new_palette  # Use the new color palette
    
    # Update settings with the new colors
    gsettings_set("visible-name", f"Rootloops {flavor.capitalize()}", uuid)
    gsettings_set("background-color", colors["background"], uuid)
    gsettings_set("foreground-color", colors["foreground"], uuid)
    gsettings_set("highlight-colors-set", True, uuid)
    gsettings_set("highlight-background-color", colors["yellow"], uuid)
    gsettings_set("highlight-foreground-color", colors["magenta"], uuid)
    gsettings_set("cursor-colors-set", True, uuid)
    gsettings_set("cursor-background-color", colors["cursor"], uuid)
    gsettings_set("cursor-foreground-color", colors["foreground"], uuid)
    gsettings_set("use-theme-colors", False, uuid)
    gsettings_set("bold-is-bright", True, uuid)
    gsettings_set("palette", [
        colors["black"], colors["red"], colors["green"], colors["yellow"],
        colors["blue"], colors["magenta"], colors["cyan"], colors["white"],
        colors["brightBlack"], colors["brightRed"], colors["brightGreen"], colors["brightYellow"],
        colors["brightBlue"], colors["brightMagenta"], colors["brightCyan"], colors["brightWhite"]
    ], uuid)

    # Add the profile UUID if not already present
    if uuid not in profiles:
        profiles.append(uuid)

gsettings_set("list", profiles)
print("All profiles installed.")

