# Email Address Extractor 📧

A simple **Python-based Email Address Extractor** that scans a text file, finds email addresses using a regular expression, removes duplicate addresses, and saves the unique email addresses to an output file.

This project is beginner-friendly and demonstrates Python concepts such as regular expressions, file handling, functions, lists, dictionaries, input validation, and exception-free error handling.

## Features

* 📄 Reads email addresses from a `.txt` file
* 🔍 Uses regular expressions to find email addresses
* ♻️ Removes duplicate email addresses
* 📋 Preserves the original order of unique email addresses
* 💾 Saves extracted emails to a text file
* ⚠️ Checks whether the input file exists
* ℹ️ Displays the number of unique email addresses found

The main extraction function is designed to read a text file, find email addresses, remove duplicates, and save the results.

## Requirements

* Python 3.x
* No external Python libraries are required.

The project uses Python's built-in `re` and `os` modules.

## How to Run

1. Clone this repository:

```bash
git clone https://github.com/your-username/your-repository-name.git
```

2. Navigate to the project directory:

```bash
cd your-repository-name
```

3. Run the program:

```bash
python email_extractor.py
```

4. Enter the path of the text file when prompted:

```text
=== Email Address Extractor ===
Enter the path of the .txt file to scan:
```

## How It Works

The program asks the user to provide the path to a `.txt` file.

It then:

1. Checks whether the input file exists.
2. Reads the contents of the file.
3. Searches the content for email addresses using a regular expression.
4. Removes duplicate email addresses.
5. Saves the unique addresses to `extracted_emails.txt`.
6. Displays the number of unique email addresses found.

The program performs the input-file existence check before attempting to read the file.

## Email Detection

The program uses the following regular expression to identify standard email address patterns:

```text
[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}
```

This pattern is applied to the text content using Python's `re.findall()` function.

## Duplicate Removal

If the same email address appears multiple times in the input file, the program keeps only one occurrence while maintaining the original order.

For example, if the input contains:

```text
john@example.com
admin@example.com
john@example.com
hello@example.com
admin@example.com
```

The output will contain:

```text
john@example.com
admin@example.com
hello@example.com
```

The duplicate removal is implemented using `dict.fromkeys()`.

## Output File

The extracted email addresses are saved by default to:

```text
extracted_emails.txt
```

Each unique email address is written on a separate line.

Example output:

```text
john@example.com
admin@example.com
hello@example.com
```

After processing, the program displays the number of unique addresses found and the name of the output file.

## Example

### Input File

Suppose `contacts.txt` contains:

```text
Contact John at john@example.com
Contact Admin at admin@example.com
John's email is john@example.com
Send questions to support@example.org
```

Run:

```bash
python email_extractor.py
```

Enter:

```text
contacts.txt
```

The program will create:

```text
extracted_emails.txt
```

Containing:

```text
john@example.com
admin@example.com
support@example.org
```

## Error Handling

If the specified input file does not exist, the program displays an error message instead of attempting to read the file.

```text
Error: 'filename.txt' does not exist.
```

If no email addresses are found, the program reports:

```text
No email addresses found in the file.
```

These cases are handled directly in the extraction function.

## Project Structure

```text
.
├── email_extractor.py
├── input.txt
├── extracted_emails.txt
└── README.md
```

* **`email_extractor.py`** — Main Python program.
* **`input.txt`** — Example text file to scan.
* **`extracted_emails.txt`** — Generated file containing unique email addresses.
* **`README.md`** — Project documentation.

## Concepts Demonstrated

This project demonstrates:

* Python functions
* Regular expressions (`re`)
* File handling
* Reading and writing text files
* Lists
* Dictionaries
* `dict.fromkeys()`
* Conditional statements
* User input
* Basic error handling
* String manipulation

## Future Improvements

Possible improvements for future versions include:

* Support for multiple input file formats
* Extract emails from PDF and DOCX files
* Add command-line arguments
* Allow users to specify the output filename
* Export results to CSV or JSON
* Add a graphical user interface
* Improve email validation
* Process multiple files at once

## Author

Created as a beginner-friendly Python project for learning **regular expressions, file processing, and data extraction**.

## License

This project is available for educational and personal use.
