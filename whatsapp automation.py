import pywhatkit
import time
from datetime import datetime

# Recipient data provided by the user
RECIPIENTS_DATA = [
    {"name": "Tamjid Husain Taseen", "number": "8801714340340"},
    {"name": "Ifraz Kalam", "number": "8801798587193"},
    {"name": "Md. Salfi Salehin Shochso", "number": "8801795854794"},
    {"name": "Antorip Paul", "number": "8801716282408"},
    {"name": "Nayeef Hasan", "number": "8801726935203"},
]

# Set the starting time to 10:57 PM (22:57)

START_HOUR = 23
START_MINUTE = 25

MESSAGE_TEMPLATE = """
*⚔ The Knowledge Knights — Daily Fact*

Dear {name},

Fact of the Day: AI can supercharge your studying! Tools like ChatGPT help with summarizing notes, generating quizzes, and explaining complex topics. Use AI as a study partner!

Study Smarter — 3 Quick Tips:
1. Spaced Repetition
2. Active Recall
3. Deep Work Blocks

Today's Challenge: Use one AI tool today to summarize a topic you’re learning.
"""

print(f"Attempting to schedule {len(RECIPIENTS_DATA)} personalized WhatsApp messages...")
print(f"Messages will begin sending starting at {START_HOUR:02d}:{START_MINUTE:02d}...")

for i, recipient in enumerate(RECIPIENTS_DATA):
    recipient_name = recipient["name"]
    # Add the required '+' prefix for pywhatkit.
    recipient_phone = f"+{recipient['number']}" 
    
    personalized_message = MESSAGE_TEMPLATE.format(name=recipient_name)
    
    # Stagger the sending time by adding 'i' minutes to the start minute
    current_minute = START_MINUTE + i
    current_hour = START_HOUR + (current_minute // 60)
    current_minute = current_minute % 60
    
    try:
        pywhatkit.sendwhatmsg(
            phone_no=recipient_phone, 
            message=personalized_message, 
            time_hour=current_hour, 
            time_min=current_minute, 
            tab_close=True,
            wait_time=20
        )
        print(f"Scheduled message for {recipient_name} ({recipient_phone}) at {current_hour:02d}:{current_minute:02d}.")
        
    except Exception as e:
        print(f"Error scheduling message for {recipient_name} ({recipient_phone}): {e}")

print("Scheduling complete. Ensure WhatsApp Web is logged in and ready!")