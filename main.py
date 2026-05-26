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
#we set headers
    headers = {
        'Access-Control-Allow-Origin':'*',
        'Access-Control-Allow-Methods':'POST, OPTIONS',
        'Access-Control-Allow-Headers':'Content-Type'
    }
    if request.method == 'OPTIONS':
        return ('', 204, headers)        
    if not api_key:
        return "Error: API Key ('gemlock-invoices') not found in environment variables.", 500
    request_json = request.get_json(silent=True)
#check for error    
    if not request_json or 'data' not in request_json:
        return "Error: Invalid request. JSON with 'data' (base64) field required.", 400
#we get data
    file_data = request_json['data']
    mime_type = request_json.get('mime_type', 'application/pdf')
#init gem
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = """
    Extract the information from this document:
    - Name
    - Number
    - Email
    - Home State
    - Job
    Return the result as a valid JSON object.
    """
    try:
        image_part = {
            "mime_type": mime_type,
            "data": file_data
        }
        response = model.generate_content([prompt, image_part])
        return response.text, 200, headers
    except Exception as e:
        return f"Error processing invoice: {str(e)}", 500
