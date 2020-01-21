class Device(object):
    id_num = 0
    time_of_process = 0.0
    finishing_time = 0.0

    def __init__(self, id_num):
        self.id_num = id_num

    def in_process(self, service_time, global_time):
        self.time_of_process += service_time
        self.finishing_time = global_time + service_time
        return self.finishing_time

    def __lt__(self, other):
        if self.finishing_time == other.finishing_time:
            return self.id_num < other.id_num
        return self.finishing_time < other.finishing_time


class ListOfDevices(object):
    devices = []
    time = 0.01
    tasks_in_system = 0
    counter = 0
    cur_task_in_dev = []
    avr_cur_task_in_dev = []
    coefficients_dev = []

    def __init__(self, count_of_devices=5):
        self.devices = []
        self.time = 0.01
        self.tasks_in_system = 0
        self.counter = 0
        self.cur_task_in_dev = []
        self.avr_cur_task_in_dev = []
        self.coefficients_dev = []
        for i in range(count_of_devices):
            device = Device(i)
            self.devices.append(device)

    def __del__(self):
        while len(self.devices) > 0:
            self.devices.pop()

    def in_process(self, task):
        pos = min(self.devices).id_num
        self.devices[pos].finishing_time = max(self.devices[pos].finishing_time, task.arrival_time) + task.service_time
        self.devices[pos].time_of_process += task.service_time
        self.time = min(self.devices).finishing_time

    def calc_busy(self, global_time):
        for i in self.devices:
            if i.finishing_time >= global_time:
                self.tasks_in_system += 1
        self.counter += 1

    def stat(self, global_time):
        return tuple([round(i.time_of_process / max(max(self.devices).finishing_time, global_time) * 100, 3)
                      for i in self.devices])

    def current_tasks(self, global_time):
        temp_dev = 0
        for i in self.devices:
            if i.finishing_time >= global_time:
                temp_dev += 1
        self.cur_task_in_dev.append(temp_dev)
        self.avr_cur_task_in_dev.append(self.tasks_in_system / 2 / self.counter if self.counter > 0 else 1)

    def coefficients(self):
        self.coefficients_dev.append(sum(self.stat(self.time)) / len(self.devices))
