# hello_world_project

In this example repository I would like to practice git, gitHub, and virtual usage.

<details>
<summary>Getting Started</summary>

To clone the gitHub repository in the Git Bast run:
```shell
# in Git Bash Clone the repository
git clone https://github.com/Bezonce/hello_world_project.git your-repo

# In cmd Navigate to the project directory
cd your-repo
```

Steps to initialize the sandbox
```shell
# Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate

# Install project dependencies
pip install -r requirements.txt
```
</details>

<details>
<summary>Getting Started with docker build</summary>

```shell
docker build -t streamlit-app .
docker run -p 8501:8501 streamlit-app
```

```shell
docker-compose up -d
```

</details>