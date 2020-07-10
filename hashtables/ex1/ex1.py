def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

    cache = {}
    for i in range(len(weights)):
        cache[weights[i]] = i
    for i in range(len(weights)):
        weig = limit-weights[i]
        if weig in cache:
            return (max(i, cache[weig]), min(i, cache[weig]))

    return None
