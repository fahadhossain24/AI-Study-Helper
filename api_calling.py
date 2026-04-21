from google import genai
from dotenv import load_dotenv
import os
from gtts import gTTS
import io


# loading the environment variable
load_dotenv()

my_api_key = os.getenv("GEMINI_API_KEY")


# initializing a client
client = genai.Client(api_key = my_api_key)



# note generator
def note_generator(images, selected_language):

    prompt = f"Summarize the picture in note format at max 100 words in language {selected_language}. Make sure to add necessary markdown to differentiate differnt section"

    response = client.models.generate_content(
        model = 'gemini-3.1-flash-lite-preview',
        # model = 'gemini-3-flash-preview',
        contents = [images, prompt]
    )

    return response.text


def audio_transcription(text, selected_language):
    lang_map = {
        "Bangla": "bn",
        "English": "en"
    }
    lang_code = lang_map.get(selected_language, 'en')
    
    speech= gTTS(text, lang=lang_code, slow=False)

    # speech.save("welcome.mp3")

    audio_buffer = io.BytesIO()
    speech.write_to_fp(audio_buffer)

    # st.audio("welcome.mp3")
    return audio_buffer


def quiz_generation(images, difficulty, selected_language):
    prompt = f"Generate 5 quizzes based on the {difficulty} in language {selected_language} Make sure to add markdown to differentiate the options. And given correct answer after each question."

    response = client.models.generate_content(
        model = 'gemini-3.1-flash-lite-preview',
        # model = 'gemini-3-flash-preview',
        contents = [images, prompt]
    )

    return response.text