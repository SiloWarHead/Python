import yagmail
import getpass

# --- 1. CONFIGURATION ---
MY_EMAIL = "mayukhdasbloodofseven@gmail.com" 
MY_PASSWORD = "qcdv bsik xagr zjkr" 

# Data source for mail merge
RECIPIENTS = [
    {"name": "Tamjid Husain Taseen", "email": "sharminniit@gmail.com"},
    {"name": "Ifraz Kalam", "email": "iffyiscool71@gmail.com"},
    {"name": "Md. Salfi Salehin Shochso", "email": "salfi.salehin@gmail.com"},
    {"name": "Antorip Paul", "email": "antorippaul108@gmail.com"},
    {"name": "Nayeef Hasan", "email": "tjasurovi@gmail.com"},
]

SUBJECT = "⚔ TKK Daily Fact — Study Smarter Today"

# --- 2. PLAIN TEXT TEMPLATE ---
# The template uses a placeholder {name} for personalization.
# You can use newline characters (\n) for formatting.
PLAIN_TEXT_TEMPLATE = """
Dear {name},

⚔ The Knowledge Knights — Daily Fact

Fact of the Day:
AI can supercharge your studying! Tools like Jungle AI, ChatGPT, and Notion AI help with summarizing notes, practicing recall, generating quizzes, and explaining complex topics in simple terms. Use AI as a study partner—not a replacement—to learn faster and retain knowledge longer.

Study Smarter — 3 Quick Tips:
1. Spaced Repetition: Revisit material at intervals. Builds stronger memory pathways than cramming.
2. Active Recall: Test yourself instead of rereading. Retrieval practice is more powerful than recognition.
3. Deep Work Blocks: Study in focused sessions of 25–50 minutes with breaks to recharge and consolidate.

Today's Challenge:
Use one AI tool today to summarize a topic you’re learning. Compare its output with your own notes and refine your understanding.

Try Jungle AI: https://jungle.ai/

⚔ The Knowledge Knights — Where Wisdom Meets Honor
"""

# --- 3. SENDING LOGIC (Mail Merge) ---
try:
    # Establish connection once before the loop
    yag = yagmail.SMTP(MY_EMAIL, MY_PASSWORD)
    
    print(f"\nAttempting to send {len(RECIPIENTS)} personalized emails...")

    for recipient in RECIPIENTS:
        recipient_name = recipient["name"]
        recipient_email = recipient["email"]
        
        # Create a personalized body using the .format() method
        personalized_body = PLAIN_TEXT_TEMPLATE.format(name=recipient_name)
        
        # Send the personalized email
        yag.send(
            to=recipient_email,
            subject=SUBJECT,
            # yagmail automatically sends this as text/plain
            contents=personalized_body 
        )
        print(f"✅ Sent email to: {recipient_name} ({recipient_email})")
        
    print("\nMail merge complete!")

except yagmail.AuthenticationError:
    print("\n❌ ERROR: Authentication failed. Check your App Password and email address.")
except yagmail.YagAddressError:
    print("\n❌ ERROR: Invalid email address format detected in recipient list.")
except Exception as e:
    print(f"\n❌ An unexpected error occurred: {e}")