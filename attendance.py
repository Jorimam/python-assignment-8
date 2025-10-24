"""
TASK: Create an AttendanceRegister class.

Requirements:
1. The class should allow marking a student as present or absent.
2. Store attendance records in a dictionary where the student's name is the key.
3. Provide a method to check if a student was present or absent.
4. Provide a method to display the full register.


"""
class Attendance_register:
	def __init__(self):
		self.register = {}
	
	def add_student(self, student_name):
		self.student_name = student_name
		self.register.update({ self.student_name:[]})
		

	def mark_present(self, student_name):
		self.student_name = student_name
		self.register[self.student_name].append("Present")

	def mark_absent(self, student_name):
		self.student_name = student_name
		self.register[self.student_name].append("Absent")


	def get_status(self, student_name):
		self.student_name = student_name
		return self.register[self.student_name][0]

	def show_register(self):
		return self.register

register = Attendance_register()
register.add_student("Nassi")
register.add_student("Mark")
register.add_student("Bob")
register.add_student("Lax")

register.mark_present("Nassi")
register.mark_present("Mark")

register.mark_absent("Bob")
register.mark_absent("Lax")

print(register.get_status("Nassi"))
print(register.get_status("Lax"))

print(register.show_register())

# Example Usage:
#     register = AttendanceRegister()
#     
#     register.mark_absent("Mary")
#     print(register.get_status("John"))   # "Present"
#     print(register.show_register())      # {"John": "Present", "Mary": "Absent"}