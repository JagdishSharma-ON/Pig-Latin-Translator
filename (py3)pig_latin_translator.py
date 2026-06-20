original = input("Enter a word to translate to Pig Latin: ")
word = original.lower()
first = word[0]
ay = "ay"
new_word = word+first+ay
new_word = new_word[1:len(new_word)]
if len(new_word) > 0:
    print("The Pig Latin translation of " + original + " is: " + new_word)
else:
    print("Please enter a valid word.")