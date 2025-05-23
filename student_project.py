"""
Lists
Student Project
Project Title:
"""


#hospital database- who has the same DOB, name(first of last)  

#imports
import csv

# File to store patient data
CSV_FILE = "hospital_database.csv"


#start asking questions to user
print("Welcome to the Hospital Database")
first_name = input("Enter your first name: ").lower()
last_name = input("Enter your last name: ").lower()
dob = input("Enter your date of birth (YYYY-MM-DD): ").lower()



#list of matches
f_match = []
l_match = []
d_match = []

#open the file and its append(adding you info)
with open(CSV_FILE, "a") as file:
    writer = csv.writer(file)
    writer.writerow([first_name, last_name, dob])


#Telling user the its currently checking the file
print("Checking for matches in the hospital database...")

#open the file again but as a reader, so reading it (checking)
with open(CSV_FILE, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if row[0] == first_name:
                    f_match.append(row[0])

            if row[1] == last_name:
                    l_match.append(row[0])
                        
            if row[2] == dob:
                    d_match.append(row[0])

       


#telling user who has the same first, last name or dob
if len(f_match) > 1:
    print("There are other patients with the first name " + first_name +":")

if len(l_match) > 1:
    print("There are other patients with the last name " + last_name + ":")

if len(d_match) > 1:
    print("There are other patients born on " + dob + ":")

#leting the user know that thier info has been added
print("Your information has been added to the database.")