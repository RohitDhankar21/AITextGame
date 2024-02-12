import google.generativeai as genai

genai.configure(api_key=('AIzaSyDVZKB0eaK0uT1AWXwBVQUqIu4FsFx6xhU'))


generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}


safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_NONE"
  },
]



model = genai.GenerativeModel(model_name="gemini-pro", generation_config=generation_config, safety_settings=safety_settings)



chat = model.start_chat(history=[])



def start_ai_program():
  
  initial_prompt = """
    Let's play a text adventure! You create the story with your choices. choices will be given.
    Only respond with the narrator's side of the story. 
    My response will impact future outcomes and guide the story forward.
    Limit your descriptive words and be more direct with the situation.
    Keep it short, one or two sentences, and stick to the narrator's point of view.
    """

  try:
        response = chat.send_message(initial_prompt)
        return response.text
  except Exception as e:
        return f'{type(e).__name__}: {e}'
    


def getNewAIMessage(message):
  res = chat.send_message(message)
  return res.text



