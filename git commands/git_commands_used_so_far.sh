# git commands used so far

# Start a new Git repository in the current folder
git init

# Rename (or force move) the current branch to main
git branch -M main

# Stage all changes in the folder for commit ('.' = everything here and below)
git add .

# Create a commit with a message (-m = message inline)
git commit -m "message"

# Link your local repo to a GitHub repository (replace <url> with the repo link)
git remote add origin <url>

# Push commits to GitHub and set upstream (-u = remember this branch for future pushes)
git push -u origin main

# Check staged, unstaged, and untracked files
git status

# Confirm the branch you are currently on
git branch --show-current

# List the remote repo URLs (fetch and push)
git remote -v
