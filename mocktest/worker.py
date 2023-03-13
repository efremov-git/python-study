import time


class Worker:
    normal_sleep_time = 8 * 60 * 60

    def __int__(self, name):
        self.name = name

    def can_repeat(self, sleep_time):
        if sleep_time >= self.normal_sleep_time:
            result = True
        else:
            result = False

        return requests