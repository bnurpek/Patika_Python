#QUESTION 1

input = [[1, 'a',['cat'],2],[[[3]],'dog'],4,5]  #given example
flat_list = []

def flattener(input):

    for element in input:

        if isinstance(element, list):
            flattener(element)
        else:
            flat_list.append(element)

flattener(input)
print(flat_list)