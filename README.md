# 🏠 AI DDR Report Generator

An AI-powered system that generates a **Detailed Diagnostic Report (DDR)** by analyzing:

- 📄 Inspection Report (visible issues)
- 🌡️ Thermal Report (hidden moisture detection)

---

## 🚀 Project Overview

In real-world building inspections, reports are often:

- Unstructured  
- Repetitive  
- Hard to analyze  

This project solves that problem by building an **AI pipeline** that:

1. Extracts data from PDFs  
2. Structures information area-wise  
3. Combines inspection + thermal insights  
4. Generates a clean, professional DDR report  

---

## 🧠 How It Works (Pipeline)

- PDF Input  
  ↓  
- Text + Image Extraction (PyMuPDF)  
  ↓  
- Data Structuring (Area-wise grouping)  
  ↓  
- AI Processing (OpenAI / GPT)  
  ↓  
- DDR Report Generation  
  ↓  
- Image Mapping  

---

## ⚙️ Key Features

- 📄 Extracts text and images from PDFs  
- 🏠 Identifies issues by area (Hall, Bedroom, Bathroom, etc.)  
- 🌡️ Uses thermal data to detect hidden moisture  
- 🧠 Correlates cold spots (~20–23°C) with dampness  
- 🧹 Removes duplicate and noisy data  
- 📊 Generates structured, professional DDR report  
- 📸 Maps images to relevant areas  

---

## 🛠️ Tech Stack

- **Python**
- **PyMuPDF (fitz)** → PDF extraction  
- **OpenAI (via OpenRouter)** → AI reasoning  
- **OS / File Handling**  

---

## ▶️ How to Run

### 1. Install dependencies
```bash

pip install -r requirements.txt

```

2. Add your API key

Create a .env file and add:

OPENROUTER_API_KEY=your_api_key_here

3. Run the project

python test.py

📄 Output

After running, you will get:

outputs/ddr_report.md → Final DDR report
Extracted images → Auto-saved in outputs/ folder

📸 Sample Output Includes
Property Issue Summary
Area-wise Observations
Root Cause Analysis
Severity Assessment
Recommended Actions
Supporting Images

🧠 Key Intelligence Used
Combines visible defects + thermal evidence
Detects hidden moisture using cold spots (~20–23°C)
Identifies root causes like:
Plumbing leakage
Tile joint gaps
External wall cracks
Waterproofing failure

⚠️ Limitations
Image-to-area mapping is heuristic (based on page logic)
Thermal analysis is global (not room-specific)
No advanced conflict detection between reports

🎥 Demo Video
https://www.loom.com/share/ef990fcc6ac94033b74bbcf416af74d6

---
