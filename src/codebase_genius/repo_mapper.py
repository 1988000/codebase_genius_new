import os
import git
from pathlib import Path
from text_summarizer import summarize_text

def clone_repo(repo_url, clone_dir="repo_clone"):
    """
    Clone a GitHub repository to a local directory.
    """
    repo_path = Path(clone_dir)
    if repo_path.exists():
        print(f"Repository already exists at {repo_path}.")
    else:
        print(f"Cloning {repo_url}...")
        git.Repo.clone_from(repo_url, repo_path)
        print("Clone complete.")
    return repo_path

def generate_file_tree(directory):
    """
    Generate a tree structure of files and directories.
    """
    tree = []
    for root, dirs, files in os.walk(directory):
        level = root.replace(str(directory), "").count(os.sep)
        indent = " " * 4 * level
        tree.append(f"{indent}{os.path.basename(root)}/")
        for file in files:
            sub_indent = " " * 4 * (level + 1)
            tree.append(f"{sub_indent}{file}")
    return "\n".join(tree)

def summarize_readme(repo_path):
    """
    Summarize README.md if present.
    """
    readme_path = repo_path / "README.md"
    if readme_path.exists():
        with open(readme_path, "r", encoding="utf-8") as f:
            text = f.read()
        return summarize_text(text)
    else:
        return "No README.md found in repository."

if __name__ == "__main__":
    url = input("Enter GitHub repository URL: ").strip()
    repo_path = clone_repo(url)
    print("\n📂 Repository File Tree:")
    print(generate_file_tree(repo_path))
    print("\n🧠 README Summary:")
    print(summarize_readme(repo_path))
