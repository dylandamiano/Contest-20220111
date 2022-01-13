# CONTESTANT NUMBER: 0020011

from os import path

# Naming convention here is going to utilize 'snakeCase'
maxWords = 0 # Stores the maximum number of words that you can store
currentIndex = 0 # Stores the number words that are currently provided. Starts
readFile = True # Will change status of loop
writeFile = True # Will change status of loop

storedWords = []

print("Do you want to [read] the file or [write] to the file?")
currentPrompt = input()

# IF statement block below will run a segment of code depending on what the end-user wants to do
if (currentPrompt == "read"):
    writeFile = True
    readFile = False
elif (currentPrompt == "write"):
    writeFile = False
    readFile = True

print("How many words do you want to store? (Must put in integer form as a whole number!)")
currentPrompt = input()

print("You selected to store: " + currentPrompt + " words.")
maxWords = int(currentPrompt) # Prints max words selected by user

# This 'while' loop will run if the user chooses to write to the file
while (writeFile == False):
    print("Input word below: ")
    currentPrompt = input()

    print("Storing: " + currentPrompt + " into words.txt")
    storedWords.append(currentPrompt)

    '''
        The block of code below will see if 'words.txt' exists
        in the current directory. If it does not, then the program will
        break out of the execution loop.

        The block below will also determine if the maximum number of words has been reached
    '''

    if (path.exists("words.txt")):
        print("Word file exists") # Debug statement
        
        if (currentIndex < (maxWords - 1)):
            currentIndex += 1
            print(currentIndex, maxWords) # Tells you the current index in respect to max words
            with open("words.txt", "a") as f:
                f.write(currentPrompt+"\n") # Open file
                f.close() # Close file
        elif (currentIndex >= (maxWords - 1)):
            writeFile = True
            print("Terminating...") # Debug statement
            break
    else:
        print("Word file does not exist! Create a words.txt file to run this program!")
        writeFile = True
        break

readFile = False
# This 'while' loop will run if the user chooses to read from the file
while (readFile == False):
    combinedLength = 0
    longestWord = ""
    wordsProcessed = []

    if (path.exists("words.txt")): # checking to see if file 'words.txt' exists
        with open("words.txt", "r") as f:
            wordsProcessed = f.readlines()
            print(wordsProcessed) # Outputs the list of all the words in the text file
            f.close()

        for i in range(len(wordsProcessed)): # looping through words in the document
            if ( (len(wordsProcessed[i])) >= (len(longestWord)) ): # if the current word is less than the longest word, then execute
                longestWord = wordsProcessed[i]
                combinedLength += len(longestWord)
                print(wordsProcessed[i] + " is the longest word now!") # lets you know which word has now taken the lead

        readFile = True # meant to change the status of the loop to close

    else: # If file does not exist then break out of loop
        print("Word file does not exist! Create a words.txt file to run this program!") # Error message!
        readFile = True # meant to change the status of the loop to close

    '''
    print("Longest word: " + longestWord)
    print("Number of words: " + numberOfWords)
    print("Average word length: " + averageLength)
    '''

    print("There are: " + str(len(wordsProcessed)) + " words in the words.txt file!") # Lets you know how many words are in words.txt

    averageLength = combinedLength / len(wordsProcessed) # Storing the average length in a variable
    print("The average length of all the words is: " + str(averageLength)) # Average length output
    print("The longest word is: " + longestWord) # Longest word output


       

print("Finished storing words. Please check the words.txt file to view.") # Lets you know the program has finished compiling