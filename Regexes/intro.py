import re
import string

# text_to_search = [ascii_lowercase, ascii_uppercase, ]
text_to_search = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa


metaCharacters (Need to be escaped):
> ^ $ * + ? { } [] \ | ( )

 coreyms.com

 321-555-4321
 123.555.1234

 Mr. Schafer
 Mr Smith
 Ms Davis
 Mrs. Robinson
 Mr. T
'''

sentence = 'Start a sentence and then bring it to an end'

pattern = re.compile(r"\d\d\d.\d\d\d.\d\d\d\d")
matches = pattern.finditer(text_to_search)

with open("data.txt", "r") as f:
    contents = f.read()

    matches = pattern.finditer(contents)

    for match in matches:
        print(match)



for match in matches:
    print(match)




# What is a raw string: it is used to express a string of characters with
# all of the  backslashes not performing any issues
