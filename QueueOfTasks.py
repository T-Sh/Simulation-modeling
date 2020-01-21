from queue import Queue
from distributions import *


class Task(object):
    arrival_time = 0.0
    service_time = 0.0
    waiting_time = 0.0

    def __init__(self, current_time, middle_processing_time, middle_arrival_time):
        self.arrival_time = current_time + exp_dist(middle_arrival_time)
        self.service_time = exp_dist_proc(middle_processing_time)

    def calc_waiting_time(self, global_time):
        self.waiting_time = max(global_time, self.arrival_time) - self.arrival_time
        return self.waiting_time


class QueueOfTasks(object):
    fail = 0
    ready = 0
    all_tasks = 0
    time = 0.0
    waiting_time = 0.0
    time_in_system = 0.0
    size_of_queue = 0
    cur_task_in_queue = []
    avr_cur_task_in_queue = []

    def __init__(self, count_of_tasks=34, middle_processing_time=25, middle_arrival_time=10):
        self.tasks = Queue(count_of_tasks)
        self.middle_processing_time = middle_processing_time
        self.middle_arrival_time = middle_arrival_time
        self.exp_dist_prc = []
        self.exp_dist_arrive = []
        self.fail = 0
        self.ready = 0
        self.all_tasks = 0
        self.time = 0.0
        self.waiting_time = 0.0
        self.time_in_system = 0.0
        self.size_of_queue = 0
        self.cur_task_in_queue = []
        self.avr_cur_task_in_queue = []

    def __del__(self):
        while self.tasks.qsize() > 0:
            self.tasks.get()

    def input(self):
        task = Task(self.time, self.middle_processing_time, self.middle_arrival_time)
        self.exp_dist_prc.append(task.service_time)
        self.exp_dist_arrive.append(task.arrival_time)
        self.time = task.arrival_time
        self.all_tasks += 1
        if self.tasks.qsize() < self.tasks.maxsize:
            self.tasks.put(task)
        else:
            self.fail += 1
        self.size_of_queue += self.tasks.qsize()

    def output(self, global_time):
        task = self.tasks.get()
        self.waiting_time += task.calc_waiting_time(global_time)
        self.time_in_system += task.service_time
        self.ready += 1
        return task

    def current_tasks(self):
        self.cur_task_in_queue.append(self.tasks.qsize())
        self.avr_cur_task_in_queue.append(self.size_of_queue / self.time)
