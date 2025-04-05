"""Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file."""
file2=open('output.txt','w')
a=input("Enter text to write to the file= ")
writing_file=file2.write(a)
print("Data successfully written to output.txt")
file2.close()
file2=open('output.txt','a')
b=input("Enter additional text to append= ")
appending_file= file2.write(b)
print("Data successfully appended")
file2.close()
file2= open('output.txt','r')
reading_file=file2.read()
print("Final content of output.txt:")
print(reading_file)
file2.close()
