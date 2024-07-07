from dotenv import load_dotenv
import os
import anthropic

load_dotenv()

# Set up the client
client = anthropic.Anthropic()


# Example conversation
messages = [
    {"role": "human", "content": "Hello, Claude!"},
    {"role": "assistant", "content": "Hello! How can I assist you today?"},
    {"role": "human", "content": "Can you explain what artificial intelligence is?"},
]

# Send the request to the API
response = client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=1000,
    messages=messages,
)

# Print the response
print(response.content[0].text)