# Mobile-API

### **📌 Code Explanation (Short & Simple)**

This is a Python program for **chatbot** that do the basic things like:\
✅ Uses **Google Gemini AI** to analyze user queries.\
✅ Fetches **latest phone models** based on a given **SoC (Processor)** using **GSMArena API (RapidAPI)**.

---

### **🔹 Breakdown of the Code**

1️⃣ **`get_latest_phones(soc_name)`**

- Takes a **SoC name** (e.g., "Snapdragon 8 Gen 3").
- Calls **GSMArena API** to get **latest phones** using that processor.
- Handles API errors (e.g., invalid key, access denied).

2️⃣ **`ai_understand_query(user_input)`**

- Uses **Google Gemini AI** to check if the user **asked about new phones**.
- If AI detects a relevant question → Returns **"yes"**, otherwise **"no"**.

3️⃣ **`chatbot_response(user_input, soc_name)`**

- Calls **AI function** to analyze the query.
- If AI says **"yes"** → Fetches latest phones using `get_latest_phones()`.
- Otherwise, responds **"Ask me about latest phone models"**.

4️⃣ **Execution**

- Example query: `"What’s the latest phone model?"`
- Calls `chatbot_response("What’s the latest phone model?", "Snapdragon 8 Gen 3")`.
- If API key & subscription are valid, it returns a list of latest phones.

---

### \*\*🚀 API Keys \*\*

🔴 **API Keys**

- 02d55bf0e4msh1a7610ad4ad2d5bp1ae9b6jsnbc8251d5969c → It is \*\*Our RapidAPI key\*\*.
- AIzaSyBReedK0QcsRL8V2dnEJAHDJl3Sf6YctKI → It is the Google gemini API Key.

🔴 **Check API Subscription**

- `403 Forbidden` means you're **not subscribed** to the API.
- Subscribe via [RapidAPI](https://rapidapi.com/).
- Because My bank name and my card details is not accepted by the **RapidAPI Site** therefore I am unable to use the API for Mobile phone details.
- I attach the screenshot of my output which shows that I am not able to use the API.
