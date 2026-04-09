import google.generativeai as genai

genai.configure(api_key="AIzaSyCkgtRr5Xj9ZQ8VUyq_Obe9_qhtw-bFD5E")

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Hello")

print(response.text)
