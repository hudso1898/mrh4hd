# Matt Hudson - Software Engineering I Fall '19 - Assignment 5: Testing Focus

My five functions were:

	1) Login
	2) View Assignments
	3) Add Student
	4) Add TA
	5) Add Assignment

I have the functions in [functions.py](./code/functions.py).

I defined classes to represent the data in [classes.py](./code/classes.py).

My test functions are defined in [tests.py](./code/tests.py) using fixtures defined in [fixtures.py](./code/fixtures.py).
Here is the CLI output showing the **passed** tests:

![test-output](./test-output.png)

I wrote two tests for each function to check for different input cases.

For the failing tests, I gave 5 of the test functions the wrong input in [failingtests.py](./code/failingtests.py) (i.e. passed them the wrong fixtures), so I expected them to fail for assignment requirement #4.
Here is the CLI output showing the **failed** tests:

![failed-test-output](./failed-test-output.png)
