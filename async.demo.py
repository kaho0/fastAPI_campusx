import asyncio
from timeit import default_timer as timer

async def run_task(name, seconds):
    print(f"Task {name} started, will take {seconds} seconds.")
    await asyncio.sleep(seconds)
    print(f"Task {name} completed.")

async def main():
    start = timer()
    await asyncio.gather(
        run_task("A", 2),
        run_task("B", 3),
        run_task("C", 1)
    )
    end = timer()
    print(f"All tasks completed in {end - start} seconds.")

asyncio.run(main())
