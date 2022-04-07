# This file handles the addinf of synthetic data into the SQLite database as used by the Code-Review-Cupid project

from nbformat import write
import numpy as np
import pandas as pd
import sqlite3
from make_database import *

RAW_DATA = 'codereviewcupid-mockdata.csv'

def write_data():
    # Read CSV data
    df = pd.read_csv(RAW_DATA)
    # Open connection to db
    make_database()
    conn = get_database()
    c = conn.cursor()
    # Iterate through CSV by row
    for row in df.to_dict(orient='records'):
        exec_string = """
                INSERT INTO user_data (user_id, user_name, user_email,
                user_skills_per, user_skills_req, user_score)

                        VALUES
                        (?, ?, ?, ?, ?, ?)
    """

        c.execute(exec_string, tuple(row.values()))
        conn.commit()
    conn.close()

if __name__ =='__main__':
    write_data()
