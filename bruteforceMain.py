import threading
import queue
from BruteForce.pwdConsumer import PwdConsumer
from BruteForce.pwdProducer import PwdProducer


queue = queue.Queue(maxsize=10)
condition = threading.Condition()

producer = PwdProducer(queue, condition)
consumer = PwdConsumer(queue, condition)

producer.start()
consumer.start()


