# import MySQLdb

# try:
#    connection = MySQLdb.connect(
#        host="mysql-2f37c2e-ukonud4-0673.g.aivencloud.com",
#        user="scoutuser",
#        passwd="AVNS_3xhPG5SiQKSxSMRgkXn",
#        db="football_scouting_db",
#        port=11292
#    )
#    print("Connection successful")
#    connection.close()
# except MySQLdb.OperationalError as e:
#    print(f"Connection failed: {e}")

import pymysql
# import ssl

timeout = 10
# ssl_context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
connection = pymysql.connect(
    charset="utf8mb4",
    connect_timeout=timeout,
    cursorclass=pymysql.cursors.DictCursor,
    db="defaultdb",     # "football_scouting_db"
    host="mysql-2f37c2e-ukonud4-0673.g.aivencloud.com",   # "mysql-2f37c2e-ukonud4-0673.g.aivencloud.com"
    password="AVNS_kTxJV9BPoDRoUmNlMcW",   #"AVNS_3xhPG5SiQKSxSMRgkXn"
    # read_timeout=timeout,
    port=11292,
    user="avnadmin",     #"scoutuser"
    # write_timeout=timeout,
    # ssl=ssl_context,
)

try:
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS mytest (id INTEGER PRIMARY KEY)")
    cursor.execute("INSERT INTO mytest (id) VALUES (1), (2)")
    cursor.execute("SELECT * FROM mytest")
    print(cursor.fetchall())
finally:
    connection.close()

