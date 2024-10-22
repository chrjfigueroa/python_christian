# while loop demo
counter = 10
while counter > 0:
    print("Slay")
    counter -= 1

# for loop demo
sum_of_fifty = 0
for i in range(1,51):
    sum_of_fifty += i
print(sum_of_fifty)    

# iterative for loop
list_of_names = ['pranathi', 'charlie', 'mira', 'katie', 'brianna']
for name in list_of_names:
    print(len(name))

# loops inside loops
for i in range(2,4):
    for j in range(9,15):
        print(i,j)
    