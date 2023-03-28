def count_vowel(arr):
#define a string of vowels
  vowel = "aeiouAEIOU"
  count = 0
  for char in arr:
      if char in vowel:
          count += 1

  return count

arr = input("Enter a string: ")
c = count_vowel(arr)
print(f"The count of vowel in {arr} is {c}")