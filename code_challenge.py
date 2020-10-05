#U: only print out that are divisible by 3
#P: modulo operator == 0 as you iterate over the list
#E:

divide_by_3 = [85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]

for i in divide_by_3:
    if i % 3 == 0:
        print(i)

# print out all the strings in the array that represent a number divisible by three

stringz = [
  "five",
  "twenty six",
  "nine hundred ninety nine",
  "twelve",
  "eighteen",
  "one hundred one",
  "fifty two",
  "forty one",
  "seventy seven",
  "six",
  "twelve",
  "four",
  "sixteen"
]

for i in stringz:
    