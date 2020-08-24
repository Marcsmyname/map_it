#! python3
# Mapit gets a map from your web browser
#from Automate the Boring Stuff
#comand line or clipboard
#pyperclip must be installed


import sys, webbrowser, pyperclip
if len(sys.argv) > 1:
    #get address from comand line.
    address = ''.join(sys.argv[1:])
else:
    #Get address from clipboard.
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
