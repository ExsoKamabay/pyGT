from src import *
class Api_js:
    pass
if __name__=="__main__":
    kmy = Api_js();
    win = webview.create_window("KAMABAY",
    html=html,js_api=kmy,min_size=(900,650));
    webview.start(loadCSS,win); 
