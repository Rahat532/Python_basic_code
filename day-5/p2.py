# find  email address in text and  replace it with [EMAIL REDACTED]
import re
def redact_email(text):
    # Regular expression pattern for matching email addresses
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    # Replace all occurrences of the email pattern with '[EMAIL REDACTED]'
    redacted_text = re.sub(email_pattern, '[EMAIL REDACTED]', text)
    return redacted_text
# Example usage
sample_text = input("Enter a text containing email addresses: ")
redacted_text = redact_email(sample_text)
print(redacted_text)