if __name__ == "__main__":
    from queue import PriorityQueue

    events = set()
    dependencies = {}
    with open("seven/input.txt", "r") as dependencies_file:
        # build dependency dict and event set
        for dependency in dependencies_file.readlines():
            event = dependency[36]
            depends_on = dependency[5]

            events.add(event)
            events.add(depends_on)

            if (event not in dependencies):
                dependencies[event] = []
            
            dependencies[event].append(depends_on)

    completed_events = []
    remaining_events = list(events)
    possible_events = PriorityQueue()

    # create dict to keep track of workers
    events_in_progress = {}
    num_workers = 5
    for worker in range(num_workers):
        events_in_progress[worker] = tuple()

    print("Time\t" + "".join(["Worker {}\t".format(n+1) for n in range(num_workers)]))

    time = 0
    while len(completed_events) != len(events):
        # check all workers to see if they have finished events
        for worker in events_in_progress.keys():
            in_progress_event = events_in_progress[worker]

            # progress event if they're working on one
            if (in_progress_event != tuple()):
                if (in_progress_event[1] == 0):
                    events_in_progress[worker] = tuple()
                    completed_events.append(in_progress_event[0])
                else:
                    events_in_progress[worker] = (in_progress_event[0], in_progress_event[1] - 1)
        
        # check all remaining events to see if they can be worked on
        for event in remaining_events:
            can_complete = True
            if (event in dependencies):
                for dependency in dependencies[event]:
                    if dependency not in completed_events:
                        can_complete = False
                        break

            if (can_complete and event not in possible_events.queue):
                possible_events.put(event)

        # add events to workers with nothing to do
        for worker in events_in_progress.keys():
            in_progress_event = events_in_progress[worker]

            if (in_progress_event == tuple() and not possible_events.empty()):
                event = possible_events.get()
                remaining_events.remove(event)
                events_in_progress[worker] = (event, 60 + "ABCDEFGHIJKLMNOPQRSTUVWXYZ".index(event))

        print("{}\t".format(time) + "".join(["{}\t".format(events_in_progress[worker]) if len(events_in_progress[worker]) == 2 else "\t\t" for worker in events_in_progress.keys()]))
        
        time += 1

    print("Event Order: {}".format("".join(completed_events)))
    print("Time-to-Complete: {}".format(time - 1))