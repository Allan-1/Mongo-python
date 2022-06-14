def addStudent():
    regno = input('Enter students registration number: ')
    fname = input('Enter students firstname: ')
    lname = input('Enter students lastname: ')
    course = input('Enter students course: ')
    marks = input('Enter students average marks: ')

    record = "%s %s %s %s %s \n" % (regno, fname, lname, course, marks)

    with open('records.txt', 'a') as f:
        f.writelines(record)
        f.close()
    print('Record addded succesfully')


def deleteStudent():
    regno = input('Enter students registration number: ')
    with open('records.txt') as f:
        lines = f.readlines()
        for ind, line in enumerate(lines):
            l = line.split()
            if l[0] == regno:
                lines[ind] = ""
        with open('records.txt', "w") as f:
            f.writelines(lines)
            print('record succesfully deleted')


def viewStudent():
    with open('records.txt', 'r') as f:
        print(f.read())
        f.close()


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
        addStudent()
    elif(selection == 'V'):
        viewStudent()
    elif(selection == 'D'):
        deleteStudent()
    elif(selection == 'Q'):
        quit()
    else:
        print('Invalid choice')


display()
