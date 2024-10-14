from datetime import datetime

class Student:
	def __init__(self, aadhar, name, dob, email, mobile, admission_no, admission_year, dse_status):
		self.personal_info = {aadhar: (name, dob, email, mobile)}
		self.admission_info = [admission_no, admission_year, dse_status]
		self.academic_info = []

	def add_subject(self, subject, marks):
		self.academic_info.append([subject, marks])

class StudentManagementSystem:
	def __init__(self):
		self.students = []

	def validate_email(self, email):
		return email.endswith("@student.mes.ac.in")

	def calculate_age(self, dob):
		birth_date = datetime.strptime(dob, "%d-%m-%Y")
		today = datetime.now()
		age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
		return age

	def accept_records(self):
		try:
			aadhar = int(input("Enter last 4 digits of Aadhar: "))
			name = input("Enter first name: ")
			dob = input("Enter Date of Birth (dd-mm-yyyy): ")
			email = input("Enter email: ")
			mobile = int(input("Enter 10-digit mobile number: "))
			admission_no = int(input("Enter last 5 digits of Admission number: "))
			admission_year = int(input("Enter admission year (yyyy): "))
			dse_status = input("DSE admission? (True/False): ").lower() == 'true'

			if not self.validate_email(email):
				print("Invalid email. Must end with @student.mes.ac.in")
				return

			if self.calculate_age(dob) < 17:
				print("You are not eligible for admission to Engineering.")
				return

			if len(str(mobile)) != 10 or len(str(aadhar)) != 4 or len(str(admission_no)) != 5:
				print("Invalid input length for mobile, Aadhar, or admission number.")
				return

			student = Student(aadhar, name, dob, email, mobile, admission_no, admission_year, dse_status)

			while True:
				subject = input("Enter subject name (or press Enter to finish): ")
				if not subject:
					break
				marks = int(input(f"Enter marks for {subject}: "))
				student.add_subject(subject, marks)

			self.students.append(student)
			print("Student record added successfully.")

		except ValueError as e:
			print(f"Invalid input: {e}")
		except Exception as e:
			print(f"An error occurred: {e}")

	def display_records(self):
		for student in self.students:
			aadhar, info = list(student.personal_info.items())[0]
			print(aadhar)
			print(info)
			print(student.admission_info)
			for subject, marks in student.academic_info:
				print(f"{marks} in {subject}")
		print("Thank You")

	def run(self):
		while True:
			print("\n1. Accept records")
			print("2. Display all records")
			print("3. Exit")
			choice = input("Enter your choice: ")

			if choice == '1':
				self.accept_records()
			elif choice == '2':
				self.display_records()
			elif choice == '3':
				print("Thank You")
				break
			else:
				print("Invalid choice. Please try again.")

if __name__ == "__main__":
	sms = StudentManagementSystem()
	sms.run()

