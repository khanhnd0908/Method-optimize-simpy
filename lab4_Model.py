import random
import simpy


class Agent(object):
    def __init__(self, appear_time):
        self.appear_time = appear_time
        self.start_work_time = -1
        self.finish_work_time = -1

    def start_work(self, start_work_time):
        self.start_work_time = start_work_time

    def finish_work(self, finish_work_time):
        self.finish_work_time = finish_work_time


class Log(object):  # для печати информации об агенте и блоке
    def __init__(self, time, size):
        self.time = time
        self.size = size


class Block(object):
    def __init__(self):
        self.logs = [Log(0, 0)]

    def last_size(self):
        return self.logs[-1].size


class Work(Block):  # Calculate working time
    def start_work(self, agent):
        self.logs.append(Log(agent.start_work_time, self.last_size() + 1))

    def finish_work(self, agent):
        self.logs.append(Log(agent.finish_work_time, self.last_size() - 1))


class Queue(Block): # Calculate queueing time
    def in_queue(self, agent):
        self.logs.append(Log(agent.appear_time, self.last_size() + 1))

    def start_work(self, agent):
        self.logs.append(Log(agent.start_work_time, self.last_size() - 1))


class SMO(object):
    def __init__(self):
        self.worker = simpy.Resource(env, staff)

    def work(self, agent):
        agent.start_work(env.now)
        work_block.start_work(agent)
        queue_block.start_work(agent)

        if random.random() < error_possibility:
            yield env.timeout(random.randint(error_time - error_time_delta,
                                             error_time + error_time_delta))
        else:
            yield env.timeout(random.randint(average_working_time - average_working_time // 2,
                                             average_working_time + average_working_time // 2))
        agent.finish_work(env.now)
        work_block.finish_work(agent)

    def request_for_work(self, agent):
        with self.worker.request() as request:
            yield request
            yield env.process(self.work(agent))


def run_smo():
    smo = SMO()
    while True:
        agents.append(Agent(env.now))
        queue_block.in_queue(agents[-1])
        env.process(smo.request_for_work(agents[-1]))
        yield env.timeout(random.randint(average_start_time - average_start_time // 2,
                                         average_start_time + average_start_time // 2))


staff = 7
average_start_time = 50
average_working_time = 150

error_possibility = 0.2
error_time = 400
error_time_delta = 25

modeling_time = 5000

random_seed = 273973
random.seed(random_seed)

agents = []
work_block = Work()
queue_block = Queue()

env = simpy.Environment()
env.process(run_smo())
env.run(until=modeling_time)

in_work_time = [agent.finish_work_time - agent.start_work_time for agent in agents if agent.finish_work_time >= 0]
in_queue_time = [agent.start_work_time - agent.appear_time for agent in agents if agent.start_work_time >= 0]

in_work_size = [0] * modeling_time
for agent in agents:
    for i in range(agent.start_work_time, agent.finish_work_time):
        in_work_size[i] += 1
in_queue_size = [0] * modeling_time
for agent in agents:
    for i in range(agent.appear_time, agent.start_work_time):
        in_queue_size[i] += 1

mean_time_work = sum(in_work_time) / len(in_work_time)
mean_time_queue = sum(in_queue_time) / len(in_queue_time)
mean_size_work = sum(in_work_size) / len(in_work_size)
mean_size_queue = sum(in_queue_size) / len(in_queue_size)

print(f"Mean working time:        {mean_time_work:.5f} (second)")
print(f"Mean queueing time:       {mean_time_queue:.5f} (second)")
print(f"Mean of client :  {mean_size_work:.5f}")
print(f"Mean queue size in queue:          {mean_size_queue:.5f}")
print(f"Performance's rate:       {100 * mean_size_work / staff:.5f}%")


