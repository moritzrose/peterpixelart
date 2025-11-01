from datetime import datetime

CHECK_INTERVAL = 300  # s
MORGENS = 12
MITTAGS = 18
ABENDS = 22



class TimeManager:
    def __init__(self):
        self.last_check:datetime = datetime.now()
        self.current_period   = self.determine_period()

    def determine_period(self):
        current_time = datetime.now()
        self.last_check = current_time
        current_hour = current_time.hour
        if 7 < current_hour < MORGENS:
            return "MORGENS"
        elif current_hour < MITTAGS:
            return "MITTAGS"
        elif current_hour < ABENDS:
            return "ABENDS"
        else:
            return "NACHTS"


    def update(self):
        last_check_too_old = (datetime.now() - self.last_check).total_seconds() > CHECK_INTERVAL

        if last_check_too_old:
            current_period = self.current_period
            new_period = self.determine_period()
            if current_period != new_period:
                self.current_period = new_period
                return True
        return False