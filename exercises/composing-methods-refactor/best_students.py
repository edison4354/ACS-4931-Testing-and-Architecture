# By Kamran Bigdely Nov. 2020
# Replace temp variable with query

# TODO: Use 'extract method' refactoring technique to improve this code.
# TODO: If required, use 'replace temp variable with query' technique to make it easier to extract methods.

class Employer:
    """A class to represent a employer"""

    def __init__(self, name):
        self.name = name

    def send(self, students):
        print("Students' contact info were sent to", self.name + '.')


class Student:
    """A class to represent a student"""

    def __init__(self, gpa, name):
        self.gpa = gpa
        self.name = name

    def get_gpa(self):
        return self.gpa

    def send_congrat_email(self):
        print("Congrats", self.name + ". You graduated successfully!")


class School:
    """A class to represent a schools"""

    def __init__(self, students) -> None:
        self.students = students
        self.min_gpa = 2.5  # minimum acceptable GPA

    def print_student_name(self, students):
        '''Print student's name.'''
        for student in students:
            print(student.name)

    def passed_students(self):
        '''Return a list of students who has passed.'''
        passed_students = []
        for student in self.students:
            if student.get_gpa() > self.min_gpa:
                passed_students.append(student)
        return passed_students

    def top_10_percent_students(self, students):
        '''Return a list of the top 10% of students who passes'''
        students.sort(key=lambda s: s.get_gpa())
        percentile = 0.9
        index = int(percentile * len(students))
        return students[index:]

    def process_graduation(self):
        passed_students = self.passed_students()
        # Find and print the students in the school who have successfully graduated.
        print('*** Student who graduated ***')
        self.print_student_name(passed_students)
        print('****************************')

        # Send congrat emails to them.
        for student in passed_students:
            student.send_congrat_email()

        # Find the top 10% of them and send their contact to the top employers
        top_employers = [Employer('Microsoft'), Employer(
            'Free Software Foundation'), Employer('Google')]
        for employer in top_employers:
            employer.send(self.top_10_percent_students(passed_students))


students = [Student(2.1, 'donald'), Student(2.3, 'william'), Student(2.7, 'toro'),
            Student(3.9, 'lili'), Student(3.2, 'kami'), Student(3, 'sarah')]
school = School(students)
school.process_graduation()
