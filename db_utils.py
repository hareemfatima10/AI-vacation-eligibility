import sqlite3

def get_employee_record(id):
    conn = sqlite3.connect('vacation_system_db.sqlite')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM employees WHERE id = ? LIMIT 1
    ''', (id,))

    record = cursor.fetchone()
    conn.close()
    formatted_record = format_employee_record(record)

    return formatted_record

def format_employee_record(record):
    if record:
        formatted_record = (
            f"id: {record[0]}\n"
            f"first name: {record[1]}\n"
            f"last name: {record[2]}\n"
            f"join_date: {record[3]}\n"
            f"probation_end_date: {record[4]}\n"
            f"probation_status: {record[5]}\n"
            f"remaining_vacation_days: {record[6]}\n"
            f"department_id: {record[7]}\n"
        )
        return formatted_record
    else:
        return "No record found."
    
