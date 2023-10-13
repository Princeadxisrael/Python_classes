import re

# text_to_search= '''
# abcdefghijklmnopqurluwxyz
# ABCDEFGHIJKLMNOPQRSTTUVWXYZ
# 1234567890

# Ha lo HAha

# Python
# MultiPying
# MetaCharacters(should be escaped):
# . ^ $ * + ? { } [ ] \ | ( )

# moringa.com

# +234-81444899-00
# 123-678-9099
# 123.555.1234
# 123*555*1234

# bat
# cat
# mat
# pat

# Mr.Smith
# Mr John
# Ms.Joy
# Mrs. Robinstone
# Mr. F
# aaaab aabaaa
# aaab
# aaaaab
# aaa
# aaaaaaa
# '''

# sentence='Start a sentence and then bring it to an end'

# pattern=re.compile(r'')

# matches=pattern.finditer(text_to_search)

# for match in matches:
#     print(match)


# # with open('data.txt', 'r') as f:
# #     contents=f.read()

# # pattern=re.compile(r'')

# # matches=pattern.finditer(contents)

# # for match in matches:
# #     print(match)

# text="He was not carefully disgused but was captured qickly by the police"
# pattern=re.compile(r'\w+ly\b')
# obj=pattern.findall(text)
# print(obj)

text="Errors are a part of a Developer journey"
pattern=re.compile(r'\b[aeiouAEIOU]\w+')
obj=pattern.findall(text)
print(obj)
