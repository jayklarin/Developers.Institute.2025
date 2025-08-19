# Assumptions:
# - You are in the correct project folder (via cd or "New Terminal at Folder").
# - This folder is NOT yet a git repo (no .git folder).
# - You already created the GitHub repository online and copied its URL.
# - There is at least one file in this folder (like test.txt) to commit.

# Initialize a new Git repository in this folder
git init

# -M (UPPERCASE) = forcefully Move/Rename the current branch to 'main',
# even if a branch named 'main' already exists
git branch -M main

# Stage (add) all new and modified files
# The '.' acts as a wildcard, meaning "everything in this folder and its subfolders."
# Be sure to put a space between 'add' and '.'
git add .

# -m (LOWERCASE) = add a commit Message inline instead of opening an editor
git commit -m "Initial commit" #GitHub requires a comment

# Connect this local repo to the remote GitHub repository
# - To find your repo link: go to the repo’s main page on GitHub →
#   click the green "<> Code" button → copy the HTTPS URL.
git remote add origin https_url_gets_pasted_here

# Push the commit to GitHub, creating the 'main' branch there
# -u sets upstream so future pushes can use just `git push`
git push -u origin main

# Here they are together
git init
git branch -M main
git add .
git commit -m "Initial commit"
git remote add origin https_url_gets_pasted_here
git push -u origin main