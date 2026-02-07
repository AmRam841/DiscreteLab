

# DiscreteLab

**DiscreteLab** is a Python CLI-based educational lab for demonstrating core **discrete mathematics** and **security concepts**. It provides hands-on modules for logic, cryptography, graph theory, and file encryption. This project was developed as a university learning and demonstration tool.

---

## 🚀 Features

### 1. Truth Table Generator
- Accepts variables (comma-separated) and a Python-style boolean formula.
- Evaluates all combinations of variables and renders a formatted table in terminal output using Rich.

### 2. RSA Educational Demo (Weak Parameters)
- Generates intentionally weak RSA parameters or allows manual weak value entry.
- Includes attack demonstrations:
  - Small Prime Factorization
  - Fermat Factorization
  - Low Exponent Attack (`m^e < n` scenario)

### 3. Graph Module
- Visualizes sampled Facebook graph edge lists.
- Generates random directed weighted graphs for shortest-path experimentation.
- Algorithms supported: Dijkstra, Bellman-Ford, BFS-style shortest path, Floyd-Warshall.

### 4. AES File Encryption/Decryption
- AES-CBC file encryption with PBKDF2-derived key.
- Reads/writes files in chunks (4096 bytes).
- Prepends salt + IV to encrypted file for proper decryption.

---

## 📁 Project Structure

```text
DiscreteLab/
├── LICENSE
├── README.md
├── docs/
│   └── README.md
└── app/
    ├── main.py
    ├── requirements.txt
    ├── facebook_combined.txt
    ├── logic/
    │   └── TruthTable.py
    ├── Cryptography_algos/
    │   ├── AES.py
    │   └── rsa.py
    └── GraphModels/
        ├── graph.py
        ├── facebook_combined.txt
        └── graph_with_menu.html
````

---

## ⚙️ Requirements

Install dependencies via pip:

```bash
pip install -r app/requirements.txt
```

**Dependencies:**

* typer
* questionary
* sympy
* pycryptodome
* networkx
* pandas
* pyvis

---

## 🏃 Running the Application
For people who downloaded the Pyinstaller Version :
Go to the Directory of The downloaded File called __main__
```bash     
./__main__
```
From the repository root:

```bash
python app/main.py interactive-menu
```

> **Note:** Typer converts function names to CLI command names (e.g., `interactive_Menu` → `interactive-menu`).

---

## 📌 Module Usage

### Truth Table

* Select option 1 in interactive menu.
* Input variables (e.g., `q,r`) and a formula (e.g., `q or r`).
* Output renders as a Rich table with `1` (True) / `0` (False).

### RSA Educational Demo

* Select option 2.
* Choose weak parameter generation:

  * `y` → random weak primes
  * `n` → manual weak values
* Optional attacks:

  1. Small Prime Attack
  2. Fermat Factorization
  3. Low Exponent Attack

### Graph Module

* Select option 3.
* Options:

  1. Graph visualizer on sampled Facebook edges.
  2. Shortest-path mode on random graph.
* In shortest-path mode:

  * Choose algorithm
  * Enter start and end node IDs
  * Receive path and distance

### AES Encryption/Decryption

* Select option 4.
* Choose `e` (encrypt) or `d` (decrypt)
* Enter password
* Select input file (via questionary path picker)
* Provide output filename

---

## ⚠️ Security / Educational Notice

* RSA module intentionally uses **weak values** for demonstration and attacks. **Not production-grade cryptography.**
* AES uses **CBC + PBKDF2**; password correctness and file integrity are required.
* Truth table evaluation uses `eval` — do **not** input untrusted formulas.

---

## 📝 Known Caveats

* Some menu or variable names contain minor typos.
* Graph visualizer requires `facebook_combined.txt` in working directory.
* Floyd-Warshall path reconstruction may need custom handling depending on NetworkX version.
* Input validation and error handling can be expanded.

---

## 📚 License

This project is licensed under **Apache License 2.0** — see [LICENSE](LICENSE).

---

## 🔧 For Developers / Contributors

* Core modules are located under `app/`:

  * `logic/TruthTable.py`
  * `Cryptography_algos/rsa.py` and `AES.py`
  * `GraphModels/graph.py`
* CLI orchestration: `app/main.py` using Typer + Rich.
* Graph visualizations use PyVis + NetworkX.
* RSA demo demonstrates:

  * Weak prime generation
  * Small exponent attacks
  * Fermat factorization

---

## 💡 Recommendations / Improvements

1. Replace `eval` with a safe logic parser.
2. Add input validation for all numeric/CLI inputs.
3. Standardize naming and menu labels.
4. Add unit tests for:

   * Truth tables
   * RSA attack functions
   * AES round-trip encryption/decryption
   * Graph algorithms
5. Add reproducibility flags (fixed random seeds).
6. Separate CLI from core logic for easier testing.

```


