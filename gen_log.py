import random
from datetime import datetime, timedelta

# Function to generate random IP addresses
def generate_random_ip():
    return ".".join(str(random.randint(0, 255)) for _ in range(4))

# Function to generate log entries
def generate_log_entry():
    timestamp = datetime.now() - timedelta(days=random.randint(1, 365), hours=random.randint(1, 24))
    method = random.choice(["GET", "POST", "PUT", "DELETE"])
    url = random.choice(["https://www.example.com", "https://www.sample.com", "https://www.test.com"])
    ip_address = generate_random_ip()

    return f"{timestamp},{method},{url},{ip_address}"

# Create a log file with 100 examples
with open("ip_log_file.txt", "w") as file:
    for _ in range(100):
        file.write(generate_log_entry() + "\n")

print("Log file created: log_file.txt")
