"""
    Turbowarp API Usage:
    1.Install Turbowarp.
    2.Load “Clipboard” script.
    3.Run TURBOWARP API.
    4.Use 
        Copy to clipboard “&\runcmd?<cmd>”
      Or
        Copy to clipboard “&\runpy?<pycode>”
"""

import pyperclip, os, time

print("Welcome to Turbowarp API V0.0.2!\u7f51\u6613\u6b7b\u5168\u5bb6\u4e86\u64cd\u6b7b\u4f60\u7684\u5988")

while True:
    clipboard = pyperclip.paste()
    if clipboard[0:2] == "&\\":
        if clipboard[2:8] == "runpy?":
            try:
                exec(clipboard[8::])
            except:
                pass
        elif clipboard[2:9] == "runcmd?":
            os.system(clipboard[9::])
    pyperclip.copy(" ")
    time.sleep(0.1)