def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    result=[]
    
    numbers = {}
    
    for item in arrays[0]:
        numbers[item] = 1
    for arr in arrays[1:]:
        for item in arr:
            if item in numbers:
                numbers[item] += 1
    for number in numbers:
        if numbers[number] == len(arrays):
            result.append(number)
    return result

if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
