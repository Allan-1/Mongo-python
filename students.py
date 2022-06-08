import pymongo

myclient = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
mydb = myclient['students']
mycol = mydb['studentdetails']


def addStudents():
    regno = input('Enter students registration number: ')
    fname = input('Enter students firstname: ')
    lname = input('Enter students lastname: ')
    course = input('Enter students course: ')
    marks = input('Enter students average marks: ')

    details = {
        'regno': regno,
        'fname': fname,
        'lname': lname,
        'course': course,
        'marks': marks
    }
    mycol.insert_one(details)
    print('Student record succesfully recorded')


def viewStudent():
    for students in mycol.find({}, {'_id': 0}):
        print(students)


def deleteStudent():
    regno = input('Enter students regno: ')
    query = {'regno': regno}
    if(mycol.find_one(query)):
        mycol.delete_one(query)
        print('Student record succesfully deleted')
    else:
        print('Student record not found')


def display():
    choices = '''
    A - Add student record
    D - Delete Student Record
    V - View all records
    Q - Quit
    '''

    print(choices)

    selection = input('Enter you choice: ')

    if(selection == 'A'):
        addStudents()
    elif(selection == 'V'):
        viewStudent()
    elif(selection == 'D'):
        deleteStudent()
    elif(selection == 'Q'):
        quit()
    else:
        print('Invalid choice')


display()
