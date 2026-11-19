from django.shortcuts import render

def insert(request):
    import sqlite3
    db=r"C:\Users\acer\Desktop\Projects\P2_crud\db.sqlite3"
    db=sqlite3.connect(db)
    cursor=db.cursor()
    s1="""CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_name TEXT NOT NULL,
    dob DATE NOT NULL,
    email TEXT NOT NULL,
    roll_number TEXT NOT NULL UNIQUE
);"""
    cursor.execute(s1)
    student_name = request.POST.get('student_name')
    date_of_birth = request.POST.get('date_of_birth')
    email = request.POST.get('email')
    roll_number = request.POST.get('roll_number')
    # Here you can add code to save the data to the database or perform any other actions
    print(f"Student Name: {student_name}, Date of Birth: {date_of_birth}, Email: {email}, Roll Number: {roll_number}")
    s2=f"""
    INSERT INTO students (student_name, dob, email, roll_number)
VALUES ('{student_name}', '{date_of_birth}', '{email}', '{roll_number}');
    """
    cursor.execute(s2)
    db.commit()
    db.close()


def select(rollno):
    import sqlite3
    db=r"C:\Users\acer\Desktop\Projects\P2_crud\db.sqlite3"
    db=sqlite3.connect(db)
    cursor=db.cursor()
    s1=f"SELECT * FROM students WHERE roll_number='{rollno}'"
    cursor.execute(s1)
    data=cursor.fetchall()
    db.close()
    return data

def create(request):
    if request.method == 'POST':
        insert(request)
        return render(request, 'status.html', {'message': 'DB updated successfully!'})
    return render(request, 'create.html')

def pick(request):
    if request.method == 'GET':
        return render(request, 'pick.html')
    elif request.method == 'POST':
        data = select(request.POST.get('roll_number'))
        name = data[0][1]
        dob = data[0][2]
        email = data[0][3]
        roll_no = data[0][4]
        return render(request, 'display_student.html', {'name': name, 'dob': dob, 'email': email, 'roll_number': roll_no})
def edit_name(request):
    if request.method == 'GET':
        # form to pick the target student..
        return render(request, 'edit_name.html')
    elif request.method == 'POST':
        # Next for to edit..
        roll_number = request.POST.get('roll_number')
        name = select(roll_number)[0][1]
        return render(request, 'name_change.html', context={'roll_number': roll_number, 'name': name})

def update_name(request):
    if request.method == 'POST':
        import sqlite3
        db=r"C:\Users\acer\Desktop\Projects\P2_crud\db.sqlite3"
        db=sqlite3.connect(db)
        cursor=db.cursor()
        new_name = request.POST.get('new_name')
        roll_number = request.POST.get('roll_number')
        s1=f"UPDATE students SET student_name='{new_name}' WHERE roll_number='{roll_number}'"
        cursor.execute(s1)
        db.commit()
        db.close()
    return render(request, 'status.html', {'message': 'Name updated in DB successfully!'})

