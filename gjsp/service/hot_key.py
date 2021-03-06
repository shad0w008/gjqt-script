import logging
import time
from threading import Thread
from typing import Dict
from functional import seq
from pyhooked import Hook, KeyboardEvent

from gjsp.service.even_loop import EvenLoop

_logger = logging.getLogger("even_loop")


# _press_key_file = open("D:/press_key.txt", "a")


class HotKey:
    def __init__(self):
        self.hk = Hook()
        self.handler: Dict[str, EvenLoop] = {}
        self.thread = None

    def add_handler(self, even_loop: EvenLoop):
        assert even_loop.key() not in self.handler, "exists:%s" % (even_loop.key())
        self.handler[even_loop.key()] = even_loop

    def start_hook(self):
        def handle_events(args: KeyboardEvent):
            key = args.current_key
            if key not in self.handler or not args.event_type == 'key up':
                return
            handlers = seq(self.handler.values())
            if handlers.exists(lambda x: x.is_run):
                handlers.for_each(lambda x: x.set_stop())
            else:
                handlers.filter(lambda x: x.key() == key).for_each(lambda x: x.update())

        self.hk.handler = handle_events
        self.thread = Thread(target=lambda: self.hk.hook())
        self.thread.start()

    def run_even_loop(self):
        while True:
            runed_even: EvenLoop = seq(self.handler.values()).find(lambda x: x.is_run)
            if runed_even is None:
                time.sleep(0.1)
            else:
                runed_even.run()
                runed_even.delay()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)


    class TestEvenLoop(EvenLoop):

        def run(self):
            print("123")
            time.sleep(1)

        def clear(self):
            print("clear")


    hot_key = HotKey()
    hot_key.add_handler(TestEvenLoop(name="test", key="F5"))
    hot_key.start_hook()
    hot_key.run_even_loop()
