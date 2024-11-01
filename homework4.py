#2.1
one_through_twenty = []
for i in range(20):
    one_through_twenty.append(i+1)
print(one_through_twenty)

#2.2
def square(numbers):
    second_power = []
    for element in numbers:
        second_power.append(element**2)
    return second_power

one_through_twenty_squared = square(one_through_twenty)
print(one_through_twenty_squared)

#2.3
def first_fifteen(numbers):
    fifteen = numbers[0:15]
    return fifteen

first_fifteenOf_twenty = first_fifteen(one_through_twenty)
print(first_fifteenOf_twenty)

#2.4
list_squared = square(one_through_twenty)
def five_strider(list_squared):
    fifths=list_squared[0:len(list_squared):5]
    return fifths
stride_five = five_strider(list_squared)
print(stride_five)

#2.5
one_through_fifty=[]
for i in range(50):
    one_through_fifty.append(i+1)
print(one_through_fifty)

new_list = square(one_through_fifty)

def slice_and_stride(new_list):
    x=len(new_list)
    third_back = new_list[:x-30:-3]
    return third_back
third_back = slice_and_stride(new_list)
print(third_back)

#3.1
def create_2D_list():
    list = []
    for i in range(5):
        list2 = []
        for x in range(5):
            list2.append(5*i+x+1)
        list.append(list2)
    return list
matrix = create_2D_list()
print(matrix)

