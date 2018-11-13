from git import Repo


def update_time(repo_dir: str, branch: str, repo: Repo, email: str):
    """
    Updates the keys-last-changed and password-last-changed in twx-scm-monitoring repo
    commits and pushes the files.

    :param repo_dir: directory where to checkout the twx-scm-monitoring repo
    :param branch: your branch in the repo
    :param repo: The git repo object.
    :param email: email id to use in author for git commit
    """
    import datetime
    assert not repo.bare
    # put current date in keys-last-changed file.
    now = datetime.datetime.utcnow().strftime("%a %b %d %H:%M:%S UTC %Y")
    files = ['%s/%s/keys-last-changed' % (repo_dir, branch), '%s/%s/password-last-changed' % (repo_dir, branch)]
    for path in files:
        with open(path, 'w') as f:
            f.write(now)
            print('Updated %s to contain time %s' % (path, now))
        repo.git.add(path)
    commit_msg = 'Updated key and pass on %s' % now
    repo.git.commit('-m "%s"' % commit_msg, author=email)
    repo.git.push('origin')
    print(commit_msg)
    print('pushed to remote.')


def init_repo(dest_dir: str) -> (str, Repo):
    """
    Clones the twx-scm-monitoring.git repo to the specified dest_dir if not alredy present.

    :param dest_dir:
    """
    import os
    twx_scm_repo_path = os.path.join(dest_dir, 'twx-scm-monitoring')
    if not os.path.exists(twx_scm_repo_path):
        os.makedirs(twx_scm_repo_path)
        print('Created new directory :- %s' % twx_scm_repo_path)

    try:
        repo = Repo(twx_scm_repo_path)
    except:
        print('cloning twx-scm-monitoring to %s' % twx_scm_repo_path)
        repo = Repo.clone_from('git@bitbucket.org:thingworx-ondemand/twx-scm-monitoring.git', twx_scm_repo_path)
        print('fininshed cloning')
    return (twx_scm_repo_path, repo)


def update_twx_scm_monitoring(dest_dir: str, branch: str, email: str):
    """

    :param dest_dir: parent directory where the twx-scm-monitoring repo exists. repo is cloned if does not exist in dest_dir.
    :param branch: the branch to check out
    :param email: email id to use in commit message

    """
    # init repo. clone if necessary.
    (location, repo) = init_repo(dest_dir)
    # checkout the correct branch.
    if not repo.active_branch == branch:
        if branch in repo.branches:
            print('checking out local branch:- origin/%s' % branch)
            repo.git.checkout(branch)
        else:
            print('checking out remote branch:- origin/%s' % branch)
            repo.git.checkout('-t', 'origin/%s' % branch)

    update_time(location, branch, repo, email)
