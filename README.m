Request your GitHub API token and set it as an environment variable

Create a virtual environment by running the following command:
```bash
python3 -m venv env
```

Run the following command to install the required packages:
```bash
pip install -r requirements.txt
```

set the env var of the github repo you want to get the data from
```bash
export GITHUB_REPO=your_repo
export GITHUB_ACCESS_TOKEN=your_token
```
example 'move-coop/parsons'

Activat the virtual environment by running the following command:
```bash
source env/bin/activate
```

Run the following command to start the application:
```bash
python get_repo_data.py
```

Use the notebook to do analysis on your repor

cells that are charts of number of issues, users, commits

cells word cloud analysis of issues, commits, users

cells most modified files

cells most active users

cells most commented issues