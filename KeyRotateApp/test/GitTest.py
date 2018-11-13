from keyrotate import git_service as gs
from git import Repo
import git
import os
dir = "/home/agoyal/test/new"




def init_repo(dir: str):
    if not os.path.exists(dir):
        os.makedirs(dir)
        print('Created new directory :- %s' % dir)

    twx_scm_repo_path = os.path.join(dir, 'twx-scm-monitoring')
    if not os.path.exists(twx_scm_repo_path):
        os.makedirs(twx)
    try:
        repo = Repo(dir)
    except git.exc.InvalidGitRepositoryError:
        print("error occured")

init_repo(dir)