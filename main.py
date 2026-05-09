
class Student:
	status = True
	pay = 1000

	def __init__(self, first_name: str, last_name: str, age: int, grades: list):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.grades = grades
		self.status = Student.status
		self.pay = Student.pay

	def get_full_name(self):
		return f"{self.first_name} {self.last_name}"

	def get_discount(self):
		if self.age < 18:
			return self.pay * 0.8
		return self.pay

	def calculate_average(self):
		if not self.grades:
			return 0
		return sum(self.grades) / len(self.grades)

	def get_status(self):
		avg = self.calculate_average()
		if avg > 90:
			return "Excellent"
		elif 70 < avg <= 90:
			return "Good"
		elif 50 < avg <= 70:
			return "Average"
		else:
			self.status = False
			return "Poor"
