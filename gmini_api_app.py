

import google.generativeai as genai

genai.configure(api_key='API_key')     #API_gmini_key

generation_config = {
    "temperature": 0,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 1000,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
    system_instruction='''
    #HOW YOU WANT YOU MODEL TO BE OR TO SPEAK AND ANSWER QUESTIONS ,,,EX:


    speak like a teen .
    and use  jokes and symbols,emojis.
    be helpful and smart when talking.


    ''',
)

chat_session = model.start_chat(
    history=[
    ]
)



