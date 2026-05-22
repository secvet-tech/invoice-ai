import os
import functions_framework
import google.generativeai as genai

api_key = os.environ.get('gemlock-invoices')
genai.configure(api_key=api_key)

@functions_framework.http
def process_invoice(request):
    if not api_key:
        return "Error: API Key not found.", 500

    model = genai.GenerativeModel('gemini-1.5-flash')

    try:
        # prompt = "Extract the name and email."
        # response = model.generate_content([prompt, image_data])
        return "API Key detected! Ready for processing.", 200
    except Exception as e:
        return f"Error: {str(e)}", 500

