"""
Author: Ayelet Raful
This program reads a poem from a file, then reverses the poem and writes it into a different file. Then the reversed poem is read and
appended to it is the reason why I like this poem.
Basic Pseudocode:
1. Choose a poem and copy it into poem.txt
2. Create the file structure and insert it into Pycharm
3. Import os and create 2 blank lists that will store the poem and the reversed poem
4. Read the poem from the file and print it
5. Reverse the poem
6. Write it into a different file
7.Read the reversed poem from the second file
8. Append to it why I like it
9. Call all the functions
"""



# Importing os
import os
#Creating blank lists to read the poem and reversed poem into them
poem = []
reversed_poem = []
"""
This function reads the poem from the file and appends it to a blank list. It has a parameter of file so that it
can be used to read two different files
"""
def reading_poem(file):
    # Referencing the file using os.path.join so that it will work on all operating systems
    with open(os.path.join("docs", file), "r") as f:
        # Using a for loop to append the read poem to a list
        for line in f:
            line = line.strip()
            # Appending it to list
            poem.append(line)
            # Printing the pome
            print(line)

"""This function reverses the poem using a while loop"""
def reversing_poem():
    # Accessing the last line of the poem by calculating the length of the poem and subtracting one to reach the last index
    index = len(poem) - 1
    # Using a while loop to iterate through each line in the poem
    while index >= 0:
        # Appending the reversed poem to a list
        reversed_poem.append(poem[index])
        # Calculating the next line to be appended to the list - by subtracting one from the current index
        index -= 1

"""Writing the reversed poem to the file poem2txt.txt"""
def write():
    # Using os.path.join to reference file location
    with open(os.path.join("docs", "poem2txt.txt"), "w") as p:
        # Using a for loop to write the reversed poem into the file poem2txt.txt
        for line in reversed_poem:
            # Writing in each line to the file
            p.write(line + "\n")

"""This function appends my name and why I like this poem into the file poem2txt.txt"""
def append():
    # Using os.path.join to reference the file location and appending to it
    with open(os.path.join("docs", "poem2txt.txt"), "a") as a:
        # Appending my answer to the file
        a.write(" \n I like this poem because it really hits home and nails exactly how I feel when I have to make decisions"
                "It is also especially relevant to my current stage of life where I have to make decisions that are long impacting."
                "- Ayelet Raful "
                )

# Calling all the functions with parameters when needed.
if __name__ == "__main__":
    reading_poem("poem.txt")
    print("")
    reversing_poem()
    write()
    reading_poem("poem2txt.txt")
    append()





