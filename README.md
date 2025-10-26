# 🧠 Codebase Genius

**Codebase Genius** is an AI-powered documentation generator that analyzes software repositories and automatically produces high-quality markdown documentation.  
It is built using **JacLang (Jaseci)** and **Python** with modular agent-based architecture.

---

## 🚀 Features
- Automatically clones a GitHub repository.
- Maps file structures and summarizes README files.
- Analyzes Python code and builds a **Code Context Graph (CCG)**.
- Generates clean, structured markdown documentation.
- Uses T5 model for intelligent text summarization.

---

## 🧩 System Architecture
The system consists of four main modules (agents):
1. **Repo Mapper** – Clones repositories and reads file trees.  
2. **Code Analyzer** – Extracts functions, classes, and relationships.  
3. **DocGenie** – Generates final documentation in markdown format.  
4. **Code Genius (Supervisor)** – Orchestrates all agents and manages workflow.

---

## 🛠️ Setup Instructions
```bash
# 1. Clone this project
git clone <your_project_repo_or_local_path>
cd codebase_genius

# 2. Create virtual environment
python3 -m venv jaseci_env
source jaseci_env/bin/activate

# 3. Install dependencies
pip install -r requirements.txt
