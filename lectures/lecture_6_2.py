#Hopfield nets 0-----0
                  #2.1 0 would minimize the weight (if negative put 1)


#Print all combinations of numbers 0-2 and 0-3 and letters E,n,g
for i in range(3):
    for j in range(4):
        print("About to print all combinations of", i, j, "and a letter")
        for letter in ["E", "n", "g"]:
            print(i, j, letter)

#print out all the possible 5-letter combinations of ["a b c d"]
alphabet = ["a", "b", "c", "d"]

for letter1 in alphabet:
    for letter2 in alphabet:
        for letter3 in alphabet:
            for letter4 in alphabet:
                for letter5 in alphabet:
                    print(letter1 + letter2 + letter3 + letter4 + letter5)