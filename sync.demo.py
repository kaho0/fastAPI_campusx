import time
from timeit import default_timer as timer
def run_task(name,seconds):
    print(f"Task {name} started, will take {seconds} seconds.")
    time.sleep(seconds)
    print(f"Task {name} completed.")
start=timer()
run_task("A",2)
run_task("B",3)
run_task("C",1)
end=timer()
print(f"All tasks completed in {end-start} seconds.")