import os
from git import Git , Repo, GitDB
from git.db import GitCmdObjectDB
from os import path
# from dotenv import load_dotenv

# load_dotenv()

untrack = []
modified = []

def main():
    # print(os.getenv("EMAIL"))
    # print(os.listdir('J:\Program\Github\COMMITS_BANGER\TestProject'))
    #print(os.system('cmd /c "git status"'))
    # p = os.system('cmd /c "git status"')
    # print(p)
    url = "J:\C-sharp-Practice"
    url2 = "J:\Program\Github\COMMITS_BANGER"
    repo = Repo(url2, odbt=GitCmdObjectDB)
    # repo = Repo("", odbt=GitDB)
    # f = repo.git
    diff = repo.git.diff('HEAD~1..HEAD', name_only=True)
    count = 0
    # for i in diff:
    #     count +=1
    # print(count)
    # for item in repo.index.diff(None):
    #      print(item.a_path)
    # print(repo.untracked_files)
    for i in repo.untracked_files:
        untrack.append(i)
    changed = [ item.a_path for item in repo.index.diff(None) ]
    for i in changed:
        modified.append(i)
        
    print(untrack)


    

if __name__ == '__main__':
    main()
