#Python Essential Traning Course 
import sys
from termcolor import colored, cprint

text = colored ('hello, world', 'white', attrs=['reverse', 'blink'])
print(text)
cprint('Hello, Mido!😃', 'magenta', 'on_green')
for i in range (1):
    cprint (i, 'yellow`', end=' ')

print(colored('😃RAINBOW😃', 'red')) 
print(colored('😃RAINBOW😃', 'yellow'))
print(colored('😃RAINBOW😃', 'green'))   
print(colored('😃RAINBOW😃', 'cyan'))   
print(colored('😃RAINBOW😃', 'blue')) 
print(colored('😀RAINBOW😀', 'magenta')) 