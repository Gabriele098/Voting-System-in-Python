import sqlite3
from abc import ABC
from NamesLists import president_names, officer_names, as_faculty_names, eh_faculty_names, \
    sb_faculty_names, es_faculty_names

conn = sqlite3.connect("VotingDatabase.db")
c = conn.cursor()

president_results = []
officer_results = []
faculty_results = []


# Abstract class used as for inheritance into each position class shown below.
class CandidateResults(ABC):
    """
       Is an abstract class with every attributes that a candidate will have
    """

    def __init__(self, full_name, faculty, first=0, second=0, third=0, fourth=0):
        self.full_name = full_name
        self.faculty = faculty
        self.first = first
        self.second = second
        self.third = third
        self.fourth = fourth


class PresidentResults(CandidateResults):
    """
      Inherit from CandidateResults class and stores in integer value the vote for the PresidetResults
    """

    def __init__(self, full_name, faculty, first=0, second=0, third=0, fourth=0):
        super().__init__(full_name, faculty, first, second, third, fourth)


class OfficerResults(CandidateResults):
    """
    Inherits from the CandidateResults class and stores integer values of the votes for the officer candidates
    """

    def __init__(self, full_name, faculty, first=0, second=0, third=0, fourth=0):
        super().__init__(full_name, faculty, first, second, third, fourth)


class FacultyResults(CandidateResults):
    """
    Inherits from the CandidateResults class and stores integer values of the votes for the faculty candidates
    """

    def __init__(self, full_name, faculty, first=0, second=0, third=0, fourth=0):
        super().__init__(full_name, faculty, first, second, third, fourth)


c.execute("SELECT Forename, Surname, Faculty FROM Candidate WHERE Position = 'President'")
for x in c:
    president_results.append(PresidentResults(full_name=x[0] + " " + x[1], faculty=x[2]))

c.execute("SELECT Forename, Surname, Faculty FROM Candidate WHERE Position = 'GSU Officer'")
for x in c:
    officer_results.append(OfficerResults(full_name=x[0] + " " + x[1], faculty=x[2]))

c.execute("SELECT Forename, Surname, Faculty FROM Candidate WHERE Position = 'Faculty Officer'")
for x in c:
    faculty_results.append(FacultyResults(full_name=x[0] + " " + x[1], faculty=x[2]))


def count_president(sql_one, sql_two, voting_list, attr, president_list):
    """
    Function Queries from our SQLite database and counts the number of votes each candidate receives
    Data is then stored within the relevant voting lists as integer values
    """
    counter_dict = {"counter1": 0, "counter2": 0, "counter3": 0, "counter4": 0}

    if sql_two == "PresidentVotes":
        c.execute(f"SELECT {sql_one} FROM {sql_two}")
        for names in c:
            if president_list[0] in names:
                for x in voting_list:
                    if x.full_name == president_list[0]:
                        counter_dict["counter1"] += 1
                        setattr(x, attr, counter_dict["counter1"])
            elif president_list[1] in names:
                for x in voting_list:
                    if x.full_name == president_list[1]:
                        counter_dict["counter2"] += 1
                        setattr(x, attr, counter_dict["counter2"])
            elif president_list[2] in names:
                for x in voting_list:
                    if x.full_name == president_list[2]:
                        counter_dict["counter3"] += 1
                        setattr(x, attr, counter_dict["counter3"])
            elif president_list[3] in names:
                for x in voting_list:
                    if x.full_name == president_list[3]:
                        counter_dict["counter4"] += 1
                        setattr(x, attr, counter_dict["counter4"])


def count_officer(sql_one, sql_two, voting_list, attr, officer_list):
    """
    Function Queries from our SQLite database and counts the number of votes each candidate receives
    Data is then stored within the relevant voting lists as integer values
    """
    counter_dict = {"counter1": 0, "counter2": 0, "counter3": 0, "counter4": 0,
                    "counter5": 0, "counter6": 0, "counter7": 0, "counter8": 0,
                    "counter9": 0, "counter10": 0, "counter11": 0, "counter12": 0}

    c.execute(f"SELECT {sql_one} FROM {sql_two}")
    for names in c:
        if officer_list[0] in names:
            for x in voting_list:
                if x.full_name == officer_list[0]:
                    counter_dict["counter1"] += 1
                    setattr(x, attr, counter_dict["counter1"])
        elif officer_list[1] in names:
            for x in voting_list:
                if x.full_name == officer_list[1]:
                    counter_dict["counter2"] += 1
                    setattr(x, attr, counter_dict["counter2"])
        elif officer_list[2] in names:
            for x in voting_list:
                if x.full_name == officer_list[2]:
                    counter_dict["counter3"] += 1
                    setattr(x, attr, counter_dict["counter3"])
        elif officer_list[3] in names:
            for x in voting_list:
                if x.full_name == officer_list[3]:
                    counter_dict["counter4"] += 1
                    setattr(x, attr, counter_dict["counter4"])
        elif officer_list[4] in names:
            for x in voting_list:
                if x.full_name == officer_list[4]:
                    counter_dict["counter5"] += 1
                    setattr(x, attr, counter_dict["counter5"])
        elif officer_list[5] in names:
            for x in voting_list:
                if x.full_name == officer_list[5]:
                    counter_dict["counter6"] += 1
                    setattr(x, attr, counter_dict["counter6"])
        elif officer_list[6] in names:
            for x in voting_list:
                if x.full_name == officer_list[6]:
                    counter_dict["counter7"] += 1
                    setattr(x, attr, counter_dict["counter7"])
        elif officer_list[7] in names:
            for x in voting_list:
                if x.full_name == officer_list[7]:
                    counter_dict["counter8"] += 1
                    setattr(x, attr, counter_dict["counter8"])
        elif officer_list[8] in names:
            for x in voting_list:
                if x.full_name == officer_list[8]:
                    counter_dict["counter9"] += 1
                    setattr(x, attr, counter_dict["counter9"])
        elif officer_list[9] in names:
            for x in voting_list:
                if x.full_name == officer_list[9]:
                    counter_dict["counter10"] += 1
                    setattr(x, attr, counter_dict["counter10"])
        elif officer_list[10] in names:
            for x in voting_list:
                if x.full_name == officer_list[10]:
                    counter_dict["counter11"] += 1
                    setattr(x, attr, counter_dict["counter11"])
        elif officer_list[11] in names:
            for x in voting_list:
                if x.full_name == officer_list[11]:
                    counter_dict["counter12"] += 1
                    setattr(x, attr, counter_dict["counter12"])


def count_faculty(sql_one, voting_list, attr, faculty_names):
    """
    Function Queries from our SQLite database and counts the number of votes each candidate receives
    Data is then stored within the relevant voting lists as integer values
    """
    counter_dict = {"counter1": 0, "counter2": 0, "counter3": 0, "counter4": 0,
                    "counter5": 0, "counter6": 0, "counter7": 0, "counter8": 0,
                    "counter9": 0, "counter10": 0, "counter11": 0, "counter12": 0,
                    "counter13": 0, "counter14": 0, "counter15": 0, "counter16": 0}

    c.execute(f"SELECT {sql_one} FROM FacultyOfficerVotes")
    for names in c:
        if faculty_names[0] in names:
            for x in voting_list:
                if x.full_name == faculty_names[0]:
                    counter_dict["counter1"] += 1
                    setattr(x, attr, counter_dict["counter1"])
        elif faculty_names[1] in names:
            for x in voting_list:
                if x.full_name == faculty_names[1]:
                    counter_dict["counter2"] += 1
                    setattr(x, attr, counter_dict["counter2"])
        elif faculty_names[2] in names:
            for x in voting_list:
                if x.full_name == faculty_names[2]:
                    counter_dict["counter3"] += 1
                    setattr(x, attr, counter_dict["counter3"])
        elif faculty_names[3] in names:
            for x in voting_list:
                if x.full_name == faculty_names[3]:
                    counter_dict["counter4"] += 1
                    setattr(x, attr, counter_dict["counter4"])
        elif faculty_names[4] in names:
            for x in voting_list:
                if x.full_name == faculty_names[4]:
                    counter_dict["counter5"] += 1
                    setattr(x, attr, counter_dict["counter5"])
        elif faculty_names[5] in names:
            for x in voting_list:
                if x.full_name == faculty_names[5]:
                    counter_dict["counter6"] += 1
                    setattr(x, attr, counter_dict["counter6"])
        elif faculty_names[6] in names:
            for x in voting_list:
                if x.full_name == faculty_names[6]:
                    counter_dict["counter7"] += 1
                    setattr(x, attr, counter_dict["counter7"])
        elif faculty_names[7] in names:
            for x in voting_list:
                if x.full_name == faculty_names[7]:
                    counter_dict["counter8"] += 1
                    setattr(x, attr, counter_dict["counter8"])
        elif faculty_names[8] in names:
            for x in voting_list:
                if x.full_name == faculty_names[8]:
                    counter_dict["counter9"] += 1
                    setattr(x, attr, counter_dict["counter9"])
        elif faculty_names[9] in names:
            for x in voting_list:
                if x.full_name == faculty_names[9]:
                    counter_dict["counter10"] += 1
                    setattr(x, attr, counter_dict["counter10"])
        elif faculty_names[10] in names:
            for x in voting_list:
                if x.full_name == faculty_names[10]:
                    counter_dict["counter11"] += 1
                    setattr(x, attr, counter_dict["counter11"])
        elif faculty_names[11] in names:
            for x in voting_list:
                if x.full_name == faculty_names[11]:
                    counter_dict["counter12"] += 1
                    setattr(x, attr, counter_dict["counter12"])
        elif faculty_names[12] in names:
            for x in voting_list:
                if x.full_name == faculty_names[12]:
                    counter_dict["counter13"] += 1
                    setattr(x, attr, counter_dict["counter13"])
        elif faculty_names[13] in names:
            for x in voting_list:
                if x.full_name == faculty_names[13]:
                    counter_dict["counter14"] += 1
                    setattr(x, attr, counter_dict["counter14"])
        elif faculty_names[14] in names:
            for x in voting_list:
                if x.full_name == faculty_names[14]:
                    counter_dict["counter15"] += 1
                    setattr(x, attr, counter_dict["counter15"])
        elif faculty_names[15] in names:
            for x in voting_list:
                if x.full_name == faculty_names[15]:
                    counter_dict["counter16"] += 1
                    setattr(x, attr, counter_dict["counter16"])


count_president("FirstPreference", "PresidentVotes", president_results,
                "first", president_names)
count_president("SecondPreference", "PresidentVotes", president_results,
                "second", president_names)
count_president("ThirdPreference", "PresidentVotes", president_results,
                "third", president_names)
count_president("FourthPreference", "PresidentVotes", president_results,
                "fourth", president_names)

count_officer("FirstPreference", "GSUOfficerVotes", officer_results,
              "first", officer_names)
count_officer("SecondPreference", "GSUOfficerVotes", officer_results,
              "second", officer_names)
count_officer("ThirdPreference", "GSUOfficerVotes", officer_results,
              "third", officer_names)
count_officer("FourthPreference", "GSUOfficerVotes", officer_results,
              "fourth", officer_names)

count_faculty("FirstPreference", faculty_results,
              "first", sb_faculty_names)
count_faculty("SecondPreference", faculty_results,
              "second", sb_faculty_names)
count_faculty("ThirdPreference", faculty_results,
              "third", sb_faculty_names)
count_faculty("FourthPreference", faculty_results,
              "fourth", sb_faculty_names)

count_faculty("FirstPreference", faculty_results,
              "first", as_faculty_names)
count_faculty("SecondPreference", faculty_results,
              "second", as_faculty_names)
count_faculty("ThirdPreference", faculty_results,
              "third", as_faculty_names)
count_faculty("FourthPreference", faculty_results,
              "fourth", as_faculty_names)

count_faculty("FirstPreference", faculty_results,
              "first", eh_faculty_names)
count_faculty("SecondPreference", faculty_results,
              "second", eh_faculty_names)
count_faculty("ThirdPreference", faculty_results,
              "third", eh_faculty_names)
count_faculty("FourthPreference", faculty_results,
              "fourth", eh_faculty_names)

count_faculty("FirstPreference", faculty_results,
              "first", es_faculty_names)
count_faculty("SecondPreference", faculty_results,
              "second", es_faculty_names)
count_faculty("ThirdPreference", faculty_results,
              "third", es_faculty_names)
count_faculty("FourthPreference", faculty_results,
              "fourth", es_faculty_names)

# The below for loops print out the results from the voting.

# PRESIDENT PART
# In this part we create a txt file for all the candidates president with their respective votes
list_president_votes = []
with open("PresidentResults", "w") as TXTPresident:
    TXTPresident.write("------------------------------------------------------------------------------" + "\n")
    TXTPresident.write(" Position: GSU President" + "\n")
    TXTPresident.write("------------------------------------------------------------------------------" + "\n")
    TXTPresident.write(
        "  Candidate   " + "  1st Preference " + " 2nd Preference " + " 3rd Preference " + " 4th Preference " + "\n")
    TXTPresident.write("  ---------     --------------  --------------  --------------  --------------" + "\n")
    # For loop to write all the detail for every single candidate
    for x in president_results:
        TXTPresident.write(x.full_name + ":" + str(x.first) + "," + str(x.second) + "," + str(x.third) + "," + str(
            x.fourth) + "\n")
        # create a list where we append just the vote so we can sort them
        list_president_votes.append(
            str(x.first) + "," + str(x.second) + "," + str(x.third) + "," + str(
                x.fourth))
    TXTPresident.write("------------------------------------------------------------------------------" + "\n")

# sort the list that we can have the highest vote at the beginning
list_president_votes.sort(reverse=True)

# we are giving the first index of the previews list to a variable and we check if that variable is in the txt file with all the votes
data = (list_president_votes[0])
fk_winner_president = ""
pk_winner_president = []
# chech in whitch line the winner is in and we append the entire line to a list
with open("PresidentResults", "r") as full_president_detail:
    for line in full_president_detail:
        if data in line:
            fk_winner_president = line
            pk_winner_president.append(fk_winner_president)
full_president_detail.close()
# take the specific full name of the winner
newList = []
for i in pk_winner_president:
    newList.append(i.split(':')[0])
# appending the winner, score, tot vote and percentage
t = 0  # counter for the total votes
w = 0  # counter for the winner/s
c.execute("SELECT FirstPreference from PresidentVotes")
# for loop that count how many time the winner name is in the database
for row in c:
    t += 1
    # separate counter for the winner
    if newList[0] in row:
        w += 1
# calculation of the percentage
if t != 0:
    p = (w * 100) / t
else:
    p = 0

# appending the winner name, tot votes, votes received and percentage
with open("PresidentResults", "a+") as PresidentWinner:
    PresidentWinner.write("\n" + "Winner: " + newList[0] + "\n" + "Total votes overall: " + str(t) + "\n" +
                          "Votes the winner received: " + str(
        w) + "\n" + "Percentage of votes received by the winner: " +
                          str(p) + "\n")







# Hack task 6 - Gabriele Qazolli 001037593
# creating a list that will contain the scores of the presidents without the 1st preference
list_president_votes2 = []
# creating a txt file where to store the full details of each president
with open("PresidentResults2", "w") as TXTPresident2:
    # For loop to write all the detail for every single candidate
    for x in president_results:
        TXTPresident2.write(x.full_name + ":" + str(x.second) + "," + str(x.third) + "," + str(
            x.fourth) + "\n")
        # create a list where we append just the vote so we can sort them
        list_president_votes2.append(str(x.second) + "," + str(x.third) + "," + str(
            x.fourth))
# sort the list from the highest to the lowest
list_president_votes2.sort(reverse=True)
# creating a variable that contains the winner
data_sec = (list_president_votes2[0])
# creating a variable that will contain the whole line
fk_winner_president2 = ""
# creating a list that will contains the winner/s
pk_winner_president2 = []
# check in whitch line the winner that has more votes on the second preference is in and we append the entire line to
# a list
with open("PresidentResults2", "r") as full_president_detail2:
    # for loop that find the winner and append the whole line in the list pk_winner_presindent2
    for line in full_president_detail2:
        if data_sec in line:
            fk_winner_president2 = line
            pk_winner_president2.append(fk_winner_president2)
full_president_detail2.close()

# take just the full name of the winner
newList_second_preference = []
# for loop that split the list so we can take just the part we want
for i in pk_winner_president2:
    newList_second_preference.append(i.split(':')[0])

# printing the winner with the highest second preference score
print(newList_second_preference[0])








# OFFICERS PART
# In this part we create a txt file for all the candidates officer with their respective votes
list_officers_votes = []
with open("OfficersResults", "w") as TXTOfficers:
    TXTOfficers.write("------------------------------------------------------------------------------" + "\n")
    TXTOfficers.write(" Position: GSU Officers" + "\n")
    TXTOfficers.write("------------------------------------------------------------------------------" + "\n")
    TXTOfficers.write(
        "  Candidate   " + "  1st Preference " + " 2nd Preference " + " 3rd Preference " + " 4th Preference " + "\n")
    TXTOfficers.write("  ---------     --------------  --------------  --------------  --------------" + "\n")
    for x in officer_results:
        TXTOfficers.write(x.full_name + ":" + str(x.first) + "," + str(x.second) + "," + str(x.third) + "," + str(
            x.fourth) + "\n")
        # create a list where we append just the votes so we can sort them
        list_officers_votes.append(
            str(x.first) + "," + str(x.second) + "," + str(x.third) + "," + str(
                x.fourth))
    TXTOfficers.write("------------------------------------------------------------------------------" + "\n")
list_officers_votes.sort(reverse=True)
# we are giving the first 3 index of the previews list to a variable and we check if these variables are in the txt file with all the votes
data0 = (list_officers_votes[0])  # first winner votes
data1 = (list_officers_votes[1])  # second winner votes
data2 = (list_officers_votes[2])  # third winner votes
fk_winner_officer = ""
pk_winner_officer = []
# creating a list that contain all the details of the winners
with open("OfficersResults", "r") as full_officers_detail:
    for line in full_officers_detail:
        if data0 in line:
            fk_winner_officer = line
            pk_winner_officer.insert(0, fk_winner_officer)
        if data1 in line:
            fk_winner_officer = line
            pk_winner_officer.insert(1, fk_winner_officer)
        if data2 in line:
            fk_winner_officer = line
            pk_winner_officer.insert(2, fk_winner_officer)

full_officers_detail.close()
# taking the full name in a list
newList1 = []
for i in pk_winner_officer:
    newList1.append(i.split(':')[0])
# appending the winners, score, tot vote and percentage
t = 0
w = 0
c.execute("SELECT FirstPreference from GSUOfficerVotes")
for row in c:
    t += 1
    if newList1[0] in row:
        w += 1
    elif newList1[1] in row:
        w += 1
    elif newList1[2] in row:
        w += 1

if t != 0:
    p = (w * 100) / t
else:
    p = 0

with open("OfficersResults", "a+") as OfficerWinner:
    OfficerWinner.write("\n" + "Winners are: " + newList1[0] + ", " + newList1[1] + ", " + newList1[
        2] + "\n" + "Total votes overall: " + str(t) + "\n" +
                        "Votes the winners received: " + str(
        w) + "\n" + "Percentage of votes received by the winners: " +
                        str(p) + "\n")

# In this part we create a txt file for all the candidates for each faculty with their respective votes

# FACULTY SB PART
list_faculty1_votes = []
with open("FacultySBResults", "w") as TXTFacultySB:
    TXTFacultySB.write("------------------------------------------------------------------------------" + "\n")
    TXTFacultySB.write("GSU Faculty: School of Business" + "\n")
    TXTFacultySB.write("------------------------------------------------------------------------------" + "\n")
    TXTFacultySB.write(
        "  Candidate   " + "  1st Preference " + " 2nd Preference " + " 3rd Preference " + " 4th Preference " + "\n")
    TXTFacultySB.write("  ---------     --------------  --------------  --------------  --------------" + "\n")
    for x in faculty_results:
        if x.faculty == "SB":
            TXTFacultySB.write(x.full_name + ":" + str(x.first) + "," + str(x.second) + "," + str(x.third) + "," + str(
                x.fourth) + "\n")
            # create a list where we append just the votes so we can sort them
            list_faculty1_votes.append(
                str(x.first) + "," + str(x.second) + "," + str(x.third) + "," + str(
                    x.fourth))
    TXTFacultySB.write("------------------------------------------------------------------------------" + "\n")

list_faculty1_votes.sort(reverse=True)

# we are giving the first index of the previews list to a variable and we check if that variable is in the txt file with all the votes
data0 = (list_faculty1_votes[0])
data1 = (list_faculty1_votes[1])
data2 = (list_faculty1_votes[2])
data3 = (list_faculty1_votes[3])
fk_winner_facultySB = ""
pk_winner_facultySB = []
with open("FacultySBResults", "r") as full_facultySB_detail:
    for line in full_facultySB_detail:
        if data0 in line:
            fk_winner_facultySB = line
            pk_winner_facultySB.insert(0, fk_winner_facultySB)
        if data1 in line:
            fk_winner_facultySB = line
            pk_winner_facultySB.insert(1, fk_winner_facultySB)
        if data2 in line:
            fk_winner_facultySB = line
            pk_winner_facultySB.insert(2, fk_winner_facultySB)
        if data3 in line:
            fk_winner_facultySB = line
            pk_winner_facultySB.insert(3, fk_winner_facultySB)

full_facultySB_detail.close()
# taking just the full name
newList2 = []
for i in pk_winner_facultySB:
    newList2.append(i.split(':')[0])
# appending the winners, score, tot vote and percentage
t = 0
w = 0
c.execute("SELECT FirstPreference FROM FacultyOfficerVotes WHERE Faculty = 'SB'")
for row in c:
    t += 1
    if newList2[0] in row:
        w += 1
    elif newList2[1] in row:
        w += 1
    elif newList2[2] in row:
        w += 1
    elif newList2[3] in row:
        w += 1

if t != 0:
    p = (w * 100) / t
else:
    p = 0

with open("FacultySBResults", "a+") as FacultySBWinner:
    FacultySBWinner.write(
        "\n" + "Winner: " + newList2[0] + ", " + newList2[1] + ", " + newList2[2] + ", " + newList2[3] + "\n" +
        "Total votes overall: " + str(t) + "\n" +
        "Votes the winners received: " + str(
            w) + "\n" + "Percentage of votes received by the winners: " +
        str(p) + "\n")

# FACULTY ES PART
list_faculty2_votes = []
with open("FacultyESResults", "w") as TXTFacultyES:
    TXTFacultyES.write("------------------------------------------------------------------------------" + "\n")
    TXTFacultyES.write("GSU Faculty: Faculty of Engineering and Science" + "\n")
    TXTFacultyES.write("------------------------------------------------------------------------------" + "\n")
    TXTFacultyES.write(
        "  Candidate   " + "  1st Preference " + " 2nd Preference " + " 3rd Preference " + " 4th Preference " + "\n")
    TXTFacultyES.write("  ---------     --------------  --------------  --------------  --------------" + "\n")
    for x in faculty_results:
        if x.faculty == "ES":
            TXTFacultyES.write(x.full_name + ":" + str(x.first) + "," + str(x.second) + "," + str(x.third) + "," + str(
                x.fourth) + "\n")
            # create a list where we append just the votes so we can sort them
            list_faculty2_votes.append(
                str(x.first) + "," + str(x.second) + "," + str(x.third) + "," + str(
                    x.fourth))
    TXTFacultyES.write("------------------------------------------------------------------------------" + "\n")

list_faculty2_votes.sort(reverse=True)
# we are giving the first index of the previews list to a variable and we check if that variable is in the txt file with all the votes
data0 = (list_faculty2_votes[0])
data1 = (list_faculty2_votes[1])
data2 = (list_faculty2_votes[2])
data3 = (list_faculty2_votes[3])
fk_winner_facultyES = ""
pk_winner_facultyES = []
with open("FacultyESResults", "r") as full_facultyES_detail:
    for line in full_facultyES_detail:
        if data0 in line:
            fk_winner_facultyES = line
            pk_winner_facultyES.insert(0, fk_winner_facultyES)
        if data1 in line:
            fk_winner_facultyES = line
            pk_winner_facultyES.insert(1, fk_winner_facultyES)
        if data2 in line:
            fk_winner_facultyES = line
            pk_winner_facultyES.insert(2, fk_winner_facultyES)
        if data3 in line:
            fk_winner_facultyES = line
            pk_winner_facultyES.insert(3, fk_winner_facultyES)
full_facultyES_detail.close()

# taking just the full name
newList3 = []
for i in pk_winner_facultyES:
    newList3.append(i.split(':')[0])
# appending the winners, score, tot vote and percentage
t = 0
w = 0
c.execute("SELECT FirstPreference FROM FacultyOfficerVotes WHERE Faculty = 'ES'")
for row in c:
    t += 1
    if newList3[0] in row:
        w += 1
    elif newList3[1] in row:
        w += 1
    elif newList3[2] in row:
        w += 1
    elif newList3[3] in row:
        w += 1

if t != 0:
    p = (w * 100) / t
else:
    p = 0

with open("FacultyESResults", "a+") as FacultyESWinner:
    FacultyESWinner.write(
        "\n" + "Winner: " + newList3[0] + ", " + newList3[1] + ", " + newList3[2] + ", " + newList3[3] + "\n" +
        "Total votes overall: " + str(t) + "\n" +
        "Votes the winners received: " + str(
            w) + "\n" + "Percentage of votes received by the winners: " +
        str(p) + "\n")

# FACULTY EH PART
list_faculty3_votes = []
with open("FacultyEHResults", "w") as TXTFacultyEH:
    TXTFacultyEH.write("------------------------------------------------------------------------------" + "\n")
    TXTFacultyEH.write("GSU Faculty: Faculty of Education" + "\n")
    TXTFacultyEH.write("------------------------------------------------------------------------------" + "\n")
    TXTFacultyEH.write(
        "  Candidate   " + "  1st Preference " + " 2nd Preference " + " 3rd Preference " + " 4th Preference " + "\n")
    TXTFacultyEH.write("  ---------     --------------  --------------  --------------  --------------" + "\n")
    for x in faculty_results:
        if x.faculty == "EH":
            TXTFacultyEH.write(x.full_name + ":" + str(x.first) + "," + str(x.second) + "," + str(x.third) + "," + str(
                x.fourth) + "\n")
            # create a list where we append just the votes so we can sort them
            list_faculty3_votes.append(
                str(x.first) + "," + str(x.second) + "," + str(x.third) + "," + str(
                    x.fourth))
    TXTFacultyEH.write("------------------------------------------------------------------------------" + "\n")

list_faculty3_votes.sort(reverse=True)
# we are giving the first index of the previews list to a variable and we check if that variable is in the txt file with all the votes
data0 = (list_faculty3_votes[0])
data1 = (list_faculty3_votes[1])
data2 = (list_faculty3_votes[2])
data3 = (list_faculty3_votes[3])
fk_winner_facultyEH = ""
pk_winner_facultyEH = []
with open("FacultyEHResults", "r") as full_facultyEH_detail:
    for line in full_facultyEH_detail:
        if data0 in line:
            fk_winner_facultyEH = line
            pk_winner_facultyEH.insert(0, fk_winner_facultyEH)
        if data1 in line:
            fk_winner_facultyEH = line
            pk_winner_facultyEH.insert(1, fk_winner_facultyEH)
        if data2 in line:
            fk_winner_facultyEH = line
            pk_winner_facultyEH.insert(2, fk_winner_facultyEH)
        if data3 in line:
            fk_winner_facultyEH = line
            pk_winner_facultyEH.insert(3, fk_winner_facultyEH)
full_facultyEH_detail.close()

# taking just the full name
newList4 = []
for i in pk_winner_facultyEH:
    newList4.append(i.split(':')[0])
# appending the winners, score, tot vote and percentage
t = 0
w = 0
c.execute("SELECT FirstPreference FROM FacultyOfficerVotes WHERE Faculty = 'EH'")
for row in c:
    t += 1
    if newList4[0] in row:
        w += 1
    elif newList4[1] in row:
        w += 1
    elif newList4[2] in row:
        w += 1
    elif newList4[3] in row:
        w += 1

if t != 0:
    p = (w * 100) / t
else:
    p = 0

with open("FacultyEHResults", "a+") as FacultyEHWinner:
    FacultyEHWinner.write(
        "\n" + "Winner: " + newList4[0] + ", " + newList4[1] + ", " + newList4[2] + ", " + newList4[3] + "\n" +
        "Total votes overall: " + str(t) + "\n" +
        "Votes the winners received: " + str(
            w) + "\n" + "Percentage of votes received by the winners: " +
        str(p) + "\n")

# FACULTY AS PART
list_faculty4_votes = []
with open("FacultyASResults", "w") as TXTFacultyAS:
    TXTFacultyAS.write("------------------------------------------------------------------------------" + "\n")
    TXTFacultyAS.write("GSU Faculty: Faculty of Liberal Arts and Sciences" + "\n")
    TXTFacultyAS.write("------------------------------------------------------------------------------" + "\n")
    TXTFacultyAS.write(
        "  Candidate   " + "  1st Preference " + " 2nd Preference " + " 3rd Preference " + " 4th Preference " + "\n")
    TXTFacultyAS.write("  ---------     --------------  --------------  --------------  --------------" + "\n")
    for x in faculty_results:
        if x.faculty == "AS":
            TXTFacultyAS.write(x.full_name + ":" + str(x.first) + "," + str(x.second) + "," + str(x.third) + "," + str(
                x.fourth) + "\n")
            # create a list where we append just the votes so we can sort them
            list_faculty4_votes.append(
                str(x.first) + "," + str(x.second) + "," + str(x.third) + "," + str(
                    x.fourth))
    TXTFacultyAS.write("------------------------------------------------------------------------------" + "\n")

list_faculty4_votes.sort(reverse=True)
# we are giving the first index of the previews list to
# a variable and we check if that variable is in the txt file with all the votes
data0 = (list_faculty4_votes[0])
data1 = (list_faculty4_votes[1])
data2 = (list_faculty4_votes[2])
data3 = (list_faculty4_votes[3])
fk_winner_facultyAS = ""
pk_winner_facultyAS = []
with open("FacultyASResults", "r") as full_facultyAS_detail:
    for line in full_facultyAS_detail:
        if data0 in line:
            fk_winner_facultyAS = line
            pk_winner_facultyAS.insert(0, fk_winner_facultyAS)
        if data1 in line:
            fk_winner_facultyAS = line
            pk_winner_facultyAS.insert(1, fk_winner_facultyAS)
        if data2 in line:
            fk_winner_facultyAS = line
            pk_winner_facultyAS.insert(2, fk_winner_facultyAS)
        if data3 in line:
            fk_winner_facultyAS = line
            pk_winner_facultyAS.insert(3, fk_winner_facultyAS)
full_facultyAS_detail.close()

# taking just the full name
newList5 = []
for i in pk_winner_facultyAS:
    newList5.append(i.split(':')[0])
# appending the winners, score, tot vote and percentage
t = 0
w = 0
# check the amount of 1st preference votes the winner received
c.execute(
    "SELECT FirstPreference FROM FacultyOfficerVotes WHERE Faculty = 'AS'")
for row in c:
    t += 1
    if newList5[0] in row:
        w += 1
    elif newList5[1] in row:
        w += 1
    elif newList5[2] in row:
        w += 1
    elif newList5[3] in row:
        w += 1

if t != 0:
    p = (w * 100) / t
else:
    p = 0

with open("FacultyASResults", "a+") as FacultyASWinner:
    FacultyASWinner.write(
        "\n" + "Winner: " + newList5[0] + ", " + newList5[1] + ", " + newList5[2] + ", " + newList5[
            3] + "\n" + "Total votes overall: " + str(t) + "\n" +
        "Votes the winners received: " + str(
            w) + "\n" + "Percentage of votes received by the winners: " +
        str(p) + "\n")
