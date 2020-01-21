from ListOfDevices import *
from QueueOfTasks import *


def main(finish_condition, sys_state, count_of_devices=5, queue_size=34, process_time=25.0, arrival_time=10.0):
    global_time = 0.0
    cur_state = 0
    dev = ListOfDevices(count_of_devices)
    que = QueueOfTasks(queue_size, process_time, arrival_time)

    while True:
        if cur_state == 0:
            que.input()
        elif cur_state == 1:
            task = que.output(dev.time)
            dev.in_process(task)
            dev.calc_busy(global_time)
        global_time = min(que.time, dev.time)
        que.current_tasks()
        dev.current_tasks(max(que.time, dev.time))
        dev.coefficients()
        if que.time >= dev.time and not que.tasks.empty():
            cur_state = 1
        else:
            cur_state = 0
        if sys_state == 1:
            if global_time >= finish_condition:
                break
        else:
            if que.all_tasks >= finish_condition:
                break

    global_time = max(dev.time, que.time)
    dictionary = dict()
    dictionary['devices'] = dev.stat(global_time)
    dictionary['global_time'] = global_time
    dictionary['p'] = round(sum(dictionary['devices']) / len(dev.devices), 2)
    dictionary['Tq'] = round(que.waiting_time / que.ready, 5)
    dictionary['Ts'] = round((que.time_in_system + que.waiting_time) / que.ready, 5)
    dictionary['Nq'] = round(que.size_of_queue / que.time, 5)
    dictionary['Ns'] = round(dev.tasks_in_system / dev.counter / 2 + que.size_of_queue / que.time, 2)
    dictionary['Ca'] = (1-que.fail / que.all_tasks) / arrival_time
    dictionary['Cr'] = 1-que.fail / que.all_tasks
    return dictionary, que, dev
