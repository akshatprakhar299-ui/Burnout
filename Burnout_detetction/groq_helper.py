from groq import Groq

import os

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def get_ai_analysis(
    study_hours,
    sleep_hours,
    screen_time,
    breaks_taken,
    burnout_score,
    productivity_score,
    fake_productivity
):

    prompt = f"""
You are an expert student wellness and productivity advisor.

Analyze the following student data:

Study Hours: {study_hours}
Sleep Hours: {sleep_hours}
Screen Time: {screen_time}
Breaks Taken: {breaks_taken}

Burnout Score: {burnout_score}/100
Productivity Score: {productivity_score}/100
Fake Productivity Risk: {fake_productivity}

Generate a report in this format:

🧠 Burnout Analysis
(Explain burnout risk)

📈 Productivity Analysis
(Explain productivity level)

🎭 Fake Productivity Analysis
(Explain whether planning exceeds execution)

🎯 Action Plan
(Give 3-5 practical actions)

Keep the response concise, professional and student-friendly.
"""

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return completion.choices[0].message.content