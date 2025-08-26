
# 🚀 PR-Sentinel

An **AI-powered code review application** that integrates with GitHub pull requests to automatically analyze code changes using Google Gemini API.

---

## 📌 Features
- Connects to GitHub via **Personal Access Token (PAT)**.
- Listens to **pull request events** (via GitHub Actions workflow).
- Fetches the **diff/patch** of PR changes.
- Sends the diff to **Google Gemini API** for AI-powered review.
- Prints AI suggestions for better code quality.

---

## 🛠️ Setup Instructions

### 1. Create GitHub Repository
- Initialize a new GitHub repo (e.g., `AI-code-review-demo`).
- Add a sample `main.py` file (or any code file) to test with.
- Clone the repo locally:
  ```bash
  git clone https://github.com/<your-username>/AI-code-review-demo.git
  cd AI-code-review-demo `

* * * * *

### 2. Create a GitHub Personal Access Token (PAT)

1. Go to your GitHub account:  
   **Profile > Settings > Developer Settings > Personal Access Tokens > Fine-grained Tokens**

2. Click **Generate new token**.

3. Select **"Only select repositories"** and choose the repository where you want to enable AI code review.  
   (This ensures the token is restricted to just your project and not all repos.)

4. Under **Repository permissions**, grant the following:
   - **Contents** → Read and Write (needed to fetch and comment on PRs)  
   - **Pull requests** → Read and Write (to post AI review comments on PRs)  
   - **Workflows** → Read and Write (so Actions can use the token)  

5. (Optional) Under **Account permissions**, you can leave defaults unless your repo setup requires more.

6. Set an **expiry date** for security (recommended).  

7. Generate the token and **copy it immediately** — GitHub will only show it once.

8. Save this token in your `.env` file as:

   ```env
   GITHUB_PAT_TOKEN=ghp_yourGeneratedTokenHere

* * * * *

### 3\. Add Google Gemini API Key

1.  Go to Google AI Studio.

2.  Create an API key.

3.  Save it in `.env` file.

* * * * *

### 4\. Create `.env` File

In the project root, create a `.env` file:

`GITHUB_PAT_TOKEN=ghp_yourgithubtoken
GEMINI_API_KEY=AIzaSyDxxxxxxx`

* * * * *

## Note:
To write an automated comment on the PR use this command on git bash:
```bash
curl -X POST \
  -H "Authorization: token YOUR_GITHUB_TOKEN" \
  -H "Accept: application/vnd.github+json" \
  https://api.github.com/repos/OWNER/REPO/issues/PR_NUMBER/comments \
  -d '{"body":"🤖 AI Code Review Suggestion:\n\nYour review text goes here"}'
```
### 5\. Install Dependencies

Inside your project folder:

`pip install requests python-dotenv google-generativeai`

* * * * *

### 6\. Project Structure

```AI-code-review-demo/
│── AI_review/
│   ├── review_pr.py   # Main script to fetch PR diff and send to Gemini
│   ├── script.py      # Additional utilities
│── .env               # Environment variables
│── .gitignore
│── README.md
│── main.py            # Sample file
```
* * * * *

### 7\. GitHub Actions Workflow

Inside `.github/workflows/code_review.yml`:

```yaml
name: AI Code Review

on:
  pull_request:
    types: [opened, synchronize]

jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repo
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.10"

      - name: Install dependencies
        run: pip install requests python-dotenv google-generativeai

      - name: Run AI Code Review
        env:
          GITHUB_PAT_TOKEN: ${{ secrets.GITHUB_PAT_TOKEN }}
          GEMINI_API_KEY: ${{ secrets.GEMINI_API_KEY }}
        run: python AI_review/review_pr.py
```
### 8\. Running the Script Locally

To test without workflow:

`python AI_review/review_pr.py`

It will:

-   Fetch latest PR diff.

-   Send to Gemini.

-   Print AI review in console.

* * * * *

✅ Example Output
----------------

`{
  "status": "success",
  "pull_request": 12,
  "ai_review": "Consider adding error handling for file operations in main.py..."
}`

* * * * *

🔑 Notes
--------

-   If you used a **dummy webhook** earlier, you don't need it now since GitHub Actions workflow handles PR events.

-   Always keep `.env` and tokens secure (never commit them).

-   For merging branches:

    `git checkout main
    git merge branch-2
    git push origin main`

* * * * *

🎯 Summary
----------

This project demonstrates **end-to-end AI integration** with GitHub PRs, automating code reviews using Gemini API.

