import sqlite3


class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS students(
            studentid Integer Primary Key,
            name text,
            surname text,
            email text,
            gender text,
            contact text,
            campus text,
            degree text
        )
        """
        self.cur.execute(sql)
        self.con.commit()

    # Insert Function
    def insert(self, name, surname, email, gender, contact, campus, degree):
        self.cur.execute("insert into students values (NULL,?,?,?,?,?,?,?)",
                         (name, surname, email, gender, contact, campus, degree))
        self.con.commit()

    # Fetch All Data from DB
    def fetch(self):
        self.cur.execute("SELECT * from students")
        rows = self.cur.fetchall()
        # print(rows)
        return rows

    # Delete a Record in DB
    def remove(self, studentid):
        self.cur.execute("delete from students where studentid=?", (studentid,))
        self.con.commit()

    # Update a Record in DB
    def update(self, studentid, name, surname, email, gender, contact, campus, degree):
        self.cur.execute(
            "update students set name=?, surname=?, email=?, gender=?, contact=?, campus=?, degree=? where studentid=?",
            (name, surname, email, gender, contact, campus, degree, studentid))
        self.con.commit()

    # Display student records in association with campus in DB
    def get_students(self, campus):
        self.cur.execute(
            "SELECT * FROM students WHERE campus=?", (campus,))
        rows = self.cur.fetchall()
        # print(rows)
        return rows