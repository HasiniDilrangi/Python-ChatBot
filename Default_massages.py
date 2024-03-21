import random

# Default messages
def defaultMsg():
    response = [    
        "Can you please clarify?",
        "Sorry, I didn\'t get that.",
        "What does that mean?",
        "Can you explain it differently?"
    ]
    
    return random.choice(response)
