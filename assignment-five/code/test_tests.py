import pytest
from functions import *
from classes   import *
from fixtures  import *

# tests for function 1
def test_loginSuccess(valid_user):
	assert login(valid_user.username, valid_user.password)

def test_loginFailure(invalid_user):
	assert not login(invalid_user.username, invalid_user.password)

# tests for function 2
def test_viewAssignmentsDisplaysAssignment(valid_user, unix_course):
	assignments = viewAssignments(valid_user, unix_course)
	assert len(assignments) > 0

def test_viewAssignmentsRestrictsUser(invalid_user, unix_course):
	assignments = viewAssignments(invalid_user, unix_course)
	assert len(assignments) == 0

# tests for function 3
def test_addStudentRestrictsInstructor(valid_user, seng_course, unix_instructor):
	assert not addStudentToCourse(unix_instructor, seng_course, valid_user)
	assert len(seng_course.students) == 0

def test_addStudentAddsStudent(valid_user, seng_course, seng_instructor):
	assert addStudentToCourse(seng_instructor, seng_course, valid_user)
	assert valid_user.username in seng_course.students

# tests for function 4
def test_addTAAddsTA(valid_user, seng_course, seng_instructor):
	assert addTAToCourse(seng_instructor, seng_course, valid_user)
	assert valid_user.username in seng_course.students

def test_addTARestrictsDuplicates(valid_user, unix_course, unix_instructor):
	assert not addTAToCourse(unix_instructor, unix_course, valid_user)

# tests for function 5
def test_addAssignmentRestrictsInstructor(unix_course, seng_instructor, unix_assignment):
	assert not addAssignmentToCourse(seng_instructor, unix_course, unix_assignment)
	assert unix_assignment not in unix_course.assignments

def test_addAssignmentAddsAssignment(unix_course, unix_instructor, unix_assignment):
	assert addAssignmentToCourse(unix_instructor, unix_course, unix_assignment)
	assert unix_assignment in unix_course.assignments
