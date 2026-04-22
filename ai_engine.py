import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

if not API_KEY:
    raise ValueError("❌ OPENROUTER_API_KEY not found in .env")

# Initialize client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=API_KEY,
)


def generate_ddr(structured_input: str) -> str:
    prompt = f"""
You are a senior building inspection expert specializing in moisture, leakage, and structural diagnostics.

Your task is to ANALYZE and COMBINE:
1. Inspection Report (visible defects)
2. Thermal Report (hidden moisture detection)

-------------------------------------
STRICT INSTRUCTIONS (FOLLOW ALL):
-------------------------------------

1. Use ONLY the provided data — DO NOT assume or invent anything.
2. Be SPECIFIC:
   - Mention exact areas (e.g., "Hall skirting level dampness")
   - Avoid vague terms like "some dampness"
3. Correlate thermal data:
   - Cold spots (~20–23°C) = moisture presence
   - Repeated cold spots = widespread issue
4. Avoid repetition — merge similar observations.
5. If information is missing → write "Not Available"
6. If conflicting information exists → clearly explain it
7. If no conflict → explicitly state:
   "No conflicting information observed"
8. Maintain technical clarity (professional tone)

-------------------------------------
OUTPUT FORMAT (STRICT):
-------------------------------------

### 1. Property Issue Summary
- High-level overview of all major problems

### 2. Area-wise Observations
For EACH area:
- Area Name
- Issue Description
- Evidence:
  - Inspection findings
  - Thermal correlation (with temperature values if available)
- [Insert Image: relevant description]

### 3. Probable Root Cause
- Clearly connect inspection + thermal findings
- Mention causes like:
  - Concealed plumbing leakage
  - Tile joint gaps
  - External wall cracks
  - Waterproofing failure

### 4. Severity Assessment
- Overall severity: Low / Medium / High
- Justify using:
  - Spread of issue
  - Thermal consistency
  - Structural impact risk

### 5. Recommended Actions
- Provide SPECIFIC technical solutions:
  - Re-grouting tile joints
  - Plumbing repair
  - Waterproofing treatment
  - Crack sealing

### 6. Additional Notes
- Any extra technical observations

### 7. Missing or Unclear Information
- Explicitly list missing fields (e.g., Customer Name, Age, etc.)
- If none missing → write "None"

-------------------------------------
IMPORTANT:
-------------------------------------
- Do NOT generate generic answers
- Do NOT repeat same issue across multiple areas unnecessarily
- Keep output structured and readable

-------------------------------------
DATA:
-------------------------------------
{structured_input}
"""

    try:
        response = client.chat.completions.create(
            model="openai/gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a precise and strict technical report generator."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.1  # lower = more accurate, less creative
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"❌ Error generating DDR: {str(e)}"