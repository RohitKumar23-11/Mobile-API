import requests
import google.generativeai as genai
import urllib.parse

# Function to fetch phone models based on SoC
def get_latest_phones(soc_name):
    """
    Fetch the latest phone models from the GSMArena API via RapidAPI for a given SoC.
    """
    soc_encoded = urllib.parse.quote(soc_name)  # Encode SoC name for URL
    url = f"https://gsmarenaparser.p.rapidapi.com/api/values/devicesbysoc/{soc_encoded}"

    headers = {
        "X-RapidAPI-Key": "YOUR_RAPIDAPI_KEY",  # 🔹 Replace with your actual API Key
        "X-RapidAPI-Host": "gsmarenaparser.p.rapidapi.com"
    }

    try:
        response = requests.get(url, headers=headers)
        print(f"API Response Status: {response.status_code}")  # Debugging
        print(f"API Response: {response.text}")  # Debugging

        if response.status_code == 403:
            return ["Error: Access Denied (403). Check API key or subscription."]

        response.raise_for_status()  # Raise exception for 4xx/5xx responses
        phone_data = response.json()
        
        return [phone.get("name", "Unknown Model") for phone in phone_data.get("data", [])]
    except requests.exceptions.RequestException as e:
        print(f"Error fetching phone data: {e}")
        return ["Could not fetch the latest phone models."]
    except (ValueError, KeyError) as e:
        print(f"Error parsing phone data: {e}")
        return ["Could not parse phone data correctly."]

# Function to check if user is asking for latest phones
def ai_understand_query(user_input):
    """
    Use Google Gemini AI to determine if the query asks about new phone models.
    """
    genai.configure(api_key="AIzaSyBReedK0QcsRL8V2dnEJAHDJl3Sf6YctKI")  # 🔹 Replace with actual API Key
    model = genai.GenerativeModel("gemini-1.5-pro-latest")  # Ensure correct model

    prompt = f"""
    User Query: "{user_input}"
    Does this query ask for the latest phone models? Answer only with 'yes' or 'no'.
    """

    try:
        response = model.generate_content(prompt)
        return response.text.strip().lower()
    except Exception as e:
        print(f"Error during Gemini API call: {e}")
        return "no"

# Chatbot Response Function
def chatbot_response(user_input, soc_name="Snapdragon 8 Gen 3"):
    """
    Process user input, determine if it asks about new phones, and respond.
    """
    ai_decision = ai_understand_query(user_input)

    if ai_decision == "yes":
        latest_phones = get_latest_phones(soc_name)
        response = f"Here are the latest phone models with {soc_name}:\n- " + "\n- ".join(latest_phones)
    else:
        response = "I'm here to assist! Ask me about the latest phone models."

    return response

# Example Usage:
user_query = "What’s the latest phone model?"
print(chatbot_response(user_query, "Snapdragon 8 Gen 3"))  # Replace with any SoC
