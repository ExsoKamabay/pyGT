try:
    from .setWin import *
except:
    from os import name,system;
    if name == "nt":
        system("pip install pywebview");
    else:
        system("pip install webview")