from ipaddress import summarize_address_range


num_choco = 60
num_people = 4
sum_of_products = 0
count = 1

# Finding the sum of products
while count <= num_people:
    sum_of_products = sum_of_products + (count * 2)
    count += 1

print(sum_of_products)


# Checking how many times the chocolate can be distributed
count1 = 0

while num_choco >= sum_of_products:
     
    num_choco = num_choco - sum_of_products
    count1 += 1

#adding the total number of chocolate per person

array = []

for k in range (1, (num_people + 1)):
    array.append(2*k*count1)


print(count1)

print(array)




