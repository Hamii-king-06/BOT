import os, platform
os.system("play-audio WELCOME_TO_HAMI_BOOT_818.mp3")
os.system('git pull')

import requests

bit = platform.architecture()[0]

if bit == '64bit':

    from BOT64 import menu

    menu()

elif bit == '32bit':

    from BOT import menu

    menu()
