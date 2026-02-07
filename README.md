# 🧮 DiscreteLab

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![Built with Rich](https://img.shields.io/badge/built%20with-rich-green.svg)](https://github.com/Textualize/rich)

**DiscreteLab** is a comprehensive Python-based toolkit for Discrete Mathematics and Cryptography. It provides a terminal-based interface to visualize logical operations and cryptographic transformations with high clarity and color-coded feedback.

---

## ✨ Features

### 1. Dynamic Truth Table Generator
* **Variable Support:** Handles any number of variables (e.g., $p, q, r, s, t$).
* **Logical Evaluation:** Uses Python's engine to evaluate complex boolean expressions.
* **Visual Output:** Uses the `Rich` library to render tables with 1/0 binary representation.

### 2. Cryptographic Algorithms
* **AES Implementation:** Modular AES logic located in `app/Cryptography_algos`.
* **Extensible Design:** Easily add new algorithms like RSA or Diffie-Hellman by following the modular folder structure.

---

## 🚀 Installation

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/AmRam841/DiscreteLab.git](https://github.com/AmRam841/DiscreteLab.git)
    cd DiscreteLab
    ```

2.  **Create a Virtual Environment:**
    ```bash
    python -m venv DiscreteLabVenv
    source DiscreteLabVenv/bin/activate  # Linux/macOS
    # .\DiscreteLabVenv\Scripts\activate  # Windows
    ```

3.  **Install Dependencies:**
    ```bash
    pip install rich
    ```

---

## 📖 Usage

Run the main application using:
```bash
python -m app

Logical Operator Cheat Sheet
When the script asks for a formula, use the following Python syntax:

Operator	Math Symbol	Python Syntax
AND	p∧q	p and q
OR	p∨q	p or q
XOR	p⊕q	p ^ q
NOT	¬p	not p
IF...THEN	p→q	not p or q
IFF (Equals)	p↔q	p == q

📂 Project Structure
Plaintext

DiscreteLab/
├── app/
│   ├── __main__.py             # Entry point
│   ├── Cryptography_algos/     # Crypto implementations
│   │   ├── __init__.py
│   │   └── AES.py
│   └── logic_tools.py          # Logic and table generation utilities
├── README.md                   # You are here
└── requirements.txt            # Project dependencies
🛠 Troubleshooting
If you encounter an ImportError regarding Console, ensure your imports in all files look like this:

Python

# CORRECT
from rich.console import Console

# INCORRECT
# from rich import Console
🤝 Contributing
Contributions are welcome! If you'd like to add a new discrete math tool or a crypto algorithm:

Fork the repo.

Create your feature branch.

Submit a Pull Request.
