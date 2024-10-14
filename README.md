# Student Management System

This Python project is a **Student Management System** that allows users to add and manage student records. The system can store personal information, academic details, and admission status for students. It also includes validation checks for input and displays all the student records in an easy-to-read format.

## Features

- Add student personal information (Aadhar, name, date of birth, email, mobile).
- Validate email addresses and check if the student is eligible for admission based on age.
- Record student academic information such as subjects and marks.
- View all stored student records in a readable format.
- Input validation for Aadhar, mobile number, and admission number.

## Requirements

- Python 3.x
- `datetime` module (included in the Python Standard Library)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Himanshu-Vishwakarma-GH/Student-Management-System.git
2. Navigate to the project directory:
   ```bash
    cd student-management-system
3. Run The Python Script:
   ```bash
   python app.py
## Usage
Once the script is running, follow the on-screen prompts to:

1. Add Student Record: Enter the student's details, validate the inputs, and store the record.
2. Display All Records: View all stored student data in the system.
3. Exit: End the program.

## Example
  ```bash
1. Accept records
2. Display all records
3. Exit
Enter your choice: 1
Enter last 4 digits of Aadhar: 1234
Enter first name: John
Enter Date of Birth (dd-mm-yyyy): 15-08-2005
Enter email: john@student.mes.ac.in
Enter 10-digit mobile number: 9876543210
Enter last 5 digits of Admission number: 54321
Enter admission year (yyyy): 2022
DSE admission? (True/False): False
Enter subject name (or press Enter to finish): Mathematics
Enter marks for Mathematics: 90
Student record added successfully.```

