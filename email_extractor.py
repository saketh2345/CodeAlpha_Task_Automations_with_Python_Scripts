
import re
import os


def extract_emails(input_file, output_file="extracted_emails.txt"):
    """Reads a text file, finds all email addresses using regex,
    removes duplicates, and saves them to an output file."""

    if not os.path.exists(input_file):
        print(f"Error: '{input_file}' does not exist.")
        return

    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Regex pattern to match standard email addresses
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    emails = re.findall(email_pattern, content)

    # Remove duplicates while keeping order
    unique_emails = list(dict.fromkeys(emails))

    if not unique_emails:
        print("No email addresses found in the file.")
        return

    with open(output_file, "w", encoding="utf-8") as f:
        for email in unique_emails:
            f.write(email + "\n")

    print(f"Found {len(unique_emails)} unique email address(es).")
    print(f"Saved to '{output_file}'")


def main():
    print("=== Email Address Extractor ===")
    input_file = input("Enter the path of the .txt file to scan: ").strip()
    extract_emails(input_file)


if __name__ == "__main__":
    main()
