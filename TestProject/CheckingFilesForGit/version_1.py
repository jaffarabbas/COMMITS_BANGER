import os
from git import Git, Repo, GitDB
from git.db import GitCmdObjectDB
from os import path

# from dotenv import load_dotenv

# load_dotenv()
ListForCommit = []
url = "J:\C-sharp-Practice"
url2 = "J:\Program\Github\COMMITS_BANGER"
repo = Repo(url2, odbt=GitCmdObjectDB)
diff = repo.git.diff('HEAD~1..HEAD', name_only=True)
changed = [item.a_path for item in repo.index.diff(None)]


def PopulateListWithFiles():
    for i in repo.untracked_files:
        ListForCommit.append(i)
    for i in changed:
        ListForCommit.append(i)
    print(ListForCommit)


def main():
    # populate files
    PopulateListWithFiles()
    # add and commit the files
    for i in ListForCommit:
        repo.index.add(i)
        repo.index.commit("9-23-2021")
        print(True)


if __name__ == '__main__':
    main()
