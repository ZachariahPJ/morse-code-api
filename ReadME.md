# Text ↔ Morse Code Converter API
**Task 1B - Medium Level Submission**

This project is a robust RESTful API built with **Python** and **FastAPI** that performs bidirectional conversion between plain text and International Morse Code. It features automatic input type detection and interactive documentation.


## Live API Endpoint
* **Base URL:** [https://morse-code-api-moneybois.onrender.com]
* **Interactive Docs (Swagger UI):** [https://morse-code-api-moneybois.onrender.com/docs]

## Key Features
* **Bidirectional Conversion:** Seamlessly converts Text-to-Morse and Morse-to-Text through a single endpoint.
* **Automatic Detection:** The system intelligently identifies if the input is plain text or Morse code based on the character set.
* **Interactive Documentation:** Fully documented using Swagger UI, allowing for easy testing without external tools.
* **Robust Error Handling:** Unsupported characters are replaced with `?` to ensure stability.


## Tech Stack
* **Language:** Python 3.x
* **Framework:** FastAPI
* **Server:** Uvicorn
* **Data Handling:** Python-multipart (Form Data)


## ⚙️ Working Principle

### 1. Request Handling
The API exposes a single `POST` endpoint: `/translate`. It accepts data via **Form URL Encoded** format. This ensures compatibility with standard HTML forms and API testing tools.

### 2. Input Identification
Upon receiving a request, the logic inspects the input string:
* If the string contains **only** characters from the set `{'.', '-', '/', ' '}`, it is identified as **Morse Code**.
* If it contains any other characters (A-Z, 0-9, etc.), it is identified as **Plain Text**.

### 3. Conversion Logic
* **Text → Morse:** The input is normalized to uppercase. Each character is mapped to its Morse equivalent using a dictionary lookup ($O(1)$ complexity). Letters are separated by spaces.
* **Morse → Text:** The string is split by `" / "` to separate words, then by `" "` to separate letters. These sequences are reverse-mapped to their alphanumeric equivalents.

**Mapping Reference:** Mapping Reference is provided in API.


## Local Setup Guide

1.  **Clone the repository**
    ```bash
    git clone <your-repo-url>
    cd <your-folder-name>
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Server**
    ```bash
    uvicorn main:app --reload
    ```

4.  **Test the API**
    Open your browser to: `http://127.0.0.1:8000/docs`


## 📖 API Usage Guide

### Endpoint: `/translate`
* **Method:** `POST`
* **Content-Type:** `application/x-www-form-urlencoded`

#### Example 1: Text to Morse
**Request:**
* **Field:** `content`
* **Value:** `HELLO WORLD`

**Response:**
```json
{
  "original": "HELLO WORLD",
  "translated": ".... . .-.. .-.. --- / .-- --- .-. .-.. -..",
  "direction": "text_to_morse"
}
```

#### Example 2: Morse to Text
**Request:**
* **Field:** `content`
* **Value:** `... --- ...`

**Response:**
```json
{
  "original": "... --- ...",
  "translated": "SOS",
  "direction": "morse_to_text"
}
```
### Below are the screenshots demonstrating successful API calls, as required for validation.
### Execution Proof

Here is the screenshot of the TEXT TO MORSE:
![TEXT TO MORSE Screenshot](images/text_to_morse.png)

Here is the screenshot of the MORSE TO TEXT:
![MORSE TO TEXT Screenshot](images/morse_to_text.png)