import collections.abc
import time

time.clock = time.time

collections.Hashable = collections.abc.Hashable
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chat bot named Charlie

chatbot = ChatBot('Charlie')
# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
trainer.train("chatterbot.corpus.english.greetings")


trainer.export_for_training('./my_export.json')
# Get a response to an input statement
chatbot.get_response("Hello")

from chatterbot.trainers import ListTrainer

conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

trainer = ListTrainer(chatbot)

trainer.train(conversation)

response = chatbot.get_response("Good morning!")
print(response)


from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.conversation import Statement

# Create a new instance of a ChatBot
chatbot = ChatBot('ContextualBot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on the English corpus
trainer.train('chatterbot.corpus.english.greetings')

# Start a conversation with the chatbot
print("Bot: Hello! How can I help you today?")

context = []

while True:
    user_input = input("You: ")

    if user_input.lower() == 'bye':
        print("Bot: Goodbye! Have a great day.")
        break

    # Maintain conversation context
    if context:
        response = chatbot.get_response(user_input)
    else:
        response = chatbot.get_response(user_input)
    
    # Update context for the next iteration
    context = [Statement(user_input), response.text]
    #context.add_response(response)

    print("Bot:", response)
    
