"""Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist."""
try:
    file1= open('sample.txt','r')
    reading_file = file1.read()
except FileNotFoundError:
     print("The file 'sample.txt' does not exist.")
finally:
     print(reading_file)
     file1.close()
