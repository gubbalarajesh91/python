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
