import os
import json

# ✅ Change this to your actual repo path
REPO_PATH = "/home/evans/codebase_genius/repos/requests"
OUTPUT_PATH = "/home/evans/codebase_genius/output/analysis.json"

def analyze_repo(repo_path):
    analysis = {"files": []}

    for root, dirs, files in os.walk(repo_path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        lines = f.readlines()
                    analysis["files"].append({
                        "path": os.path.relpath(file_path, repo_path),
                        "lines": len(lines)
                    })
                    print(f"Analyzing: {file_path}")
                except Exception as e:
                    print(f"⚠️ Skipped {file_path}: {e}")

    return analysis

if __name__ == "__main__":
    data = analyze_repo(REPO_PATH)

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w") as f:
        json.dump(data, f, indent=2)

    print(f"✅ Analysis data saved to: {OUTPUT_PATH}")
