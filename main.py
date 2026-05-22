import os
import functions_framework
import google.generativeai as genai

# This line pulls your secret from the GCP environment
api_key = os.environ.get('gemlock-invoices')

# Configure the Gemini library with your key
genai.configure(api_key=api_key)

@functions_framework.http
def process_invoice(request):
    # Quick sanity check: If the key is missing, return an error
    if not api_key:
        return "Error: GEMINI_API_KEY environment variable is not set.", 500
    
    # ... your Gemini logic here ...
    return "API Key detected! Ready for processing."

