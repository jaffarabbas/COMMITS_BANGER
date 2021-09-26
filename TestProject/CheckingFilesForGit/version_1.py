from git import Repo
from git.db import GitCmdObjectDB
from datetime import datetime

repo = Repo("J:\Program\Github\COMMITS_BANGER", odbt=GitCmdObjectDB)
origin = repo.remote('origin')


def GitCommandRunner(commit, commit_message):
    repo.index.add(commit)
    repo.index.commit(commit_message)
    print(f'committed file : {commit}')


def main():
    # counter for counter committed files
    count = 0
    # commit message
    commit_message = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    # add files to stage and commit
    for i in repo.untracked_files:
        GitCommandRunner(i, commit_message)
        count += 1
    for item in repo.index.diff(None):
        GitCommandRunner(item.a_path, commit_message)
        count += 1
    # push all commits at once  
    origin.push()

    # print(f"Done !!! committing : {count} files")
    for i in repo.index.diff(None):
        print(i.deleted_file)


if __name__ == '__main__':
    main()
