from flask import Flask
from flask_mysqldb import MySQL

# Initialize Flask app and MySQL
app = Flask(__name__)

# MySQL configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = 'Bank_db'

# Initialize MySQL
mysql = MySQL(app)

@app.route('/insert_data')
def insert_data():
    try:
        # Get a cursor
        cursor = mysql.connection.cursor()

        # Insert data into `accounts` table
        account_data = [
            ('101', 'John Doe', 1000.00),  # Example: (account_id, account_name, balance)
            ('102', 'Jane Smith', 5000.00),
            ('103', 'Tom Hardy', 300.00)
        ]
        cursor.executemany("INSERT INTO accounts (account_id, account_name, balance) VALUES (%s, %s, %s)", account_data)

        # Insert data into `transactions` table
        transaction_data = [
            ('101', 'deposit', 1500.00, '2025-01-01'),
            ('102', 'withdrawal', 200.00, '2025-01-02'),
            ('103', 'deposit', 100.00, '2025-01-03')
        ]
        cursor.executemany("INSERT INTO transactions (account_id, transaction_type, amount, transaction_date) VALUES (%s, %s, %s, %s)", transaction_data)

        # Insert data into `loans` table
        loan_data = [
            ('101', 5000.00, 5.5, '2023-01-01', '2025-01-01'),
            ('102', 20000.00, 3.5, '2023-05-01', '2026-05-01')
        ]
        cursor.executemany("INSERT INTO loans (account_id, loan_amount, interest_rate, loan_start_date, loan_end_date) VALUES (%s, %s, %s, %s, %s)", loan_data)

        # Insert data into `cards` table
        card_data = [
            ('101', 'Visa', 10000.00, '2026-12-31'),
            ('102', 'MasterCard', 15000.00, '2027-05-30')
        ]
        cursor.executemany("INSERT INTO cards (account_id, card_type, card_limit, expiration_date) VALUES (%s, %s, %s, %s)", card_data)

        # Insert data into `banking_alerts` table
        alert_data = [
            ('101', 'Your monthly statement is available.'),
            ('102', 'Payment due for your loan.'),
            ('103', 'Suspicious activity detected on your account.')
        ]
        cursor.executemany("INSERT INTO banking_alerts (account_id, alert_message) VALUES (%s, %s)", alert_data)

        # Insert data into `locations` table (ATM locations)
        location_data = [
            ('ATM1', '123 Main St, City, Country'),
            ('ATM2', '456 Elm St, City, Country'),
            ('ATM3', '789 Oak St, City, Country')
        ]
        cursor.executemany("INSERT INTO locations (location_name, address, type) VALUES (%s, %s, 'ATM')", location_data)

        # Insert data into `investments` table
        investment_data = [
            ('101', 'Stocks', 2000.00, 7.0),
            ('102', 'Mutual Funds', 5000.00, 5.0)
        ]
        cursor.executemany("INSERT INTO investments (account_id, investment_type, amount_invested, annual_return) VALUES (%s, %s, %s, %s)", investment_data)

        # Commit the changes
        mysql.connection.commit()

        return "Data inserted successfully!"
    
    except Exception as e:
        return f"An error occurred: {str(e)}"
    
    finally:
        # Close the cursor
        cursor.close()

if __name__ == '__main__':
    app.run(debug=True)
