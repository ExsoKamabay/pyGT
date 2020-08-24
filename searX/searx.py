from src import *;
class SearX:
    pass
if __name__=="__main__":
    kamabay = SearX()
    window = webview.create_window("KAMABAY",html=html,
    js_api=kamabay,width=850,height=650,text_select=False)
    webview.start(loadCSS,window);   