import tkinter as tk
import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
import datetime
from PIL import Image, ImageTk
from SQLite import students
from NamesLists import president_names, officer_names, es_faculty_names, sb_faculty_names, as_faculty_names
from NamesLists import eh_faculty_names
from SQLiteQueries import president_main, faculty_main, officer_main
from VotingResults import *

# Creating global variables initially to check later that the user has not voted for a position twice
globals()["presidential_votes"] = 0
globals()["faculty_votes"] = 0
globals()["officer_votes"] = 0

# Connecting to voting database
conn = sqlite3.connect("VotingDatabase.db")
c = conn.cursor()

# Creating List of student usernames
student_usernames = []


class MainWindow:

    def __init__(self, master):
        self.master = master

        # Setting the window up
        self.master.geometry("850x750")
        self.master.title("GSU ELECTIONS 2020")
        # self.master.configure()
        self.master.resizable(width=False, height=False)
        # set a Background
        self.load = Image.open("BCgreenwich.jpg")
        self.render = ImageTk.PhotoImage(self.load)
        self.main_label1 = tk.Label(image=self.render)
        self.main_label1.place(relx=0.5, rely=0.40, anchor="center")
        # set a University Logo
        self.logo = Image.open("UoGlogo.png")
        self.logorender = ImageTk.PhotoImage(self.logo)
        self.main_label2 = tk.Label(image=self.logorender, relief="sunken")
        self.main_label2.place(relx=0.5, rely=0.46, anchor="center")

        self.main_label = tk.Label(text="GSU Elections 2020", background="cornflowerblue", fg="white",
                                   font=("Georgia", "45", "bold", "italic"))
        self.main_label.place(relx=0.5, rely=0.30, anchor="center")

        self.vote_button = tk.Button(text="Vote", font=("Georgia", "12", "bold"), height="2", width=20,
                                     background="lightsteelblue", foreground="black", bd="4", relief="raised",
                                     command=self.vote)
        self.vote_button.place(relx=0.146, rely=0.75, anchor="sw")

        self.quit_button = tk.Button(text="Quit", font=("Georgia", "12", "bold"), height="2", width=20,
                                     background="lightsteelblue", foreground="black", bd="4", relief="raised",
                                     command=self.close_window)
        self.quit_button.place(relx=0.58, rely=0.75, anchor="sw")

        self.results_button = tk.Button(text="Results", font=("Georgia", "12", "bold"), height="2", width=20,
                                        background="lightsteelblue", foreground="black", bd="4", relief="raised",
                                        command=self.result_day)
        self.results_button.place(relx=0.50, rely=0.87, anchor="center")

    def result_day(self):
        """
        Functionality for the button Results that makes it works just in a specific day/days
        """
        open_date = datetime.date.today()
        start_date = datetime.date(2020, 1, 22)
        end_date = datetime.date(2020, 2, 15)

        if start_date <= open_date <= end_date:
            self.visualise_results()
        else:
            showinfo("Alert Message", "The results will be available at the end of the voting period!")

    def vote(self):
        """
        Functionality for user when they press vote on main page
        """
        # Code below checks that voting is open in that specific days
        open_date = datetime.date.today()
        start_date = datetime.date(2020, 1, 20)
        end_date = datetime.date(2020, 1, 26)

        if start_date <= open_date <= end_date:
            self.new_window()
        else:
            showinfo("Alert Message", "Voting is now closed!")

    def close_window(self):
        self.master.destroy()

    def new_window(self):
        self.list = root.place_slaves()
        for l in self.list:
            l.destroy()

        # next window
        self.second_window = SecondWindow(self.master)

    def visualise_results(self):
        self.list = root.place_slaves()
        for l in self.list:
            l.destroy()
        self.results_window = ResultsWindow(self.master)


class SecondWindow:

    def __init__(self, master):
        self.master = master

        # set a Background
        self.load = Image.open("BCgreenwich.jpg")
        self.render = ImageTk.PhotoImage(self.load)
        self.main_label1 = tk.Label(image=self.render)
        self.main_label1.place(relx=0.5, rely=0.40, anchor="center")
        # set a University Logo
        self.logo = Image.open("UoGlogo.png")
        self.logorender = ImageTk.PhotoImage(self.logo)
        self.main_label2 = tk.Label(image=self.logorender, relief="sunken")
        self.main_label2.place(relx=0.51, rely=0.14, anchor="center")
        # login text
        self.login_label = tk.Label(text="Log in with your University Username and Password", bg="cornflowerblue",
                                    fg="white", width="40", height=1, font=("Georgia", "18", "bold", "italic"))
        self.login_label.place(relx=0.50, rely=0.25, anchor="center")

        # Login buttons and Labels
        self.user_label = tk.Label(text="Username", width="15", height="1", bg="RoyalBlue4",
                                   fg="white", font=("Georgia", "10", "bold"))
        self.user_label.place(relx=0.42, rely=0.35, anchor="center")
        self.user_entry = tk.Entry(width="25", borderwidth="3", relief="sunken")
        self.user_entry.place(relx=0.71, rely=0.35, anchor="e")
        self.password_label = tk.Label(text="Password", width="15", height="1", bg="RoyalBlue4",
                                       fg="white", font=("Georgia", "10", "bold"))
        self.password_label.place(relx=0.42, rely=0.40, anchor="center")

        self.password_entry = tk.Entry(show="*", width="25", borderwidth="3", relief="sunken")
        self.password_entry.place(relx=0.71, rely=0.40, anchor="e")

        self.login_entry = tk.Button(text="LOG IN", font=("Gill Sans MT", "12", "bold"), height=1, width="18",
                                     command=self.check_user)
        self.login_entry.place(relx=0.60, rely=0.48, anchor="e")

        self.login_entry = tk.Button(text="EXIT", font=("Gill Sans MT", "12", "bold"), height=1, width="18",
                                     command=self.go_back)
        self.login_entry.place(relx=0.60, rely=0.55, anchor="e")

    def go_back(self):
        self.list = root.place_slaves()
        for l in self.list:
            l.destroy()

        # next window
        self.main_window = MainWindow(self.master)

    def check_user(self):
        self.valid_user = False
        self.has_voted = False
        self.password_attempt = self.password_entry.get()
        self.username_attempt = self.user_entry.get()
        ####PART to UPDATE
        for student in students:
            if student.username == self.username_attempt and student.password == self.password_attempt:
                # check that student is registered to vote or note
                if student.has_registered:
                    student_usernames.append(self.username_attempt)
                    self.valid_user = True
                    globals()["student_faculty"] = student.faculty
                    globals()["student_username"] = student.username

                    cuv = 0
                    c.execute("SELECT StudentUsername from PresidentVotes")
                    for row in c:
                        if student.username in row:
                            cuv += 1

                    c.execute("SELECT StudentUsername from GSUOfficerVotes")
                    for row in c:
                        if student.username in row:
                            cuv += 1

                    c.execute("SELECT StudentUsername from FacultyOfficerVotes")
                    for row in c:
                        if student.username in row:
                            cuv += 1

                    if cuv < 3:
                        self.new_window()
                    else:
                        self.password_entry.delete(0, "end")
                        self.user_entry.delete(0, "end")
                        showinfo("Window", "You have already voted")
                else:
                    self.valid_user = True
                    showinfo("Window", "Sorry {}, you are not registered to vote. "
                                       "Please contact the GSU to request permission to vote".format(student.forename))
        if not self.valid_user:
            self.password_entry.delete(0, "end")
            self.user_entry.delete(0, "end")
            showinfo("Incorrect Details", "Incorrect password or username. Please try again.")

    def new_window(self):
        self.list = root.place_slaves()
        for l in self.list:
            l.destroy()

        # next window
        self.third_window = ThirdWindow(self.master)


class ThirdWindow:
    def __init__(self, master):
        self.master = master
        root.configure(background='MistyRose2')

        self.logo3 = Image.open("GSU-electionsLogo1.jpg")
        self.logorender3 = ImageTk.PhotoImage(self.logo3)
        self.main_label2 = tk.Label(image=self.logorender3)
        self.main_label2.place(relx=0.51, rely=0.38, anchor="center")

        self.choose_label = tk.Label(text="  Choose one of these three", bg="white",
                                     fg="black", width="40", height="1", font=("Georgia", "32", "bold", "italic"))
        self.choose_label.place(relx=0.5, rely=0.10, anchor="center")

        self.president_button = tk.Button(text="GSU President", font=("Gill Sans MT", "12", "bold"), height="3",
                                          width="20", command=self.vote_president)
        self.president_button.place(relx=0.5, rely=0.70, anchor="center")

        self.officer_button = tk.Button(text="GSU Officers", font=("Gill Sans MT", "12", "bold"), height="3",
                                        width="20",
                                        command=self.vote_officer)
        self.officer_button.place(relx=0.20, rely=0.70, anchor="center")

        self.faculty_button = tk.Button(text="GSU Faculty Officers", font=("Gill Sans MT", "12", "bold"), height="3",
                                        width="20", command=self.vote_faculty)
        self.faculty_button.place(relx=0.80, rely=0.70, anchor="center")

        self.back_button = tk.Button(text="Sign Out", font=("Gill Sans MT", "12", "bold"), height="1", width="20",
                                     command=self.go_back)
        self.back_button.place(relx=0.5, rely=0.80, anchor="center")

    def go_back(self):
        self.list = root.place_slaves()
        for l in self.list:
            l.destroy()

        self.signout_window = SignOutWindow(self.master)

    def vote_president(self):
        global presidential_votes

        if not presidential_votes:
            self.list = root.place_slaves()
            for l in self.list:
                l.destroy()
            # Next window class
            self.president_window = PresidentWindow(self.master)
        else:
            showinfo("window", "You cannot vote for this position again. Please try another position")

    def vote_officer(self):
        global officer_votes

        if not officer_votes:
            self.list = root.place_slaves()
            for l in self.list:
                l.destroy()
            self.officer_window = OfficerWindow(self.master)
        else:
            showinfo("window", "You cannot vote for this position again. Please try another position")

    def vote_faculty(self):
        global faculty_votes

        if not faculty_votes:
            self.list = root.place_slaves()
            for l in self.list:
                l.destroy()

            # Code checks what faculty the user is in and then takes them to the correct page
            global student_faculty
            if student_faculty == "EH":
                self.eh_faculty__window = FacultyWindowEH(self.master)
            elif student_faculty == "ES":
                self.es_faculty_window = FacultyWindowES(self.master)
            elif student_faculty == "AS":
                self.as_faculty_window = FacultyWindowAS(self.master)
            elif student_faculty == "SB":
                self.sb_faculty_window = FacultyWindowSB(self.master)
        else:
            showinfo("window", "You cannot vote for this position again. Please try another position")


class SignOutWindow:

    def __init__(self, master):
        self.master = master

        self.thank_you = tk.Label(text="Thank you!", bg="white",
                                     fg="black", width="40", height=1, font=("Georgia", "32", "bold", "italic"))
        self.thank_you.place(relx=0.5, rely=0.10, anchor="center")
        self.label = tk.Label(text="For entering the GSU Voting System",
                              bg="white",
                              fg="black", width="40", height=1, font=("Georgia", "32", "bold", "italic"))
        self.label.place(relx=0.5, rely=0.17, anchor="center")
        self.info_label = tk.Label(text="If you are another student who would like to vote,",
                                   bg="white",
                                   fg="black", width="50", height="1",
                                   font=("Georgia", "20", "bold", "italic"))
        self.info_label.place(relx=0.5, rely=0.44, anchor="center")
        self.info_label_two = tk.Label(text="please close this program and login again to vote correctly.",
                                       bg="white",
                                       fg="black", width="50", height="1",
                                       font=("Georgia", "20", "bold", "italic"))
        self.info_label_two.place(relx=0.5, rely=0.485, anchor="center")
        self.quit_button = tk.Button(text="Quit", font=("Gill Sans MT", "12", "bold"), height="2", width=15, command=self.close_window)
        self.quit_button.place(relx=0.5, rely=0.65, anchor="center")
        # logo GSU
        self.logo4 = Image.open("logogsu.png")
        self.logorender4 = ImageTk.PhotoImage(self.logo4)
        self.main_label2 = tk.Label(image=self.logorender4)
        self.main_label2.place(relx=0.85, rely=0.90, anchor="center")

    def close_window(self):
        self.master.destroy()


class PresidentWindow:

    def __init__(self, master):
        self.master = master

        # Main Headers
        self.president_label = tk.Label(text="GSU President", bg="white",
                                        fg="black", width="40", height="1", font=("Georgia", "32", "bold", "italic"))
        self.president_label.place(relx=0.5, rely=0.10, anchor="center")

        self.president_two_label = tk.Label(text="Please rank each candidate in order of preference", bg="white",
                                            fg="black", width="40", height="1",
                                            font=("Georgia", "22", "bold", "italic"))
        self.president_two_label.place(relx=0.5, rely=0.2, anchor="center")

        # Logo candidate
        self.logoGUI = Image.open("userLogo2.png")
        self.logorender1 = ImageTk.PhotoImage(self.logoGUI)
        self.main_label2 = tk.Label(image=self.logorender1)
        self.main_label2.place(relx=0.15, rely=0.35, anchor="center")
        self.main_label2 = tk.Label(image=self.logorender1)
        self.main_label2.place(relx=0.375, rely=0.35, anchor="center")
        self.main_label2 = tk.Label(image=self.logorender1)
        self.main_label2.place(relx=0.625, rely=0.35, anchor="center")
        self.main_label2 = tk.Label(image=self.logorender1)
        self.main_label2.place(relx=0.848, rely=0.35, anchor="center")

        # All combo boxes
        self.first_box = ttk.Combobox(values=president_names, state="readonly")
        self.first_box.place(relx=0.15, rely=0.55, anchor="center")
        self.second_box = ttk.Combobox(values=president_names, state="readonly")
        self.second_box.place(relx=0.375, rely=0.55, anchor="center")
        self.third_box = ttk.Combobox(values=president_names, state="readonly")
        self.third_box.place(relx=0.625, rely=0.55, anchor="center")
        self.fourth_box = ttk.Combobox(values=president_names, state="readonly")
        self.fourth_box.place(relx=0.85, rely=0.55, anchor="center")

        # Preference labels
        self.first_label = tk.Label(text="1st Preference", bg="RoyalBlue4", width="12",
                                    height="2", fg="white", font=("Georgia", "12", "bold"))
        self.first_label.place(relx=0.15, rely=0.50, anchor="center")
        self.second_label = tk.Label(text="2nd Preference", bg="RoyalBlue4", width="12",
                                     height="2", fg="white", font=("Georgia", "12", "bold"))
        self.second_label.place(relx=0.375, rely=0.50, anchor="center")
        self.third_label = tk.Label(text="3rd Preference", bg="RoyalBlue4", width="12",
                                    height="2", fg="white", font=("Georgia", "12", "bold"))
        self.third_label.place(relx=0.625, rely=0.50, anchor="center")
        self.fourth_label = tk.Label(text="4th Preference", bg="RoyalBlue4", width="12",
                                     height="2", fg="white", font=("Georgia", "12", "bold"))
        self.fourth_label.place(relx=0.85, rely=0.50, anchor="center")

        # Buttons
        self.save_choice = tk.Button(text="Save Choice", font=("Gill Sans MT", "12", "bold"), height="2", width=15,
                                     command=self.save_choice)
        self.save_choice.place(relx=0.5, rely=0.75, anchor="center")
        self.back_button = tk.Button(text="Back", font=("Gill Sans MT", "12", "bold"), height="2", width=15,
                                     command=self.go_back)
        self.back_button.place(relx=0.15, rely=0.90, anchor="center")

        # logo GSU
        self.logo4 = Image.open("logogsu.png")
        self.logorender4 = ImageTk.PhotoImage(self.logo4)
        self.main_label2 = tk.Label(image=self.logorender4)
        self.main_label2.place(relx=0.85, rely=0.90, anchor="center")

    def save_choice(self):
        global student_username
        self.first_choice = self.first_box.get()
        self.second_choice = self.second_box.get()
        self.third_choice = self.third_box.get()
        self.fourth_choice = self.fourth_box.get()
        globals()["presidential_votes"] = 0

        # if user has voted for all four preferences correctly without errors then save entry and continue
        if (self.first_box.get() in president_names and self.second_box.get() in president_names and
                self.third_box.get() in president_names and self.fourth_box.get() in president_names):
            if (self.first_box.get() != self.second_box.get() and self.first_box.get() != self.third_box.get() and
                    self.first_box.get() != self.fourth_box.get() and self.second_box.get() != self.third_box.get() and
                    self.second_box.get() != self.fourth_box.get() and self.third_box.get() != self.fourth_box.get()):
                self.msgbox = tk.messagebox.askquestion("Save & Exit", "Please confirm you are happy with your choices")
                if self.msgbox == "yes":
                    globals()["presidential_votes"] = 1
                    # SQLite Query that saves choices straight into relevant table
                    president_main(username=student_username, first_pref=self.first_choice,
                                   second_pref=self.second_choice, third_pref=self.third_choice,
                                   fourth_pref=self.fourth_choice)
                    self.go_back()

            # If user selects the same candidate twice
            elif (self.first_box.get() == self.second_box.get() or self.first_box.get() == self.third_box.get() or
                  self.first_box.get() == self.fourth_box.get() or self.second_box.get() == self.third_box.get() or
                  self.second_box.get() == self.fourth_box.get() or self.third_box.get() == self.fourth_box.get()):
                showinfo("window", "You cannot select the same candidate twice. Please try again")

        # if user only votes for first preference
        elif (self.first_box.get() in president_names and self.second_box.get() == "" and self.third_box.get() == ""
              and self.fourth_box.get() == ""):
            self.msgbox = tk.messagebox.askquestion("Save & Exit", "Please confirm you are happy with your choice")
            if self.msgbox == "yes":
                globals()["presidential_votes"] = 1
                president_main(username=student_username, first_pref=self.first_choice)
                self.go_back()

        # if user votes for 1st and 2nd preference but not 3rd or 4th
        elif (self.first_box.get() in president_names and self.second_box.get() in president_names and
              self.third_box.get() == "" and self.fourth_box.get() == ""):
            if self.first_box.get() != self.second_box.get():
                self.msgbox = tk.messagebox.askquestion("Save & Exit", "Please confirm you are happy with your choices")
                if self.msgbox == "yes":
                    globals()["presidential_votes"] = 1
                    president_main(username=student_username, first_pref=self.first_choice,
                                   second_pref=self.second_choice)
                    self.go_back()

            else:
                showinfo("Incorrect Input", "You have voted incorrectly. Please try again")

        # if user votes for 1st and 3rd but not 2nd or 4th
        elif (self.first_box.get() in president_names and self.second_box.get() == "" and
              self.third_box.get() in president_names and self.fourth_box.get() == ""):
            if self.first_box.get() != self.third_box.get():
                self.msgbox = tk.messagebox.askquestion("Save & Exit", "Please confirm you are happy with your choices")
                if self.msgbox == "yes":
                    globals()["presidential_votes"] = 1
                    # SQLite Query that saves choices straight into relevant table
                    president_main(username=student_username, first_pref=self.first_choice,
                                   third_pref=self.third_choice)
                    self.go_back()
            else:
                showinfo("Incorrect Input", "You have voted incorrectly. Please try again")

        # if user votes for 1st and 4th but not 2nd or 3rd
        elif (self.first_box.get() in president_names and self.second_box.get() == "" and
              self.third_box.get() == "" and self.fourth_box.get() in president_names):
            if self.first_box.get() != self.fourth_box.get():
                self.msgbox = tk.messagebox.askquestion("Save & Exit", "Please confirm you are happy with your choices")
                if self.msgbox == "yes":
                    globals()["presidential_votes"] = 1
                    # SQLite Query that saves choices straight into relevant table
                    president_main(username=student_username, first_pref=self.first_choice,
                                   fourth_pref=self.fourth_choice)
                    self.go_back()
            else:
                showinfo("Incorrect Input", "You have voted incorrectly. Please try again")

        # if user votes for 1st, 3rd and 4th but not 2nd
        elif (self.first_box.get() in president_names and self.second_box.get() == "" and
              self.third_box.get() in president_names and self.fourth_box.get() in president_names):
            if (self.first_box.get() != self.fourth_box.get() and self.first_box.get() != self.third_box.get() and
                    self.third_box.get() != self.fourth_box.get()):
                self.msgbox = tk.messagebox.askquestion("Save & Exit", "Please confirm you are happy with your choices")
                if self.msgbox == "yes":
                    globals()["presidential_votes"] = 1
                    # SQLite Query that saves choices straight into relevant table
                    president_main(username=student_username, first_pref=self.first_choice,
                                   third_pref=self.third_choice, fourth_pref=self.fourth_choice)
                    self.go_back()
            else:
                showinfo("Incorrect Input", "You have voted incorrectly. Please try again")

        # if user votes for 1st, 2nd and 4th but not 3rd
        elif (self.first_box.get() in president_names and self.second_box.get() in president_names and
              self.third_box.get() == "" and self.fourth_box.get() in president_names):
            if (self.first_box.get() != self.second_box.get() and self.first_box.get() != self.fourth_box.get() and
                    self.second_box.get() != self.fourth_box.get()):
                self.msgbox = tk.messagebox.askquestion("Save & Exit", "Please confirm you are happy with your choices")
                if self.msgbox == "yes":
                    globals()["presidential_votes"] = 1
                    # SQLite Query that saves choices straight into relevant table
                    president_main(username=student_username, first_pref=self.first_choice,
                                   second_pref=self.second_choice, fourth_pref=self.fourth_choice)
                    self.go_back()
            else:
                showinfo("Incorrect Input", "You have voted incorrectly. Please try again")

        # if user votes for 1st, 2nd and 3rd but not 4th
        elif (self.first_box.get() in president_names and self.second_box.get() in president_names and
              self.third_box.get() in president_names and self.fourth_box.get() == ""):
            if (self.first_box.get() != self.second_box.get() and self.first_box.get() != self.third_box.get() and
                    self.second_box.get() != self.third_box.get()):
                self.msgbox = tk.messagebox.askquestion("Save & Exit", "Please confirm you are happy with your choices")
                if self.msgbox == "yes":
                    globals()["presidential_votes"] = 1
                    # SQLite Query that saves choices straight into relevant table
                    president_main(username=student_username, first_pref=self.first_choice,
                                   second_pref=self.second_choice, third_pref=self.third_choice)
                    self.go_back()
            else:
                showinfo("Incorrect Input", "You have voted incorrectly. Please try again")

        # Incorrect voting
        else:
            showinfo("Incorrect Input", "You have voted incorrectly please try again")

    def go_back(self):
        self.list = root.place_slaves()
        for l in self.list:
            l.destroy()

        self.third_window = ThirdWindow(self.master)


class FacultyWindowEH:

    def __init__(self, master):
        self.master = master

        # Main Headers
        self.faculty_label = tk.Label(text="GSU Faculty Officers", bg="white",
                                      fg="black", width="40", height="1", font=("Georgia", "32", "bold", "italic"))
        self.faculty_label.place(relx=0.5, rely=0.10, anchor="center")

        self.faculty_two_label = tk.Label(text="Please rank each candidate in order of preference",
                                          bg="white",
                                          fg="black", width="40", height="1", font=("Georgia", "22", "bold", "italic"))
        self.faculty_two_label.place(relx=0.5, rely=0.2, anchor="center")

        self.unique_label = tk.Label(text="Faculty of Education, ", bg="white",
                                     width="30", height="1", fg="black", font=("Georgia", "14", "bold"))
        self.unique_label.place(relx=0.488, rely=0.88, anchor="center")
        self.unique_label = tk.Label(text="Health and Human Sciences", bg="white",
                                     width="30", height="1", fg="black", font=("Georgia", "14", "bold"))
        self.unique_label.place(relx=0.488, rely=0.915, anchor="center")

        # Logo candidate
        self.logoGUI = Image.open("userLogo2.png")
        self.logorender1 = ImageTk.PhotoImage(self.logoGUI)
        self.main_label2 = tk.Label(image=self.logorender1)
        self.main_label2.place(relx=0.15, rely=0.35, anchor="center")
        self.main_label2 = tk.Label(image=self.logorender1)
        self.main_label2.place(relx=0.375, rely=0.35, anchor="center")
        self.main_label2 = tk.Label(image=self.logorender1)
        self.main_label2.place(relx=0.625, rely=0.35, anchor="center")
        self.main_label2 = tk.Label(image=self.logorender1)
        self.main_label2.place(relx=0.848, rely=0.35, anchor="center")

        # All combo boxes
        self.first_box = ttk.Combobox(values=eh_faculty_names, state="readonly")
        self.first_box.place(relx=0.15, rely=0.55, anchor="center")
        self.second_box = ttk.Combobox(values=eh_faculty_names, state="readonly")
        self.second_box.place(relx=0.375, rely=0.55, anchor="center")
        self.third_box = ttk.Combobox(values=eh_faculty_names, state="readonly")
        self.third_box.place(relx=0.625, rely=0.55, anchor="center")
        self.fourth_box = ttk.Combobox(values=eh_faculty_names, state="readonly")
        self.fourth_box.place(relx=0.85, rely=0.55, anchor="center")

        # Preference labels
        self.first_label = tk.Label(text="1st Preference", bg="RoyalBlue4", width="12",
                                    height="2", fg="white", font=("Georgia", "12", "bold"))
        self.first_label.place(relx=0.15, rely=0.50, anchor="center")
        self.second_label = tk.Label(text="2nd Preference", bg="RoyalBlue4", width="12",
                                     height="2", fg="white", font=("Georgia", "12", "bold"))
        self.second_label.place(relx=0.375, rely=0.50, anchor="center")
        self.third_label = tk.Label(text="3rd Preference", bg="RoyalBlue4", width="12",
                                    height="2", fg="white", font=("Georgia", "12", "bold"))
        self.third_label.place(relx=0.625, rely=0.50, anchor="center")
        self.fourth_label = tk.Label(text="4th Preference", bg="RoyalBlue4", width="12",
                                     height="2", fg="white", font=("Georgia", "12", "bold"))
        self.fourth_label.place(relx=0.85, rely=0.50, anchor="center")

        # Buttons
        self.save_choice = tk.Button(text="Save Choice", font=("Gill Sans MT", "12", "bold"), height="2", width="15",
                                     command=self.save_choice)
        self.save_choice.place(relx=0.5, rely=0.75, anchor="center")
        self.back_button = tk.Button(text="Back", font=("Gill Sans MT", "12", "bold"), height="2", width="15",
                                     command=self.go_back)
        self.back_button.place(relx=0.15, rely=0.90, anchor="center")

        # logo GSU
        self.logo4 = Image.open("logogsu.png")
        self.logorender4 = ImageTk.PhotoImage(self.logo4)
        self.main_label2 = tk.Label(image=self.logorender4)
        self.main_label2.place(relx=0.85, rely=0.90, anchor="center")

    def save_choice(self):
        global student_username
        self.first_choice = self.first_box.get()
        self.second_choice = self.second_box.get()
        self.third_choice = self.third_box.get()
        self.fourth_choice = self.fourth_box.get()
        globals()["faculty_votes"] = 0

        # if user has voted for all four preferences correctly without errors then save entry and continue
        if (self.first_box.get() in eh_faculty_names and self.second_box.get() in eh_faculty_names and
                self.third_box.get() in eh_faculty_names and self.fourth_box.get() in eh_faculty_names):
            if (self.first_box.get() != self.second_box.get() and self.first_box.get() != self.third_box.get() and
                    self.first_box.get() != self.fourth_box.get() and self.second_box.get() != self.third_box.get() and
                    self.second_box.get() != self.fourth_box.get() and self.third_box.get() != self.fourth_box.get()):
                self.msgbox = tk.messagebox.askquestion("Save & Exit", "Please confirm you are happy with your choices")
                if self.msgbox == "yes":
                    globals()["faculty_votes"] = 1
                    # SQLite Query that saves choices straight into relevant table
                    faculty_main(faculty="EH", username=student_username, first_pref=self.first_choice,
                                 second_pref=self.second_choice, third_pref=self.third_choice,
                                 fourth_pref=self.fourth_choice)
                    self.go_back()

            # If user selects the same candidate twice
            elif (self.first_box.get() == self.second_box.get() or self.first_box.get() == self.third_box.get() or
                  self.first_box.get() == self.fourth_box.get() or self.second_box.get() == self.third_box.get() or
                  self.second_box.get() == self.fourth_box.get() or self.third_box.get() == self.fourth_box.get()):
                showinfo("window", "You cannot select the same candidate twice. Please try again")

        # if user only votes for first preference
        elif (self.first_box.get() in eh_faculty_names and self.second_box.get() == "" and self.third_box.get() == ""
              and self.fourth_box.get() == ""):
            self.msgbox = tk.messagebox.askquestion("Save & Exit", "Please confirm you are happy with your choice")
            if self.msgbox == "yes":
                globals()["faculty_votes"] = 1
                faculty_main(faculty="EH", username=student_username, first_pref=self.first_choice)
                self.go_back()

        # if user votes for 1st and 2nd preference but not 3rd or 4th
        elif (self.first_box.get() in eh_faculty_names and self.second_box.get() in eh_faculty_names and
              self.third_box.get() == "" and self.fourth_box.get() == ""):
            if self.first_box.get() != self.second_box.get():
                self.msgbox = tk.messagebox.askquestion("Save & Exit", "Please confirm you are happy with your choices")
                if self.msgbox == "yes":
                    globals()["faculty_votes"] = 1
                    self.go_back()
                    faculty_main(faculty="EH", username=student_username, first_pref=self.first_choice,
                                 second_pref=self.second_choice)
                    self.go_back()

            else:
                showinfo("Incorrect Input", "You have voted incorrectly. Please try again")

        # if user votes for 1st and 3rd but not 2nd or 4th
        elif (self.first_box.get() in eh_faculty_names and self.second_box.get() == "" and
              self.third_box.get() in eh_faculty_names and self.fourth_box.get() == ""):
            if self.first_box.get() != self.third_box.get():
                self.msgbox = tk.messagebox.askquestion("Save & Exit", "Please confirm you are happy with your choices")
                if self.msgbox == "yes":
                    globals()["faculty_votes"] = 1
                    # SQLite Query that saves choices straight into relevant table
                    faculty_main(faculty="EH", username=student_username, first_pref=self.first_choice,
                                 third_pref=self.third_choice)
                    self.go_back()
            else:
                showinfo("Incorrect Input", "You have voted incorrectly. Please try again")

        # if user votes for 1st and 4th but not 2nd or 3rd
        elif (self.first_box.get() in eh_faculty_names and self.second_box.get() == "" and
              self.third_box.get() == "" and self.fourth_box.get() in eh_faculty_names):
            if self.first_box.get() != self.fourth_box.get():
                self.msgbox = tk.messagebox.askquestion("Save & Exit", "Please confirm you are happy with your choices")
                if self.msgbox == "yes":
                    globals()["faculty_votes"] = 1
                    # SQLite Query that saves choices straight into relevant table
                    faculty_main(faculty="EH", username=student_username, first_pref=self.first_choice,
                                 fourth_pref=self.fourth_choice)
                    self.go_back()
            else:
                showinfo("Incorrect Input", "You have voted incorrectly. Please try again")

        # if user votes for 1st, 3rd and 4th but not 2nd
        elif (self.first_box.get() in eh_faculty_names and self.second_box.get() == "" and
              self.third_box.get() in eh_faculty_names and self.fourth_box.get() in eh_faculty_names):
            if (self.first_box.get() != self.fourth_box.get() and self.first_box.get() != self.third_box.get() and
                    self.third_box.get() != self.fourth_box.get()):
                self.msgbox = tk.messagebox.askquestion("Save & Exit", "Please confirm you are happy with your choices")
                if self.msgbox == "yes":
                    globals()["faculty_votes"] = 1
                    # SQLite Query that saves choices straight into relevant table
                    faculty_main(faculty="EH", username=student_username, first_pref=self.first_choice,
                                 third_pref=self.third_choice, fourth_pref=self.fourth_choice)
                    self.go_back()
            else:
                showinfo("Incorrect Input", "You have voted incorrectly. Please try again")

        # if user votes for 1st, 2nd and 4th but not 3rd
        elif (self.first_box.get() in eh_faculty_names and self.second_box.get() in eh_faculty_names and
              self.third_box.get() == "" and self.fourth_box.get() in eh_faculty_names):
            if (self.first_box.get() != self.second_box.get() and self.first_box.get() != self.fourth_box.get() and
                    self.second_box.get() != self.fourth_box.get()):
                self.msgbox = tk.messagebox.askquestion("Save & Exit", "Please confirm you are happy with your choices")
                if self.msgbox == "yes":
                    globals()["faculty_votes"] = 1
                    # SQLite Query that saves choices straight into relevant table
                    faculty_main(faculty="EH", username=student_username, first_pref=self.first_choice,
                                 second_pref=self.second_choice, fourth_pref=self.fourth_choice)
                    self.go_back()
            else:
                showinfo("Incorrect Input", "You have voted incorrectly. Please try again")

        # if user votes for 1st, 2nd and 3rd but not 4th
        elif (self.first_box.get() in eh_faculty_names and self.second_box.get() in eh_faculty_names and
              self.third_box.get() in eh_faculty_names and self.fourth_box.get() == ""):
            if (self.first_box.get() != self.second_box.get() and self.first_box.get() != self.third_box.get() and
                    self.second_box.get() != self.third_box.get()):
                self.msgbox = tk.messagebox.askquestion("Save & Exit", "Please confirm you are happy with your choices")
                if self.msgbox == "yes":
                    globals()["faculty_votes"] = 1
                    # SQLite Query that saves choices straight into relevant table
                    faculty_main(faculty="EH", username=student_username, first_pref=self.first_choice,
                                 second_pref=self.second_choice, third_pref=self.third_choice)
                    self.go_back()
            else:
                showinfo("Incorrect Input", "You have voted incorrectly. Please try again")

        # Incorrect voting
        else:
            showinfo("Incorrect Input", "You have voted incorrectly please try again")

    def go_back(self):
        self.list = root.place_slaves()
        for l in self.list:
            l.destroy()
        self.third_window = ThirdWindow(self.master)


class FacultyWindowES:

    def __init__(self, master):
        self.master = master

        # Main Headers
        self.faculty_label = tk.Label(text="GSU Faculty Officers", bg="white",
                                      fg="black", width="40", height="1", font=("Georgia", "32", "bold", "italic"))
        self.faculty_label.place(relx=0.5, rely=0.10, anchor="center")

        self.faculty_two_label = tk.Label(text="Please rank each candidate in order of preference",
                                          bg="white",
                                          fg="black", width="40", height="1", font=("Georgia", "22", "bold", "italic"))
        self.faculty_two_label.place(relx=0.5, rely=0.2, anchor="center")

        self.unique_label = tk.Label(text="Faculty of Engineering and Science", bg="white",
                                     width="28", height="1", fg="black", font=("Georgia", "15", "bold"))
        self.unique_label.place(relx=0.488, rely=0.88, anchor="center")

        # Logo candidate
        self.logoGUI = Image.open("userLogo2.png")
        self.logorender1 = ImageTk.PhotoImage(self.logoGUI)
        self.main_label2 = tk.Label(image=self.logorender1)
        self.main_label2.place(relx=0.15, rely=0.35, anchor="center")
        self.main_label2 = tk.Label(image=self.logorender1)
        self.main_label2.place(relx=0.375, rely=0.35, anchor="center")
        self.main_label2 = tk.Label(image=self.logorender1)
        self.main_label2.place(relx=0.625, rely=0.35, anchor="center")
        self.main_label2 = tk.Label(image=self.logorender1)
        self.main_label2.place(relx=0.848, rely=0.35, anchor="center")

        # All combo boxes
        self.first_box = ttk.Combobox(values=es_faculty_names, state="readonly")
        self.first_box.place(relx=0.15, rely=0.55, anchor="center")
        self.second_box = ttk.Combobox(values=es_faculty_names, state="readonly")
        self.second_box.place(relx=0.375, rely=0.55, anchor="center")
        self.third_box = ttk.Combobox(values=es_faculty_names, state="readonly")
        self.third_box.place(relx=0.625, rely=0.55, anchor="center")
        self.fourth_box = ttk.Combobox(values=es_faculty_names, state="readonly")
        self.fourth_box.place(relx=0.85, rely=0.55, anchor="center")

        # Preference labels
        self.first_label = tk.Label(text="1st Preference", bg="RoyalBlue4", width="12",
                                    height="2", fg="white", font=("Georgia", "12", "bold"))
        self.first_label.place(relx=0.15, rely=0.50, anchor="center")
        self.second_label = tk.Label(text="2nd Preference", bg="RoyalBlue4", width="12",
                                     height="2", fg="white", font=("Georgia", "12", "bold"))
        self.second_label.place(relx=0.375, rely=0.50, anchor="center")
        self.third_label = tk.Label(text="3rd Preference", bg="RoyalBlue4", width="12",
                                    height="2", fg="white", font=("Georgia", "12", "bold"))
        self.third_label.place(relx=0.625, rely=0.50, anchor="center")
        self.fourth_label = tk.Label(text="4th Preference", bg="RoyalBlue4", width="12",
                                     height="2", fg="white", font=("Georgia", "12", "bold"))
        self.fourth_label.place(relx=0.85, rely=0.50, anchor="center")

        # Buttons
        self.save_choice = tk.Button(text="Save Choice", font=("Gill Sans MT", "12", "bold"), height="2", width="15",
                                     command=self.save_choice)
        self.save_choice.place(relx=0.5, rely=0.75, anchor="center")
        self.back_button = tk.Button(text="Back", font=("Gill Sans MT", "12", "bold"), height="2", width="15",
                                     command=self.go_back)
        self.back_button.place(relx=0.15, rely=0.90, anchor="center")
        # logo GSU
        self.logo4 = Image.open("logogsu.png")
        self.logorender4 = ImageTk.PhotoImage(self.logo4)
        self.main_label2 = tk.Label(image=self.logorender4)
        self.main_label2.place(relx=0.85, rely=0.90, anchor="center")

    def save_choice(self):
        global student_username
        self.first_choice = self.first_box.get()
        self.second_choice = self.second_box.get()
        self.third_choice = self.third_box.get()
        self.fourth_choice = self.fourth_box.get()
        globals()["faculty_votes"] = 0

        # if user has voted for all four preferences correctly without errors then save entry and continue
        if (self.first_box.get() in es_faculty_names and self.second_box.get() in es_faculty_names and
                self.third_box.get() in es_faculty_names and self.fourth_box.get() in es_faculty_names):
            if (self.first_box.get() != self.second_box.get() and self.first_box.get() != self.third_box.get() and
                    self.first_box.get() != self.fourth_box.get() and self.second_box.get() != self.third_box.get() and
                    self.second_box.get() != self.fourth_box.get() and self.third_box.get() != self.fourth_box.get()):
                self.msgbox = tk.messagebox.askquestion("Save & Exit", "Please confirm you are happy with your choices")
                if self.msgbox == "yes":
                    globals()["faculty_votes"] = 1
                    # SQLite Query that saves choices straight into relevant table
                    faculty_main(faculty="ES", username=student_username, first_pref=self.first_choice,
                                 second_pref=self.second_choice, third_pref=self.third_choice,
                                 fourth_pref=self.fourth_choice)
                    self.go_back()

            # If user selects the same candidate twice
            elif (self.first_box.get() == self.second_box.get() or self.first_box.get() == self.third_box.get() or
                  self.first_box.get() == self.fourth_box.get() or self.second_box.get() == self.third_box.get() or
                  self.second_box.get() == self.fourth_box.get() or self.third_box.get() == self.fourth_box.get()):
                showinfo("window", "You cannot select the same candidate twice. Please try again")

        # if user only votes for first preference
        elif (self.first_box.get() in es_faculty_names and self.second_box.get() == "" and self.third_box.get() == ""
              and self.fourth_box.get() == ""):
            self.msgbox = tk.messagebox.askquestion("Save & Exit", "Please confirm you are happy with your choice")
            if self.msgbox == "yes":
                globals()["faculty_votes"] = 1
                faculty_main(faculty="ES", username=student_username, first_pref=self.first_choice)
                self.go_back()

        # if user votes for 1st and 2nd preference but not 3rd or 4th
        elif (self.first_box.get() in es_faculty_names and self.second_box.get() in es_faculty_names and
              self.third_box.get() == "" and self.fourth_box.get() == ""):
            if self.first_box.get() != self.second_box.get():
                self.msgbox = tk.messagebox.askquestion("Save & Exit", "Please confirm you are happy with your choices")
                if self.msgbox == "yes":
                    globals()["faculty_votes"] = 1
                    self.go_back()
                    faculty_main(faculty="ES", username=student_username, first_pref=self.first_choice,
                                 second_pref=self.second_choice)
                    self.go_back()

            else:
                showinfo("Incorrect Input", "You have voted incorrectly. Please try again")

        # if user votes for 1st and 3rd but not 2nd or 4th
        elif (self.first_box.get() in es_faculty_names and self.second_box.get() == "" and
              self.third_box.get() in es_faculty_names and self.fourth_box.get() == ""):
            if self.first_box.get() != self.third_box.get():
                self.msgbox = tk.messagebox.askquestion("Save & Exit", "Please confirm you are happy with your choices")
                if self.msgbox == "yes":
                    globals()["faculty_votes"] = 1
                    # SQLite Query that saves choices straight into relevant table
                    faculty_main(faculty="ES", username=student_username, first_pref=self.first_choice,
                                 third_pref=self.third_choice)
                    self.go_back()
            else:
                showinfo("Incorrect Input", "You have voted incorrectly. Please try again")

        # if user votes for 1st and 4th but not 2nd or 3rd
        elif (self.first_box.get() in es_faculty_names and self.second_box.get() == "" and
              self.third_box.get() == "" and self.fourth_box.get() in es_faculty_names):
            if self.first_box.get() != self.fourth_box.get():
                self.msgbox = tk.messagebox.askquestion("Save & Exit", "Please confirm you are happy with your choices")
                if self.msgbox == "yes":
                    globals()["faculty_votes"] = 1
                    # SQLite Query that saves choices straight into relevant table
                    faculty_main(faculty="ES", username=student_username, first_pref=self.first_choice,
                                 fourth_pref=self.fourth_choice)
                    self.go_back()
            else:
                showinfo("Incorrect Input", "You have voted incorrectly. Please try again")

        # if user votes for 1st, 3rd and 4th but not 2nd
        elif (self.first_box.get() in es_faculty_names and self.second_box.get() == "" and
              self.third_box.get() in es_faculty_names and self.fourth_box.get() in es_faculty_names):
            if (self.first_box.get() != self.fourth_box.get() and self.first_box.get() != self.third_box.get() and
                    self.third_box.get() != self.fourth_box.get()):
                self.msgbox = tk.messagebox.askquestion("Save & Exit", "Please confirm you are happy with your choices")
                if self.msgbox == "yes":
                    globals()["faculty_votes"] = 1
                    # SQLite Query that saves choices straight into relevant table
                    faculty_main(faculty="ES", username=student_username, first_pref=self.first_choice,
                                 third_pref=self.third_choice, fourth_pref=self.fourth_choice)
                    self.go_back()
            else:
                showinfo("Incorrect Input", "You have voted incorrectly. Please try again")

        # if user votes for 1st, 2nd and 4th but not 3rd
        elif (self.first_box.get() in es_faculty_names and self.second_box.get() in es_faculty_names and
              self.third_box.get() == "" and self.fourth_box.get() in es_faculty_names):
            if (self.first_box.get() != self.second_box.get() and self.first_box.get() != self.fourth_box.get() and
                    self.second_box.get() != self.fourth_box.get()):
                self.msgbox = tk.messagebox.askquestion("Save & Exit", "Please confirm you are happy with your choices")
                if self.msgbox == "yes":
                    globals()["faculty_votes"] = 1
                    # SQLite Query that saves choices straight into relevant table
                    faculty_main(faculty="ES", username=student_username, first_pref=self.first_choice,
                                 second_pref=self.second_choice, fourth_pref=self.fourth_choice)
                    self.go_back()
            else:
                showinfo("Incorrect Input", "You have voted incorrectly. Please try again")

        # if user votes for 1st, 2nd and 3rd but not 4th
        elif (self.first_box.get() in es_faculty_names and self.second_box.get() in es_faculty_names and
              self.third_box.get() in es_faculty_names and self.fourth_box.get() == ""):
            if (self.first_box.get() != self.second_box.get() and self.first_box.get() != self.third_box.get() and
                    self.second_box.get() != self.third_box.get()):
                self.msgbox = tk.messagebox.askquestion("Save & Exit", "Please confirm you are happy with your choices")
                if self.msgbox == "yes":
                    globals()["faculty_votes"] = 1
                    # SQLite Query that saves choices straight into relevant table
                    faculty_main(faculty="ES", username=student_username, first_pref=self.first_choice,
                                 second_pref=self.second_choice, third_pref=self.third_choice)
                    self.go_back()
            else:
                showinfo("Incorrect Input", "You have voted incorrectly. Please try again")

        # Incorrect voting
        else:
            showinfo("Incorrect Input", "You have voted incorrectly please try again")

    def go_back(self):
        self.list = root.place_slaves()
        for l in self.list:
            l.destroy()
        self.third_window = ThirdWindow(self.master)


class FacultyWindowAS:

    def __init__(self, master):
        self.master = master

        # Main Headers
        self.faculty_label = tk.Label(text="GSU Faculty Officers", bg="white",
                                      fg="black", width="40", height="1", font=("Georgia", "32", "bold", "italic"))
        self.faculty_label.place(relx=0.5, rely=0.10, anchor="center")

        self.faculty_two_label = tk.Label(text="Please rank each candidate in order of preference",
                                          bg="white",
                                          fg="black", width="40", height="1", font=("Georgia", "22", "bold", "italic"))
        self.faculty_two_label.place(relx=0.5, rely=0.2, anchor="center")

        self.unique_label = tk.Label(text="Faculty of Liberal Arts and Sciences", bg="white",
                                     width="30", height="1", fg="black", font=("Georgia", "14", "bold"))
        self.unique_label.place(relx=0.488, rely=0.88, anchor="center")

        # Logo candidate
        self.logoGUI = Image.open("userLogo2.png")
        self.logorender1 = ImageTk.PhotoImage(self.logoGUI)
        self.main_label2 = tk.Label(image=self.logorender1)
        self.main_label2.place(relx=0.15, rely=0.35, anchor="center")
        self.main_label2 = tk.Label(image=self.logorender1)
        self.main_label2.place(relx=0.375, rely=0.35, anchor="center")
        self.main_label2 = tk.Label(image=self.logorender1)
        self.main_label2.place(relx=0.625, rely=0.35, anchor="center")
        self.main_label2 = tk.Label(image=self.logorender1)
        self.main_label2.place(relx=0.848, rely=0.35, anchor="center")

        # All combo boxes
        self.first_box = ttk.Combobox(values=as_faculty_names, state="readonly")
        self.first_box.place(relx=0.15, rely=0.55, anchor="center")
        self.second_box = ttk.Combobox(values=as_faculty_names, state="readonly")
        self.second_box.place(relx=0.375, rely=0.55, anchor="center")
        self.third_box = ttk.Combobox(values=as_faculty_names, state="readonly")
        self.third_box.place(relx=0.625, rely=0.55, anchor="center")
        self.fourth_box = ttk.Combobox(values=as_faculty_names, state="readonly")
        self.fourth_box.place(relx=0.85, rely=0.55, anchor="center")

        # Preference labels
        self.first_label = tk.Label(text="1st Preference", bg="RoyalBlue4", width="12",
                                    height="2", fg="white", font=("Georgia", "12", "bold"))
        self.first_label.place(relx=0.15, rely=0.50, anchor="center")
        self.second_label = tk.Label(text="2nd Preference", bg="RoyalBlue4", width="12",
                                     height="2", fg="white", font=("Georgia", "12", "bold"))
        self.second_label.place(relx=0.375, rely=0.50, anchor="center")
        self.third_label = tk.Label(text="3rd Preference", bg="RoyalBlue4", width="12",
                                    height="2", fg="white", font=("Georgia", "12", "bold"))
        self.third_label.place(relx=0.625, rely=0.50, anchor="center")
        self.fourth_label = tk.Label(text="4th Preference", bg="RoyalBlue4", width="12",
                                     height="2", fg="white", font=("Georgia", "12", "bold"))
        self.fourth_label.place(relx=0.85, rely=0.50, anchor="center")

        # Buttons
        self.save_choice = tk.Button(text="Save Choice", font=("Gill Sans MT", "12", "bold"), height="2", width="15",
                                     command=self.save_choice)
        self.save_choice.place(relx=0.5, rely=0.75, anchor="center")
        self.back_button = tk.Button(text="Back", font=("Gill Sans MT", "12", "bold"), height="2", width="15",
                                     command=self.go_back)
        self.back_button.place(relx=0.15, rely=0.90, anchor="center")

        # logo GSU
        self.logo4 = Image.open("logogsu.png")
        self.logorender4 = ImageTk.PhotoImage(self.logo4)
        self.main_label2 = tk.Label(image=self.logorender4)
        self.main_label2.place(relx=0.85, rely=0.90, anchor="center")

    def save_choice(self):
        global student_username
        self.first_choice = self.first_box.get()
        self.second_choice = self.second_box.get()
        self.third_choice = self.third_box.get()
        self.fourth_choice = self.fourth_box.get()
        globals()["faculty_votes"] = 0

        # if user has voted for all four preferences correctly without errors then save entry and continue
        if (self.first_box.get() in as_faculty_names and self.second_box.get() in as_faculty_names and
                self.third_box.get() in as_faculty_names and self.fourth_box.get() in as_faculty_names):
            if (self.first_box.get() != self.second_box.get() and self.first_box.get() != self.third_box.get() and
                    self.first_box.get() != self.fourth_box.get() and self.second_box.get() != self.third_box.get() and
                    self.second_box.get() != self.fourth_box.get() and self.third_box.get() != self.fourth_box.get()):
                self.msgbox = tk.messagebox.askquestion("Save & Exit", "Please confirm you are happy with your choices")
                if self.msgbox == "yes":
                    globals()["faculty_votes"] = 1
                    # SQLite Query that saves choices straight into relevant table
                    faculty_main(faculty="AS", username=student_username, first_pref=self.first_choice,
                                 second_pref=self.second_choice, third_pref=self.third_choice,
                                 fourth_pref=self.fourth_choice)
                    self.go_back()

            # If user selects the same candidate twice
            elif (self.first_box.get() == self.second_box.get() or self.first_box.get() == self.third_box.get() or
                  self.first_box.get() == self.fourth_box.get() or self.second_box.get() == self.third_box.get() or
                  self.second_box.get() == self.fourth_box.get() or self.third_box.get() == self.fourth_box.get()):
                showinfo("window", "You cannot select the same candidate twice. Please try again")

        # if user only votes for first preference
        elif (self.first_box.get() in as_faculty_names and self.second_box.get() == "" and self.third_box.get() == ""
              and self.fourth_box.get() == ""):
            self.msgbox = tk.messagebox.askquestion("Save & Exit", "Please confirm you are happy with your choice")
            if self.msgbox == "yes":
                globals()["faculty_votes"] = 1
                faculty_main(faculty="AS", username=student_username, first_pref=self.first_choice)
                self.go_back()

        # if user votes for 1st and 2nd preference but not 3rd or 4th
        elif (self.first_box.get() in as_faculty_names and self.second_box.get() in as_faculty_names and
              self.third_box.get() == "" and self.fourth_box.get() == ""):
            if self.first_box.get() != self.second_box.get():
                self.msgbox = tk.messagebox.askquestion("Save & Exit", "Please confirm you are happy with your choices")
                if self.msgbox == "yes":
                    globals()["faculty_votes"] = 1
                    self.go_back()
                    faculty_main(faculty="AS", username=student_username, first_pref=self.first_choice,
                                 second_pref=self.second_choice)
                    self.go_back()

            else:
                showinfo("Incorrect Input", "You have voted incorrectly. Please try again")

        # if user votes for 1st and 3rd but not 2nd or 4th
        elif (self.first_box.get() in as_faculty_names and self.second_box.get() == "" and
              self.third_box.get() in as_faculty_names and self.fourth_box.get() == ""):
            if self.first_box.get() != self.third_box.get():
                self.msgbox = tk.messagebox.askquestion("Save & Exit", "Please confirm you are happy with your choices")
                if self.msgbox == "yes":
                    globals()["faculty_votes"] = 1
                    # SQLite Query that saves choices straight into relevant table
                    faculty_main(faculty="AS", username=student_username, first_pref=self.first_choice,
                                 third_pref=self.third_choice)
                    self.go_back()
            else:
                showinfo("Incorrect Input", "You have voted incorrectly. Please try again")

        # if user votes for 1st and 4th but not 2nd or 3rd
        elif (self.first_box.get() in as_faculty_names and self.second_box.get() == "" and
              self.third_box.get() == "" and self.fourth_box.get() in as_faculty_names):
            if self.first_box.get() != self.fourth_box.get():
                self.msgbox = tk.messagebox.askquestion("Save & Exit", "Please confirm you are happy with your choices")
                if self.msgbox == "yes":
                    globals()["faculty_votes"] = 1
                    # SQLite Query that saves choices straight into relevant table
                    faculty_main(faculty="AS", username=student_username, first_pref=self.first_choice,
                                 fourth_pref=self.fourth_choice)
                    self.go_back()
            else:
                showinfo("Incorrect Input", "You have voted incorrectly. Please try again")

        # if user votes for 1st, 3rd and 4th but not 2nd
        elif (self.first_box.get() in as_faculty_names and self.second_box.get() == "" and
              self.third_box.get() in as_faculty_names and self.fourth_box.get() in as_faculty_names):
            if (self.first_box.get() != self.fourth_box.get() and self.first_box.get() != self.third_box.get() and
                    self.third_box.get() != self.fourth_box.get()):
                self.msgbox = tk.messagebox.askquestion("Save & Exit", "Please confirm you are happy with your choices")
                if self.msgbox == "yes":
                    globals()["faculty_votes"] = 1
                    # SQLite Query that saves choices straight into relevant table
                    faculty_main(faculty="AS", username=student_username, first_pref=self.first_choice,
                                 third_pref=self.third_choice, fourth_pref=self.fourth_choice)
                    self.go_back()
            else:
                showinfo("Incorrect Input", "You have voted incorrectly. Please try again")

        # if user votes for 1st, 2nd and 4th but not 3rd
        elif (self.first_box.get() in as_faculty_names and self.second_box.get() in as_faculty_names and
              self.third_box.get() == "" and self.fourth_box.get() in as_faculty_names):
            if (self.first_box.get() != self.second_box.get() and self.first_box.get() != self.fourth_box.get() and
                    self.second_box.get() != self.fourth_box.get()):
                self.msgbox = tk.messagebox.askquestion("Save & Exit", "Please confirm you are happy with your choices")
                if self.msgbox == "yes":
                    globals()["faculty_votes"] = 1
                    # SQLite Query that saves choices straight into relevant table
                    faculty_main(faculty="AS", username=student_username, first_pref=self.first_choice,
                                 second_pref=self.second_choice, fourth_pref=self.fourth_choice)
                    self.go_back()
            else:
                showinfo("Incorrect Input", "You have voted incorrectly. Please try again")

        # if user votes for 1st, 2nd and 3rd but not 4th
        elif (self.first_box.get() in as_faculty_names and self.second_box.get() in as_faculty_names and
              self.third_box.get() in as_faculty_names and self.fourth_box.get() == ""):
            if (self.first_box.get() != self.second_box.get() and self.first_box.get() != self.third_box.get() and
                    self.second_box.get() != self.third_box.get()):
                self.msgbox = tk.messagebox.askquestion("Save & Exit", "Please confirm you are happy with your choices")
                if self.msgbox == "yes":
                    globals()["faculty_votes"] = 1
                    # SQLite Query that saves choices straight into relevant table
                    faculty_main(faculty="AS", username=student_username, first_pref=self.first_choice,
                                 second_pref=self.second_choice, third_pref=self.third_choice)
                    self.go_back()
            else:
                showinfo("Incorrect Input", "You have voted incorrectly. Please try again")

        # Incorrect voting
        else:
            showinfo("Incorrect Input", "You have voted incorrectly please try again")

    def go_back(self):
        self.list = root.place_slaves()
        for l in self.list:
            l.destroy()
        self.third_window = ThirdWindow(self.master)


class FacultyWindowSB:

    def __init__(self, master):
        self.master = master

        # Main Headers
        self.faculty_label = tk.Label(text="GSU Faculty Officers", bg="white",
                                      fg="black", width="40", height="1", font=("Georgia", "32", "bold", "italic"))
        self.faculty_label.place(relx=0.5, rely=0.10, anchor="center")

        self.faculty_two_label = tk.Label(text="Please rank each candidate in order of preference",
                                          bg="white",
                                          fg="black", width="40", height="1", font=("Georgia", "22", "bold", "italic"))
        self.faculty_two_label.place(relx=0.5, rely=0.2, anchor="center")

        self.unique_label = tk.Label(text="School of Business", bg="white",
                                     width="25", height="1", fg="black", font=("Georgia", "18", "bold"))
        self.unique_label.place(relx=0.488, rely=0.88, anchor="center")

        # Logo candidate
        self.logoGUI = Image.open("userLogo2.png")
        self.logorender1 = ImageTk.PhotoImage(self.logoGUI)
        self.main_label2 = tk.Label(image=self.logorender1)
        self.main_label2.place(relx=0.15, rely=0.35, anchor="center")
        self.main_label2 = tk.Label(image=self.logorender1)
        self.main_label2.place(relx=0.375, rely=0.35, anchor="center")
        self.main_label2 = tk.Label(image=self.logorender1)
        self.main_label2.place(relx=0.625, rely=0.35, anchor="center")
        self.main_label2 = tk.Label(image=self.logorender1)
        self.main_label2.place(relx=0.848, rely=0.35, anchor="center")

        # All combo boxes
        self.first_box = ttk.Combobox(values=sb_faculty_names, state="readonly")
        self.first_box.place(relx=0.15, rely=0.55, anchor="center")
        self.second_box = ttk.Combobox(values=sb_faculty_names, state="readonly")
        self.second_box.place(relx=0.375, rely=0.55, anchor="center")
        self.third_box = ttk.Combobox(values=sb_faculty_names, state="readonly")
        self.third_box.place(relx=0.625, rely=0.55, anchor="center")
        self.fourth_box = ttk.Combobox(values=sb_faculty_names, state="readonly")
        self.fourth_box.place(relx=0.85, rely=0.55, anchor="center")

        # Preference labels
        self.first_label = tk.Label(text="1st Preference", bg="RoyalBlue4", width="12",
                                    height="2", fg="white", font=("Georgia", "12", "bold"))
        self.first_label.place(relx=0.15, rely=0.50, anchor="center")
        self.second_label = tk.Label(text="2nd Preference", bg="RoyalBlue4", width="12",
                                     height="2", fg="white", font=("Georgia", "12", "bold"))
        self.second_label.place(relx=0.375, rely=0.50, anchor="center")
        self.third_label = tk.Label(text="3rd Preference", bg="RoyalBlue4", width="12",
                                    height="2", fg="white", font=("Georgia", "12", "bold"))
        self.third_label.place(relx=0.625, rely=0.50, anchor="center")
        self.fourth_label = tk.Label(text="4th Preference", bg="RoyalBlue4", width="12",
                                     height="2", fg="white", font=("Georgia", "12", "bold"))
        self.fourth_label.place(relx=0.85, rely=0.50, anchor="center")

        # Buttons
        self.save_choice = tk.Button(text="Save Choice", font=("Gill Sans MT", "12", "bold"), height="2", width="15",
                                     command=self.save_choice)
        self.save_choice.place(relx=0.5, rely=0.75, anchor="center")
        self.back_button = tk.Button(text="Back", font=("Gill Sans MT", "12", "bold"), height="2", width="15",
                                     command=self.go_back)
        self.back_button.place(relx=0.15, rely=0.90, anchor="center")

        # logo GSU
        self.logo4 = Image.open("logogsu.png")
        self.logorender4 = ImageTk.PhotoImage(self.logo4)
        self.main_label2 = tk.Label(image=self.logorender4)
        self.main_label2.place(relx=0.85, rely=0.90, anchor="center")

    def save_choice(self):
        global student_username
        self.first_choice = self.first_box.get()
        self.second_choice = self.second_box.get()
        self.third_choice = self.third_box.get()
        self.fourth_choice = self.fourth_box.get()
        globals()["faculty_votes"] = 0

        # if user has voted for all four preferences correctly without errors then save entry and continue
        if (self.first_box.get() in sb_faculty_names and self.second_box.get() in sb_faculty_names and
                self.third_box.get() in sb_faculty_names and self.fourth_box.get() in sb_faculty_names):
            if (self.first_box.get() != self.second_box.get() and self.first_box.get() != self.third_box.get() and
                    self.first_box.get() != self.fourth_box.get() and self.second_box.get() != self.third_box.get() and
                    self.second_box.get() != self.fourth_box.get() and self.third_box.get() != self.fourth_box.get()):
                self.msgbox = tk.messagebox.askquestion("Save & Exit", "Please confirm you are happy with your choices")
                if self.msgbox == "yes":
                    globals()["faculty_votes"] = 1
                    # SQLite Query that saves choices straight into relevant table
                    faculty_main(faculty="SB", username=student_username, first_pref=self.first_choice,
                                 second_pref=self.second_choice, third_pref=self.third_choice,
                                 fourth_pref=self.fourth_choice)
                    self.go_back()

            # If user selects the same candidate twice
            elif (self.first_box.get() == self.second_box.get() or self.first_box.get() == self.third_box.get() or
                  self.first_box.get() == self.fourth_box.get() or self.second_box.get() == self.third_box.get() or
                  self.second_box.get() == self.fourth_box.get() or self.third_box.get() == self.fourth_box.get()):
                showinfo("window", "You cannot select the same candidate twice. Please try again")

        # if user only votes for first preference
        elif (self.first_box.get() in sb_faculty_names and self.second_box.get() == "" and self.third_box.get() == ""
              and self.fourth_box.get() == ""):
            self.msgbox = tk.messagebox.askquestion("Save & Exit", "Please confirm you are happy with your choice")
            if self.msgbox == "yes":
                globals()["faculty_votes"] = 1
                faculty_main(faculty="SB", username=student_username, first_pref=self.first_choice)
                self.go_back()

        # if user votes for 1st and 2nd preference but not 3rd or 4th
        elif (self.first_box.get() in sb_faculty_names and self.second_box.get() in sb_faculty_names and
              self.third_box.get() == "" and self.fourth_box.get() == ""):
            if self.first_box.get() != self.second_box.get():
                self.msgbox = tk.messagebox.askquestion("Save & Exit", "Please confirm you are happy with your choices")
                if self.msgbox == "yes":
                    globals()["faculty_votes"] = 1
                    self.go_back()
                    faculty_main(faculty="SB", username=student_username, first_pref=self.first_choice,
                                 second_pref=self.second_choice)
                    self.go_back()

            else:
                showinfo("Incorrect Input", "You have voted incorrectly. Please try again")

        # if user votes for 1st and 3rd but not 2nd or 4th
        elif (self.first_box.get() in sb_faculty_names and self.second_box.get() == "" and
              self.third_box.get() in sb_faculty_names and self.fourth_box.get() == ""):
            if self.first_box.get() != self.third_box.get():
                self.msgbox = tk.messagebox.askquestion("Save & Exit", "Please confirm you are happy with your choices")
                if self.msgbox == "yes":
                    globals()["faculty_votes"] = 1
                    # SQLite Query that saves choices straight into relevant table
                    faculty_main(faculty="SB", username=student_username, first_pref=self.first_choice,
                                 third_pref=self.third_choice)
                    self.go_back()
            else:
                showinfo("Incorrect Input", "You have voted incorrectly. Please try again")

        # if user votes for 1st and 4th but not 2nd or 3rd
        elif (self.first_box.get() in sb_faculty_names and self.second_box.get() == "" and
              self.third_box.get() == "" and self.fourth_box.get() in sb_faculty_names):
            if self.first_box.get() != self.fourth_box.get():
                self.msgbox = tk.messagebox.askquestion("Save & Exit", "Please confirm you are happy with your choices")
                if self.msgbox == "yes":
                    globals()["faculty_votes"] = 1
                    # SQLite Query that saves choices straight into relevant table
                    faculty_main(faculty="SB", username=student_username, first_pref=self.first_choice,
                                 fourth_pref=self.fourth_choice)
                    self.go_back()
            else:
                showinfo("Incorrect Input", "You have voted incorrectly. Please try again")

        # if user votes for 1st, 3rd and 4th but not 2nd
        elif (self.first_box.get() in sb_faculty_names and self.second_box.get() == "" and
              self.third_box.get() in sb_faculty_names and self.fourth_box.get() in sb_faculty_names):
            if (self.first_box.get() != self.fourth_box.get() and self.first_box.get() != self.third_box.get() and
                    self.third_box.get() != self.fourth_box.get()):
                self.msgbox = tk.messagebox.askquestion("Save & Exit", "Please confirm you are happy with your choices")
                if self.msgbox == "yes":
                    globals()["faculty_votes"] = 1
                    # SQLite Query that saves choices straight into relevant table
                    faculty_main(faculty="SB", username=student_username, first_pref=self.first_choice,
                                 third_pref=self.third_choice, fourth_pref=self.fourth_choice)
                    self.go_back()
            else:
                showinfo("Incorrect Input", "You have voted incorrectly. Please try again")

        # if user votes for 1st, 2nd and 4th but not 3rd
        elif (self.first_box.get() in sb_faculty_names and self.second_box.get() in sb_faculty_names and
              self.third_box.get() == "" and self.fourth_box.get() in sb_faculty_names):
            if (self.first_box.get() != self.second_box.get() and self.first_box.get() != self.fourth_box.get() and
                    self.second_box.get() != self.fourth_box.get()):
                self.msgbox = tk.messagebox.askquestion("Save & Exit", "Please confirm you are happy with your choices")
                if self.msgbox == "yes":
                    globals()["faculty_votes"] = 1
                    # SQLite Query that saves choices straight into relevant table
                    faculty_main(faculty="SB", username=student_username, first_pref=self.first_choice,
                                 second_pref=self.second_choice, fourth_pref=self.fourth_choice)
                    self.go_back()
            else:
                showinfo("Incorrect Input", "You have voted incorrectly. Please try again")

        # if user votes for 1st, 2nd and 3rd but not 4th
        elif (self.first_box.get() in sb_faculty_names and self.second_box.get() in sb_faculty_names and
              self.third_box.get() in sb_faculty_names and self.fourth_box.get() == ""):
            if (self.first_box.get() != self.second_box.get() and self.first_box.get() != self.third_box.get() and
                    self.second_box.get() != self.third_box.get()):
                self.msgbox = tk.messagebox.askquestion("Save & Exit", "Please confirm you are happy with your choices")
                if self.msgbox == "yes":
                    globals()["faculty_votes"] = 1
                    # SQLite Query that saves choices straight into relevant table
                    faculty_main(faculty="SB", username=student_username, first_pref=self.first_choice,
                                 second_pref=self.second_choice, third_pref=self.third_choice)
                    self.go_back()
            else:
                showinfo("Incorrect Input", "You have voted incorrectly. Please try again")

        # Incorrect voting
        else:
            showinfo("Incorrect Input", "You have voted incorrectly please try again")

    def go_back(self):
        self.list = root.place_slaves()
        for l in self.list:
            l.destroy()
        self.third_window = ThirdWindow(self.master)


class OfficerWindow:

    def __init__(self, master):
        self.master = master

        # Main Headers
        self.officer_label = tk.Label(text="GSU Officers", bg="white",
                                      fg="black", width="40", height="1", font=("Georgia", "32", "bold", "italic"))
        self.officer_label.place(relx=0.5, rely=0.10, anchor="center")

        self.officer_two_label = tk.Label(text="Please rank each candidate in order of preference",
                                          bg="white",
                                          fg="black", width="40", height="1", font=("Georgia", "22", "bold", "italic"))
        self.officer_two_label.place(relx=0.5, rely=0.2, anchor="center")

        # Logo candidate
        self.logoGUI = Image.open("userLogo2.png")
        self.logorender1 = ImageTk.PhotoImage(self.logoGUI)
        self.main_label2 = tk.Label(image=self.logorender1)
        self.main_label2.place(relx=0.15, rely=0.35, anchor="center")
        self.main_label2 = tk.Label(image=self.logorender1)
        self.main_label2.place(relx=0.375, rely=0.35, anchor="center")
        self.main_label2 = tk.Label(image=self.logorender1)
        self.main_label2.place(relx=0.625, rely=0.35, anchor="center")
        self.main_label2 = tk.Label(image=self.logorender1)
        self.main_label2.place(relx=0.848, rely=0.35, anchor="center")

        # All combo boxes

        self.first_box = ttk.Combobox(values=officer_names, state="readonly")
        self.first_box.place(relx=0.15, rely=0.55, anchor="center")
        self.second_box = ttk.Combobox(values=officer_names, state="readonly")
        self.second_box.place(relx=0.375, rely=0.55, anchor="center")
        self.third_box = ttk.Combobox(values=officer_names, state="readonly")
        self.third_box.place(relx=0.625, rely=0.55, anchor="center")
        self.fourth_box = ttk.Combobox(values=officer_names, state="readonly")
        self.fourth_box.place(relx=0.85, rely=0.55, anchor="center")

        # Preference labels
        self.first_label = tk.Label(text="1st Preference", bg="RoyalBlue4", width="12",
                                    height="2", fg="white", font=("Georgia", "11", "bold"))
        self.first_label.place(relx=0.15, rely=0.50, anchor="center")
        self.second_label = tk.Label(text="2nd Preference", bg="RoyalBlue4", width="12",
                                     height="2", fg="white", font=("Georgia", "11", "bold"))
        self.second_label.place(relx=0.375, rely=0.50, anchor="center")
        self.third_label = tk.Label(text="3rd Preference", bg="RoyalBlue4", width="12",
                                    height="2", fg="white", font=("Georgia", 11, "bold"))
        self.third_label.place(relx=0.625, rely=0.50, anchor="center")
        self.fourth_label = tk.Label(text="4th Preference", bg="RoyalBlue4", width="12",
                                     height="2", fg="white", font=("Georgia", "11", "bold"))
        self.fourth_label.place(relx=0.85, rely=0.50, anchor="center")

        # Buttons
        self.save_choice = tk.Button(text="Save Choice", font=("Gill Sans MT", "12", "bold"), height="2", width="15",
                                     command=self.save_choice)
        self.save_choice.place(relx=0.5, rely=0.75, anchor="center")
        self.back_button = tk.Button(text="Back", font=("Gill Sans MT", "12", "bold"), height="2", width="15",
                                     command=self.go_back)
        self.back_button.place(relx=0.15, rely=0.90, anchor="center")

        # logo GSU
        self.logo4 = Image.open("logogsu.png")
        self.logorender4 = ImageTk.PhotoImage(self.logo4)
        self.main_label2 = tk.Label(image=self.logorender4)
        self.main_label2.place(relx=0.85, rely=0.90, anchor="center")

    def save_choice(self):
        global student_username
        self.first_choice = self.first_box.get()
        self.second_choice = self.second_box.get()
        self.third_choice = self.third_box.get()
        self.fourth_choice = self.fourth_box.get()
        globals()["officer_votes"] = 0

        # if user has voted for all four preferences correctly without errors then save entry and continue
        if (self.first_box.get() in officer_names and self.second_box.get() in officer_names and
                self.third_box.get() in officer_names and self.fourth_box.get() in officer_names):
            if (self.first_box.get() != self.second_box.get() and self.first_box.get() != self.third_box.get() and
                    self.first_box.get() != self.fourth_box.get() and self.second_box.get() != self.third_box.get() and
                    self.second_box.get() != self.fourth_box.get() and self.third_box.get() != self.fourth_box.get()):
                self.msgbox = tk.messagebox.askquestion("Save & Exit", "Please confirm you are happy with your choices")
                if self.msgbox == "yes":
                    globals()["officer_votes"] = 1
                    # SQLite Query that saves choices straight into relevant table
                    officer_main(username=student_username, first_pref=self.first_choice,
                                 second_pref=self.second_choice, third_pref=self.third_choice,
                                 fourth_pref=self.fourth_choice)
                    self.go_back()

            # If user selects the same candidate twice
            elif (self.first_box.get() == self.second_box.get() or self.first_box.get() == self.third_box.get() or
                  self.first_box.get() == self.fourth_box.get() or self.second_box.get() == self.third_box.get() or
                  self.second_box.get() == self.fourth_box.get() or self.third_box.get() == self.fourth_box.get()):
                showinfo("window", "You cannot select the same candidate twice. Please try again")

        # if user only votes for first preference
        elif (self.first_box.get() in officer_names and self.second_box.get() == "" and self.third_box.get() == ""
              and self.fourth_box.get() == ""):
            self.msgbox = tk.messagebox.askquestion("Save & Exit", "Please confirm you are happy with your choice")
            if self.msgbox == "yes":
                globals()["officer_votes"] = 1
                officer_main(username=student_username, first_pref=self.first_choice)
                self.go_back()

        # if user votes for 1st and 2nd preference but not 3rd or 4th
        elif (self.first_box.get() in officer_names and self.second_box.get() in officer_names and
              self.third_box.get() == "" and self.fourth_box.get() == ""):
            if self.first_box.get() != self.second_box.get():
                self.msgbox = tk.messagebox.askquestion("Save & Exit", "Please confirm you are happy with your choices")
                if self.msgbox == "yes":
                    globals()["officer_votes"] = 1
                    officer_main(username=student_username, first_pref=self.first_choice,
                                 second_pref=self.second_choice)
                    self.go_back()
            else:
                showinfo("Incorrect Input", "You have voted incorrectly. Please try again")

        # if user votes for 1st and 3rd but not 2nd or 4th
        elif (self.first_box.get() in officer_names and self.second_box.get() == "" and
              self.third_box.get() in officer_names and self.fourth_box.get() == ""):
            if self.first_box.get() != self.third_box.get():
                self.msgbox = tk.messagebox.askquestion("Save & Exit", "Please confirm you are happy with your choices")
                if self.msgbox == "yes":
                    globals()["officer_votes"] = 1
                    # SQLite Query that saves choices straight into relevant table
                    officer_main(username=student_username, first_pref=self.first_choice,
                                 third_pref=self.third_choice)
                    self.go_back()
            else:
                showinfo("Incorrect Input", "You have voted incorrectly. Please try again")

        # if user votes for 1st and 4th but not 2nd or 3rd
        elif (self.first_box.get() in officer_names and self.second_box.get() == "" and
              self.third_box.get() == "" and self.fourth_box.get() in officer_names):
            if self.first_box.get() != self.fourth_box.get():
                self.msgbox = tk.messagebox.askquestion("Save & Exit", "Please confirm you are happy with your choices")
                if self.msgbox == "yes":
                    globals()["officer_votes"] = 1
                    # SQLite Query that saves choices straight into relevant table
                    officer_main(username=student_username, first_pref=self.first_choice,
                                 fourth_pref=self.fourth_choice)
                    self.go_back()
            else:
                showinfo("Incorrect Input", "You have voted incorrectly. Please try again")

        # if user votes for 1st, 3rd and 4th but not 2nd
        elif (self.first_box.get() in officer_names and self.second_box.get() == "" and
              self.third_box.get() in officer_names and self.fourth_box.get() in officer_names):
            if (self.first_box.get() != self.fourth_box.get() and self.first_box.get() != self.third_box.get() and
                    self.third_box.get() != self.fourth_box.get()):
                self.msgbox = tk.messagebox.askquestion("Save & Exit", "Please confirm you are happy with your choices")
                if self.msgbox == "yes":
                    globals()["officer_votes"] = 1
                    # SQLite Query that saves choices straight into relevant table
                    officer_main(username=student_username, first_pref=self.first_choice,
                                 third_pref=self.third_choice, fourth_pref=self.fourth_choice)
                    self.go_back()
            else:
                showinfo("Incorrect Input", "You have voted incorrectly. Please try again")

        # if user votes for 1st, 2nd and 4th but not 3rd
        elif (self.first_box.get() in officer_names and self.second_box.get() in officer_names and
              self.third_box.get() == "" and self.fourth_box.get() in officer_names):
            if (self.first_box.get() != self.second_box.get() and self.first_box.get() != self.fourth_box.get() and
                    self.second_box.get() != self.fourth_box.get()):
                self.msgbox = tk.messagebox.askquestion("Save & Exit", "Please confirm you are happy with your choices")
                if self.msgbox == "yes":
                    globals()["officer_votes"] = 1
                    # SQLite Query that saves choices straight into relevant table
                    officer_main(username=student_username, first_pref=self.first_choice,
                                 second_pref=self.second_choice, fourth_pref=self.fourth_choice)
                    self.go_back()
            else:
                showinfo("Incorrect Input", "You have voted incorrectly. Please try again")

        # if user votes for 1st, 2nd and 3rd but not 4th
        elif (self.first_box.get() in officer_names and self.second_box.get() in officer_names and
              self.third_box.get() in officer_names and self.fourth_box.get() == ""):
            if (self.first_box.get() != self.second_box.get() and self.first_box.get() != self.third_box.get() and
                    self.second_box.get() != self.third_box.get()):
                self.msgbox = tk.messagebox.askquestion("Save & Exit", "Please confirm you are happy with your choices")
                if self.msgbox == "yes":
                    globals()["officer_votes"] = 1
                    # SQLite Query that saves choices straight into relevant table
                    officer_main(username=student_username, first_pref=self.first_choice,
                                 second_pref=self.second_choice, third_pref=self.third_choice)
                    self.go_back()
            else:
                showinfo("Incorrect Input", "You have voted incorrectly. Please try again")

        # Incorrect voting
        else:
            showinfo("Incorrect Input", "You have voted incorrectly please try again")

    def go_back(self):
        self.list = root.place_slaves()
        for l in self.list:
            l.destroy()
        self.third_window = ThirdWindow(self.master)


###ResultsGUI
positions = ['President', 'GSU Officers', 'AS Faculty Officers', 'EH Faculty Officers', 'ES Faculty Officers',
             'SB Faculty Officers', 'All GSU Positions']


class ResultsWindow:
    def __init__(self, master):
        self.master = master
        root.configure(background='#252850')
        self.firstlabel = tk.Label(text="GSU ELECTIONS : Results", width="50", fg="#FFC0CB", bg="#252850",
                                   font=("Century Gothic", "55", "bold"))
        self.firstlabel.place(relx=0.5, rely=0.20, anchor='center')
        self.choose = tk.Label(text="Choose the position to see results", width="30", fg="white", bg="#252850",
                               font=("Century Gothic", "35", "italic"))
        self.choose.place(relx=0.5, rely=0.35, anchor="center")
        self.position = ttk.Combobox(values=positions, state="readonly")
        self.position.place(relx=0.5, rely=0.45, anchor="center")
        self.select = tk.Button(text="Select", font=("Gill Sans MT", "12", "bold"), height="1", width="20",
                                command=self.results_position)
        self.select.place(relx=0.5, rely=0.72, anchor="center")
        self.back = tk.Button(text='Back', font=("Gill Sans MT", "12", "bold"), height="1", width="20",
                              command=self.go_back)
        self.back.place(relx=0.5, rely=0.80, anchor="center")

    def go_back(self):
        self.list = root.place_slaves()
        for l in self.list:
            l.destroy()
        self.main_window = MainWindow(self.master)

    def results_position(self):
        self.position_selected = self.position.get()
        if self.position_selected == 'President':
            self.list = root.place_slaves()
            for l in self.list:
                l.destroy()
            self.results_president = ResultsPresidentW(self.master)
        elif self.position_selected == 'GSU Officers':
            self.list = root.place_slaves()
            for l in self.list:
                l.destroy()
            self.results_gsuofficer = ResultsGSUW(self.master)
        elif self.position_selected == 'AS Faculty Officers':
            self.list = root.place_slaves()
            for l in self.list:
                l.destroy()
            self.results_ASfacultyofficer = ResultsASFacultyWindow(self.master)
        elif self.position_selected == 'EH Faculty Officers':
            self.list = root.place_slaves()
            for l in self.list:
                l.destroy()
            self.results_EHfacultyofficer = ResultsEHFacultyWindow(self.master)
        elif self.position_selected == 'ES Faculty Officers':
            self.list = root.place_slaves()
            for l in self.list:
                l.destroy()
            self.results_ESfacultyofficer = ResultsESFacultyWindow(self.master)
        elif self.position_selected == 'SB Faculty Officers':
            self.list = root.place_slaves()
            for l in self.list:
                l.destroy()
            self.results_SBfacultyofficer = ResultsSBFacultyWindow(self.master)
        elif self.position_selected == 'All GSU Positions':
            self.list = root.place_slaves()
            for l in self.list:
                l.destroy()
            self.results_allGSU = ResultsSummaryWindow(self.master)


class ResultsPresidentW:
    def __init__(self, master):
        self.master = master
        root.configure(background='#252850')
        self.firstlabel = tk.Label(text="GSU ELECTIONS : Results", width="50", fg="#FFC0CB", bg="#252850",
                                   font=("Century Gothic", "55", "bold"))
        self.firstlabel.place(relx=0.5, rely=0.15, anchor='center')
        self.secondlabel = tk.Label(text="President", width="30", fg="white", bg="#252850",
                                    font=("Century Gothic", "40", "bold", "italic", "underline"))
        self.secondlabel.place(relx=0.5, rely=0.30, anchor='center')
        self.candidatelist = Listbox(master, width=32, height=6, bg="white", fg="#252850",
                                     font=("Century Gothic", "20"))
        self.candidatelist.place(relx=0.30, rely=0.54, anchor='center')
        # self.candidatelist.insert(END, "    Candidate  :    1stP    -    2ndP    -    3rdP    -    4thP")
        self.candidatelist.insert(END, "\n  ")
        for x in president_results:
            self.candidatelist.insert(END, "\n    %s " % x.full_name + ":   " + str(x.first) + "   -   " + str(
                x.second) + "  -   " + str(x.third) + "  -  " + str(
                x.fourth) + "\n")

        self.winner = tk.Label(text="GSU President 2020: ", width="18", fg="#252850", bg="#FFC0CB",
                               font=("Century Gothic", "20"))
        self.winner.place(relx=0.80, rely=0.50, anchor='center')
        self.winnername = tk.Label(text="Winner: %s" % newList[0], width="18", fg="#252850", bg="#FFC0CB",
                                   font=("Century Gothic", "20", "bold"))
        self.winnername.place(relx=0.80, rely=0.55, anchor='center')
        t = 0
        w = 0
        c.execute("SELECT FirstPreference from PresidentVotes")
        for row in c:
            t += 1
            if newList[0] in row:
                w += 1
        self.totalvotes = tk.Label(text="Total votes overall: %d" % t, width="18", fg="white", bg="#252850",
                                   font=("Century Gothic", "19"))
        self.totalvotes.place(relx=0.5, rely=0.75, anchor='center')
        self.voteswinner = tk.Label(text="Votes the winner received: %d" % w, width="25", fg="white", bg="#252850",
                                    font=("Century Gothic", "19"))
        self.voteswinner.place(relx=0.5, rely=0.80, anchor='center')
        p = (w * 100) / t
        self.percentage = tk.Label(text="Percentage of votes received by the winner: %d" % p, width="45", fg="white",
                                   bg="#252850",
                                   font=("Century Gothic", "19"))
        self.percentage.place(relx=0.5, rely=0.85, anchor='center')
        self.back = tk.Button(text='Back', font=("Gill Sans MT", "12", "bold"), height="1", width="20",
                              command=self.go_back)
        self.back.place(relx=0.5, rely=0.92, anchor="center")

    def go_back(self):
        self.list = root.place_slaves()
        for l in self.list:
            l.destroy()
        self.third_window = ResultsWindow(self.master)


class ResultsGSUW:
    def __init__(self, master):
        self.master = master
        root.configure(background='#252850')
        self.firstlabel = tk.Label(text="GSU ELECTIONS : Results", width="50", fg="#FFC0CB", bg="#252850",
                                   font=("Century Gothic", "55", "bold"))
        self.firstlabel.place(relx=0.5, rely=0.15, anchor='center')
        self.secondlabel = tk.Label(text="GSU Officers", width="30", fg="white", bg="#252850",
                                    font=("Century Gothic", "40", "bold", "italic", "underline"))
        self.secondlabel.place(relx=0.5, rely=0.27, anchor='center')
        self.candidatelist = Listbox(master, width=35, height=14, bg="white", fg="#252850",
                                     font=("Century Gothic", "15"))
        self.candidatelist.place(relx=0.30, rely=0.54, anchor='center')
        # self.candidatelist.insert(END, "    Candidate  :    1stP    -    2ndP    -    3rdP    -    4thP")
        self.candidatelist.insert(END, "\n  ")
        for x in officer_results:
            self.candidatelist.insert(END, "\n    %s " % x.full_name + ":   " + str(x.first) + "   -   " + str(
                x.second) + "  -   " + str(x.third) + "  -  " + str(
                x.fourth) + "\n")

        self.winner = tk.Label(text="GSU Officers 2020: ", width="18", fg="#252850", bg="#FFC0CB",
                               font=("Century Gothic", "20"))
        self.winner.place(relx=0.80, rely=0.50, anchor='center')
        # Depends on the votes
        self.winnername = tk.Label(text="Winners: %s" % newList1[0] + "\n %s" % newList1[1] + "\n %s" % newList1[2],
                                   fg="#252850", bg="#FFC0CB", width="18",
                                   font=("Century Gothic", "20", "bold"))
        self.winnername.place(relx=0.80, rely=0.59, anchor='center')
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
        self.totalvotes = tk.Label(text="Total votes overall: %d" % t, width="18", fg="white", bg="#252850",
                                   font=("Century Gothic", "18"))
        self.totalvotes.place(relx=0.50, rely=0.80, anchor='center')
        self.voteswinner = tk.Label(text="Votes the winner received: %d" % w, width="25", fg="white", bg="#252850",
                                    font=("Century Gothic", "18"))
        self.voteswinner.place(relx=0.50, rely=0.85, anchor='center')
        p = (w * 100) / t
        self.percentage = tk.Label(text="Percentage of votes received by the winners: %d" % p, width="45", fg="white",
                                   bg="#252850",
                                   font=("Century Gothic", "18"))
        self.percentage.place(relx=0.50, rely=0.90, anchor='center')
        self.back = tk.Button(text='Back', font=("Gill Sans MT", "12", "bold"), height="1", width="20",
                              command=self.go_back)
        self.back.place(relx=0.50, rely=0.95, anchor="center")

    def go_back(self):
        self.list = root.place_slaves()
        for l in self.list:
            l.destroy()
        self.third_window = ResultsWindow(self.master)


class ResultsASFacultyWindow:
    def __init__(self, master):
        self.master = master
        root.configure(background='#252850')
        self.firstlabel = tk.Label(text="GSU ELECTIONS : Results", width="50", fg="#FFC0CB", bg="#252850",
                                   font=("Century Gothic", "55", "bold"))
        self.firstlabel.place(relx=0.5, rely=0.05, anchor='center')
        self.secondlabel = tk.Label(text="Faculty Officers - Liberal Arts and Sciences", width="60", fg="white",
                                    bg="#252850", font=("Century Gothic", "30", "bold", "italic", "underline"))
        self.secondlabel.place(relx=0.5, rely=0.15, anchor='center')
        self.candidatelist = Listbox(master, width=35, height=18, bg="white", fg="#252850",
                                     font=("Century Gothic", "15"))
        self.candidatelist.place(relx=0.30, rely=0.48, anchor='center')
        # self.candidatelist.insert(END, "    Candidate  :    1stP    -    2ndP    -    3rdP    -    4thP")
        self.candidatelist.insert(END, "\n  ")
        for x in faculty_results:
            if x.faculty == "AS":
                self.candidatelist.insert(END, "\n    %s " % x.full_name + ":   " + str(x.first) + "   -   " +
                                          str(x.second) + "  -   " + str(x.third) + "  -  " + str(x.fourth) + "\n")

        self.winner = tk.Label(text="AS Faculty Officers 2020: ", width="20", fg="#252850", bg="#FFC0CB",
                               font=("Century Gothic", "20"))
        self.winner.place(relx=0.77, rely=0.40, anchor='center')
        # Depends on the votes
        self.winnername = tk.Label(text="Winners: %s" % newList5[0] + "\n %s" % newList5[1] + "\n %s" % newList5[2] +
                                        "\n %s" % newList5[3], fg="#252850", bg="#FFC0CB",
                                   width="20", font=("Century Gothic", "20", "bold"))
        self.winnername.place(relx=0.77, rely=0.51, anchor='center')
        t = 0
        w = 0
        c.execute("SELECT FirstPreference FROM FacultyOfficerVotes WHERE Faculty = 'AS'") #check the amount of 1st preference votes the winner received
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

        self.totalvotes = tk.Label(text="Total votes overall: %d" % t, width="18", fg="white", bg="#252850",
                                   font=("Century Gothic", "18"))
        self.totalvotes.place(relx=0.5, rely=0.80, anchor='center')
        self.voteswinner = tk.Label(text="Votes the winners received: %d" % w, width="25", fg="white", bg="#252850",
                                    font=("Century Gothic", "18"))
        self.voteswinner.place(relx=0.5, rely=0.85, anchor='center')
        if t != 0:
            p = (w * 100) / t
        else:
            p = 0
        self.percentage = tk.Label(text="Percentage of votes received by the winners: %d" % p, width="45", fg="white",
                                   bg="#252850",
                                   font=("Century Gothic", "18"))
        self.percentage.place(relx=0.5, rely=0.90, anchor='center')
        self.back = tk.Button(text='Back', font=("Gill Sans MT", "12", "bold"), height="1", width="20",
                              command=self.go_back)
        self.back.place(relx=0.5, rely=0.95, anchor="center")

    def go_back(self):
        self.list = root.place_slaves()
        for l in self.list:
            l.destroy()
        self.third_window = ResultsWindow(self.master)


class ResultsEHFacultyWindow:
    def __init__(self, master):
        self.master = master
        root.configure(background='#252850')
        self.firstlabel = tk.Label(text="GSU ELECTIONS : Results", width="50", fg="#FFC0CB", bg="#252850",
                                   font=("Century Gothic", "55", "bold"))
        self.firstlabel.place(relx=0.5, rely=0.05, anchor='center')
        self.secondlabel = tk.Label(text="Faculty of Education Officers", width="60", fg="white", bg="#252850",
                                    font=("Century Gothic", "30", "bold", "italic", "underline"))
        self.secondlabel.place(relx=0.5, rely=0.15, anchor='center')
        self.candidatelist = Listbox(master, width=35, height=18, bg="white", fg="#252850",
                                     font=("Century Gothic", "15"))
        self.candidatelist.place(relx=0.30, rely=0.48, anchor='center')
        # self.candidatelist.insert(END, "    Candidate  :    1stP    -    2ndP    -    3rdP    -    4thP")
        self.candidatelist.insert(END, "\n  ")
        for x in faculty_results:
            if x.faculty == "EH":
                self.candidatelist.insert(END, "\n    %s " % x.full_name + ":   " + str(x.first) + "   -   " + str(
                    x.second) + "  -   " + str(x.third) + "  -  " + str(
                    x.fourth) + "\n")

        self.winner = tk.Label(text="Faculty of Education Officers 2020: ", width="30", fg="#252850", bg="#FFC0CB",
                               font=("Century Gothic", "15"))
        self.winner.place(relx=0.77, rely=0.40, anchor='center')
        # Depends on the votes
        self.winnername = tk.Label(text="Winners: %s" % newList4[0] + "\n %s" % newList4[1] + "\n %s" % newList4[2] +
                                        "\n %s" % newList4[3], fg="#252850", bg="#FFC0CB",
                                   width="30", font=("Century Gothic", "15", "bold"))
        self.winnername.place(relx=0.77, rely=0.48, anchor='center')
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
        self.totalvotes = tk.Label(text="Total votes overall: %d" % t, width="18", fg="white", bg="#252850",
                                   font=("Century Gothic", "18"))
        self.totalvotes.place(relx=0.5, rely=0.80, anchor='center')
        self.voteswinner = tk.Label(text="Votes the winners received: %d" % w, width="25", fg="white", bg="#252850",
                                    font=("Century Gothic", "18"))
        self.voteswinner.place(relx=0.5, rely=0.85, anchor='center')
        if t != 0:
            p = (w * 100) / t
        else:
            p = 0
        self.percentage = tk.Label(text="Percentage of votes received by the winners: %d" % p, width="45", fg="white",
                                   bg="#252850",
                                   font=("Century Gothic", "18"))
        self.percentage.place(relx=0.5, rely=0.90, anchor='center')
        self.back = tk.Button(text='Back', font=("Gill Sans MT", "12", "bold"), height="1", width="20",
                              command=self.go_back)
        self.back.place(relx=0.5, rely=0.95, anchor="center")

    def go_back(self):
        self.list = root.place_slaves()
        for l in self.list:
            l.destroy()
        self.third_window = ResultsWindow(self.master)


class ResultsESFacultyWindow:
    def __init__(self, master):
        self.master = master
        root.configure(background='#252850')
        self.firstlabel = tk.Label(text="GSU ELECTIONS : Results", width="50", fg="#FFC0CB", bg="#252850",
                                   font=("Century Gothic", "55", "bold"))
        self.firstlabel.place(relx=0.5, rely=0.05, anchor='center')
        self.secondlabel = tk.Label(text="Faculty of Engineering and Science Officers", width="60", fg="white",
                                    bg="#252850", font=("Century Gothic", "30", "bold", "italic", "underline"))
        self.secondlabel.place(relx=0.5, rely=0.15, anchor='center')
        self.candidatelist = Listbox(master, width=35, height=18, bg="white", fg="#252850",
                                     font=("Century Gothic", "15"))
        self.candidatelist.place(relx=0.30, rely=0.48, anchor='center')
        # self.candidatelist.insert(END, "    Candidate  :    1stP    -    2ndP    -    3rdP    -    4thP")
        self.candidatelist.insert(END, "\n  ")
        for x in faculty_results:
            if x.faculty == "ES":
                self.candidatelist.insert(END, "\n    %s " % x.full_name + ":   " + str(x.first) + "   -   " + str(
                    x.second) + "  -   " + str(x.third) + "  -  " + str(
                    x.fourth) + "\n")

        self.winner = tk.Label(text="ES Faculty Officers 2020: ", width="22", fg="#252850", bg="#FFC0CB",
                               font=("Century Gothic", "20"))
        self.winner.place(relx=0.77, rely=0.40, anchor='center')
        # Depends on the votes
        self.winnername = tk.Label(text="Winners: %s" % newList3[0] + "\n %s" % newList3[1] + "\n %s" % newList3[2] +
                                        "\n %s" % newList3[3], fg="#252850", bg="#FFC0CB",
                                   width="22", font=("Century Gothic", "20", "bold"))
        self.winnername.place(relx=0.77, rely=0.51, anchor='center')
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
        self.totalvotes = tk.Label(text="Total votes overall: %d" % t, width="18", fg="white", bg="#252850",
                                   font=("Century Gothic", "18"))
        self.totalvotes.place(relx=0.5, rely=0.80, anchor='center')
        self.voteswinner = tk.Label(text="Votes the winners received: %d" % w, width="25", fg="white", bg="#252850",
                                    font=("Century Gothic", "18"))
        self.voteswinner.place(relx=0.5, rely=0.85, anchor='center')
        if t != 0:
            p = (w * 100) / t
        else:
            p = 0
        self.percentage = tk.Label(text="Percentage of votes received by the winners: %d" % p, width="45", fg="white",
                                   bg="#252850",
                                   font=("Century Gothic", "18"))
        self.percentage.place(relx=0.5, rely=0.90, anchor='center')
        self.back = tk.Button(text='Back', font=("Gill Sans MT", "12", "bold"), height="1", width="20",
                              command=self.go_back)
        self.back.place(relx=0.5, rely=0.95, anchor="center")

    def go_back(self):
        self.list = root.place_slaves()
        for l in self.list:
            l.destroy()
        self.third_window = ResultsWindow(self.master)


class ResultsSBFacultyWindow:
    def __init__(self, master):
        self.master = master
        root.configure(background='#252850')
        self.firstlabel = tk.Label(text="GSU ELECTIONS : Results", width="50", fg="#FFC0CB", bg="#252850",
                                   font=("Century Gothic", "55", "bold"))
        self.firstlabel.place(relx=0.5, rely=0.05, anchor='center')
        self.secondlabel = tk.Label(text="School of Business Officers", width="60", fg="white", bg="#252850",
                                    font=("Century Gothic", "30", "bold", "italic", "underline"))
        self.secondlabel.place(relx=0.5, rely=0.15, anchor='center')
        self.candidatelist = Listbox(master, width=35, height=18, bg="white", fg="#252850",
                                     font=("Century Gothic", "15"))
        self.candidatelist.place(relx=0.30, rely=0.48, anchor='center')
        # self.candidatelist.insert(END, "    Candidate  :    1stP    -    2ndP    -    3rdP    -    4thP")
        self.candidatelist.insert(END, "\n  ")
        for x in faculty_results:
            if x.faculty == "SB":
                self.candidatelist.insert(END, "\n    %s " % x.full_name + ":   " + str(x.first) + "   -   " + str(
                    x.second) + "  -   " + str(x.third) + "  -  " + str(
                    x.fourth) + "\n")

        self.winner = tk.Label(text="SB Faculty Officers 2020: ", width="20", fg="#252850", bg="#FFC0CB",
                               font=("Century Gothic", "20"))
        self.winner.place(relx=0.77, rely=0.40, anchor='center')
        # Depends on the votes
        self.winnername = tk.Label(text="Winners: %s" % newList2[0] + "\n %s" % newList2[1] + "\n %s" % newList2[2] +
                                        "\n %s" % newList2[3], fg="#252850", bg="#FFC0CB",
                                   width="20", font=("Century Gothic", "20", "bold"))
        self.winnername.place(relx=0.77, rely=0.51, anchor='center')
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
        self.totalvotes = tk.Label(text="Total votes overall: %d" % t, width="18", fg="white", bg="#252850",
                                   font=("Century Gothic", "18"))
        self.totalvotes.place(relx=0.5, rely=0.80, anchor='center')
        self.voteswinner = tk.Label(text="Votes the winners received: %d" % w, width="25", fg="white", bg="#252850",
                                    font=("Century Gothic", "18"))
        self.voteswinner.place(relx=0.5, rely=0.85, anchor='center')
        if t != 0:
            p = (w * 100) / t
        else:
            p = 0
        self.percentage = tk.Label(text="Percentage of votes received by the winners: %d" % p, width="45", fg="white",
                                   bg="#252850",
                                   font=("Century Gothic", "18"))
        self.percentage.place(relx=0.5, rely=0.90, anchor='center')
        self.back = tk.Button(text='Back', font=("Gill Sans MT", "12", "bold"), height="1", width="20",
                              command=self.go_back)
        self.back.place(relx=0.5, rely=0.95, anchor="center")

    def go_back(self):
        self.list = root.place_slaves()
        for l in self.list:
            l.destroy()
        self.third_window = ResultsWindow(self.master)


class ResultsSummaryWindow:
    def __init__(self, master):
        self.master = master
        root.configure(background='#252850')
        self.firstlabel = tk.Label(text="GSU ELECTIONS : Results", width="50", fg="#FFC0CB", bg="#252850",
                                   font=("Century Gothic", "55", "bold"))
        self.firstlabel.place(relx=0.5, rely=0.05, anchor='center')
        self.secondlabel = tk.Label(text="Summary", width="60", fg="white", bg="#252850",
                                    font=("Century Gothic", "30", "bold", "italic", "underline"))
        self.secondlabel.place(relx=0.5, rely=0.15, anchor='center')
        self.presidentlbl = tk.Label(text="President", fg="#252850", bg="white", width=22,
                                     font=("Century Gothic", "23", "bold", "italic"))
        self.presidentlbl.place(relx=0.25, rely=0.24, anchor='center')
        self.presidentwinner = tk.Label(text=" %s" % newList[0], fg="#252850", bg="#FFC0CB", width=27,
                                        font=("Century Gothic", "18"))
        self.presidentwinner.place(relx=0.75, rely=0.24, anchor='center')
        self.GSUOlbl = tk.Label(text="GSU Officers", fg="#252850", bg="white", width=22,
                                font=("Century Gothic", "23", "bold", "italic"))
        self.GSUOlbl.place(relx=0.25, rely=0.33, anchor='center')
        self.GSUwinner = tk.Label(text=" %s," % newList1[0] + " %s," % newList1[1] + "\n %s" % newList1[2],
                                  fg="#252850", bg="#FFC0CB", width=27, font=("Century Gothic", "18"))
        self.GSUwinner.place(relx=0.75, rely=0.33, anchor='center')
        self.SBlbl = tk.Label(text="School of Business", fg="#252850", bg="white", width=22,
                              font=("Century Gothic", "23", "bold", "italic"))
        self.SBlbl.place(relx=0.25, rely=0.44, anchor='center')
        self.SBwinner = tk.Label(text=" %s," % newList2[0] + " %s," % newList2[1] + "\n %s," % newList2[2] +
                                      " %s" % newList2[3], fg="#252850", bg="#FFC0CB", width=27,
                                 font=("Century Gothic", "18"))
        self.SBwinner.place(relx=0.75, rely=0.44, anchor='center')
        self.ASlbl = tk.Label(text="Faculty of Liberal Arts \n and Sciences", fg="#252850", bg="white", width=22,
                              font=("Century Gothic", "23", "bold", "italic"))
        self.ASlbl.place(relx=0.25, rely=0.57, anchor='center')
        self.ASwinner = tk.Label(text=" %s," % newList5[0] + " %s," % newList5[1] + "\n %s," % newList5[2] +
                                      " %s" % newList5[3], fg="#252850", bg="#FFC0CB", width=27,
                                 font=("Century Gothic", "18"))
        self.ASwinner.place(relx=0.75, rely=0.57, anchor='center')
        self.EHlbl = tk.Label(text="Faculty of Education", fg="#252850", bg="white", width=22,
                              font=("Century Gothic", "23", "bold", "italic"))
        self.EHlbl.place(relx=0.25, rely=0.69, anchor='center')
        self.EHwinner = tk.Label(text=" %s," % newList4[0] + " %s," % newList4[1] + "\n %s," % newList4[2] +
                                      " %s" % newList4[3], fg="#252850", bg="#FFC0CB", width=27,
                                 font=("Century Gothic", "18"))
        self.EHwinner.place(relx=0.75, rely=0.69, anchor='center')
        self.ESlbl = tk.Label(text="Faculty of Engenieering \n and Science", fg="#252850", bg="white", width=22,
                              font=("Century Gothic", "23", "bold", "italic"))
        self.ESlbl.place(relx=0.25, rely=0.82, anchor='center')
        self.ESwinner = tk.Label(text=" %s," % newList3[0] + " %s," % newList3[1] + "\n %s," % newList3[2] +
                                      " %s" % newList3[3], fg="#252850", bg="#FFC0CB", width=27,
                                 font=("Century Gothic", "18"))
        self.ESwinner.place(relx=0.75, rely=0.82, anchor='center')
        self.back = tk.Button(text='Back', font=("Gill Sans MT", "12", "bold"), height="1", width="20",
                              command=self.go_back)
        self.back.place(relx=0.50, rely=0.94, anchor="center")

    def go_back(self):
        self.list = root.place_slaves()
        for l in self.list:
            l.destroy()
        self.results_window = ResultsWindow(self.master)

if __name__ == '__main__':
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()
