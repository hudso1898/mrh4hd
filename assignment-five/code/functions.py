from classes import *

def login(username, password):
	"""
	Function 1: login

	Takes in a username and password string entered by the user.
	Checks if that username/password is in the "database" 
	(here, mocked as a static list)
	*obviously in the real system, it would hash the password and
	check the hashes*

	Parameters:
		username - username provided by the user trying to log in
		password - password provided by the user trying to log in
	
	Returns:
		True if the credentials match to indicate the user logs in
		False if the credentials do not match to indicate an invalid
		username/password combination
	"""
	credentials = [username, password]
	query = queryUserCredentials()
	try:
		i = query.index(credentials)
		return True
	except ValueError:
			return False

def viewAssignments(user, course):
	"""
	Function 2: viewAssignments

	Allows TA or Instructor to view a list of assignments.

	Parameters:
		user - User attempting to view assignments
		course - Course which the user is attempting to view assignments

	Returns: List of Assignments
	or
	[] if user is not a TA or the Instructor of the course.
	(i.e. doesn't have sufficient permissions)

	"""

	if (course.instructor == user.username or user.username in course.assistants):
		return course.assignments
	else:
		return []

def addStudentToCourse(user, course, student):
	"""
	Function 3: addStudentToCourse

	Allows Instructor to add a student to the course.

	Parameters:
		user - User attempting to add a student
		course - Course which the user is attempting to add the student to
		student - User representing the student to add

	Returns:
		True to indicate successful addition
		or
		False to indicate insufficient permissions, or the user is already in the course.
	"""

	if (course.instructor == user.username and student.username not in course.students):
		course.students.append(student.username)
		return True
	else:
		return False

def addTAToCourse(user, course, ta):
	"""
	Function 4: addTAToCourse

	Allows Instructor to add a ta to the course.

	Parameters:
		user - User attempting to add a ta
		course - Course which the user is attempting to add the ta to
		ta - User representing the ta to add

	Returns:
		True to indicate successful addition
		or
		False to indicate insufficient permissions, or the user is already in the course.
	"""

	if (course.instructor == user.username and ta.username not in course.assistants):
		course.assistants.append(ta.username)
		return True
	else:
		return False

def addAssignmentToCourse(user, course, assignment):
	"""
	Function 5: addAssignmentToCourse

	Allows Instructor to add an assignment to the course.

	Parameters:
		user - User attempting to add an assignment
		course - Course which the user is attempting to add the assignment to
		assignment - Assignment to add

	Returns:
		True to indicate successful addition
		or
		False to indicate insufficint permissions
	"""

	if (course.instructor == user.username):
		course.assignments.append(assignment)
		return True
	else:
		return False


# utility mock function that returns mock entries i.e. username, password
def queryUserCredentials():
	return [["mrh4hd","password12345"], ["sgoggins", "coolpassword"]]