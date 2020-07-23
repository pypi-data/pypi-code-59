"""Console script for pycefsharp."""
import sys
import argparse
from .cef import CefApp, CefView

def main():
    """Console script for pycefsharp."""
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help = "url to show in cefview")
    parser.add_argument("--title", default = "pycefsharp", help = "title for cefview window")
    parser.add_argument("--icon", default = None, help = "icon for cefview window")
    # geometry
    parser.add_argument("--geometry", default = "-1,-1,-1,-1", help = "initial geometry for cefview window(x,y,width,height)")
    args = vars(parser.parse_args())

    CefApp().Run(
        CefView(
            args["url"], args["title"], args["icon"],
            [int(g) for g in args["geometry"].split(",")]
        )
    )

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
