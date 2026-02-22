import messages_functions
from messages_functions import show_messages
from messages_functions import send_messages as sm
import messages_functions as mf
from messages_functions import *

# using module name
print("Using module name:")
messages = ["Hello World!", "Python is fun.", "I love Python."]
messages_functions.show_messages(messages)

sent_messages = []
messages_functions.send_messages(messages[:], sent_messages)

print("\nMessage lists:") 
print(messages)
print(sent_messages)

# using function name and alias
print("\nUsing function name and alias:")
messages = ["Hello World!", "Python is fun.", "I love Python."]
show_messages(messages)

sent_messages = []
sm(messages[:], sent_messages)

print("\nMessage lists:")
print(messages)
print(sent_messages)

# using module alias
print("\nUsing module alias:")
messages = ["Hello World!", "Python is fun.", "I love Python."]
mf.show_messages(messages)

sent_messages = []
mf.send_messages(messages[:], sent_messages)

print("\nMessage lists:")
print(messages)
print(sent_messages)

# using import *
print("\nUsing import *:")
messages = ["Hello World!", "Python is fun.", "I love Python."]
show_messages(messages)

sent_messages = []
send_messages(messages[:], sent_messages)

print("\nMessage lists:")
print(messages)
print(sent_messages)