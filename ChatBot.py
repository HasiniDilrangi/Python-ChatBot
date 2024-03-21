import re
from Default_massages import defaultMsg

#  Evaluate probability of recognized words
def message_probability(user_message, recognised_word, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

 # Check required words are present
    for word in user_message:
        if word in recognised_word:
            message_certainty += 1

# Evaluate percent of words in user massage
    percentage = float(message_certainty / float(len(recognised_word)))

    for word in recognised_word:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

# Suggested responses
def check_all_messages(message):
    responses = [ 
        ('Hello!', ['hello', 'hi', 'hey', 'yo', 'what\'s up', 'sup'], True, []),
        ('I am doing fine, and how about you?', ['how', 'you', 'doing'], True, []),
        ('I don\'t have Name.I am only Computer programme', ['name'], True, []),
        ('I don\'t have Age.I am only Computer programme', ['age'], True, []),
        ('I don\'t like Eat.I am only Computer programme', ['eat'], True, []),
        ('I don\'t like Sleep.I am only Computer programme', ['sleep'], True, []),
        ('Currently, I speak only English?', ['languages', 'speak'], True, []),
        ('How can I help you?', ['help'], True, []),
        ('Let\'s make the most of our conversation!', ['make', 'most', 'conversation'], True, []),
        ('Nice to meet you!', ['nice', 'meet', 'you'], True, []),
        ('I\'m here to assist you. What can I do for you today?', ['assist', 'today'], True, []),
        ('I love learning new things. What\'s something you recently learned?', ['learn', 'new', 'things'], True, []),
        ('I enjoy chatting with you!', ['enjoy', 'chatting'], True, []),
        ('If you have any more questions or if there is anything else I can help you', ['questions', 'chat', 'bot'], True, []),
        ('You are welcome! If you ever need assistance in the future, Have a great day!', ['thanks', 'exit', 'bye'], True, []),
        ('I\'m sorry, but I don\'t have information on that topic. Anything else I can help you with?', ['information', 'topic'], True, []),
    ]

    highest_prob_list = {}

# Evaluate the probability
    for response_info in responses:
        bot_response, list_of_words, single_response, required_words = response_info
        probability = message_probability(
            message, list_of_words, single_response, required_words
        )
        highest_prob_list[bot_response] = probability

# Select the response with the highest probability
    best_match = max(highest_prob_list, key=highest_prob_list.get)
    print(highest_prob_list)

    return defaultMsg() if highest_prob_list[best_match] == 0 else best_match

# Function to get user response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

# Testing response
while True:
    print('Bot:', get_response(input('You: ')))
