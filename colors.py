"""This is my colors  module.

Here is my description of my mod.
"""


base03 = '\033[1;30m'
base02 = '\033[0;30m'
base01 = '\033[1;32m'
base00 = '\033[1;33m'
base0 = '\033[1;34m'
base1 = '\033[1;36m'
base2 = '\033[0;37m'
base3 = '\033[1;37m'
magenta = "\033[0;35m"
orange = "\033[0;31m"
blue = "\033[1;35m"
cyan = "\033[0;36m"
green = "\033[0;32m"
red = "\033[0;31m"
magenta = "\033[0;35m"
reset = "\033[0m"
clear = "\033[H\033[2J"
yellow = "\033[0;33m"

colors = [magenta, orange, blue, red, cyan, yellow]
import random
def random_color(): return random.choice(colors)

if __name__ == '__main__':
    
    print(reset)
    print(base03 + 'Base03' + reset)
    print(base02 + 'Base02' + reset)
    print(base01 + 'Base01' + reset)
    print(base00 + 'Base00' + reset)
    print(base0 + 'Base0' + reset)
    print(base3 + 'Base3' + reset)
    print(base2 + 'Base2' + reset)
    print(base1 + 'Base1' + reset)
    print(green + 'Green' + reset)
    print(red + 'Red' + reset)
    print(magenta + 'Magenta' + reset)
    print(cyan + 'Cyan' + reset)
    print(magenta + 'Magenta' + reset)
    print(blue + 'Blue' + reset)
    print(orange + 'Orange' + reset)
    print(random_color() + 'Random' + reset)








