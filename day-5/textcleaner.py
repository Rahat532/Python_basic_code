import re

def clean_text(text):
    # remove the punctuation
    text = re.sub(r'[^\w\s]', '', text)
    # remove extra whitespace
    text = ' '.join(text.split())
    # convert to lowercase
    text = text.lower()
    return text
# Example usage
sample_text = "  Hello, World! Welcome to AI BootCamp.  "
cleaned = clean_text(sample_text)
print("Original Text:", sample_text)
print("Cleaned Text:", cleaned)