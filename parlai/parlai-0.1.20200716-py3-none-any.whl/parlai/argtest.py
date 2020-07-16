def main():
    import argparse
    import argcomplete

    import time

    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(required=True)
    sap = sp.add_parser('a')
    sap.add_argument('--foo')
    sap.add_argument('--bar', help='this is bar')

    sbp = sp.add_parser('b')
    sbp.add_argument('--cat')

    argcomplete.autocomplete(ap)

    ap.parse_args()
