from snail_print import snail_print
from color import bcolors as b
import time

delay = 0.05
meta_delay = 0.3
print(f" {b.GREEN}❯{b.NORMAL} python")
time.sleep(1)
print(
    """ Python 3.10.4 (main, Apr  2 2022, 18:06:22) [GCC 9.4.0] on linux
 Type "help", "copyright", "credits" or "license" for more information"""
)
time.sleep(1)
print(f" {b.NORMAL}>>>", end=" ")
snail_print(
    f"{b.GREEN}from{b.NORMAL} {b.ORANGE}snail_print{b.NORMAL} {b.GREEN}import{b.NORMAL} {b.NORMAL}snail_print",
    delay=delay,
)

print(f" {b.NORMAL}>>>", end=" ")
snail_print(
    f'{b.NORMAL}snail_print({b.YELLOW}"Hello World"{b.NORMAL}, delay={b.GREEN}{meta_delay}{b.NORMAL})',
    delay=delay,
)
snail_print(" Hello World", delay=meta_delay)
print(" >>>")
