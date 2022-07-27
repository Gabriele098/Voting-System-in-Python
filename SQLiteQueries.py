import sqlite3
from sqlite3 import Error


# Connecting to our SQLite Database

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def save_president_votes(conn, info):
    """
    :param conn:
    :param info: stu username and their votes
    :return: Student's votes are recorded
    """
    sql = '''INSERT OR IGNORE INTO PresidentVotes(StudentUsername, FirstPreference, SecondPreference, ThirdPreference,
             FourthPreference) VALUES(?, ?, ?, ?, ?)'''
    cur = conn.cursor()
    cur.execute(sql, info)
    return cur.lastrowid


def president_main(username, first_pref, second_pref=None, third_pref=None, fourth_pref=None):
    database = r"C:\Users\qazol\PycharmProjects\VotingSystem3\VotingDatabase.db"
    conn = create_connection(database)

    with conn:
        votes = (username, first_pref, second_pref, third_pref, fourth_pref);
        voting_id = save_president_votes(conn, votes)


# Votes for Faculty Officers

def save_faculty_votes(conn, info):
    """
    :param conn: stu username and their votes
    :param info: Student's facutly votes are recorded
    :return:
    """
    sql = '''INSERT OR IGNORE INTO FacultyOfficerVotes(Faculty, StudentUsername, FirstPreference, SecondPreference,
                                                       ThirdPreference, FourthPreference) VALUES(?, ?, ?, ?, ?, ?)'''
    cur = conn.cursor()
    cur.execute(sql, info)
    return cur.lastrowid


def faculty_main(faculty, username, first_pref, second_pref=None, third_pref=None, fourth_pref=None):
    database = r"C:\Users\qazol\PycharmProjects\VotingSystem3\VotingDatabase.db"
    conn = create_connection(database)

    with conn:
        votes = (faculty, username, first_pref, second_pref, third_pref, fourth_pref);
        voting_id = save_faculty_votes(conn, votes)


# Votes for GSU Officers


def save_officer_votes(conn, info):
    """
    :param conn: stu username and their votes
    :param info: Student's GSU Officer votes are recorded
    :return:
    """
    sql = '''INSERT OR IGNORE INTO GSUOfficerVotes(StudentUsername, FirstPreference, SecondPreference,
                                                   ThirdPreference, FourthPreference) VALUES(?, ?, ?, ?, ?)'''
    cur = conn.cursor()
    cur.execute(sql, info)
    return cur.lastrowid


def officer_main(username, first_pref, second_pref=None, third_pref=None, fourth_pref=None):
    database = r"C:\Users\qazol\PycharmProjects\VotingSystem3\VotingDatabase.db"
    conn = create_connection(database)

    with conn:
        votes = (username, first_pref, second_pref, third_pref, fourth_pref);
        voting_id = save_officer_votes(conn, votes)
