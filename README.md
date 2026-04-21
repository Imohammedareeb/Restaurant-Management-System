# 🍽️ Savory Bistro - Restaurant Management System

Savory Bistro is a sophisticated, full-stack web application designed to streamline restaurant operations and enhance the guest experience. From real-time reservation management with capacity logic to a dynamic, mobile-responsive culinary showcase, this system brings modern digital solutions to the dining industry.

![License](https://img.shields.io/github/license/Imohammedareeb/Restaurant-Management-System?style=flat-square)
![Flask](https://img.shields.io/badge/Flask-3.1.0-blue?style=flat-square&logo=flask)
![SQLite](https://img.shields.io/badge/SQLite-3-003B57?style=flat-square&logo=sqlite)
![Vercel](https://img.shields.io/badge/Vercel-Deployed-black?style=flat-square&logo=vercel)

---

## 🚀 Live Demo
**[View Live Project on Vercel](https://restaurant-management-system-iota.vercel.app/)** *(Note: Replace with your actual link after deployment)*

---

## ✨ Key Features

### 📅 Advanced Reservation System
- **Intelligent Validation:** Prevents past-date bookings and enforces strict data formatting on both client and server sides.
- **Dynamic Capacity Management:** Built-in logic to prevent overbooking, ensuring the kitchen and staff are never overwhelmed.
- **Instant Feedback:** Real-time flash notifications for successful bookings or specific validation errors.

### 🍱 Digital Culinary Showcase
- **Dynamic Menu Engine:** Categorized menu display pulled directly from the database.
- **Daily Specials:** Automated highlighting for "Chef's Specials" with specialized UI treatments.
- **PDF Integration:** Seamless access to full printable menus for traditional diners.

### 📱 Responsive & Accessible UI
- **Mobile-First Design:** Optimized for smartphones, tablets, and desktops using modern CSS Flexbox and Grid.
- **Refined UX:** Strategic Call-to-Action (CTA) placements to maximize reservation conversions.
- **Modern Aesthetics:** Clean, typography-focused design that reflects a premium dining atmosphere.

---

## 🛠️ Technical Stack

- **Backend:** Python / Flask
- **Database:** SQLAlchemy / SQLite (File-based for high portability)
- **Frontend:** HTML5, CSS3 (Vanilla), JavaScript (ES6+)
- **Deployment:** Vercel (Serverless Functions)

---

## ⚙️ Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Imohammedareeb/Restaurant-Management-System.git
   cd Restaurant-Management-System
   ```

2. **Set Up Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Locally**
   ```bash
   python app.py
   ```
   The app will be available at `http://127.0.0.1:5000`.

---

## 🛡️ QA & Security Implementations

This project underwent a rigorous QA audit, resulting in several critical security and stability patches:
- **Server-Side Guardrails:** Eliminated dependency on frontend-only validation to prevent malicious data injection.
- **Error Resilience:** Replaced potentially crashing key-lookups with safe `.get()` methods.
- **Path Sanitization:** Integrated `url_for` across all assets to ensure broken links are impossible regardless of the hosting environment.
- **Security:** Parameterized SQL queries via SQLAlchemy to prevent SQL Injection attacks.

---

## 📄 License
Distributed under the MIT License. See `LICENSE` for more information.

---

**Developed with ❤️ by [Mohammed Areeb](https://github.com/Imohammedareeb)**
