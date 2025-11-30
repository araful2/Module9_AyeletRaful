"""
Author: Ayelet Raful
This program reads a poem from a file, then reverses the poem, replaces the word "I" with "we" and writes it into a different file.
Then the reversed poem is read and appended to it is the reason why I like this poem.
Pseudocode:
1. Choose a poem and copy it into poem_original.txt and create a file that will store the remixed poem
2. Create the file structure and insert it into Pycharm
3. Import os and create 2 blank lists that will store the poem and the remixed poem
4. Read the poem from the file using a for loop to iterate through each line and save it to a list and then print the poem from the list
5. Reverse the poem using a while loop and "len" to access the last line of the poem and then reverse it
6. Modify the poem save in the list and replace "I" with "we" using a for loop to iterate through every string in the list.
7. Use the replace method to replace "I" with "we"
6. Write the remixed pome into a different file using a for loop to iterate through the list
7. Read the remixed poem from the second file and print it
8. Append to poem what I changed using "a"
9. Call all the functions
"""



# Importing os
import os
#Creating blank lists to read the poem and reversed poem into them
poem = []
remixed_poem = []



def reading_poem(file):
    """
    This function reads the poem from the file and appends it to a blank list. It has a parameter of file so that it
    can be used to read two different files.
    """
    try:
    # Referencing the file using os.path.join so that it will work on all operating systems, and reading it in.
        with open(os.path.join("docs", file), "r") as f:
            # Using a for loop to append the read poem to a list
            for line in f:
                line = line.strip()
                # Appending it to list
                poem.append(line)
                # Printing the poem
                print(line)
    except FileNotFoundError as err:
        print("File not found", err)



def reversing_poem():
    """This function reverses the poem using a while loop"""
    # Accessing the last line of the poem by calculating the length of the poem and subtracting one to reach the last index.
    index = len(poem) - 1
    # Using a while loop to iterate through each line in the poem
    while index >= 0:
        # Appending the reversed poem to a list
        remixed_poem.append(poem[index])
        # Calculating the next line to be appended to the list - by subtracting one from the current index
        index -= 1


def modifying_poem():
    """This function replaces 'I' with 'we' in the poem"""
    # Using a for loop to iterate through each string in the list
    for ch in range(len(remixed_poem)):
        # Editing the remixed_poem list and replacing I with we
        remixed_poem[ch] = remixed_poem[ch].replace("I","We")



def write():
    """Writing the reversed poem to the file poem_remix.txt"""
    try:
        # Using os.path.join to reference file location
        with open(os.path.join("docs", "poem_remix.txt"), "w") as p:
            # Using a for loop to write the reversed poem into the file poem_remix.txt
            for line in remixed_poem:
                # Writing in each line to the file
                p.write(line + "\n")
    except FileNotFoundError as err:
        print("File not found", err)



def append():
    """This function appends my name and why I like this poem into the file poem_remix.txt"""
    try:
        # Using os.path.join to reference the file location and appending to it.
        with open(os.path.join("docs", "poem_remix.txt"), "a") as a:
            # Appending my answer to the file
            a.write(" \n ---\n"
                    "Remixed by: Ayelet Raful\n"
                    "I reversed the order of the poem and I replaced all the 'I's with 'we'. "
                    )
    except FileNotFoundError as err:
        print("File not found", err)


# Calling all the functions with parameters when needed.
if __name__ == "__main__":
    reading_poem("poem_original.txt")
    print("")
    reversing_poem()
    modifying_poem()
    write()
    reading_poem("poem_remix.txt")
    append()





