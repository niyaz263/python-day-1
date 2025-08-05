 n = input("Enter a name: ")
 r_str = ""

 for i in range(len(n)-1, -1, -1):
     r_str += n[i]

 print("Palindrome" if r_str == n else "Not palindrome")

import re

n = input("Enter a name: ")

# Remove all non-alphanumeric characters and convert to lowercase
cleaned = re.sub(r'[^A-Za-z0-9]', '', n).lower()

# Check if it's a palindrome
print("Palindrome" if cleaned == cleaned[::-1] else "Not palindrome")

