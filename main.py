from fastapi import FastAPI, Form

# --- Configuration & Documentation ---
description_text = """
### API Documentation
This API converts plain text to Morse code and vice versa.

### Morse Code Reference Chart
Below is the mapping scheme used for this API:

![Morse Code Chart](https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/International_Morse_Code.svg/315px-International_Morse_Code.svg.png)
"""

app = FastAPI(
    title="Morse Code Converter",
    description=description_text,
    version="1.0.0"
)

# --- Logic & Dictionaries ---
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..',
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': '/'
}

REVERSE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}

def text_to_morse(text: str) -> str:
    """Converts text to Morse code, separating letters with spaces."""
    return ' '.join(MORSE_CODE_DICT.get(char.upper(), '?') for char in text)

def morse_to_text(morse: str) -> str:
    """Converts Morse code to text. Handles ' / ' as word separators."""
    words = morse.split(' / ') 
    decoded_words = []
    for word in words:
        decoded_chars = "".join(REVERSE_DICT.get(char, '?') for char in word.split())
        decoded_words.append(decoded_chars)
    return " ".join(decoded_words)

# --- API Endpoints ---
@app.post("/translate")
async def translate(content: str = Form(...)):
    """
    Receives a string and automatically detects if it is Morse code or Text.
    Returns the translated result and the detection direction.
    """
    data = content.strip()
    
    # Automatic Detection: Morse usually only contains '.', '-', '/', and spaces
    is_morse = all(c in ".-/ " for c in data)
    
    if is_morse:
        result = morse_to_text(data)
        direction = "morse_to_text"
    else:
        result = text_to_morse(data)
        direction = "text_to_morse"
        
    return {
        "original": data,
        "translated": result,
        "direction": direction
    }