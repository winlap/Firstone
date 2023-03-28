def word_count(paragraph, word):
    word_count = 0
    words = paragraph.split()
    for x in words:
        if x == word:
            word_count += 1
    return word_count


paragraph = input("\nEnter the paragraph: ")

word = input("\nEnter the word you want to count: ")
count = word_count(paragraph, word)
print(f"\nThe word appears {count} times in the paragraph")

 