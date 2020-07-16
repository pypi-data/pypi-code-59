from multiprocessing import Process, SimpleQueue, Value
import time
import random
import numpy as np

__all__ = ["DataLoader"]


class StopGenerator:
    def __init__(self, pid=None):
        self.pid = pid


def default_collate(batch):
    if batch is None or not isinstance(batch, list) or len(batch) == 0:
        return batch

    result = [[] for _ in range(len(batch[0]))]
    for items in batch:
        for idx, item in enumerate(items):
            result[idx].append(item)

    result_cvt = []
    for i in range(len(result)):
        if isinstance(result[i][0], np.ndarray):
            result_cvt.append(np.stack(result[i]))
        elif isinstance(result[i][0], float) or isinstance(result[i][0], int):
            result_cvt.append(np.array(result[i]))
        else:
            result_cvt.append(result[i])

    return tuple(result_cvt)


class DataLoader:
    def __init__(self, generator, batch_size=0, maxsize=-1, shuffle=False, num_worker=1, collate_fn=default_collate,
                 seed=None):
        self.generator = generator
        self.batch_size = max(0, int(batch_size))
        self.num_worker = max(1, int(num_worker))
        self.maxsize = min(1, self.batch_size) * self.num_worker * 2 if maxsize < 0 else maxsize
        self.collate_fn = collate_fn
        self.shuffle = shuffle
        self.seed = seed

    def __iter__(self):
        def sample_generator(generator, data_queue, count, tid):
            if self.seed is not None:
                random.seed(self.seed + tid)
                np.random.seed(self.seed + tid)

            idx_ls = list(range(len(generator)))
            if self.shuffle:
                random.shuffle(idx_ls)

            for i in idx_ls:
                if i % self.num_worker != tid:
                    continue

                while count.value >= self.maxsize > 0:
                    time.sleep(0.02)
                    continue

                data_queue.put(generator[i])
                with count.get_lock():
                    count.value += 1

            data_queue.put(StopGenerator(pid=tid))
            with count.get_lock():
                count.value += 1

        data_queue = SimpleQueue()
        count = Value('i', 0)

        process_map = dict()
        for tid in range(self.num_worker):
            process = Process(target=sample_generator, args=(self.generator, data_queue, count, tid))
            process.daemon = True
            process.start()
            process_map[tid] = process

        def single_generator():
            while len(process_map) > 0:
                item = data_queue.get()
                with count.get_lock():
                    count.value -= 1

                if isinstance(item, StopGenerator):
                    del process_map[item.pid]
                    continue

                yield item

        def parallel_generator():
            result = []
            while len(process_map) > 0:
                item = data_queue.get()
                with count.get_lock():
                    count.value -= 1

                if isinstance(item, StopGenerator):
                    del process_map[item.pid]
                    continue

                result.append(item)
                if len(result) >= self.batch_size:
                    if self.collate_fn is not None:
                        result = self.collate_fn(result)

                    yield result
                    result = []

        return parallel_generator() if self.batch_size else single_generator()
