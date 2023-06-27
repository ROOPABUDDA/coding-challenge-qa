import time
from datetime import datetime, timezone


class Clock:
    def __init__(self):
        self.start_time: float = None
        self.stop_time: float = None

    def start(self):
        self.reset()
        self.start_time = time.time()

    def stop(self) -> float:
        self.stop_time = time.time()
        return self.get_elapsed_time()

    def get_elapsed_time(self) -> float:
        if self.start_time is None or self.stop_time is None:
            return None
        return self.stop_time - self.start_time

    def reset(self):
        self.start_time = None
        self.stop_time = None


class Measure:
    @classmethod
    def start_clock(cls) -> Clock:
        m = Clock()
        m.start()
        return m

    @staticmethod
    def current_time():
        return datetime.now(tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f+00:00")
