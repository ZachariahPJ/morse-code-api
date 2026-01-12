# 📡 Text ↔ Morse Code Web App

We built a full-stack web app that translates **Text to Morse Code** (and back again) instantly. It’s powered by **FastAPI** on the backend and currently running live on **Render**.

### 🔗 Try it out
**Live App:** 👉 **[https://morse-code-api-moneybois.onrender.com/](https://morse-code-api-moneybois.onrender.com/)**

---

### ⚡ What it does
Instead of just a basic script, we turned this into a proper web interface.
* **Smart Detection:** You don't need to select a mode. Just type "Hello" or "... --- ..." and the app figures out which way to translate.
* **Web UI:** Clean HTML/CSS interface so you don't have to use raw API calls.
* **Documentation:** If you prefer the API view, the Swagger docs are auto-generated at `/docs`.

---

### 📸 Proof it works
We tested it with the classic "Hello World" example.

**1. Text → Morse**
*(Input: "Hello World")*
![Text to Morse](images/text_to_morse.png)

**2. Morse → Text**
*(Input: ".... . .-.. .-.. --- / .-- --- .-. .-.. -..")*
![Morse to Text](images/morse_to_text.png)

---

### 🛠️ The Stack
* **Backend:** Python 3.9 + FastAPI
* **Server:** Uvicorn
* **Hosting:** Render (Cloud)

---

### 💻 Run it locally
If you want to test this on your own machine:

1.  **Clone the repo:**
    ```bash
    git clone [https://github.com/ZachariahPJ/morse-code-api.git](https://github.com/ZachariahPJ/morse-code-api.git)
    cd morse-code-api
    ```

2.  **Get the requirements:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Launch:**
    ```bash
    uvicorn main:app --reload
    ```