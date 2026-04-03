import components
import manager
import datetime
from datetime import datetime, timedelta
import zenmenu

if __name__ == "__main__":
        m = manager.CalManager()
        my_zen = zenmenu.ZenMenu(m)
        my_zen.run_zen()