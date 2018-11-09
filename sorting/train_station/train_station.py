def is_possible(arrival_list): 
    """
    Determines whether a given arrival list (explained in the problem
    description) is possible or not.
    Args:
        arrival_list: A list denoting the labels of the trains in arrival 
            order
    Returns:
        is_possible: True if such an arrival order is possible in this
            problem, False if not
    """
    # Represents the largest labeled train that has arrived.
    largest_label_arrived = -1 
    # Represents the first train that came from the middle part after a sequence of 
    # trains, which have come directly from the left part.
    label_from_middle = -1 
    for train_label in arrival_list:
        # If the label of the current train is smaller than the largest label it means
        # that the train has come from the middle part.
        if train_label < largest_label_arrived: 
            # Given that the train came from the middle part, it must have a  
            # label smaller than the label of the first train that has come from 
            # the middle part, since the middle part operates in a LIFO fashion.
            if label_from_middle != -1 and train_label > label_from_middle:
                return False
           # No trains have come from the middle part after a sequence of trains 
           # that have come from the left part, until this train came.    
            elif label_from_middle == -1:
                label_from_middle = train_label
        # A train came from the left part, since it has the largest label.
        else:
            largest_label_arrived = train_label
        # If the label of the current train is greater than the label of the first 
        # train of a sequence of trains that have come from the middle part, it means
        # that those trains stopped coming, hence we reset to default.
        if train_label > label_from_middle:
            label_from_middle = -1
    return True

# Some test cases
print(is_possible([0, 1, 5, 4, 3, 7, 6, 2, 8, 9]))
print(is_possible([0, 1, 5, 3, 4, 7, 6, 2, 8, 9]))
print(is_possible([0, 3, 2, 1]))
print(is_possible([0, 3, 1, 2]))


        
        




        
    