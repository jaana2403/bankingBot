import nltk
from nltk.chat.util import Chat, reflections
import mysql.connector

def chatbot_response(user_message, mysql, account_id):
    try:
        cursor = mysql.connection.cursor()

        # Account Inquiries
        if "balance" in user_message:
            query = "SELECT balance FROM accounts WHERE account_id=%s"
            print(f"Executing query: {query} with account_id={account_id}")
            cursor.execute(query, (account_id,))
            balance = cursor.fetchone()
            if balance:
                return f"Your account balance is ${balance[0]:.2f}."
            else:
                return "Account not found. Please check your account number."

        # Transaction History Query
        if "transaction history" in user_message:
            query = (
                "SELECT transaction_type, amount, transaction_date FROM transactions "
                "WHERE account_id=%s ORDER BY transaction_date DESC LIMIT 10"
            )
            print(f"Executing query: {query} with account_id={account_id}")
            cursor.execute(query, (account_id,))
            transactions = cursor.fetchall()
            if transactions:
                response = "Recent transactions:\n"
                response += "\n".join([f"{t[0].capitalize()} on {t[2]}: ${t[1]:.2f}" for t in transactions])
                return response
            else:
                return "No recent transactions found."

        # Loan Information Query
        if "loan" in user_message:
            query = "SELECT loan_id, loan_amount, interest_rate, duration_months FROM loans WHERE account_id=%s"
            print(f"Executing query: {query} with account_id={account_id}")
            cursor.execute(query, (account_id,))
            loan_info = cursor.fetchone()
            if loan_info:
                return (
                    f"Your loan amount is ${loan_info[1]:.2f} at an interest rate of {loan_info[2]:.1f}%. "
                    f"Loan duration: {loan_info[3]} days."
                )
            else:
                return "No loan information found for this account."

        # Card Service Query
        if "credit card" in user_message or "card" in user_message:
            query = "SELECT card_type, credit_limit, outstanding_balance FROM cards WHERE account_id=%s"
            print(f"Executing query: {query} with account_id={account_id}")
            cursor.execute(query, (account_id,))
            card_info = cursor.fetchone()
            if card_info:
                return (
                    f"Your {card_info[0]} card has a limit of ${card_info[1]:.2f} and outstanding balance {card_info[2]}."
                )
            else:
                return "No credit card information found for this account."

        # Banking Alerts Query
        if "alert" in user_message:
            query = "SELECT alert_message FROM banking_alerts WHERE account_id=%s"
            print(f"Executing query: {query} with account_id={account_id}")
            cursor.execute(query, (account_id,))
            alerts = cursor.fetchall()
            if alerts:
                response = "Recent alerts:\n"
                response += "\n".join([alert[0] for alert in alerts])
                return response
            else:
                return "No recent alerts found for this account."

        # ATM and Branch Locator Query
        if "ATM" in user_message or "branch" in user_message:
            query = "SELECT location_name, address FROM atmbranchlocator WHERE is_atm='true' LIMIT 5"
            print(f"Executing query: {query}")
            cursor.execute(query)
            locations = cursor.fetchall()
            if locations:
                response = "Here are nearby ATMs:\n"
                response += "\n".join([f"{loc[0]} - {loc[1]}" for loc in locations])
                return response
            else:
                return "No ATMs or branches found near your location."

        # Fund Transfers
        if "transfer" in user_message:
            return (
                "To transfer funds, please provide the recipient's account number, amount, and any additional details. "
                "Make sure you have sufficient balance."
            )

        # Investment Queries
        if "investment" in user_message:
            query = "SELECT investment_type, amount_invested, annual_return FROM investments WHERE account_id=%s"
            print(f"Executing query: {query} with account_id={account_id}")
            cursor.execute(query, (account_id,))
            investments = cursor.fetchall()
            if investments:
                response = "Your current investments:\n"
                response += "\n".join([f"{inv[0]}: ${inv[1]:.2f}" for inv in investments])
                return response
            else:
                return "No investment information found for this account."

        # Customer Support
        if "support" in user_message or "help" in user_message:
            return (
                "How can I assist you? Common topics include account access, transaction errors, and more. "
                "If your issue requires urgent attention, please call our helpline."
            )

        # Default response
        return "Sorry, I didn't understand that. Can you please rephrase?"

    except Exception as e:
        return f"An error occurred: {str(e)}"

