import threading
import queue
from BruteForce.password import Password


class PwdProducer(threading.Thread):

    def __init__(self, queue, condition):
        threading.Thread.__init__(self)  # call to super constructor
        self.queue = queue
        self.condition = condition

    def run(self):
        password = input("Next Password: ")
        while True:

            self.condition.acquire()

            try:
                self.queue.put(Password(password), block=False)
                self.condition.notify()
            except:
                self.condition.wait()
            self.condition.release()
