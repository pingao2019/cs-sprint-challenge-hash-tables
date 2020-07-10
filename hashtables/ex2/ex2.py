#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here

    route = []
    connect = {}

    for Ticket in tickets:
        connect[Ticket.source] = Ticket.destination

        if Ticket.source == 'NONE':
            route.append(Ticket.destination)

    for i in range(length):
        route.append(connect[route[i]])

        if connect[route[i]] == 'NONE':
            break


    return route
