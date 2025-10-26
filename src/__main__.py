import os
import subprocess
from pathlib import Path

def run_script(script_name):
    """Helper to run a Python script from src/ directory."""
    script_path = Path(__file__).parent / script_name
    print(f"\n🔍 Running {script_name}...")
    subprocess.run(["python3", str(script_path)], check=True)

def main():
    print("🤖 Welcome to Codebase Genius Supervisor!")

    repo_url = input("Enter a GitHub repository URL: ").strip()
    if not repo_url:
        print("❌ No URL provided. Exiting.")
        return

    # Step 1: Clone repository
    print(f"\n🔍 Cloning repository from {repo_url}...")
    clone_dir = Path.home() / "codebase_genius" / "repos"
    clone_dir.mkdir(parents=True, exist_ok=True)
    repo_name = repo_url.split("/")[-1].replace(".git", "")
    repo_path = clone_dir / repo_name

    if repo_path.exists():
        print("⚠️ Repository already exists, skipping clone.")
    else:
        subprocess.run(["git", "clone", repo_url, str(repo_path)], check=True)
    print("✅ Repository cloned successfully!")

    # Step 2: Run analyzer
    run_script("code_analyzer.py")

    # Step 3: Run documentation generator
    run_script("doc_genie.py")

    print("\n✨ Workflow complete!")
    print("Check the /output folder for your DOCUMENTATION.md file.")

if __name__ == "__main__":
    main()
