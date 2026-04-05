from backend import CalendarAPI, CalManager

if __name__ == "__main__":
    manager = CalManager()
    manager.load()
    api = CalendarAPI(manager)
    print(api.create_task("testweb"))