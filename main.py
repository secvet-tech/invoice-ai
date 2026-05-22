import os
import functions_framework
import google.generativeai as genai

# Use the exact environment variable name you set in GCP
api_key = os.environ.get('gemlock-invoices')
genai.configure(api_key=api_key)

@functions_framework.http
def process_invoice(request):
    if not api_key:
        return "Error: API Key environment variable not found.", 500

    # Initialize the model (Gemini 1.5 Flash is great for invoices)
    model = genai.GenerativeModel('gemini-1.5-flash')

    # Example: Processing a public image URL or base64 from the request
    # For now, we'll just verify the setup
    try:
        # prompt = "Extract the total amount and vendor name from this invoice."
        # response = model.generate_content([prompt, image_data])
        return "API Key detected! Ready for processing.", 200
    except Exception as e:
        return f"Error: {str(e)}", 500

