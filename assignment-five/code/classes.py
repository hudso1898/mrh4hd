class User:
	def __init__(self, username,password):
		self.username = username;
		self.password = password;

class Course:
	def __init__(self, course_name, course_description, instructor):
		self.course_name = course_name
		self.course_description = course_description
		self.instructor = instructor

	students    = []
	assistants  = []
	assignments = []

class Assignment:

	def __init__(self, name, description):
		self.assignment_name = name
		self.description = description

