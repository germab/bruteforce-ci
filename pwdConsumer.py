import threading
import queue
import time
import itertools


class PwdConsumer(threading.Thread):

    def __init__(self, queue, condition):
        threading.Thread.__init__(self)
        self.queue = queue
        self.condition = condition

    def run(self):
        password = None
        while True:
            self.condition.acquire()
            try:
                password = self.queue.get(block=False)
                self.condition.notify()
            except queue.Empty:
                self.condition.wait()
            self.condition.release()

            your_list = 'abc'
            complete_list = []
            for current in range(5):
                a = [i for i in your_list]
                for y in range(current):
                    a = [x + i for i in your_list for x in a]
                complete_list = complete_list + a
                if password.check(a):
                    print("" + a + len(complete_list))
                    break

            #if not password is None:
             #   print("Testing with '123' = " + str(password.check("123")))
