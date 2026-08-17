"""
Task 3: Task Automation with Python Scripts
Project: Email Address Extractor

Concepts Used:
os, re, file handling, functions, loops,
input/output, string handling
"""

import re
import os


# --------------------------------------------------
# EMAIL EXTRACTION FUNCTION
# --------------------------------------------------

def extract_emails_from_file(input_file):
    """Reads a text file and extracts email addresses."""

    if not os.path.exists(input_file):
        print("\nError: File does not exist.")
        return []

    if not os.path.isfile(input_file):
        print("\nError: The given path is not a file.")
        return []

    try:
        with open(input_file, "r", encoding="utf-8") as file:
            content = file.read()

    except Exception as e:
        print("\nError while reading file:", e)
        return []

    # Regular expression for email addresses
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

    emails = re.findall(email_pattern, content)

    # Remove duplicates while keeping case-insensitive uniqueness
    unique_emails = []
    seen = set()

    for email in emails:
        email = email.strip()

        if email.lower() not in seen:
            unique_emails.append(email)
            seen.add(email.lower())

    # Sort alphabetically
    unique_emails.sort(key=str.lower)

    return unique_emails


# --------------------------------------------------
# SAVE EMAILS FUNCTION
# --------------------------------------------------

def save_emails(emails, output_file):
    """Saves extracted emails to a text file."""

    try:
        with open(output_file, "w", encoding="utf-8") as file:

            file.write("EXTRACTED EMAIL ADDRESSES\n")
            file.write("=" * 40 + "\n\n")

            for email in emails:
                file.write(email + "\n")

            file.write("\n")
            file.write("=" * 40 + "\n")
            file.write("Total unique emails: " + str(len(emails)))

        print("\nEmails successfully saved!")
        print("Output file:", output_file)

    except Exception as e:
        print("\nError while saving file:", e)


# --------------------------------------------------
# DISPLAY EMAILS FUNCTION
# --------------------------------------------------

def display_emails(emails):
    """Displays extracted emails on the screen."""

    if not emails:
        print("\nNo email addresses were found.")
        return

    print("\nExtracted Email Addresses")
    print("-" * 35)

    for number, email in enumerate(emails, start=1):
        print(str(number) + ". " + email)

    print("-" * 35)
    print("Total unique emails:", len(emails))


# --------------------------------------------------
# FILE INFORMATION FUNCTION
# --------------------------------------------------

def show_file_info(input_file):
    """Displays basic information about the input file."""

    if not os.path.exists(input_file):
        return

    file_size = os.path.getsize(input_file)

    print("\nFile Information")
    print("-" * 30)
    print("File name :", os.path.basename(input_file))
    print("File size :", file_size, "bytes")
    print("File path :", os.path.abspath(input_file))


# --------------------------------------------------
# MAIN EXTRACTOR
# --------------------------------------------------

def process_file():

    print("\n" + "=" * 50)
    print("        EMAIL ADDRESS EXTRACTOR")
    print("=" * 50)

    input_file = input(
        "\nEnter the path of the .txt file: "
    ).strip()

    if input_file == "":
        print("Please enter a file path.")
        return

    # Display file information
    show_file_info(input_file)

    # Extract emails
    emails = extract_emails_from_file(input_file)

    if not emails:
        print("\nNo email addresses found.")
        return

    # Display results
    display_emails(emails)

    # Ask whether to save
    save_choice = input(
        "\nDo you want to save these emails? (yes/no): "
    ).strip().lower()

    if save_choice in ("yes", "y"):

        output_file = input(
            "Enter output filename "
            "(press Enter for extracted_emails.txt): "
        ).strip()

        if output_file == "":
            output_file = "extracted_emails.txt"

        save_emails(emails, output_file)

    else:
        print("\nEmails were not saved.")


# --------------------------------------------------
# MAIN PROGRAM
# --------------------------------------------------

def main():

    print("\n" + "=" * 55)
    print("       PYTHON EMAIL AUTOMATION TOOL")
    print("=" * 55)

    while True:

        print("\nMenu")
        print("-" * 30)
        print("1. Extract emails from a file")
        print("2. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":

            process_file()

        elif choice == "2":

            print("\nThank you for using the Email Automation Tool!")
            print("Goodbye!")
            break

        else:

            print("\nInvalid choice.")
            print("Please select 1 or 2.")


# --------------------------------------------------
# START PROGRAM
# --------------------------------------------------

if __name__ == "__main__":
    main()
