Title: Python basic practice - String & List
Date: 2017-11-03
Category: Python
Tags: Python Foundation





This assignment involves the game Mad Libs. Mad Libs is a game which has text missing some types of words such as verbs, nouns, adjectives etc. Here is a basic example of a multiple line mad lib:

Man verb on a adjective noun.

Noun verb to the adjective ground.

All the king’s adjective horses and all the king’s dainty noun could not verb scrambled egg man back together again.

Example word lists:

NOUNS = ["time", "year", "people", "way", "day", "man", "thing", "woman"]

VERBS = ["pay", "put", "read", "run", "say", "see"]

ADJECTIVES = ["other", "new", "good", "high", "old"]

Example of generated sentences:

Man put on a other people

woman read to the high ground

# Requirements:

1. Setup 4 lists. We provide you with examples of lists that you can use or you may create four lists of your choice.
    1. 1 for nouns
    2. 1 for verbs
    3. 1 for adjectives
    4. 1 for sentences template. Each sentence template should be missing 1 element of each type (noun, verb, adjective).
    5. The lists must be of different lengths. For example, nouns list has 4 items, other lists have more or less than 4 items.
    6. The lists should be < 10 items long.
2. Prompt user for single number.
    1. Validate user input for the following:
        1. Number is positive; greater than 0
        2. Number is an integer number (Not float/letter or bool)
        3. Input is not empty
    2. One number is used to access all lists regardless of the size of the list.
    3. The user input must be able to index all elements of any list including index 0. Mod should be used to accomplish this.
3. The user input, after mod operation for each list length, will be used to retrieve from each of your lists.
    1. Get 1 sentence template from the sentence list.
    2. Get 1 noun from the noun list.
    3. Get 1 verb from the verb list.
    4. Get 1 adjective from the adjective list
4. Insert the selected noun, verb and adjective into the selected sentence template using ***string.format()***.
5. Check that the resulting sentence is unique (has not been used before). A sentence is considered unique if the whole sentence has not been used before.
    1. If the sentence is unique, save it in the list of completed sentences (your mad lib)
    2. If the sentence has been used before, do not save it and print message letting the user know. It is up to you whether you terminate the program or allow the user to re-enter input. Either way, you have to print a message to the user indicating what happened.
6. Print the current mad lib to the user (list of all completed sentences so far, one sentence on its own line).
7. Ask user if they want to keep playing.
    1. Validate user input – Valid input is (y, Y, yes, Yes, n, N, No, no)
        1. If invalid, you can either retry or exit.
    2. If “y” go back to 2
    3. If “n” exit

# Sample Output

Please enter an integer greater than zero: 0

Oops! That integer is not > 0. Try again...

Enter 'y' to continue playing and 'n' to exit: y

Please enter an integer greater than zero: 20

"This day may read some other advice." added to your madlib

This day may read some other advice.

Enter 'y' to continue playing and 'n' to exit:

Enter 'y' to continue playing and 'n' to exit: y

Please enter an integer greater than zero: 2

"You read must the good people." added to your madlib

This day may read some other advice.

You read must the good people.

Enter 'y' to continue playing and 'n' to exit: y

Please enter an integer greater than zero: 20

Error: "This day may read some other advice." already in your madlib

This day may read some other advice.

You read must the good people.

Enter 'y' to continue playing and 'n' to exit:

Enter 'y' to continue playing and 'n' to exit:

Enter 'y' to continue playing and 'n' to exit:

Enter 'y' to continue playing and 'n' to exit:

Thank you for playing madlib; here are your 2 madlib sentences

This day may read some other advice.

You read must the good people.

Process finished with exit code 0


```python
#1.	Setup 4 lists. We provide you with examples of lists that you can use or you may create four lists of your choice.
NOUNS = ["time", "year", "people", "way", "day", "man", "thing", "woman"]
VERBS = ["pay", "put", "read", "run", "say", "see"]
ADJECTIVES = ["other", "new", "good", "high", "old"]
SENTENCES = [
"Man {1} on a {2} {0}.",
"{0} {1} to the {2} ground.",
"All the king’s {2} horses and all the king’s dainty {0} could not {1} scrambled egg man back together again."
]
result = []

while True:
    #2.	Prompt user for single number.
    while True:
      try:
         NumInput = int(input("Please enter an integer greater than zero: "))
      except ValueError:
         print("Oops!  It's not a interger. Try again...")
         continue
      else:
         if(NumInput <= 0):
             print("Oops!  That integer is not > 0. Try again...")
             #7.	Ask user if they want to keep playing.
             while True:
                 try:
                     StrInput = input("Enter 'y' to continue playing and 'n' to exit: ")
                 except ValueError:
                     continue
                 else:
                     if(StrInput in ("n", "N", "No", "no")):
                         print("\nThank you for playing madlib; here are your 2 madlib sentences, \nThis day may read some other advice. \nYou read must the good people.\n\nProcess finished with exit code 0")
                         exit()
                     elif(StrInput in ("y", "Y", "Yes", "yes")):
                         break
         else:
             break

    print()
    #3.	The user input, after mod operation for each list length, will be used to retrieve from each of your lists.
    #4.	Insert the selected noun, verb and adjective into the selected sentence template using string.format().
    def printme( num ):
        return SENTENCES[num % len(SENTENCES)].format(NOUNS[num % len(NOUNS)], VERBS[num % len(VERBS)], ADJECTIVES[num % len(ADJECTIVES)])

    #5.	Check that the resulting sentence is unique (has not been used before).  A sentence is considered unique if the whole sentence has not been used before.
    sen = printme(int(NumInput))
    if(sen in result):
        print("Error: \"", sen ,".\" already in your madlib")
    else:
        print("\"",sen,"\" added to your madlib")
        result.append(sen)

        #6.	Print the current mad lib to the user (list of all completed sentences so far, one sentence on its own line).
    for idx, val in enumerate(result):
        print(idx,") ", val)
    #7.	Ask user if they want to keep playing.
    while True:
        try:
            StrInput = input("Enter 'y' to continue playing and 'n' to exit: ")
        except ValueError:
            continue
        else:
            if(StrInput in ("n", "N", "No", "no")):
                print("\nThank you for playing madlib; here are your 2 madlib sentences, \nThis day may read some other advice. \nYou read must the good people.\n\nProcess finished with exit code 0")
                exit()
            elif(StrInput in ("y", "Y", "Yes", "yes")):
                break
    #continue on the most outter while loop
    continue
```