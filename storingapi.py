import sqlite3
import json
import os


def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn

def create_tastedive_table(cur, conn):
    cur.execute("DROP TABLE IF EXISTS tastedive")
    cur.execute("CREATE TABLE tastedive (artist_id INTEGER PRIMARY KEY, similar_artist_id INTEGER, media_type TEXT)")
    conn.commit()

def create_artists_table(cur, conn):
    cur.execute("DROP TABLE IF EXISTS artists")
    cur.execute("CREATE TABLE artists (artist_id INTEGER PRIMARY KEY, name TEXT, age INTEGER, net_worth INTEGER)")
    conn.commit()

def create_spotify_table(cur, conn):
    cur.execute("DROP TABLE IF EXISTS spotify")
    cur.execute("CREATE TABLE spotify (artist_id INTEGER PRIMARY KEY, popularity INTEGER, genre_id INTEGER)")
    conn.commit()

def create_genre_table(cur, conn):
    cur.execute("DROP TABLE IF EXISTS genre")
    cur.execute("CREATE TABLE genre (genre_id INTEGER PRIMARY KEY, genre_name TEXT)")
    conn.commit()






'''
def create_employee_table(cur, conn):
    cur.execute("DROP TABLE IF EXISTS Employees")
    cur.execute("CREATE TABLE Employees (employee_id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, hire_date TEXT,job_id INTEGER, salary INTEGER)")
    conn.commit()

# ADD EMPLOYEE'S INFORMTION TO THE TABLE

def add_employee(filename, cur, conn):
    #load .json file and read job data
    # WE GAVE YOU THIS TO READ IN DATA
    f = open(os.path.abspath(os.path.join(os.path.dirname(__file__), filename)))
    file_data = f.read()
    f.close()
    # THE REST IS UP TO YOU
    json_data = json.loads(file_data)
    for item in json_data:
        emp_id = int(item['employee_id'])
        first = item['first_name']
        last = item['last_name']
        hire = item['hire_date']
        job_id = int(item['job_id'])
        salary = int(item['salary'])
        cur.execute("INSERT OR IGNORE INTO Employees (employee_id, first_name, last_name, hire_date, job_id, salary) VALUES(?,?,?,?,?,?)", (emp_id, first, last, hire, job_id, salary))
    conn.commit()

# TASK 2: GET JOB AND HIRE_DATE INFORMATION
def job_and_hire_date(cur, conn):
    pass

# TASK 3: IDENTIFY PROBLEMATIC SALARY DATA
# Apply JOIN clause to match individual employees
def problematic_salary(cur, conn):
    pass

# TASK 4: VISUALIZATION
def visualization_salary_data(cur, conn):
    cur.execute("SELECT Employees.salary, Jobs.job_title FROM Employees JOIN Jobs on Employees.job_id = Jobs.job_id")
    salary_job_list = cur.fetchall()
    job_list = []
    salary_list = []
    for item in salary_job_list:
        job_list.append(item[1])
        salary_list.append(item[0])

    plt.figure()
    plt.scatter(x = job_list, y = salary_list)

    cur.execute("SELECT min_salary, max_salary, job_title FROM Jobs")
    
    plt.xticks(rotation = 45)
    plt.tight_layout()
    plt.show()
'''

def main():
    cur, conn = setUpDatabase("junkies.db")
    create_tastedive_table(cur, conn)
    create_artists_table(cur, conn)
    create_spotify_table(cur, conn)
    create_genre_table(cur, conn)

if __name__ == "__main__":
    main()
