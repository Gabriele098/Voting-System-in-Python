from abc import ABC, abstractmethod


class Person(ABC):
    """
    Base class which student and candidate sub-classes will inherit from
    """

    def __init__(self, forename, surname, faculty, gender, year_group):
        self.forename = forename
        self.surname = surname
        self.faculty = faculty
        self.gender = gender
        self.year_group = year_group


class Candidate(Person):
    """
    Sub-Class inheriting from Person
    """

    def __init__(self, forename, surname, position, username, faculty, gender, year_group):
        self.position = position
        self.username = username
        super().__init__(forename, surname, gender, faculty, year_group)


class Student(Person):
    """
    Sub-Class inheriting from Person
    """

    def __init__(self, forename, surname, username, password, faculty, gender, year_group, has_registered=False):
        self.username = username
        self.has_registered = has_registered
        self.password = password
        super().__init__(forename, surname, faculty, gender, year_group)

    def get_registered(self):

        if self.has_registered:
            return f'Student {self.forename} {self.surname} has registered to vote'
        else:
            return f'Student {self.forename} {self.surname} has not registered to vote'

    def set_registered(self, newvalue):

        self.has_registered = newvalue


class PresidentVotes:
    def __init__(self, voting_id, student_username, first_preference, second_preference=None, third_preference=None,
                 fourth_preference=None):
        self.voting_id = voting_id
        self.student_username = student_username
        self.first_preference = first_preference
        self.second_preference = second_preference
        self.third_preference = third_preference
        self.fourth_preference = fourth_preference


class GSUOfficerVotes:
    def __init__(self, voting_id, student_username, first_preference, second_preference=None, third_preference=None,
                 fourth_preference=None):
        self.voting_id = voting_id
        self.student_username = student_username
        self.first_preference = first_preference
        self.second_preference = second_preference
        self.third_preference = third_preference
        self.fourth_preference = fourth_preference


class FacultyOfficerVotes:
    def __init__(self, voting_id, faculty, student_username, first_preference, second_preference=None,
                 third_preference=None, fourth_preference=None):
        self.voting_id = voting_id
        self.faculty = faculty
        self.student_username = student_username
        self.first_preference = first_preference
        self.second_preference = second_preference
        self.third_preference = third_preference
        self.fourth_preference = fourth_preference


class Results:
    def __init__(self, candidate_name, position, faculty, first_preference=0, second_preference=0, third_preference=0,
                 fourth_preference=0):
        self.position = position
        self.faculty = faculty
        self.candidate_name = candidate_name
        self.first_preference = first_preference
        self.second_preference = second_preference
        self.third_preference = third_preference
        self.fourth_preference = fourth_preference
