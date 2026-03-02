import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta

# ==========================================
# 1. Email Configuration
# ==========================================
MY_EMAIL = "YourEmail@gmail.com"  # Put your real email here
MY_PASSWORD = "App Password"  # Use Google App Password here
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

# ==========================================
# 2. Reading and Filtering Excel Data
# ==========================================
print("Analyzing the Excel file...")

try:
    df = pd.read_excel('employees.xlsx')
    
    df['Last_Login'] = pd.to_datetime(df['Last_Login'])
    
    cutoff_date = datetime.now() - timedelta(days=21)
    
    inactive_employees = df[df['Last_Login'] < cutoff_date]
    
    print(f"Found {len(inactive_employees)} inactive accounts.")

    # ==========================================
    # 3. Sending the Emails
    # ==========================================
    if len(inactive_employees) > 0:
        print("Connecting to the email server (via SSL)...")
        server = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
        server.login(MY_EMAIL, MY_PASSWORD)

        for index, row in inactive_employees.iterrows():
            emp_name = row['Name']    
            emp_email = row['Email']  

            msg = MIMEMultipart()
            msg['From'] = MY_EMAIL
            msg['To'] = emp_email
            msg['Subject'] = "Action Required: Inactive Email Account"

            body = f"""Hello {emp_name},
            
We noticed that you haven't synced data for over 21 days.
If you are experiencing any technical issues or need help, please reply to this email so we can assist you.

Best regards,
IT Support Team
"""
            msg.attach(MIMEText(body, 'plain', 'utf-8'))
            
            server.send_message(msg)
            print(f"[SUCCESS] Email sent to: {emp_name} ({emp_email})")

        server.quit()
        print("Mission accomplished! All emails have been sent.")
    else:
        print("All accounts are active. No emails to send.")

except Exception as e:
    print(f"[ERROR] An error occurred: {e}")

# Keep the terminal window open to see the results

input("\nPress Enter to exit...")


