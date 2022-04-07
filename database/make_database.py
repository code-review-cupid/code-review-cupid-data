# This file exists to create the SQLite database as used by the Code-Review-Cupid project

import sqlite3

conn = sqlite3.connect('CRC_user_database')
c = conn.cursor()

# Create database with list values of given types
c.execute('''
          CREATE TABLE IF NOT EXISTS user_data
          ([user_id] INTEGER PRIMARY KEY, [user_name] TEXT,
           [user_email] TEXT, [user_skills_per] TEXT, 
           [user_skills_req] TEXT, [user_score] REAL)
          ''')

# Save changes
conn.commit()

# Close connection to database
conn.close()