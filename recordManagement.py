import csv
import os
from datetime import datetime, date

def view_records(file_name):
    try:
        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print(f"The file {file_name} does not exist.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# view_records('Attendance_Data/2023-10-18.csv')   // Testing will continue later 

def list_records(directory):
    try:
        # Check if the directory exists
        if not os.path.exists(directory):
            print("The directory does not exist.")
            return
        # Check if the path is a directory
        if not os.path.isdir(directory):
            print("This is not a directory.")
            return
        # List all files in the directory
        files = os.listdir(directory)
        for file in files:
            print(file)
    except Exception as e:
        print("An error occurred: ", e)

# list_files("Attendance_Data")    /// Testing Will continue later 

def add_records(name):
    file = 'Attendance_Data/'+str(date.today())+'.csv'
    with open(file, 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString}')
