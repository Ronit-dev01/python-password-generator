# 🔐 Password Generator with SQLite

A Python application that generates strong, random passwords and securely stores them in a local SQLite database along with the corresponding website or application name.

## Features

- 🔒 Generate strong random passwords
- 🌐 Save passwords with the website/application name
- 💾 Store credentials in a local SQLite database
- 📏 Custom password length
- 🔢 Uses uppercase letters, lowercase letters, numbers, and special characters
- ⚡ Lightweight and easy to use

## Requirements

- Python 3.7+
- SQLite (included with Python)

## Installation

```bash
git clone https://github.com/yourusername/password-generator.git
cd password-generator
```

## Usage

Run the application:

```bash
python password_generator.py
```

Example:

```text
=== Password Generator ===

Enter website name: github.com
Enter password length: 16

Generated Password:
A$7m#Q9!kLp2@R8

Password saved successfully!
```

## Database

The application automatically creates an SQLite database (if it doesn't already exist) to store generated passwords.

Example table:

| Website | Password |
|---------|----------|
| github.com | A$7m#Q9!kLp2@R8 |
| gmail.com | 9@Lm#P2vX!q7Df |

## Project Structure

```text
password-generator/
│
├── password_generator.py
├── passwords.db
├── README.md
└── LICENSE
```

## Future Improvements

- Encrypt stored passwords
- Master password authentication
- Search and update saved passwords
- Delete saved entries
- Password strength checker
- Export database to CSV
- GUI version using Tkinter or CustomTkinter

## Author

**Ronit Rai**

## License

This project is licensed under the MIT License.
## for 
IT WAS MY FIRST PROJECT ON GITHUB AND I AM UPGRADING IT TIME BY TIMEEE
