from math import floor

input = [[1,2],[3,4],[5,6,7]]

def reverser(input):
    
    m = floor(len(input)/2)
    for i in range(m):
        temp = input[i]
        input[i] = input[-(i+1)]
        input[-(i+1)] = temp

    for i in range(len(input)):
        if isinstance(input[i], list):
            input[i] = reverser(input[i])
    
    return input

output = reverser(input)
print(output)