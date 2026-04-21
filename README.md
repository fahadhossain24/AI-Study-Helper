# :books: AI Study Helper

An AI-powered study assistant that generate **Summary of the Contextj/Note, Voice Summarization and Respective Quizzes** from uploaded note/book images uusing **Google Gemini API** and **Streamlit**.

---

## 🚀 Features

- 📝 **AI Note Generator**  
  Transforms uploaded images into well-structured, concise, exam-focused notes in both Bangla and English

- ❓ **MCQ Quiz Generator**  
  Creates exam-oriented multiple-choice questions with customizable difficulty levels

- 🔊 **Audio Notes (Bangla & English)**  
  Converts generated notes into spoken audio for easy listening and revision

- 📸 **Image Input Support**  
  Supports both handwritten and printed notes (up to 3 images per session)

- ⚡ **Fast & Interactive UI**  
  Developed with Streamlit to provide a smooth and user-friendly experience


---

<!-- ## 🎥 Demo & Explanation Video

👉 https://youtu.be/8xYvQFYTALM

### 📌 What the video covers:
- Project overview  
- System workflow (Gemini + Streamlit + gTTS)  
- Live demo (upload → notes → quiz → audio)  
- Code structure explanation   -->

## 🧠 Tech Stack

- Python  
- Streamlit  
- Google Gemini API (`google-generativeai`)  
- Model (`gemini-3.1-flash-lite-preview`)  
- Pillow (PIL)  
- gTTS (Text-to-Speech)  
- python-dotenv  

---

## 🏗️ How It Works

The application follows a simple pipeline to convert images into exam-ready study materials:

1. **Upload Images**  
   Users upload up to 3 images of handwritten or printed notes through the Streamlit interface.

2. **Image Processing**  
   The uploaded images are preprocessed and sent to the Gemini API for text extraction and understanding.

3. **AI Content Generation**  
   - 📘 **Notes Generation**: Extracted content is transformed into structured, concise, exam-ready notes (Bangla & English).  
   - ❓ **Quiz Generation**: The system generates multiple-choice questions with answers based on the extracted content.

4. **Audio Conversion**  
   The generated notes are converted into speech (Bangla & English) using gTTS for audio-based learning.

5. **Output Display**  
   All generated content is displayed instantly in the Streamlit UI:
   - Structured Notes  
   - MCQ Quiz  
   - Downloadable/Playable Audio  

---

## ⚙️ Installation Guide

### 1️⃣ Clone the repository
```bash
git clone "https://github.com/fahadhossain24/AI-Study-Helper.git"
cd "AI-Study-Helper"
```

### 2️⃣ Create virtual environment (recommended)
```bash
python -m venv venv

# Linux/Mac
source venv/bin/activate  

# Windows
venv\Scripts\activate
```


### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt

🔑 Environment Setup

Create a .env file in the root directory:
GEMINI_API_KEY=your_gemini_api_key_here
```

### ▶️ Run the App
```bash 
streamlit run app.py
```

---

## 🧪 Usage
  - Upload up to 3 images of notes
  - Select quiz difficulty
  - Select response language
  - Click the button

## 🎯 Output:

📘 Exam-ready structured notes  
🔊 Audio version  
❓ MCQ quiz with answers  


---

## 📌 Use Cases

📖 Exam revision from handwritten notes  
🧠 Quick study summaries from any book page or notes  
🎯 Self-assessment using MCQs by defining deficulties  
🎧 Learning through audio  

---

## ⚠️ Limitations
Maximum 3 images per session  
Requires internet connection  
Gemini responses may vary slightly  

---

## 🔮 Future Improvements
🔐 User authentication system  
💾 Save notes & quiz history  
📊 Performance tracking dashboard  
🧾 Better image-to-text accuracy  
📱 Mobile-friendly UI  

---


## 👨‍💻 Author
**Fahad Hossain**

🎓 BSc in Computer Science (Ongoing)
[University Of The People (UoPeople), USA](https://www.uopeople.edu/)

🎓 Diploma in Computer Science and Technology
[Feni Polytechnic Institute, Feni, Bangladesh](https://feni.polytech.gov.bd/)


📧 Email: fahadhossain0503@gmail.com


---

## ⭐ Support

**If you find this project helpful, please ⭐ star the repository and share it!

