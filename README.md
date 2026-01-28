
# LinkedIn Post Generator 🚀

An AI-powered **LinkedIn Post Generator & Writing Assistant** built with **Streamlit**, designed to help users create, refine, and optimize LinkedIn posts with **context-aware AI**, **rewrite controls**, and **editor-like undo/redo functionality**.

This project goes beyond basic text generation by **learning from real LinkedIn post data** and adapting tone, language, and structure accordingly.

---

## ✨ Key Features

### 🧠 Intelligent Post Generation
- Topic-based post generation
- Configurable:
  - Length (Short / Medium / Long)
  - Language (English / Hinglish)
  - Audience (Student, Fresher, Professional, Founder, Recruiter)
  - Goal (Job Search, Personal Branding, Thought Leadership, Hiring, Networking)
  - Writing Style (Conversational, Corporate, Storytelling, Data-driven, Bold)

### 📊 Data-Driven Tone Adaptation
- Accepts **LinkedIn post data in JSON format**
- Processes and analyzes posts to learn:
  - Writing tone
  - Language patterns
  - Structural style
- Uses this processed data to **influence AI-generated posts**, making them more realistic and LinkedIn-native

### ✍️ Rewrite Assistant (Editor-like Experience)
- Improve Hook
- Strengthen CTA
- Shorten Post
- Make Tone Bolder
- Multi-step **Undo / Redo** support using state stacks

### 🎯 UX & Product Features
- Sidebar-based professional layout
- Stateful AI rewrites (no full regeneration)
- Disable invalid actions automatically
- Loading spinners & toast feedback
- Clean, distraction-free writing interface

---

## 🗂️ Project Structure

```
linkedin-post-generator/
│
├── data/
│   ├── raw_posts.json          # Raw LinkedIn posts dataset
│   └── processed_posts.json    # Cleaned & processed posts
│
├── backend/
│   ├── __init__.py             # Marks dir as a python package
│   └── few_shot.py             # Few-shot examples loader
│   └── llm_helper.py           # LLM abstraction & helpers
│   └── post_generator.py       # Core post generation logic
│   └── preprocess.py           # Data preprocessing pipeline
│   └── rewrite_post.py         # Rewrite engine (hook, CTA, shorten, bold)
│
├── state/
│   ├── session.py              # contain session state 
│
├── ui/
│   ├── sidebar.py              # renders sidebar
│   └── output.py               # show output
│
├── main.py                     # Streamlit application entry point
├── constants.py                # Contain lists of options for fields
│
├── .env                        # Environment variables
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🔄 LinkedIn Data Processing Pipeline

1. **Raw Data Ingestion**
   - LinkedIn posts are stored in `data/raw_posts.json`

2. **Preprocessing**
   - `preprocess.py` cleans and structures the raw data
   - Extracts tone, phrasing patterns, and writing style

3. **Processed Output**
   - Saved to `data/processed_posts.json`
   - Used during post generation as **few-shot / tone guidance**

4. **AI Generation**
   - While generating new posts, the system:
     - Considers user-selected options
     - Adapts tone & language based on processed LinkedIn data

This makes the generated posts **closer to real LinkedIn content**, not generic AI text.

---

## 🚀 How to Run Locally

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/linkedin-post-generator.git
cd linkedin-post-generator
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set Environment Variables
Create a `.env` file:
```
GROQ_API_KEY=your_api_key_here
```

### 5️⃣ Run the App
```bash
streamlit run main.py
```

---

## 🧪 Example Use Cases

- Freshers crafting job-search posts
- Professionals building personal brand
- Founders writing thought-leadership content
- Recruiters creating hiring posts
- Content creators experimenting with tone & style

---

## 🧠 What This Project Demonstrates

- Prompt engineering with layered constraints
- Stateful AI applications
- Undo/Redo logic using stack-based state
- Data-driven AI personalization
- Product-level UX thinking
- Clean modular architecture

---

## 📌 Future Enhancements
- Post quality scoring (hook, CTA, readability)
- Diff view for rewrites
- Draft saving & export
- Analytics-based engagement prediction

---

## 🤝 Contributing
Contributions, ideas, and improvements are welcome!  
Feel free to open issues or submit pull requests.

---

### ⭐ If you find this project useful, consider giving it a star!