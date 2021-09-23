import os
from git import Git, Repo, GitDB
from git.db import GitCmdObjectDB
from os import path
from datetime import datetime

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


def GitCommandRunner():
    CurrentDate = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    os.system('cmd /c "git commit -m "' + CurrentDate + '"')


def main():
    # populate files
    PopulateListWithFiles()
    # add and commit the files
    for i in ListForCommit:
        print(i)
        repo.index.add(i)
        GitCommandRunner()
        print(True)


if __name__ == '__main__':
    main()
