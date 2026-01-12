from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI(
    title="Morse Code Web App",
    description="A web-based application to convert Text to Morse and vice versa.",
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
    """Converts text to Morse code."""
    return ' '.join(MORSE_CODE_DICT.get(char.upper(), '?') for char in text)

def morse_to_text(morse: str) -> str:
    """Converts Morse code to text."""
    words = morse.split(' / ') 
    decoded_words = []
    for word in words:
        decoded_chars = "".join(REVERSE_DICT.get(char, '?') for char in word.split())
        decoded_words.append(decoded_chars)
    return " ".join(decoded_words)

# --- Frontend (HTML/CSS) ---
def get_html_page(input_text="", output_text=""):
    # If output is empty, show a placeholder
    display_text = output_text if output_text else '<span style="color: #888; font-style: italic;">Translation will appear here...</span>'
    
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Morse Code Converter</title>
        <style>
            body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; max-width: 800px; margin: 0 auto; padding: 40px; background-color: #f0f2f5; }}
            .container {{ background: white; padding: 40px; border-radius: 12px; box-shadow: 0 8px 16px rgba(0,0,0,0.1); }}
            h1 {{ text-align: center; color: #2c3e50; margin-bottom: 30px; }}
            
            .input-group {{ margin-bottom: 25px; }}
            label {{ display: block; font-weight: 600; margin-bottom: 8px; color: #34495e; }}
            textarea {{ width: 100%; height: 120px; padding: 15px; border: 2px solid #dfe6e9; border-radius: 8px; font-size: 16px; font-family: monospace; resize: vertical; box-sizing: border-box; transition: border-color 0.3s; }}
            textarea:focus {{ border-color: #3498db; outline: none; }}
            
            button.convert-btn {{ display: block; width: 100%; padding: 15px; background-color: #3498db; color: white; border: none; border-radius: 8px; font-size: 18px; font-weight: bold; cursor: pointer; transition: background-color 0.2s; }}
            button.convert-btn:hover {{ background-color: #2980b9; }}
            
            .output-group {{ margin-top: 30px; padding-top: 20px; border-top: 1px solid #eee; }}
            .result-box {{ background-color: #e8f5e9; border: 2px dashed #2ecc71; border-radius: 8px; padding: 20px; min-height: 80px; font-size: 18px; font-family: monospace; color: #2d3436; word-wrap: break-word; }}
            
            /* The Chart Image Style */
            img {{ display: block; margin: 0 auto 30px; max-width: 100%; border-radius: 8px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Text <span style="color:#3498db">↔</span> Morse App</h1>
            
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/International_Morse_Code.svg/630px-International_Morse_Code.svg.png" alt="Morse Chart">

            <form action="/" method="post">
                <div class="input-group">
                    <label for="content">Enter Text or Morse Code:</label>
                    <textarea id="content" name="content" placeholder="Type here (e.g. 'Hello' or '.... .')...">{input_text}</textarea>
                </div>
                
                <button type="submit" class="convert-btn">Translate Message</button>
            </form>
            
            <div class="output-group">
                <label>Result:</label>
                <div class="result-box">{display_text}</div>
            </div>
        </div>
    </body>
    </html>
    """

# --- Routes ---
@app.get("/", response_class=HTMLResponse)
async def read_root():
    """Serves the blank Web App interface."""
    return get_html_page()

@app.post("/", response_class=HTMLResponse)
async def process_form(content: str = Form(...)):
    """Handles the form submission and returns the page with results."""
    data = content.strip()
    
    # Auto-detect Morse (contains only dots, dashes, slashes, spaces)
    is_morse = all(c in ".-/ " for c in data)
    
    if is_morse:
        result = morse_to_text(data)
    else:
        result = text_to_morse(data)
        
    # Return the HTML page with the Input AND the Output filled in
    return get_html_page(input_text=data, output_text=result)