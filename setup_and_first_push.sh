# Assumptions:
# - You are in the correct project folder (via cd or "New Terminal at Folder").
# - This folder is NOT yet a git repo (no .git folder).
# - You already created the GitHub repository online and copied its URL.
# - There is at least one file in this folder (like test.txt) to commit.

# Initialize a new Git repository in this folder
git init

# Rename the default branch to 'main' (GitHub’s default)
git branch -M main

# Stage all files (the '.' means "everything in this folder")
git add .

# Create the first commit (-m lets you add the commit message inline)
git commit -m "Initial commit"

# Connect this local repo to the remote GitHub repository
git remote add origin https://github.com/your-username/your-repo.git

# Push the commit to GitHub, creating the 'main' branch there
# -u sets upstream so future pushes can use just `git push`
git push -u origin main
