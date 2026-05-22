import os
import functions_framework
import google.generativeai as genai
from google.ai.generativelanguage_v1beta.types import content
#we config key
api_key = os.environ.get('gemlock-invoices')
if api_key:
    genai.configure(api_key=api_key)
#we set up the req and check key exists
@functions_framework.http
def process_invoice(request):
    if not api_key:
        return "Error: API Key ('gemlock-invoices') not found in environment variables.", 500
    request_json = request.get_json(silent=True)
#check for error    
    if not request_json or 'data' not in request_json:
        return "Error: Invalid request. JSON with 'data' (base64) field required.", 400
#we get data
    file_data = request_json['data']
    mime_type = request_json.get('mime_type', 'image/jpeg') # Default to jpeg if missing
#init gem
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = """
    Extract the following vendor information from this invoice:
    - Vendor Name
    - Invoice Date
    - Total Amount
    - Tax Amount
    Return the result as a valid JSON object.
    """
    try:
        image_part = {
            "mime_type": mime_type,
            "data": file_data
        }
        response = model.generate_content([prompt, image_part])
        return response.text, 200
    except Exception as e:
        return f"Error processing invoice: {str(e)}", 500
