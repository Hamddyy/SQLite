from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

# Database path
DATABASE = "reservations.db"

def connect_db():
    return sqlite3.connect(DATABASE)

# Route to render the HTML page
@app.route('/')
def home():
    return render_template('index.html')

# API to handle form submission
@app.route('/add_reservation', methods=['POST'])
def add_reservation():
    try:
        table_number = request.form['table_number']
        reservation_date = request.form['reservation_date']
        customer_name = request.form['customer_name']
        customer_contact = request.form['customer_contact']

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO reservations (table_number, reservation_date, customer_name, customer_contact)
            VALUES (?, ?, ?, ?);
        """, (table_number, reservation_date, customer_name, customer_contact))
        conn.commit()
        conn.close()

        return jsonify({'message': 'Reservation added successfully!'})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
