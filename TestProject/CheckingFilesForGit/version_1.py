import os
from git import Repo
from git.db import GitCmdObjectDB
from datetime import datetime


repo = Repo("J:\Program\Github\COMMITS_BANGER", odbt=GitCmdObjectDB)
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
