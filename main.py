file = open("file12.txt", "w")
file.write("First row in")
file.write("\n")
file.write("Second row in")
file.close()

content= """
First row is the second 


THird one is none 

when 3 brackets are here"""

file.write(content)
file.close()

with open("file8.txt", "w") as file:
  file.write(content)
  file.write("\nmore\nand\nmore")