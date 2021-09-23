import os
from git import Git, Repo, GitDB
from git.db import GitCmdObjectDB
from os import path
from datetime import datetime
from multiprocessing import Process

# from dotenv import load_dotenv

# load_dotenv()
ListForCommit = []
url = "J:\C-sharp-Practice"
url2 = "J:\Program\Github\COMMITS_BANGER"
repo = Repo(url2, odbt=GitCmdObjectDB)
diff = repo.git.diff('HEAD~1..HEAD', name_only=True)
changed = [item.a_path for item in repo.index.diff(None)]
origin = repo.remote('origin')


def main():
    # commit message
    commit_message = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    # add files to stage and commit
    for i in repo.untracked_files:
        repo.index.add(i)
        repo.index.commit(commit_message)
    for i in changed:
        repo.index.add(i)
        repo.index.commit(commit_message)
    origin.push()


if __name__ == '__main__':
    main()
