if __name__ == "__main__":
    from queue import PriorityQueue

    events = set()
    dependencies = {}
    with open("seven/input.txt", "r") as dependencies_file:
        # build dependency dict
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
    while len(completed_events) != len(events):
        for event in remaining_events:
            can_complete = True
            if (event in dependencies):
                for dependency in dependencies[event]:
                    if dependency not in completed_events:
                        can_complete = False
                        break

            if (can_complete and event not in possible_events.queue):
                    possible_events.put(event)

        event = possible_events.get()
        remaining_events.remove(event)
        completed_events.append(event)

    print("Event Order: {}".format("".join(completed_events)))
        