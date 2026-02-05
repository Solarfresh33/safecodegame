# 🔐 SafeCodeGame

A simple Flask-based code-guessing game designed to demonstrate brute-force attack concepts.

## 🎮 About

This project is an educational game where:
- A **3-digit secret code** (each digit 0-9) is randomly generated when the server starts
- Players try to guess the combination through a web interface
- A brute-force script demonstrates how weak codes can be cracked

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- pip

### Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Game

Start the Flask server:
```bash
python app.py
```

Then open your browser at: http://127.0.0.1:5000

## 🔓 Brute Force Demo

The `bruteforce.py` script demonstrates how a simple 3-digit code can be cracked by trying all 1,000 possible combinations (000-999).

To run it (while the server is running):
```bash
python bruteforce.py
```

## 📁 Project Structure

```
safecodegame/
├── app.py           # Flask application
├── bruteforce.py    # Brute-force attack script
├── requirements.txt # Python dependencies
├── templates/
│   ├── index.html   # Main game page
│   └── win.html     # Victory page
└── README.md
```

## ⚠️ Educational Purpose

This project is for **educational purposes only** to understand:
- How brute-force attacks work
- Why short numeric codes are insecure
- The importance of rate limiting and account lockouts

## 📝 License

This project is open source and available for learning purposes.
