import sqlite3
from Classes import Student, Candidate

# Setting up sqlite3 - using ':memory:' instead of a database means you can run the code as many times as you want
# without receiving any errors. Once all code has been completed, a database can then be created to save all data

conn = sqlite3.connect("VotingDatabase.db")
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS Student ( 
                Forename TEXT NOT NULL, Surname TEXT NOT NULL, StudentUsername PRIMARY KEY NOT NULL,
                Password TEXT NOT NULL, Faculty TEXT NOT NULL, Gender TEXT NOT NULL, YearGroup INTEGER NOT NULL
                )""")
c.execute("""CREATE TABLE IF NOT EXISTS Candidate (
                Forename TEXT NOT NULL, Surname TEXT NOT NULL, Position TEXT NOT NULL, Faculty TEXT NOT NULL,
                CandidateUsername TEXT PRIMARY KEY NOT NULL, Gender INTEGER NOT NULL, YearGroup INTEGER NOT NULL)""")
c.execute("""CREATE TABLE IF NOT EXISTS PresidentVotes (
                id INTEGER PRIMARY KEY, StudentUsername TEXT NOT NULL, FirstPreference TEXT NOT NULL,
                SecondPreference TEXT, ThirdPreference TEXT, FourthPreference TEXT
                )""")
c.execute("""CREATE TABLE IF NOT EXISTS FacultyOfficerVotes (
                id INTEGER PRIMARY KEY, Faculty TEXT NOT NULL, StudentUsername TEXT NOT NULL,
                FirstPreference TEXT NOT NULL, SecondPreference TEXT, ThirdPreference TEXT, FourthPreference TEXT
                )""")
c.execute("""CREATE TABLE IF NOT EXISTS GSUOfficerVotes (
                id INTEGER PRIMARY KEY, StudentUsername TEXT, FirstPreference TEXT NOT NULL, SecondPreference TEXT,
                ThirdPreference TEXT, FourthPreference TEXT
                )""")
c.execute("""CREATE TABLE IF NOT EXISTS Results (
                CandidateName TEXT, Position TEXT, FirstPreference INTEGER, SecondPreference INTEGER,
                ThirdPreference INTEGER, FourthPreference INTEGER
                )""")

# Adding 20 Students to Student Table

# First five students are unable to vote as examples
c.execute("""INSERT OR IGNORE INTO Student VALUES('Dante','Christian', 'dc3045g', 'ChristDante', 'EH', 'M', 2)""")
c.execute("""INSERT OR IGNORE INTO Student VALUES('Milly','Rose', 'mr2945g', 'HelloWorld', 'EH', 'F', 1)""")
# Below students all have voting rights set by function in NamesLists.py
c.execute("""INSERT OR IGNORE INTO Student VALUES('Chloe','Miles', 'cm4935a', '99Chloe99', 'EH', 'F', 3)""")
c.execute("""INSERT OR IGNORE INTO Student VALUES('Ronny','Diaz', 'rd2034h', 'RonnyPass', 'EH', 'M', 1)""")
c.execute("""INSERT OR IGNORE INTO Student VALUES('Tre','Hawes', 'th2034w', 'TreHawes98', 'EH', 'M', 1)""")
c.execute("""INSERT OR IGNORE INTO Student VALUES('Gabriele','Qazolli', 'a', 'a', 'SB', 'M', 2)""")
c.execute("""INSERT OR IGNORE INTO Student VALUES('Maddie','Barnett', 'mb3520e', 'PasswordBarnett', 'SB', 'F', 2)""")
c.execute("""INSERT OR IGNORE INTO Student VALUES('Hannah','Quintero', 'hq3984e', '123Password', 'SB', 'F', 1)""")#not voted yet
c.execute("""INSERT OR IGNORE INTO Student VALUES('Naya','Ayala', 'na3084e', 'NayaAyala', 'SB', 'F', 3)""")
c.execute("""INSERT OR IGNORE INTO Student VALUES('Melinda','Mcneil', 'mm4927s', 'Melinda2000', 'SB', 'F', 2)""")
c.execute("""INSERT OR IGNORE INTO Student VALUES('Rebecca','Shaw', 'rs4927g', 'BeckyShaw', 'ES', 'F', 1)""")
c.execute("""INSERT OR IGNORE INTO Student VALUES('Anya','Elsom', 'ae4028y', 'ElsomAnya', 'ES', 'F', 2)""")
c.execute("""INSERT OR IGNORE INTO Student VALUES('Zain','Gillespie', 'zg4973d', 'GreenwichPass', 'ES', 'M', 3)""")
c.execute("""INSERT OR IGNORE INTO Student VALUES('Adnan','Allirakiah', 'aa9038y', 'AdnanAdnan', 'ES', 'M', 1)""")#not voted yet
c.execute("""INSERT OR IGNORE INTO Student VALUES('Connor','Ryan', 'cr3928t', 'ConnorPass', 'ES', 'M', 2)""")
c.execute("""INSERT OR IGNORE INTO Student VALUES('Fabrizio','Valentine', 'fv5938e', 'FabVal', 'AS', 'M', 3)""")
c.execute("""INSERT OR IGNORE INTO Student VALUES('Jevon','Corrighan', 'jc8495r', 'PasswordPassword', 'AS', 'M', 1)""")
c.execute("""INSERT OR IGNORE INTO Student VALUES('Brandon','Stein', 'bs0382t', 'SteinBrandon', 'AS', 'M', 2)""")
c.execute("""INSERT OR IGNORE INTO Student VALUES('Adrian','Stephens', 'as7513f', 'StephenAdrians', 'AS', 'M', 3)""")#not voted yet
c.execute("""INSERT OR IGNORE INTO Student VALUES('Rosie','Merritt', 'rm9841r', 'GSUPassword98', 'AS', 'F', 2)""")

# Adding 4 Presidents & 12 GSU Officers to Candidate Table

c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Angela', 'Schneider', 'GSU Officer', 'EH', 'as2019g', 'F', 1)""")
c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Craig', 'Gibson', 'GSU Officer', 'EH', 'cg2039g', 'F', 2)""")
c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Sade', 'Guy', 'GSU Officer', 'SB', 'sg8452s', 'F', 3)""")
c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Athena', 'Clay', 'GSU Officer', 'EH', 'ac9539e', 'F', 1)""")
c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Audrey', 'Cortez', 'GSU Officer', 'EH', 'ac9454f', 'F', 1)""")
c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Jon', 'Hook', 'GSU Officer', 'ES', 'jh1354h', 'M', 1)""")
c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Ryan', 'Oneil', 'GSU Officer', 'SB', 'ro3164f', 'M', 2)""")
c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Ethan', 'Roberts', 'GSU Officer', 'SB', 'er4657h', 'M', 2)""")
c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Ross', 'Hodge', 'GSU Officer', 'EH', 'rh7351n', 'M', 2)""")
c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Jasmine', 'Hancock', 'GSU Officer', 'ES', 'jh7651d', 'F', 3)""")
c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Samuel', 'Abotts', 'GSU Officer', 'AS', 'sa3546r', 'M', 3)""")
c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Aimee', 'Sahara', 'GSU Officer', 'SB', 'as8254l', 'M', 3)""")

c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Indi', 'Franklin', 'President', 'SB', 'if6568e', 'F', 2)""")
c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Andrei', 'Keely', 'President', 'SB', 'ak3574p', 'M', 2)""")
c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Esther', 'Barracks', 'President', 'ES', 'eb6543w', 'F', 3)""")
c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Ryan', 'Hays', 'President','EH', 'rh1656m', 'M', 3)""")

# Adding 64 Faculty Officers into Candidate Table

c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Anthony', 'Nunez', 'Faculty Officer','EH', 'an6543s', 'M', 3)""")
c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Kirby', 'Hicks', 'Faculty Officer','EH', 'kh7865g', 'F', 2)""")
c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Greyson', 'John', 'Faculty Officer','EH', 'gj6587l', 'M', 2)""")
c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Grady', 'Graham', 'Faculty Officer','EH', 'gg3284h', 'M', 1)""")
c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Imran', 'Needham', 'Faculty Officer','EH', 'in6413h', 'M', 1)""")
c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Andy', 'Collins', 'Faculty Officer','EH', 'ac6563b', 'M', 2)""")
c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Tye', 'Austin', 'Faculty Officer','EH', 'ta6354i', 'M', 2)""")
c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Shayna', 'Matthews', 'Faculty Officer','EH', 'sm6543t', 'F', 2)""")
c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Sofia', 'Gould', 'Faculty Officer','EH', 'sg3542y', 'F', 3)""")
c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Gianni', 'Foreman', 'Faculty Officer','EH', 'gf6515e', 'F', 3)""")
c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Nadia', 'Ratcliffe', 'Faculty Officer','EH', 'nr5416g', 'F', 3)""")
c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Kester', 'Spooner', 'Faculty Officer','EH', 'ks9374k', 'F', 2)""")
c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Louisa', 'Ray', 'Faculty Officer','EH', 'lr5318g', 'F', 1)""")
c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Daisy', 'Oneil','Faculty Officer','EH', 'do6536d', 'F', 3)""")
c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Ayra', 'Davis', 'Faculty Officer','EH', 'ad4831h', 'F', 2)""")
c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Ashlyn', 'Ronald', 'Faculty Officer','EH', 'ar1365t', 'F', 1)""")

c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Xavier', 'Alonso', 'Faculty Officer','ES', 'xa6535d', 'M', 1)""")
c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Jorge', 'Sinclair', 'Faculty Officer','ES', 'js7531f', 'M', 1)""")
c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Sammy', 'Rush', 'Faculty Officer','ES', 'sr2054f', 'M', 1)""")
c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Alfred', 'Soto', 'Faculty Officer','ES', 'as8752t', 'M', 1)""")
c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Giovanni', 'Santos', 'Faculty Officer','ES', 'gs6543d', 'M', 1)""")
c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Artur', 'Ramos', 'Faculty Officer','ES', 'ar7802e', 'M', 2)""")
c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Denzel', 'Curry', 'Faculty Officer','ES', 'dc2575d', 'M', 2)""")
c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Henry', 'Weber', 'Faculty Officer','ES', 'hw2067f', 'M', 2)""")
c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Ameer', 'Khan', 'Faculty Officer','ES', 'ak6086s', 'M', 2)""")
c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Dale', 'Escobar', 'Faculty Officer','ES', 'de5056e', 'M', 1)""")
c.execute("""INSERT OR IGNORE INTO Candidate VALUES('April', 'Higgs', 'Faculty Officer','ES', 'ah5076f', 'F', 3)""")
c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Gina', 'Nixon', 'Faculty Officer','ES', 'gn7055e', 'F', 2)""")
c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Taiba', 'Weiss', 'Faculty Officer','ES', 'tw6075w', 'F', 1)""")
c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Tess', 'Lu', 'Faculty Officer','ES', 'tl8067l', 'F', 3)""")
c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Naima', 'Mansell', 'Faculty Officer','ES', 'nm6079s', 'F', 2)""")
c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Ellie', 'Irving', 'Faculty Officer','ES', 'ei3048d', 'F', 1)""")

c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Lacey', 'May', 'Faculty Officer','SB', 'lm6078h', 'F', 1)""")
c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Asma', 'Lindsey', 'Faculty Officer','SB', 'al7030v', 'F', 2)""")
c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Tulisa', 'Halliday', 'Faculty Officer','SB', 'th7305e', 'F', 3)""")
c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Helena', 'Martinez', 'Faculty Officer','SB', 'hm7068s', 'F', 1)""")
c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Eshaan', 'Imad', 'Faculty Officer','SB', 'ei7065d', 'F', 2)""")
c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Daisy', 'Sampson', 'Faculty Officer','SB', 'ds6078c', 'F', 3)""")
c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Anita', 'Johnson', 'Faculty Officer','SB', 'aj3074d', 'F', 1)""")
c.execute("""INSERT OR IGNORE INTO Candidate VALUES('William', 'Stokes', 'Faculty Officer','SB', 'ws3054n', 'M', 1)""")
c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Brandon', 'Lee', 'Faculty Officer','SB', 'bl1025z', 'M', 1)""")
c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Chay', 'Cope', 'Faculty Officer','SB', 'cc2039y', 'M', 2)""")
c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Robert', 'Parlour', 'Faculty Officer','SB', 'rp3054f', 'M', 2)""")
c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Pearce', 'Floyd', 'Faculty Officer','SB', 'pf1028r', 'M', 2)""")
c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Henry', 'Potter', 'Faculty Officer','SB', 'hp3079x', 'M', 2)""")
c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Tyriq', 'Kinney', 'Faculty Officer','SB', 'tk3065k', 'M', 2)""")
c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Harry', 'Hibbert', 'Faculty Officer','SB', 'hh4056e', 'M', 1)""")
c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Trey', 'Villarreal', 'Faculty Officer','SB', 'tv7506a', 'M', 1)""")

c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Nasir', 'Castro', 'Faculty Officer','AS', 'nc6049e', 'M', 3)""")
c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Tyson', 'Baxter', 'Faculty Officer','AS', 'tb4960h', 'M', 2)""")
c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Cameron', 'Currant', 'Faculty Officer','AS', 'cc6466f', 'M', 1)""")
c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Waseem', 'Ahmed', 'Faculty Officer','AS', 'wa6099s', 'M', 3)""")
c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Clarke', 'Smith', 'Faculty Officer','AS', 'cs3719c', 'M', 3)""")
c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Loretta', 'Barnett', 'Faculty Officer','AS', 'lb6080g', 'F', 2)""")
c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Ingrid', 'Allen', 'Faculty Officer','AS', 'ia6905t', 'F', 2)""")
c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Stacey', 'Hops', 'Faculty Officer','AS', 'sh4593d', 'F', 2)""")
c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Kiana', 'Reeves', 'Faculty Officer','AS', 'kr3756s', 'F', 2)""")
c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Luna', 'Barclay', 'Faculty Officer','AS', 'lb6548v', 'F', 1)""")
c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Gabriele', 'Lucero', 'Faculty Officer','AS', 'gl6054n', 'F', 1)""")
c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Aisling', 'Spencer', 'Faculty Officer','AS', 'as3545b', 'F', 1)""")
c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Lilly', 'Cocks', 'Faculty Officer','AS', 'lc6846f', 'F', 1)""")
c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Yasmine', 'Pena', 'Faculty Officer','AS', 'yp6547b', 'F', 1)""")
c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Catherine', 'Singleton', 'Faculty Officer','AS', 'cs3928v',
                                                    'F', 1)""")
c.execute("""INSERT OR IGNORE INTO Candidate VALUES('Lincoln', 'Thompson', 'Faculty Officer','AS', 'lt60795n',
                                                    'M', 3)""")

# NOTE AGAIN - the above database will not be saved unless you create a db when connecting.

conn.commit()

# Creating objects from SQL Student and Candidate table

students = []
candidates = []

c.execute("SELECT * FROM Student")
for column in c:
    students.append(Student(forename=column[0], surname=column[1], username=column[2], password=column[3],
                            faculty=column[4], gender=column[5], year_group=column[6]))

c.execute("SELECT * FROM Candidate")
for column in c:
    candidates.append(Candidate(forename=column[0], surname=column[1], position=column[2], faculty=column[5],
                                username=column[4], gender=column[3], year_group=column[6]))


conn.close()
