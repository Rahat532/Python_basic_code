# a program log messages with timestamp to files
from datetime import datetime
def log_message(filename, message):
    """Logs a message with the current timestamp to the specified file."""
    try:
        with open(filename, 'a') as file:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            file.write(f"[{timestamp}] {message}\n")
    except IOError:
        print(f"Error: Could not write to file {filename}.")
# Example usage
log_file = 'day-6/logs.txt'
log_message(log_file, "This is a log message.") 
log_message(log_file, "Another log entry.")
print(f"Log messages have been written to {log_file}.")
