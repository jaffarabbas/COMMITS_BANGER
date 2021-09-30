from git import Repo
from git.db import GitCmdObjectDB
from datetime import datetime

repo = Repo("J:\maju", odbt=GitCmdObjectDB)
origin = repo.remote('origin')


def GitCommandRunner(count , commit, commit_message):
    repo.index.add(commit)
    repo.index.commit(commit_message)
    print(f'{count} : committed file : {commit}')


def main():
    # counter for counter committed files
    count = 0
    # commit message
    commit_message = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    # add files to stage and commit
    for i in repo.untracked_files:
        GitCommandRunner(count, i, commit_message)
        count += 1
        if count <= 50:
            break
    for item in repo.index.diff(None):
        GitCommandRunner(count, item.a_path, commit_message)
        count += 1
        if count <= 50:
            break
    # push all commits at once  
    origin.push()

    print(f"Done !!! committing : {count} files")
    


if __name__ == '__main__':
    main()
