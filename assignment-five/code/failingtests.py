import pytest
from functions import *
from classes   import *
from fixtures  import *

# these tests should all fail because they recieve bad data.

# function 1 - test should fail since it's checking for a valid login with invalid login credentials
def test_loginSuccess(invalid_user):
	assert login(invalid_user.username, invalid_user.password)

# function 2 - test should fail since the user is valid in this case
def test_viewAssignmentsRestrictsUser(valid_user, unix_course):
	assignments = viewAssignments(valid_user, unix_course)
	assert len(assignments) == 0

# function 3 - test should fail since the user is not the instructor in this case
def test_addStudentAddsStudent(valid_user, seng_course, unix_instructor):
	assert addStudentToCourse(unix_instructor, seng_course, valid_user)
	assert valid_user.username in seng_course.students

# function 4 - test should fail since the ta is different and thus is added
def test_addTARestrictsDuplicates(invalid_user, unix_course, unix_instructor):
	assert not addTAToCourse(unix_instructor, unix_course, valid_user)

# function 5 - test should fail since the instructor is correct but expects a restriction
def test_addAssignmentRestrictsInstructor(unix_course, unix_instructor, unix_assignment):
	assert not addAssignmentToCourse(unix_instructor, unix_course, unix_assignment)
	assert unix_assignment not in unix_course.assignments