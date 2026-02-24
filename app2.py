from openai import OpenAI
import config

client = OpenAI(api_key=config.OPENAI_API_KEY)

response = client.responses.create(
  model="gpt-5.1",
  input=[
    {
      "role": "developer",
      "content": [
        {
          "type": "input_text",
          "text": "You are a friendly elementary school teacher who explains science in simple, clear language."
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "input_text",
          "text": "Why is the sky blue?"
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "type": "output_text",
          "text": "The sky looks blue because sunlight is made of many colors, and when it passes through the air, tiny particles scatter the blue light more than the other colors. That scattered blue light is what we see when we look up at the sky."
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "input_text",
          "text": "Can you suggest a simple classroom demonstration to help students understand that?"
        }
      ]
    }
  ],
  text={
    "format": {
      "type": "text"
    },
    "verbosity": "low"
  },
  reasoning={
    "effort": "low",
    "summary": "auto"
  },
    tools=[
    {
      "type": "web_search",
      "user_location": {
        "type": "approximate"
      },
      "search_context_size": "medium"
    }
  ],
  store=True,
  include=[
    "reasoning.encrypted_content",
    "web_search_call.action.sources"
  ]
)

print(response.output_text)
