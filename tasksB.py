# Phase B: LLM-based Automation Agent for DataWorks Solutions

# B1 & B2: Security Checks
import os
import json
import subprocess
import duckdb
import csv 
import requests
import markdown

def B12(filepath):
    if filepath.startswith('/data'):
        # raise PermissionError("Access outside /data is not allowed.")
        # print("Access outside /data is not allowed.")
        return True
    else:
        return False

# B3: Fetch Data from an API
def B3(url, save_path):
    if not B12(save_path):
        return None
    import requests
    response = requests.get(url)
    with open(save_path, 'w') as file:
        file.write(response.text)

# B4: Clone a Git Repo and Make a Commit
def clone_git_repo_and_commit(repo_url: str, output_dir: str, commit_message: str):
    """
    This tool function clones a Git repository from the specified URL and makes a commit with the provided message.
    Args:
        repo_url (str): The URL of the Git repository to clone.
        output_dir (str): The directory where the repository will be cloned.
        commit_message (str): The commit message to use when committing changes.
    """
    try:
        subprocess.run(["git", "clone", repo_url, output_dir])
        subprocess.run(["git", "add", "."], cwd=output_dir)
        subprocess.run(["git", "commit", "-m", commit_message], cwd=output_dir)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

# B5: Run SQL Query
def B5(db_path, query, output_filename):
    if not B12(db_path):
        return None
    import sqlite3, duckdb
    conn = sqlite3.connect(db_path) if db_path.endswith('.db') else duckdb.connect(db_path)
    cur = conn.cursor()
    cur.execute(query)
    result = cur.fetchall()
    conn.close()
    with open(output_filename, 'w') as file:
        file.write(str(result))
    return result

# B6: Web Scraping
def B6(url, output_filename):
    import requests
    result = requests.get(url).text
    with open(output_filename, 'w') as file:
        file.write(str(result))

# B7: Image Processing
def B7(image_path, output_path, resize=None):
    from PIL import Image
    if not B12(image_path):
        return None
    if not B12(output_path):
        return None
    img = Image.open(image_path)
    if resize:
        img = img.resize(resize)
    img.save(output_path)

# B8: Audio Transcription

def transcribe_audio(input_file: str, output_file: str):
    transcript = "Transcribed text"  # Placeholder
    with open(output_file, "w") as file:
        file.write(transcript)

# B9: Markdown to HTML Conversion
def B9(md_path, output_path):
    import markdown
    if not B12(md_path):
        return None
    if not B12(output_path):
        return None
    with open(md_path, 'r') as file:
        html = markdown.markdown(file.read())
    with open(output_path, 'w') as file:
        file.write(html)

# B10: API Endpoint for CSV Filtering

def convert_markdown_to_html(input_file: str, output_file: str):
    with open(input_file, "r") as file:
        html = markdown.markdown(file.read())
    with open(output_file, "w") as file:
        file.write(html)

#Write an API endpoint that filters a CSV file and returns JSON data
def filter_csv(input_file: str, column: str, value: str, output_file: str):
    results = []
    with open(input_file, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row[column] == value:
                results.append(row)
    with open(output_file, "w") as file:
        json.dump(results, file)