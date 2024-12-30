from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

# الاتصال بقاعدة البيانات
def get_db_connection():
    conn = sqlite3.connect('restaurant_reservations.db')
    conn.row_factory = sqlite3.Row
    return conn

# الصفحة الرئيسية التي تعرض نموذج الحجز
@app.route('/')
def index():
    return render_template('index.html')

# التعامل مع طلبات الحجز
@app.route('/reserve', methods=['POST'])
def reserve_table():
    table_number = request.form['table_number']
    reservation_date = request.form['reservation_date']
    customer_name = request.form['customer_name']
    customer_contact = request.form['customer_contact']
    
    conn = get_db_connection()
    conn.execute('INSERT INTO reservations (table_number, reservation_date, customer_name, customer_contact) VALUES (?, ?, ?, ?)',
                 (table_number, reservation_date, customer_name, customer_contact))
    conn.commit()
    conn.close()
    
    return 'تم الحجز بنجاح!'

if __name__ == '__main__':
    app.run(debug=True)
