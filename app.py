import streamlit as st
from api_calling import note_generator, audio_transcription, quiz_generation
from PIL import Image

st.title("AI Study Helper")
st.markdown("Upload note images to generate Note Summary and Quizzes")
st.divider()

with st.sidebar:
    st.header("Controls")
    # st.divider()
    images = st.file_uploader(
        "Upload the photos of your note: ",
        type=['jpg', 'png', 'jpeg'],
        accept_multiple_files=True
    ) 

    if images:
        pil_images = []

        for img in images:
            try:
                pil_image = Image.open(img)
                pil_images.append(pil_image)
            except (IOError, SyntaxError):
                st.error("Sorry, invalid image file!")
        if len(images) > 3:
            st.error("Upload at max 3 images!")
        else:
            st.subheader(f"Your Uploaded **{len(images)}** Images")
            col = st.columns(len(images))


            for i, img in enumerate(images):
                with col[i]:
                    st.image(img)


    # difficulty
    selected_option = st.selectbox(
        "Enter the difficulty of your quiz: ",
        ("Easy", "Medium", "Hard"),
        index = None
    )

    if selected_option:
        st.markdown(f"You selected **{selected_option}** as difficulty of your quiz")
    # else:
    #     st.error("You must select a difficulty")
    
    # Language
    selected_language = st.selectbox(
        "Select the language: ",
        ("Bangla", "English"),
        index = None
    )

    if selected_language:
        st.markdown(f"You selected **{selected_language}** as language")

    pressed = st.button("Click the button to initiate AI", type="primary")

    
if pressed:
    if not images:
        st.error("You must upload 1 image")
    if not selected_option:
        st.error("You must select a difficulty for your quiz")

    if images and selected_option:

        #note

        with st.container(border=True):
            st.subheader("Your Note")
            #the portion below will replaced by API call
            try:
                with st.spinner("AI is writing note for you..."):
                    generated_note = note_generator(pil_images, selected_language)
                    st.markdown(generated_note)
            except Exception as e:
                if "503" in str(e):
                    st.error("The AI is currently overwhelmed with requests. Please wait a moment and try again!")
                else:
                    st.error(f"An unexpected error occurred: {e}")



        #audio transcript
        with st.container(border=True):
            st.subheader("Audio Transcription")
            clean_text = generated_note.replace("#", " ").replace("*", " ").replace("- ", " ").replace("\\", " ")
            
            #the portion below will replaced by API call
            with st.spinner("Audio Transcription creation in process..."):
                generated_audio = audio_transcription(clean_text, selected_language)
                st.audio(generated_audio)
                
                
                
                
        #quiz
        with st.container(border=True):
            st.subheader(f"Quiz ({selected_option} Difficulty)")
            #the portion below will replaced by API call
            with st.spinner("AI is generating quiz for you..."):
                quizzes = quiz_generation(pil_images, selected_option, selected_language)
                st.markdown(quizzes)




