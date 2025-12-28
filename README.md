# Codeforces Tag Analysis by Rating

A Python-based data analysis project that explores the distribution of **problem tags on Codeforces** across different **difficulty (rating) ranges**.  
This tool helps competitive programmers understand which topics appear most frequently at each level and plan more focused practice.

---

## 📌 Project Overview

Codeforces provides thousands of programming problems labeled with difficulty ratings and topic tags.  
This project fetches live problem data from the **Codeforces Public API**, groups problems into predefined rating buckets (0–2100), and analyzes how frequently each tag appears within those buckets.

The results are presented both as **console statistics** and **visual bar charts** for easy interpretation.

---

## ✨ Features

- Fetches real-time problem data from the Codeforces API
- Categorizes problems into rating ranges:
  - 0–1000
  - 1000–1300
  - 1300–1600
  - 1600–1900
  - 1900–2100
- Counts tag frequencies for each rating bucket
- Displays:
  - Top tags per difficulty level (console output)
  - Bar chart visualizations using Matplotlib
- Helps identify topic trends across difficulty levels

---

## 🛠️ Tech Stack

- **Python 3**
- **Requests** – API calls
- **Matplotlib** – Data visualization
- **Collections** – Efficient counting with `Counter` and `defaultdict`

---

## 📂 Project Structure

codeforces-tag-analysis/ │ ├── main.py            # Main analysis script ├── README.md          # Project documentation └── requirements.txt   # Python dependencies (optional)

---

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/codeforces-tag-analysis.git
   cd codeforces-tag-analysis

2. Install dependencies

pip install requests matplotlib


3. Run the script

python main.py




---

📊 Sample Output

Console Output
- Total tag occurrences per rating bucket
- Top 10 most frequent tags for each difficulty level


Visualization

Bar charts showing the top N tags for each rating range



---

📈 Use Cases

- Competitive programmers planning topic-wise practice
- Analyzing trends in problem difficulty
- Educational insights for CP coaching or curriculum planning
- Data analysis / data mining academic projects



---

🚀 Future Improvements

- Export results to CSV or JSON
- Interactive visualizations (Plotly / Seaborn)
- Filter analysis by specific tags
- Extend rating range beyond 2100
- Web dashboard for interactive exploration
