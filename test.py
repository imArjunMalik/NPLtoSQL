import openai
import os 

# Load and store API key
openai.api_key = os.getenv('OPENAI_API_KEY')
os.getenv('OPENAI_API_KEY')

response = openai.completions.create(
        model = 'text-davinci-003',
        prompt = 'Two reasons why I should learn python', 
        max_tokens = 50
)
print(response)