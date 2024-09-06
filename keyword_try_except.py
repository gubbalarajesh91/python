try:
    file = open('example2.txt', 'r')
    content = file.read()
    print("File content:")
    print(content)
except FileNotFoundError:
    print("Error: File not found.")
except IOError:
    print("Error: Could not read the file.")
finally:
    try:
        file.close()
        print("File closed.")
    except NameError:
        # Handle the case where file was never opened
        print("File was never opened.")

# As keyword
import numpy as np
import pandas as pd

# Using aliases to refer to the libraries
array = np.array([1, 2, 3])
dataframe = pd.DataFrame({'A': [1, 2, 3]})

print(array)
print(dataframe)