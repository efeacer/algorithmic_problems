# Train Station
## Problem Description:

- Given a T shaped train station:

    ```
    left part -> ------ * ------ <- right part
                        |
                        | -> middle part
                        |
 
    ```

    We have N trains labeled from 0 to N - 1 waiting in a line in the 
    left part of the station. A train with a smaller label waits closer
    to the front of the line. We want each train to get to the right part
    of the station. A train can go from the left part to the right part 
    directly, or it can go to the middle part, wait for an arbitrary amount
    of time and go to the right part. However, the middle part of the station
    operates in a last in first out (LIFO) fashion, meaning that if multiple 
    trains are waiting in the middle part, the train that was most recently 
    arrived can proceed to the right part first.

-   Given a list denoting the labels of trains arrived at the right
    part of the station starting (first label in the list is the label of
    the first train arrived and other labels in the list are ordered in the 
    same way), determine whether the arrival order is possible or not.

`train_station.py` : contains python implementation of the solution algorithm