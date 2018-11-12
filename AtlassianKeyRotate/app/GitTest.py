import git

# rorepo is a Repo instance pointing to the git-python repository.
# For all you know, the first argument to Repo is a path to the repository
# you want to work with
repo_dir = '/home/agoyal/keyrotate/twx-scm-monitoring'
repo = git.Repo(repo_dir)
assert not repo.bare
repo.git.push('origin')
# repo.git.add('1.txt')
# repo.git.commit('-m "test commit"', author='agoyal@ptc.com')

# for f in files.split('\n'):
#     # show_diff(f)
#     repo.git.add(f)
#
# repo.git.commit('test commit', author='agoyal@ptc.com')