# Question 3

import os
print(os.getcwd())
f = open("labs/data2.txt")

text = f.readlines()

for line in text:
    line = line.lower()
    if "lol" in line:
        print(line)

# Question 4

def dict_to_str(d):
    """Return a str containing each key and value in dict d. Keys and
    values are separated by a comma. Key-value pairs are separated
    by a newline character from each other.
    For example, dict_to_str({1:2, 5:6}) should return "1, 2\n5, 6".
    (the order of the key-value pairs doesn't matter and can be different
    every time).
    """
    
    for key,value in d.items():
        print(f"{key}, {value}")

# Question 5

L = [4, 1, 6]
L1 = sorted(L) # L1 is [1, 4, 6]

def dict_to_str_sorted(d):
    """Return a str containing each key and value in dict d. Keys and
    values are separated by a comma. Key-value pairs are separated
    by a newline character from each other, and are sorted in
    ascending order by key.
    For example, dict_to_str_sorted({1:2, 0:3, 10:5}) should
    return "0, 3\n1, 2\n10, 5". The keys in the string must be sorted
    in ascending order."""
    
    # Sort the keys
    sorted_keys = sorted(d.keys())
    
    # Create a list to store the formatted key-value strings
    key_value_pairs = [f"{key}, {d[key]}" for key in sorted_keys]
    
    # Join each pair with a newline character and return the result
    return "\n".join(key_value_pairs)

# Question 6

# Part A)

def word_counter(filename):
    f = open("labs/" + filename + ".txt")

    text = f.read()
    split_text = text.split()

    word_count_dict = {}

    for word in range(len(split_text)):
        if split_text[word] in word_count_dict == False:
            word_count_dict[split_text[word]] = 1
        else:
            word_count_dict[split_text[word]] += 1
    
    return word_count_dict

# Part B)    

def top10(L):
    res = L[:9]

    for given_nums in range(len(L)):
        for i in range(len(res)):
            if L[given_nums] > res[i]:
                res[i] = L[given_nums]
    
    return res

# Part C)

def top_ten_words(filename):
    word_count = word_counter(filename)

    count_word = {}

    for word,count in word_count.items():
        count_word[count] = word

    sorted_list = sorted(count_word.items())

    for i in range(9):
        print(i+ 1, sorted_list[i], "\n")

# Question 7 see hello.html

# Question 8

def number_search_results(search_term):
    import urllib.request
    f = urllib.request.urlopen("https://ca.search.yahoo.com/search?p=" + search_term)
    page = f.read().decode("utf-8")
    f.close()
    print(page)