
# write a python program to count the number of even and odd numbers from a series of numbers


series=(1,3,4,6,7,9,12,14,15,17)

count_odd=0
count_even=0
for i in series:
    if not i%2:
        count_even+=1
    else:
        count_odd+=1

print('number of even numbers  : ',count_even)
print('number of odd numbers  :  ',count_odd)            