from datetime import datetime
from structure import DoubleCircularList

class Clock:
    def __init__(self):
        self.seconds = DoubleCircularList()
        self.minutes = DoubleCircularList()
        self.hours = DoubleCircularList()

        for i in range(60):
            self.seconds.insert(i)
            self.minutes.insert(i)
        for i in range(12):
            self.hours.insert(i)

        self.set_to_current_time()

    def set_to_current_time(self):
        now = datetime.now()
        sec = now.second
        min_ = now.minute
        hour = now.hour % 12  

        self.current_second = self.seconds.first
        while self.current_second.value != sec:
            self.current_second = self.current_second.next

        self.current_minute = self.minutes.first
        while self.current_minute.value != min_:
            self.current_minute = self.current_minute.next

        self.current_hour = self.hours.first
        while self.current_hour.value != hour:
            self.current_hour = self.current_hour.next

    def advance_second(self):
        self.current_second = self.seconds.advance(self.current_second)
        if self.current_second.value == 0:
            self.current_minute = self.minutes.advance(self.current_minute)
            if self.current_minute.value == 0:
                self.current_hour = self.hours.advance(self.current_hour)

    def show_time(self):
        return f"{self.current_hour.value:02}:{self.current_minute.value:02}:{self.current_second.value:02}"
