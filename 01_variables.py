#Define a variable
a = 42
"""
Print the value
that is stored inside
the vaiables
"""
print(a)

#Float value
b = 42.345
print(b)

# Create a list

sample_list = ["Ansible", "Terraform", "Jenkins", "Docker", "K8s"] # list()

# Indexing, slicing
sample_ele = sample_list[4]
print(sample_ele)

import re

text = "The quick brown fox"
pattern = r"brown"

search = re.search(pattern, text)
if search:
    print("Pattern found:", search.group())
else:
    print("Pattern not found")