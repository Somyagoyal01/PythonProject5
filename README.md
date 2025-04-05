# File Reading with Error Handling

## Functionality
This Python program safely attempts to read the contents of a file named `sample.txt`. It:

1. Tries to open and read the file.
2. Displays the file content if it exists.
3. Gracefully handles the case where the file is not found.
4. Ensures the file is properly closed using a `finally` block.

## How It Works
- Uses a `try-except-finally` structure:
  - `try`: Opens and reads the file.
  - `except FileNotFoundError`: Catches the case where the file does not exist and prints an appropriate message.
  - `finally`: Prints the content if available and ensures the file is closed.

## Sample Output
If `sample.txt` exists:
```
<content of the file is printed>
```
If `sample.txt` does not exist:
```
The file 'sample.txt' does not exist.
```

## Usage
Place a file named `sample.txt` in the same directory as the script to test successful file reading. If the file is missing, the program will notify the user without crashing.

# Write, Append, and Read from a File

## Functionality
This Python program demonstrates basic file operations by interacting with a text file named `output.txt`. The program performs the following tasks:

1. **Write to a File**: Takes input from the user and writes it to `output.txt`, overwriting any existing content.
2. **Append to the File**: Takes additional user input and appends it to the same file.
3. **Read from the File**: Opens the file and displays its final content after both write and append operations.

## How It Works
- **Write Mode (`'w'`)**: Opens `output.txt` and writes user input, replacing existing data.
- **Append Mode (`'a'`)**: Reopens the file and adds new input at the end of the current content.
- **Read Mode (`'r'`)**: Opens the file to display its full content.

## Sample Output
```
Enter text to write to the file= Hello
Data successfully written to output.txt
Enter additional text to append= World!
Data successfully appended
Final content of output.txt:
HelloWorld!
```

## Usage
Run the script and follow the input prompts. You’ll see the combined output printed at the end. This is useful for basic text file manipulation and demonstrates core file I/O operations in Python.


