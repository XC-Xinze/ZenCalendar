from backend import CalManager, ZenMenu


if __name__ == "__main__":
        m = CalManager()
        my_zen = ZenMenu(m)
        my_zen.run_zen()