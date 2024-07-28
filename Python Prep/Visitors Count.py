##A manager hires a staff member to keep a record of the number of men, women, and children visiting the museum daily.
##The staff will note W if any women visit, M for men, and C for children. You need to write code that takes the string that represents the visits and
##prints the count of men, woman and children. The sequencing should be in decreasing order.
##Example:
##
##Input:
##WWMMWWCCC
##
##Expected Output:
##4W3C2M
##
##Explanation:
##‘W’ has the highest count, then ‘C’, then ‘M’.


def count_visitors(visits):
    # Count the number of men, women, and children
    num_women = visits.count('W')
    num_men = visits.count('M')
    num_children = visits.count('C')
    
    # Create a dictionary to store the counts
    counts = {'W': num_women, 'M': num_men, 'C': num_children}

    print(counts,"1")
    
    # Sort the counts in decreasing order
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)

    print(sorted_counts,"a")
    
    # Build the output string
    output_str = ''
    for item in sorted_counts:
        output_str += str(item[1]) + item[0]
    
    # Print the output string
    print(output_str)

# Example usage
count_visitors('WWMMWWCCCCC')
