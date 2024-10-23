L = [["E", "n", "g"], 
     ["S", "c", "i"]]
#want to print all possible entires. But want to prnt E, n, g, S
# print out all the elements one-by-one

def print_L(L):
    for i in range(len(L)):
        for j in range(len(L[0])):
            print("Coords:", i, j, "Value:", L[i][j])

def print_L_column_major(L):
    for j in range(len(L[0])):
        for i in range(len(L)):
            print("Coords:", i, j, "Value:", L[i][j])

#L.extend is like a loop for .append
#L.append for multiple numbers just adds another list into the chosen list

code = print("hi")

exec(code) #will execute print("hi") since variable code is python code

code = ""
for i in range(100):
    code += f"print({i});"

exec(code) 

for i in range(25):
    line ="" * i + f"for char{i} i alphabet:\n"
    code += line

line = " " * (i + 1)
line += "print("
for i in range(25):
    line += f"char{i} + "
line += "'')\n"

code += line