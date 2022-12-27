#Python Essential Traning Course 
import sys
from termcolor import colored, cprint

text = colored ('hello, world', 'white', attrs=['reverse', 'blink'])
print(text)
cprint('Hello, Mido!', 'green', 'on_green')