#Open file in write mode
file = open('NewFile.txt', 'w')
#Write to file
file.write("This is a new file!!!\n")
#Close file
file.close()


# Open a file in read mode
file = open('NewFile.txt', 'r')
# Read the contents of the file
content = file.read()
# Print the contents of the file
print(content)
# Close the file
file.close()


# Open file in append mode
file = open('NewFile.txt', 'a')
# Write to file
file.write("This is my second line!!!")
# Close file
file.close()

file = open('NewFile.txt', 'r')
content = file.read()
print(content)
file.close()

# with statement
with open('NewFile.txt', 'a') as file:
    file.write("This is my third line!!!")

with open ('NewFile.txt', 'r') as file:
    content = file.read()
    print(content)


# Read one line
with open ('NewFile.txt', 'r') as file:
    content = file.readline()
    print(content)
