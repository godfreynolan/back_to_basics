from openai import OpenAI
import config

client = OpenAI(api_key=config.OPENAI_API_KEY)

response = client.responses.create(
    model="gpt-4.1",
    input="Hello world, greet me back?"
)

print(response.output_text)
