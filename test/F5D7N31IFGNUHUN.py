#  Be sure that the text file to be opened is in the *same* directory
#  as the Python script.

#  Open the text file to be searched
openfile = open("Shakespeare.txt")
print ("Successfully opened file: ", openfile)

# Set the counter up
NumberOfTimesFound = 1

# Have user enter the word, phrase or string
wordsearched = input("Enter the case-sensitive word/phrase/string for search > ")

# Go through each line of the file and search for the word/phrase/string
for line in openfile:
    if wordsearched in line:
        print ("Found the word/phrase: ", wordsearched)
        print ("This word/phrase has been found:", NumberOfTimesFound, "times")
        NumberOfTimesFound = NumberOfTimesFound + 1