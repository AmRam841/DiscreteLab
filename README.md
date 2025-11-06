# DiscreteLab
A Project for my uni , read the ReadMe for more info ! 




Ah, now it makes sense. Let me explain clearly:

When I said **“Infra team makes this folder structure and writes the setup docs”**, I meant **two separate but related tasks** for your Infra team during the Bootcamp phase:

---

### 1️⃣ Folder Structure

* The Infra team **creates the skeleton of the project** — all the directories and empty files that other teams will use.
* They do **not write algorithms or UI yet**; they just make sure there’s a place for everything.
* Example folders they would create:

```
discretelab/
├── backend/                      <-- Backend code & Dockerfile
│   ├── app/                      <-- FastAPI app code
│   │   ├── main.py               <-- Entry point of the backend
│   │   ├── api/                  <-- API route definitions
│   │   │   └── routes_graphs.py  <-- Graph endpoints (BFS, Dijkstra stub)
│   │   ├── algorithms/           <-- Actual algorithm implementations
│   │   │   ├── bfs.py
│   │   │   ├── dijkstra.py
│   │   │   └── rsa.py
│   │   ├── models/               <-- Pydantic models for request/response
│   │   │   └── graph.py
│   │   └── core/                 <-- Config + constants
│   │       └── config.py
│   ├── tests/                     <-- Unit tests for backend code
│   │   └── test_health.py
│   ├── requirements.txt           <-- Python dependencies
│   └── Dockerfile                 <-- Instructions to build backend container
│
├── frontend/                      <-- Frontend code & Dockerfile
│   ├── src/                       <-- React/Vite app source
│   │   ├── main.tsx               <-- Entry point for React
│   │   ├── App.tsx
│   │   └── components/            <-- Reusable UI components
│   ├── package.json               <-- Node dependencies
│   └── Dockerfile                 <-- Instructions to build frontend container
│
├── docs/                          <-- Project documentation
│   ├── README.md                  <-- How to run project, conventions
│   └── learning/                  <-- Math & CS guides
│       ├── bfs.md
│       ├── dijkstra.md
│       ├── nfa.md
│       ├── dfa.md
│       ├── pascal.md
│       └── rsa.md
│
├── docker-compose.yml             <-- Orchestrates frontend + backend
└── .gitignore                     <-- Ignore unnecessary files for Git



### 2️⃣ Setup Docs

* Once the folders exist, Infra team writes **step-by-step instructions** so that anyone can get the project running locally.
* Typical things in setup docs:

  1. Install Docker and Docker Compose.
  2. Clone the repo.
  3. Run `docker-compose up --build`.
  4. Check backend at `http://localhost:8000/health`.
  5. Check frontend at `http://localhost:5173/graphs`.
* These docs make it **impossible for a teammate to get lost**, even if they’ve never used Docker or FastAPI before.

---

✅ **Why it matters**
Without this, frontend/backend teams might spend hours just figuring out paths, dependencies, or which files go where. By doing it first, Infra team **lays the foundation**, so the coding work flows smoothly.

---

If you want, I can make a **full diagram of the directories + files + Docker connections** — a visual cheat sheet for your team. It will make everything instantly clear. Do you want me to do that?
