```markdown
# GEN-AI PROJECT: AI-Powered LinkedIn Post Generator

Transform your ideas, projects, and experiences into polished, engaging LinkedIn posts using AI.  
This tool helps students and professionals quickly create high-quality posts with the right tone, structure, and hashtags.

---

## 🚀 Overview  
This project generates LinkedIn-ready posts based on:
- A topic or idea  
- Desired tone (professional, friendly, storytelling, etc.)  
- Desired length  
- (Optional) Your previous posts for style-learning  

It uses prompt-engineered LLMs and simple preprocessing to analyse your writing style and generate consistent, human-like posts.

---

## 📁 Project Structure
```


linkedin-post-generator/
│
├── data/
│   ├── raw_posts.json           # Original LinkedIn posts for style training
│   └── processed_posts.json     # Cleaned & preprocessed posts
│
├── few_shot.py                  # Few-shot examples for the LLM
├── llm_helper.py                # Handles AI model API calls
├── main.py                      # Main entry point of the application
├── post_generator.py            # Core post generation & prompt logic
├── preprocess.py                # Text cleaning & style extraction
│
├── requirements.txt             # Dependencies
└── README.md                    # Documentation

```



````

---

## 🔧 Installation & Setup

1. Clone the repository:
```bash
git clone https://github.com/your-username/linkedin-post-generator.git
cd linkedin-post-generator
````

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Add your API key in an `.env` file:

```
API_KEY=your_model_api_key
```

---

## ▶️ How to Run

Run the main script:

```bash
python main.py
```

You will be asked for:

* Topic / idea
* Preferred tone
* Length (short / medium / long)
* Whether you want to use your writing style from `raw_posts.json`

The script then generates:

* A well-formatted LinkedIn post
* Suggested hashtags
* Optional variations

---

## 🧠 How It Works

### 1. **Preprocessing**

`preprocess.py` cleans your previous posts:

* Removes links, emojis, unnecessary whitespace
* Splits long posts
* Stores the processed text

### 2. **Few-Shot Prompting**

`few_shot.py` contains handcrafted examples that show the model *how a good LinkedIn post looks*.

### 3. **LLM Interaction**

`llm_helper.py`:

* Builds the final prompt
* Calls the AI model
* Handles temperature, max tokens, safety

### 4. **Post Generation**

`post_generator.py`:

* Combines topic + tone + user style + few-shot examples
* Generates structured text with paragraphs and hashtags

---

## ✨ Example Input

```
Topic: My experience building a GenAI project
Tone: Semi-professional
Length: Medium
Use past posts? Yes
```

### Example Output (excerpt)

> Built my first GenAI project, and the journey completely changed the way I look at AI-powered workflows...
>
> Here are 3 things I learned 👇
> • Importance of prompt structure
> • Breaking tasks into modular components
> • Testing with real-world user scenarios
>
> #AI #GenAI #MachineLearning #StudentProjects

---

## 🛠 Future Enhancements

* Web UI / Streamlit interface
* Auto-post to LinkedIn using LinkedIn API
* Mood-based tone detection
* Multi-platform support (Twitter, Instagram captions)


---

## 🤝 Contributing

Feel free to open issues, suggest features, or improve prompt engineering.

---

## 📜 License

MIT License


~Kshitija Chindarkar 
#   A I - L i n k e d I N - p o s t - G e n e r a t o r 
 
 

