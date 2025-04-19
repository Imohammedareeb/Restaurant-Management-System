from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'savory_bistro'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'  # This makes results return as dictionaries

mysql = MySQL(app)

@app.route('/')
def home():
    cur = mysql.connection.cursor()
    
    # Get today's specials
    cur.execute("SELECT * FROM menu_items WHERE is_special = 1")
    specials = cur.fetchall()
    
    # Get menu categories and items
    cur.execute("SELECT DISTINCT category FROM menu_items")
    categories = [row['category'] for row in cur.fetchall()]
    
    menu_items_by_category = {}
    for category in categories:
        cur.execute("SELECT name, price FROM menu_items WHERE category = %s LIMIT 2", (category,))
        menu_items_by_category[category] = cur.fetchall()
    
    cur.close()
    
    return render_template('index.html', 
                         specials=specials,
                         menu_categories=categories,
                         menu_items=menu_items_by_category)


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/menu')
def menu():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM menu_items")
    menu_items = cur.fetchall()
    cur.close()
    return render_template('menu.html', menu_items=menu_items)

@app.route('/reservations', methods=['GET', 'POST'])
def reservations():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        date = request.form['date']
        time = request.form['time']
        guests = request.form['guests']
        requests = request.form.get('requests', '')
        
        try:
            cur = mysql.connection.cursor()
            cur.execute("""
                INSERT INTO reservations 
                (name, email, phone, date, time, guests, special_requests) 
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (name, email, phone, date, time, guests, requests))
            mysql.connection.commit()
            cur.close()
            
            flash('Your reservation has been successfully submitted!', 'success')
            return redirect(url_for('reservations'))
        except Exception as e:
            flash('There was an error processing your reservation. Please try again.', 'error')
            return redirect(url_for('reservations'))
    
    return render_template('reservations.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)