import screens.mainScreen
import sys

import curses

def main():
    curses.wrapper(screens.mainScreen())


main()