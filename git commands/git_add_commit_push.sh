# Let's understand this single command that combines multiple Git operations:
git add . && git commit -m "GitHub requires message" && git push -u origin main

# The above is these three commands individually:
git add .
git commit -m "GitHub requires message"
git push -u origin main

# Assumptions:
# - You are already in the correct project folder 
#   (via `cd path/to/folder` OR Finder → Right Click → New Terminal at Folder).
# - Git is already initialized here (`.git` exists).
# - Remote `origin` is already set and points to your GitHub repo.


# Stage (add) all new and modified files
# The '.' acts as a wildcard, meaning "everything in this folder and 
# its subfolders."  Be sure to put a space between 'add' and '.'
git add .

# Create a commit (a snapshot of changes) with a message
# -m lets you attach the commit message inline instead of opening an editor
git commit -m "GitHub requires message"

# Push commits to the 'main' branch on GitHub (remote = origin)
# -u sets upstream tracking, so next time you can just run `git push` or `git pull`
git push -u origin main