from openai import OpenAI

client = OpenAI()
client2 = OpenAI()

# multi threading
# client.summarize
# client2.analyze


a = 154

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Analyze the pros and cons of remote work vs. office work"
        }
      ]
    }
  ],
  temperature=0.8,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
  response_format={
    "type": "text"
  }
)