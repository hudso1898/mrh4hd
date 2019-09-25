# contains reusable fixtures for tests

import pytest
from classes import *

@pytest.fixture
def valid_user():
	user = User("mrh4hd", "password12345")
	yield user

@pytest.fixture
def invalid_user():
	yield User("bob", "thisisnotright")

@pytest.fixture
def seng_instructor():
	yield User("sgoggins", "pass")

@pytest.fixture
def unix_instructor():
	yield User("ronny", "whoami")

@pytest.fixture
def seng_course():
	course = Course("CS4320", "Software Engineering I", "sgoggins")
	course.assignments = [Assignment("Assignment 3", "Requirements Focus"), Assignment("Assignment 4", "Design Focus"), Assignment("Assignment 5", "Testing Focus")]
	yield course

@pytest.fixture
def unix_course():
	course = Course("CS3530", "UNIX Operating Systems", "ronny")
	course.assistants = ["mrh4hd"]
	course.assignments = [Assignment("Challenge 9", "Filesystems II")]
	yield course

@pytest.fixture
def unix_assignment():
	yield Assignment("Challenge 1", "Basic Commands")
