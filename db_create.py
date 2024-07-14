import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('vacation_system_db.sqlite')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS departments (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        description TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        join_date TEXT NOT NULL,
        probation_end_date TEXT NOT NULL,
        probation_status BOOLEAN NOT NULL DEFAULT 1, -- 1 for probation, 0 for not in probation
        remaining_paid_vacation_days INTEGER NOT NULL,
        department_id INTEGER NOT NULL,
        FOREIGN KEY (department_id) REFERENCES departments(id)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS vacation_requests (
        id INTEGER PRIMARY KEY,
        employee_id INTEGER NOT NULL,
        start_date TEXT NOT NULL,
        end_date TEXT NOT NULL,
        status TEXT NOT NULL
    )
''')

cursor.execute('''
    INSERT INTO employees (id, first_name, last_name, join_date, probation_end_date, probation_status, remaining_paid_vacation_days, department_id)
    VALUES
        (1, 'John', 'Doe', '2023-01-01', '2023-04-01', 0, 15, 1),
        (2, 'Jane', 'Smith', '2022-02-15', '2022-05-15', 0, 20, 1),
        (3, 'Alice', 'Smith', '2024-06-20', '2024-10-20', 1, 30, 2)
''')

cursor.execute('''
    INSERT INTO departments (id, name, description) VALUES 
    (1,'Engineering', 'Handles product development and maintenance'),
    (2, 'Marketing', 'Focuses on market research and promotion'),
    (3, 'Human Resources', 'Manages employee relations and administrative tasks')
''')

conn.commit()
conn.close()