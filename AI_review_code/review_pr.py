import os
import requests
import google.generativeai as genai
from dotenv import load_dotenv

# Load .env (already working)
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))

GITHUB_TOKEN = os.getenv("GITHUB_PAT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# 1. Fetch PR diff
repo = "SheikhJaveed/AI-code-review-demo"
pr_number = 2
url = f"https://api.github.com/repos/{repo}/pulls/{pr_number}"
headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3.diff"
}

diff = requests.get(url, headers=headers).text
print("Fetched diff (first 500 chars):")
print(diff[:500])

# 2. Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

# 3. Prepare prompt
prompt = f"""
You are a senior code reviewer.
Review the following code diff from a pull request.
Suggest improvements, highlight bugs, and check for best practices.

Code Diff:
{diff}
"""

# 4. Get AI review from Gemini
response = model.generate_content(prompt)

# 5. Print AI feedback
print("\n=== AI Review ===")
print(response.text)
