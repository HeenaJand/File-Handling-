##Task 1 Write sale record to  file

sales=[1200,450,980,1500,3000]

# Write each sale on a new line in the sales_data.txt file

with open("sales_data.txt","w") as file:
    for sale in sales:
        file.write(str(sale)+",")#content separated by comma's

# file closed automatically by using with open() 

# Now Reopen the file and print its content.
with open("sales_data.txt","r") as file:
   content= file.read()
print("Content of sales_data.txt :")
print(content)

# Task2: Read file in different ways 

#Read the entire file using read() and print it
with open("sales_data.txt", "r") as file:
    content=file.read()
    print("Content of Entire file using .read() :")
    print(content)


#Read the first line using.readline()

with open("sales_data.txt","w") as file:
    for sale in sales:
        file.write(str(sale)+"\n")
with open("sales_data.txt","r") as file:
    first_line= file.readline()
    print("First Line using .readline()")
    print(first_line)

#Read all lines and convert it into integer 

with open("sales_data.txt","r") as file:
    lines = file.readlines()
    sales_list=[]
    
    for line in lines:
        values=line.strip().split(",")
        for v in values:
            if v:
                sales_list.append(int(v))
                
print(" All lines using .readlines() and convert it into list of Integers")
print(sales_list)

#Task3: Append new sales

new_sales=[5000,2500,1700]
with open("sales_data.txt","a") as file:
    for sale in new_sales:
        file.write(str(sale)+"\n")

#Reopen and print updated file

with open("sales_data.txt","r") as file:
    updated_content= file.read()
    print(updated_content)
with open("sales_data.txt","r") as file:
    total_lines= len(file.readlines())
    print("Total number of lines after appending", total_lines)

# Task4: Generate summary report from file

# Read all sale values from sales_data.txt file

file = open("sales_data.txt","r")
data = file.read()
print(data)
file.close()

#Convert them into integers

with open("sales_data.txt","r") as file:
    content_str= file.read().split(",")
    content_int= [int(i) for i in content_str if i!=""]
print(f"Successfully converted to integer")

# calculate and print

total_sales= sum(sales)
highest_sales=max(sales)
lowest_sales=min(sales)
average_sales=total_sales/len(sales)

print(total_sales)
print(highest_sales)
print(lowest_sales)
print(average_sales)

#Task 5 Create product info file ( user input)

with open("products.txt","w") as file:
    for i in range(3):
        name = input("Enter the product name:")
        price= input("Enter the price of the product:")
        file.write(name    + "|" + price + "\n")

with open("products.txt","r") as file:
    print(" Product Details:")
    print(" *****************")
    for line in file:
        name,price= line.strip().split("|")
        print(f"{name : <10} | {price}")

# Task6: Read file safely ( Error Handling inside file handling only)

import os 

file_name= input("Enter the file name you want to open:") 
if os.path.exists(file_name):
    file = open(file_name,"r")
    data = file.read()
    file.close()
    print("\n File Content:")
    print(data)
else:
    print("File Not Found")

#Task 7: Mini Project- export discount prices

prices = { "Mouse" : 500, "Keyboard" : 800, "Monitor" : 7000, "Pendrive": 400, "Camera": 5000}

discount = int(input("Enter Discount Percentage:"))

with open("discount_report.txt","w") as file:
    file.write("Product| Original Price|Discounted Price \n")

    total_items = 0
    count= 0

    for item in prices:
        original= prices[item]
        discounted = original - (original*discount/100)

        file.write(f"{item} | {original} | {int(discounted)} \n")

        total_items += discounted
        count += 1
    average = total_items / count
    file.write("\n Total items: " + str(count))
    file.write(" \n Average Discounted Price :" + str(int(average)))


     # Read and print file

with open("discount_report.txt","r") as file:
    data= file.read()
    print("\n Discount Report: ")
    print("*******************")
    print(data)



