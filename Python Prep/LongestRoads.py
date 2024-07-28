##A startup company E-Motors is building driverless automated cars.
##The car contains a sensor that checks the road quality for the next N meters to decide the optimal speed at which the cars should move.
##We are given recorded data by the sensor in the form of an array, where each element of the array is the rating given to 1 meter of the road in sequence.
##
##The rating given by the sensor is from 1 to 100, where 100 represents the road with the best condition, and any rating above 60 is optimal.
##Find the longest stretch of road in meters that is categorized as optimal by the sensor.
##
##The input is an array of "strings" which needs to be converted from string to integer/number inside the function.


def longest_optimal_stretch(ratings):
    # Convert the array of strings to an array of integers
    ratings = list(map(int, ratings))
    
    # Initialize variables to track the longest optimal stretch
    current_optimal_stretch = 0
    longest_optimal_stretch = 0
    
    # Iterate through the ratings and count the optimal stretches
    for rating in ratings:
        if rating > 60:
            current_optimal_stretch += 1
        else:
            # Update the longest optimal stretch if the current one is longer
            longest_optimal_stretch = max(longest_optimal_stretch, current_optimal_stretch)
            current_optimal_stretch = 0
    
    # Return the length of the longest optimal stretch
    return longest_optimal_stretch

# Example usage
ratings = ['50', '70', '80', '90', '30', '75', '85']
print(longest_optimal_stretch(ratings)) # Output: 3
