import os
from git import Repo, GitDB


def main():
    # print(os.listdir('J:\Program\Github\COMMITS_BANGER\TestProject'))
    #os.system('cmd /c "git status"')
    repo = Repo("J:\Program\Github\COMMITS_BANGER\TestProject", odbt=GitDB)
    diff = repo.git.diff('HEAD~1..HEAD', name_only=True)
    print(diff)



if __name__ == '__main__':
    main()
