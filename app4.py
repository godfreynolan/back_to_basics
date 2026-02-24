import base64
from openai import OpenAI
import config

client = OpenAI(api_key=config.OPENAI_API_KEY)
num_images = 5

img = client.images.edit(
  image=open("chess.png", "rb"),
  prompt="Intent: board game product render. Background: dark neutral studio with soft gradient. \\
    Foreground: inlaid wooden chessboard with subtle reflections. Hero subject: marble king and queen facing each other. \\
    Finishing details: realistic stone texture, crisp highlights, no logos or trademarks, no watermark. Camera: 35mm, low-angle, cinematic framing.",
  model="gpt-image-1.5",
  n=num_images,
  size="1024x1536",
  quality="high",
  background="auto",
  input_fidelity="high",
)

for i in range(num_images):
  image_bytes = base64.b64decode(img.data[i].b64_json)
  with open(f"output_{i}.png", "wb") as f:
    f.write(image_bytes)

