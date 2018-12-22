from datetime import datetime as dt
from queue import PriorityQueue as pq

with open("four/input.txt", "r") as log_file:
    logs = [log.strip().lower() for log in log_file.readlines()]

    # parse logs to create time-based queue of events
    event_queue = pq()
    for log in logs:
        time = dt.strptime(log[1:17], "%Y-%m-%d %H:%M")

        action_char = log[19] # char at index 19 is g/w/f for guard, wake up, or fall aseleep
        event = tuple() # time, event char, parameter (guard number)
        if (action_char == 'g'):
            # split the log into sections, and select the guard number (minus the # sign)
            guard_num = int(log.split()[3][1:])
            event = (time, action_char, guard_num)
        else:
            event = (time, action_char, 0)

        event_queue.put(event)

    # parse queue of events to create list of times asleep for guards
    guards = {}
    current_guard = -1
    last_fell_asleep = dt(1500, 1, 1)
    while not event_queue.empty():
        event = event_queue.get()
        event_time = event[0]

        if (event[1] == 'g'):
            current_guard = event[2]
        elif (event[1] == 'f'):
            last_fell_asleep = event_time
        elif (event[1] == 'w'):
            if (current_guard not in guards):
                # guards in dict contain list of minutes for 00:00 to 00:59
                # list contains # of times asleep for that minute
                guards[current_guard] = [0 for _ in range(0, 59)]
            
            for minute in range(last_fell_asleep.minute, event_time.minute):
                guards[current_guard][minute] += 1

    # strategy 1
    # calculate guard who slept most
    longest_sleeper = tuple()
    longest_sleeper_time = 0
    for guard in guards.keys():
        ss = guards[guard] # sleep schedule
        sleep_time = sum(ss)
        if (sleep_time > longest_sleeper_time):
            longest_sleeper = (guard, ss)
            longest_sleeper_time = sleep_time

    # calculate minute most slept
    minute_most_slept = longest_sleeper[1].index(max(longest_sleeper[1]))

    print("== Strategy 1 ==")
    print("Longest Sleeping Guard: {}\nMinute Most Slept: {}\nProduct: {}".format(longest_sleeper[0], minute_most_slept, longest_sleeper[0] * minute_most_slept))
    
    # strategy 2
    # calculate guard with most frequent time asleep
    chosen_guard = tuple()
    max_minute_freq = 0
    for guard in guards.keys():
        ss = guards[guard] # sleep schedule
        guard_max_minute_freq = max(ss)
        if (guard_max_minute_freq > max_minute_freq):
            most_frequent_minute = ss.index(max(ss))
            max_minute_freq = guard_max_minute_freq
            chosen_guard = (guard, most_frequent_minute)
    
    print("== Strategy 2 ==")
    print("Longest Sleeping Guard: {}\nMinute Most Slept: {}\nProduct: {}".format(chosen_guard[0], chosen_guard[1], chosen_guard[0] * chosen_guard[1]))
    