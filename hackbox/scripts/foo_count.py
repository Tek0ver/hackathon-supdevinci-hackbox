from time import sleep

def foo_count(tick=2, max=60):

    print(f"Start counter for {max} ticks, with tick of {tick} seconds")

    counter = 0

    while counter <= max:
        sleep(tick)
        counter += 1
        print(f"Counter = {counter}")

    print("Counter ended")
