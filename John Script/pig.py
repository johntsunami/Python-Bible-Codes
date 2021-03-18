original_sentence = input("Please enter sentence here: ").strip().lower()

words = original_sentence.split()

# loop through words and convert to pig latin

new_words = []  # why box? because its a blank list

# add yay on end if they end in vowel
for word in words:  # no idea why word works when its not defined
    if word[0] in "aeiou":  # if it ends in any of those letters
        new_word = word + "yay"
        new_words.append(new_word)
    else:
        vowel_pos = 0
        for letter in word:
            if letter not in "aeiou":
                vowel_pos = vowel_pos + 1
            else:
                break
            cons = word[:vowel_pos]
            the_rest = word[:vowel_pos]
            the_rest = word[vowel_pos:]
            new_word = the_rest + cons + "ay"
            new_words.append(new_word)

output = " ".join(new_words)
print(new_words)


# otherwise
# add first letter to end and add ay if starts with consonant

# stick back together

# output text to show piglatin version of sentence
