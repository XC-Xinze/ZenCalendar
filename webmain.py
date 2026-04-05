from backend import CalendarAPI, CalManager
import webview
import os

def get_index_path():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_dir,"web","total.html")
def main():
    manager = CalManager()
    manager.load()
    api = CalendarAPI(manager)
    index_path = get_index_path()
    window = webview.create_window(title="ZenCalendar", url=index_path,js_api=api,width=1400,height=900)
    webview.start()

if __name__ == "__main__":
    main()