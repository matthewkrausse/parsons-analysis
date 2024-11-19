import dotenv
import os
import pandas as pd
from github import Github, Auth


dotenv.load_dotenv()

repo = os.getenv('GITHUB_REPO')


# Get the data from the Github API
def get_repo_data_and_export(repo):

    auth = Auth.Token(os.getenv('GITHUB_ACCESS_TOKEN'))

    # Public Web Github
    g = Github(auth=auth)

    repo = g.get_repo("move-coop/parsons")
    open_issues = list(repo.get_issues(state='all'))

    # downloads = repo.get_downloads()

    commits = repo.get_commits()

    # Define the data schema for the objects

    # Issue Schema

    print('issues')

    issues_schema = []
    for issue in open_issues:
        print(f"Processing issue: {issue.title}")
        issues_schema.append({
            'title': issue.title,
            'url': issue.url,
            'user': issue.user.name,
            'number': issue.number,
            'state': issue.state,
            'created_at': issue.created_at,
            'updated_at': issue.updated_at,
            'closed_at': issue.closed_at,
            'body': issue.body,
            'labels': issue.labels,
            'assignees': issue.assignees,
            'comments': issue.comments,
        })

    # Commit Schema

    commits_schema = []
    for commit in commits:
        print(f"Processing commit: {commit.sha}")
        commits_schema.append({
            'id': commit.sha,
            'message': commit.commit.message,
            'author': commit.author.login if commit.author else None,
            'files': [file.filename for file in commit.files],
            'additions': commit.stats.additions,
            'deletions': commit.stats.deletions,
        })

    # User Schema

    users = [commit.author for commit in commits if commit.author]
    user_schema = []
    for user in users:
        print(f"Processing user: {user.login}")
        user_schema.append({
            'login': user.login,
            'id': user.id,
            'avatar_url': user.avatar_url,
            'url': user.url,
            'html_url': user.html_url,
            'type': user.type,
            'site_admin': user.site_admin,
            'name': user.name,
            'company': user.company,
            'blog': user.blog,
            'location': user.location,
            'email': user.email,
            'hireable': user.hireable,
            'bio': user.bio,
            'twitter_username': user.twitter_username,
            'public_repos': user.public_repos,
            'public_gists': user.public_gists,
            'followers': user.followers,
            'following': user.following,
            'created_at': user.created_at,
            'updated_at': user.updated_at,
        })

    # convert all the data to a pandas dataframe
    # save the data to a file

    issues_df = pd.DataFrame(issues_schema)

    commits_df = pd.DataFrame(commits_schema)

    users_df = pd.DataFrame(user_schema)

    # save the data to a file
    issues_df.to_csv('data/issues.csv')
    commits_df.to_csv('data/commits.csv')
    users_df.to_csv('data/users.csv')


def main():
    get_repo_data_and_export(repo)  


if __name__ == '__main__':
    main()
