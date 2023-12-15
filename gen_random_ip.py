import random
from datetime import datetime, timedelta

# Function to generate log entries
def generate_log_entry(ip_address):
    timestamp = datetime.now() - timedelta(days=random.randint(1, 365), hours=random.randint(1, 24))
    method = random.choice(["GET", "POST", "PUT", "DELETE"])
    url = random.choice(["https://www.example.com", "https://www.sample.com", "https://www.test.com", "https://www.nyamariXCode.com"])

    return f"{timestamp},{method},{url},{ip_address}"

# Function to generate a single IP address
def generate_ip():
    return f"10.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"

# Create a log file with 100 examples
with open("file1.txt", "w") as file:
    for _ in range(100):
        ip_address = generate_ip()
        repetitions = random.randint(1, 12)
        for _ in range(repetitions):
            file.write(f"{generate_log_entry(ip_address)}\n")

print("Log file created: log_file.txt")
