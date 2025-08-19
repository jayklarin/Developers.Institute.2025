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

# Stage all files (the '.' means "everything in this folder")
git add .

# -m (LOWERCASE) = add a commit Message inline instead of opening an editor
git commit -m "Initial commit"

# Connect this local repo to the remote GitHub repository
git remote add origin https://github.com/your-username/your-repo.git

# Push the commit to GitHub, creating the 'main' branch there
# -u sets upstream so future pushes can use just `git push`
git push -u origin main


# Here they are together
git init
git branch -M main
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/your-username/your-repo.git
git push -u origin main
