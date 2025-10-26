import os
import subprocess
from pathlib import Path
import sys
import json

def run_command(command):
    """Run shell command and return output or error."""
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"⚠️ Error: {e.stderr}")
        return None


def clone_repository(repo_url):
    """Clone a GitHub repository to the input folder."""
    input_path = Path.home() / "codebase_genius" / "input_repo"
    os.makedirs(input_path, exist_ok=True)
    print(f"📥 Cloning repository from {repo_url}...")
    run_command(f"rm -rf {input_path}/*")
    run_command(f"git clone {repo_url} {input_path}")
    return str(input_path)


def analyze_repository(repo_path, output_path):
    """Perform basic code analysis and generate documentation."""
    print(f"🔍 Analyzing repository at {repo_path} ...")

    summary = []
    for root, _, files in os.walk(repo_path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                lines = sum(1 for _ in open(file_path, "r", encoding="utf-8", errors="ignore"))
                summary.append(f"- {os.path.relpath(file_path, repo_path)} — {lines} lines")

    output_content = [
        "# 🧠 Codebase Genius Documentation",
        "",
        f"## Repository Overview",
        f"This repository contains **{len(summary)} Python files.**",
        "",
        "## File Analysis",
        "\n".join(summary)
    ]

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(output_content))

    print(f"✅ Documentation generated successfully: {output_path}")


def supervisor():
    print("Welcome to Codebase Genius Supervisor!")
    repo_url = input("Enter a GitHub repository URL: ").strip()

    # Accept both GitHub URLs and local paths
    if repo_url.startswith("local:"):
        repo_path = repo_url.replace("local:", "").strip()
        if not os.path.exists(repo_path):
            print("❌ Local path does not exist.")
            return
        print(f"📁 Using local source directory: {repo_path}")
    else:
        if "github.com" not in repo_url:
            print("❌ Invalid URL. Please enter a valid GitHub repository link or local path.")
            return
        repo_path = clone_repository(repo_url)

    output_path = input("Enter the output path for documentation: ").strip()
    analyze_repository(repo_path, output_path)


if __name__ == "__main__":
    supervisor()
