#Example: Reverse the order of characters in a sentence.

string = "The quick brown fox jumps over the lazy dog"

reversed_string = ''

for char in string:
    reversed_string = char + reversed_string
print(reversed_string)

#Another way for this

string = "The quick brown fox jumps over the lazy dog"

reversed_string = ''.join(reversed(string))

print(reversed_string)
