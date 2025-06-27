import google.generativeai as genai

genai.configure(api_key="AIzaSyCnUtneVDAP2lsPlzbSfrkdzdDCGZMQckM")

model = genai.GenerativeModel("gemini-1.5-flash")

def ai_writer(text, prompt):
    try:
        response = model.generate_content(f"{prompt}\n\n{text}")
        return response.text
    except Exception as e:
        return f"[ERROR] {e}"
