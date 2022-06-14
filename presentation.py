from snail_print import snail_print
from color import bcolors
import time

delay = 0.15
meta_delay = 0.3
print(f"{bcolors.GREEN}❯{bcolors.NORMAL} python")
time.sleep(1)
print(
    """Python 3.10.4 (main, Apr  2 2022, 18:06:22) [GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information"""
)
time.sleep(1)
print(">>>", end=" ")
snail_print("from snail_print import snail_print", delay=delay)

print(">>>", end=" ")
snail_print(f'snail_print("Hello World", delay={meta_delay})', delay=delay)
snail_print("Hello World", delay=meta_delay)
print(">>>")
