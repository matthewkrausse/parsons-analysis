Request your GitHub API token and set it as an environment variable

Run the following command to install the required packages:
```bash
pip install -r requirements.txt
```

Run the following command to start the application:
```bash
python app.py
```

set the env var of the github repo you want to get the data from
```bash
export GITHUB_REPO=your_repo
```
example 'move-coop/parsons'

run the code

get_data() will be run in a jupyter notebook

basic analysis

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

cells that are charts of number of issues, users, commits

cells word cloud analysis of issues, commits, users

cells most modified files

cells most active users