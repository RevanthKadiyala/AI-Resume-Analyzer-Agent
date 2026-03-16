import openai

openai.api_key = "YOUR_API_KEY"

def analyze_resume(resume_text):
    prompt = f"""
    Analyze the following resume and provide:

    1. Strengths
    2. Weaknesses
    3. Suggestions for improvement

    Resume:
    {resume_text}
    """

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


resume = input("Paste your resume:\n")

analysis = analyze_resume(resume)

print("\nResume Feedback:\n")
print(analysis)
