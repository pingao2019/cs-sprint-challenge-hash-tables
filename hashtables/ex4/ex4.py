def has_negatives(a):
    """
    YOUR CODE HERE
    """
    
    # Your code here
    
    num_count = {}
     
    pair = []     
    for item in a:
        
        item = abs(item)
        if item not in num_count:
            
            num_count[item] = 1
        else:
            
            num_count[item] +=1

    
    for item in num_count:
        if num_count[item] == 2:
            
            pair.append(item)
    return pair

    return result
    


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
