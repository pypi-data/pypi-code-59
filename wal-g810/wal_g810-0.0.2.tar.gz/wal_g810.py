import os.path
import json
import sys
import argparse

# wal_g810 details
VERSION = "0.0.2"

# Get path for g810 profiles
g810_file = "colors-wal-g810-led"

def setConfig():
        # Get host OS
        hostOS = getOS()
        # Get user home directory
        home_dir = os.getenv("HOME", os.getenv("USERPROFILE"))
        # Set wal colors file
        wal_colors = os.path.join(home_dir, ".cache", "wal", "colors.json")
        # Confirm wal export exists
        if not os.path.isfile(wal_colors):
                # Print error and exit if not found
                print("Wal colors could not be found. Try running `wal` again")
                sys.exit(1)
        # Set g810 directory by platform
        if hostOS == "linux" or hostOS == "darwin":
                g810_path = os.path.join(home_dir, ".cache", "wal")
                g810_theme = os.path.join(g810_path, g810_file)
        elif hostOS == "win32":
                print("Windows platform not supported")
                sys.exit(1)
        else:
                # Print error and exit if OS unsupported
                print("Unsupported operating system")
                sys.exit(1)
        # Return file paths as strings for wal color file and g810 profile file
        return wal_colors, g810_theme

def themeG810(wal_colors_path, g810_theme_path):
        # Open colors.json and load
        import_colors = json.load(open(wal_colors_path))

        # Transfer wal colors to g810 profile scheme
        #generic json file
        color_string = import_colors['special']['foreground'].replace("#","")

        wal_g810 = "# A wal_g810 profile\n"
        wal_g810 += "a" + " " + color_string + "\n"
        wal_g810 += "c"

        # Write theme json to g810 themes directory
        try:
                with open(g810_theme_path, 'w') as f:
                        f.write(wal_g810)
                if os.path.isfile(g810_theme_path):
                        print("The g810-led profile written successfully. Start g810-led with `g810-led -p $HOME/.cache/wal/colors-wal-g810` to view")
        except:
                print("Error writing g810 theme file")

        finally:
                sys.exit(1)
def getOS():
        # system call for user platform
        hostOS = sys.platform
        # return os as string: linux, win32, darwin
        return hostOS

def getArgs():
    # get the arguments with argparse
    description = "wal_g810"
    arg = argparse.ArgumentParser(description=description)

    arg.add_argument("-v", "--version", action="store_true",
            help="Print wal_g810 version.")

    return arg.parse_args()

def main():
        # Parse arguments
        arguments = getArgs()
        # Print app version
        if arguments.version:
                print("wal_g810", VERSION)
                sys.exit()
        # Set file paths
        wcp, vtp = setConfig()
        # Translate and write theme
        themeG810(wcp, vtp)

if __name__ == '__main__':
        main()
