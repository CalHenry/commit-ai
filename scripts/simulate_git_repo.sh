#!/bin/bash

# I asked AI to generate a fake repo with a few git commits so i could have material to work on to develop the ai commit agent

mkdir -p fake_repo
cd fake_repo
git init

# Create initial files
cat > main.py << 'EOL'
def greet(name):
    print(f"Hello, {name}!")

if __name__ == "__main__":
    greet("World")
EOL>

cat > utils.py << 'EOL'
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
EOL

# First commit
git add .
git commit -m "feat: initial project setup with greet and utils"

# Update main.py to use utils.add
cat > main.py << 'EOL'
from utils import add

def greet(name):
    print(f"Hello, {name}!")

if __name__ == "__main__":
    greet("World")
    print(f"2 + 3 = {add(2, 3)}")
EOL

# Second commit
git add main.py
git commit -m "feat: integrate utils.add into main"

# Introduce a bug in utils.py
cat > utils.py << 'EOL'
def add(a, b):
    return a - b  # Bug: should be a + b

def subtract(a, b):
    return a - b
EOL

# Commit the bug
git add utils.py
git commit -m "WIP: accidentally broke add function"

# Fix the bug in utils.py
cat > utils.py << 'EOL'
def add(a, b):
    return a + b  # Fixed

def subtract(a, b):
    return a - b
EOL

# Commit the fix
git add utils.py
git commit -m "fix: correct add function logic"

# Add a new feature to utils.py
cat > utils.py << 'EOL'
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b
EOL

# Commit the new feature
git add utils.py
git commit -m "feat: add multiply function to utils"

# Update main.py to use the new feature
cat > main.py << 'EOL'
from utils import add, multiply

def greet(name):
    print(f"Hello, {name}!")

if __name__ == "__main__":
    greet("World")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"2 * 3 = {multiply(2, 3)}")
EOL

# Commit the update
git add main.py
git commit -m "feat: use multiply function in main"

# Refactor main.py
cat > main.py << 'EOL'
from utils import add, multiply

def say_hello(name):
    print(f"Hello, {name}!")

if __name__ == "__main__":
    say_hello("World")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"2 * 3 = {multiply(2, 3)}")
EOL

# Commit the refactor
git add main.py
git commit -m "refactor: rename greet to say_hello"

# Print the commit history
echo "Commit history:"
git log --oneline

# Introduce unstaged changes
echo "Adding unstaged changes..."
cat > utils.py << 'EOL'
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
EOL

cat > main.py << 'EOL'
from utils import add, multiply, divide

def say_hello(name):
    print(f"Hello, {name}!")

if __name__ == "__main__":
    say_hello("World")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"2 * 3 = {multiply(2, 3)}")
    print(f"6 / 3 = {divide(6, 3)}")
EOL

# Show the status to confirm unstaged changes
echo "Unstaged changes:"
git status
