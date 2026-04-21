from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date as date_obj
import os
import re

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# SQLite Configuration for Vercel (using /tmp for write access)
if os.environ.get('VERCEL'):
    db_path = '/tmp/savory_bistro.db'
else:
    basedir = os.path.abspath(os.path.dirname(__file__))
    db_path = os.path.join(basedir, 'savory_bistro.db')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Models
class Reservation(db.Model):
    __tablename__ = 'reservations'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    date = db.Column(db.String(20), nullable=False)
    time = db.Column(db.String(20), nullable=False)
    guests = db.Column(db.Integer, nullable=False)
    special_requests = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class MenuItem(db.Model):
    __tablename__ = 'menu_items'
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    is_special = db.Column(db.Boolean, default=False)

    def to_dict(self):
        return {
            'id': self.id,
            'category': self.category,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'is_special': self.is_special
        }

@app.route('/')
def home():
    specials = [item.to_dict() for item in MenuItem.query.filter_by(is_special=True).all()]
    
    categories = [row[0] for row in db.session.query(MenuItem.category).distinct().all()]
    
    menu_items_by_category = {}
    for category in categories:
        items = MenuItem.query.filter_by(category=category).limit(2).all()
        menu_items_by_category[category] = [item.to_dict() for item in items]
    
    return render_template('index.html', 
                         specials=specials,
                         menu_categories=categories,
                         menu_items=menu_items_by_category)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/menu')
def menu():
    all_items = MenuItem.query.all()
    menu_items = [item.to_dict() for item in all_items]
    categories = sorted(list(set(item['category'] for item in menu_items)))
    return render_template('menu.html', menu_items=menu_items, menu_categories=categories)

@app.route('/reservations', methods=['GET', 'POST'])
def reservations():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        date_str = request.form.get('date')
        time_str = request.form.get('time')
        guests_str = request.form.get('guests')
        requests = request.form.get('requests', '')

        # 1. Basic Validation
        if not all([name, email, phone, date_str, time_str, guests_str]):
            flash('All required fields must be filled.', 'error')
            return redirect(url_for('reservations'))

        # 2. Email Validation
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            flash('Invalid email address format.', 'error')
            return redirect(url_for('reservations'))

        try:
            # 3. Date/Time/Guest Parsing & Validation
            res_date = datetime.strptime(date_str, '%Y-%m-%d').date()
            guests = int(guests_str)

            if res_date < date_obj.today():
                flash('Reservations cannot be made for past dates.', 'error')
                return redirect(url_for('reservations'))
            
            if guests <= 0:
                flash('Number of guests must be at least 1.', 'error')
                return redirect(url_for('reservations'))

            # 4. Capacity Check
            total_guests_at_time = db.session.query(db.func.sum(Reservation.guests)).filter(
                Reservation.date == date_str,
                Reservation.time == time_str
            ).scalar() or 0

            if total_guests_at_time + guests > 30:
                flash('Sorry, we are fully booked for this time slot. Please choose another.', 'error')
                return redirect(url_for('reservations'))

            new_res = Reservation(
                name=name, email=email, phone=phone, 
                date=date_str, time=time_str, guests=guests, 
                special_requests=requests
            )
            db.session.add(new_res)
            db.session.commit()
            
            flash(f'Thank you {name}! Your reservation for {guests} guests has been successfully submitted.', 'success')
            return redirect(url_for('reservations'))
        except Exception as e:
            print(f"Error: {e}")
            flash('There was an error processing your reservation. Please check your inputs.', 'error')
            return redirect(url_for('reservations'))
    
    return render_template('reservations.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# Initialize database and seed data
def init_db():
    with app.app_context():
        db.create_all()
        if MenuItem.query.count() == 0:
            sample_items = [
                MenuItem(category='Starters', name='Bruschetta', description='Toasted bread topped with tomatoes, garlic, and fresh basil', price=9.99, is_special=False),
                MenuItem(category='Starters', name='French Onion Soup', description='Classic soup with caramelized onions and melted cheese', price=11.99, is_special=False),
                MenuItem(category='Main Courses', name='Filet Mignon', description='Premium cut beef with red wine reduction', price=39.99, is_special=False),
                MenuItem(category='Main Courses', name='Herb-Crusted Rack of Lamb', description='Tender lamb with herb crust and mint sauce', price=36.99, is_special=True),
                MenuItem(category='Desserts', name='Crème Brûlée', description='Classic vanilla custard with caramelized sugar top', price=10.99, is_special=False),
                MenuItem(category='Desserts', name='Tiramisu', description='Coffee-flavored Italian dessert with mascarpone', price=11.99, is_special=False),
                MenuItem(category='Beverages', name='Artisanal Coffee Selection', description='Locally roasted single-origin beans', price=4.50, is_special=False),
                MenuItem(category='Beverages', name='Craft Cocktails', description='Ask your server for today\'s special creations', price=12.00, is_special=False)
            ]
            db.session.bulk_save_objects(sample_items)
            db.session.commit()

# Ensure DB is initialized
init_db()

if __name__ == '__main__':
    app.run(debug=True)