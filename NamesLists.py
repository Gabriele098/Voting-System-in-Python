from SQLite import candidates, students

president_cand = []
president_names = []
faculty_cand = []
eh_faculty_names = []
es_faculty_names = []
sb_faculty_names = []
as_faculty_names = []
officer_cands = []
officer_names = []

# Creating lists of individual candidate names so that they can chosen from each drop down box

for i in candidates:
    if i.position == "President":
        president_cand.append(i)
        president_names.append(i.forename + " " + i.surname)
    elif i.position == "GSU Officer":
        officer_names.append(i.forename + " " + i.surname)
    elif i.position == "Faculty Officer" and i.faculty == "ES":
        es_faculty_names.append(i.forename + " " + i.surname)
    elif i.position == "Faculty Officer" and i.faculty == "EH":
        eh_faculty_names.append(i.forename + " " + i.surname)
    elif i.position == "Faculty Officer" and i.faculty == "SB":
        sb_faculty_names.append(i.forename + " " + i.surname)
    elif i.position == "Faculty Officer" and i.faculty == "AS":
        as_faculty_names.append(i.forename + " " + i.surname)


# Setting students to be able to vote

def voting_rights(username):
    """
    :param username: enter student's username as a string
    :return: if in list of student username set voting right to True
    """
    correct_user = False
    for student in students:
        if student.username == username:
            correct_user = True
            student.set_registered(True)
    if not correct_user:
        return "Incorrect Student Username"


voting_rights('a')
voting_rights('cm4935a')
voting_rights('rd2034h')
voting_rights('th2034w')
voting_rights('mb3520e')
voting_rights('tb4927g')
voting_rights('hq3984e')
voting_rights('na3084e')
voting_rights('mm4927s')
voting_rights('rs4927g')
voting_rights('ae4028y')
voting_rights('zg4973d')
voting_rights('aa9038y')
voting_rights('cr3928t')
voting_rights('fv5938e')
voting_rights('jc8495r')
voting_rights('bs0382t')
voting_rights('as7513f')
voting_rights('rm9841r')
