import os, platform

os.system('git pull')

import requests

bit = platform.architecture()[0]

if bit == '64bit':

    from AUTO_COMMENT64 import menu

    menu()

elif bit == '32bit':

    from AUTO_COMMENT32 import menu

    menu()
