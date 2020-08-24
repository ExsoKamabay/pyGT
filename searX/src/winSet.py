html = open("src/main.html","r").read();
def loadCSS(window):
    css = open("src/style.css","r").read();
    window.load_css(css);