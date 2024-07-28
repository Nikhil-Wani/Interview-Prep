def group_duplicates(input_list):
    result = []
    unique_elements = set(input_list)
    for element in unique_elements:
        count = input_list.count(element)
        result.append([element] * count)
    return result

input = [1,2,3,3,4,2]
output = group_duplicates(input)
print(output)

##op = [[1],[2,2],[3,3],[4]]
