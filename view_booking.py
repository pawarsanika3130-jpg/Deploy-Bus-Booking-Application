import pymysql

conn = pymysql.connect(
    host="busbookingdb.cr66kg6as3ba.ap-south-1.rds.amazonaws.com",
    user="admin",
    password="sanika123",
    database="busbooking"
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM bookings")

rows = cursor.fetchall()

print("\n=== BUS BOOKINGS ===\n")

for row in rows:
    print(row)

conn.close()
