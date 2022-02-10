# Nightmare
# by @yi64
#
# threading tool
# source -> https://docs.python.org/3/library/threading.html
import threading


threads = []

def create_thread(handler, args=()) -> threading.Thread:
    thread = threading.Thread(target=handler, args=args, daemon=True)

    threads.append(thread)

    return thread

def run_thread(thread) -> None: 
    thread.start()

def run_all_threads() -> None:
    for thread in threads:
        run_thread(thread)
