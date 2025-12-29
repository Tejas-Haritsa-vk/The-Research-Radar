import imaplib
import email
from email.header import decode_header
import time
import csv
import os

# --- CONFIGURATION ---
EMAIL_USER = "your-email@domain.com"
EMAIL_PASS = "your-app-password"  # Use an App Password, not your real password
IMAP_SERVER = "imap.gmail.com"   # Use your provider's IMAP server
POLL_INTERVAL = 60               # Seconds between checks
CSV_FILE = "subscribers.csv"
SEARCH_SUBJECT = "NEW_SUBSCRIBER_SIGNAL"

def clean_text(text):
    return text.strip().replace('\n', '').replace('\r', '')

def process_emails():
    try:
        # 1. Connect and Login
        mail = imaplib.IMAP4_SSL(IMAP_SERVER)
        mail.login(EMAIL_USER, EMAIL_PASS)
        mail.select("inbox")

        # 2. Search for unread emails from our website
        # We search for the specific subject line we set in the frontend
        status, messages = mail.search(None, f'(UNSEEN SUBJECT "{SEARCH_SUBJECT}")')
        
        if status != 'OK':
            return

        email_ids = messages[0].split()
        
        if not email_ids:
            return

        print(f"[*] Found {len(email_ids)} new signals. Processing...")

        # 3. Open CSV for appending
        file_exists = os.path.isfile(CSV_FILE)
        with open(CSV_FILE, 'a', newline='') as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(["Timestamp", "Email", "Interests"])

            for e_id in email_ids:
                # Fetch the email body
                res, msg_data = mail.fetch(e_id, "(RFC822)")
                for response_part in msg_data:
                    if isinstance(response_part, tuple):
                        msg = email.message_from_bytes(response_part[1])
                        
                        # Extract Body
                        body = ""
                        if msg.is_multipart():
                            for part in msg.walk():
                                if part.get_content_type() == "text/plain":
                                    body = part.get_payload(decode=True).decode()
                        else:
                            body = msg.get_payload(decode=True).decode()

                        # Basic Parsing logic (assumes body contains "Email: ..." and "Interests: ...")
                        # This depends on how you set up your EmailJS template.
                        try:
                            lines = body.split('\n')
                            sub_email = ""
                            sub_interests = ""
                            for line in lines:
                                if "Email:" in line: sub_email = line.split("Email:")[1].strip()
                                if "Interests:" in line: sub_interests = line.split("Interests:")[1].strip()
                            
                            if sub_email:
                                timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
                                writer.writerow([timestamp, sub_email, sub_interests])
                                print(f"[+] Decrypted: {sub_email}")
                        except Exception as parse_err:
                            print(f"[!] Parsing error on packet {e_id}: {parse_err}")

                # 4. Mark as read (already handled by fetching UNSEEN and selecting INBOX)
                # Or explicitly delete it if you prefer:
                # mail.store(e_id, '+FLAGS', '\\Deleted')

        mail.close()
        mail.logout()

    except Exception as e:
        print(f"[!] Connection Error: {e}")

if __name__ == "__main__":
    print(f"--- THE RESEARCH RADAR COLLECTOR ONLINE ---")
    print(f"[*] Monitoring {EMAIL_USER} for signals...")
    while True:
        process_emails()
        time.sleep(POLL_INTERVAL)