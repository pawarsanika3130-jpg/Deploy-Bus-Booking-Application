from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)

db = pymysql.connect(
    host="YOUR-RDS-ENDPOINT",
    user="admin",
    password="YOUR_PASSWORD"
)

cursor = db.cursor()

cursor.execute("""
CREATE DATABASE IF NOT EXISTS busbooking
""")

cursor.execute("USE busbooking")

cursor.execute("""
CREATE TABLE IF NOT EXISTS bookings(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    source_city VARCHAR(100),
    destination_city VARCHAR(100),
    travel_date DATE,
    seat_number VARCHAR(20)
)
""")

db.commit()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/book')
def book():
    return render_template('book.html')

@app.route('/submit', methods=['POST'])
def submit():

    name = request.form['name']
    email = request.form['email']
    source = request.form['source']
    destination = request.form['destination']
    travel_date = request.form['travel_date']
    seat = request.form['seat']

    cursor = db.cursor()

    sql = """
    INSERT INTO bookings
    (name,email,source_city,destination_city,travel_date,seat_number)
    VALUES(%s,%s,%s,%s,%s,%s)
    """

    cursor.execute(
        sql,
        (name,email,source,destination,travel_date,seat)
    )

    db.commit()

    return render_template(
        'success.html',
        name=name,
        source=source,
        destination=destination
    )

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000
    )
