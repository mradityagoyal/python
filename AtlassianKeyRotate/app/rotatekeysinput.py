from __future__ import print_function, unicode_literals
from PyInquirer import prompt, print_json

#Literals
BITBUCKET_USERNAME = 'bitbucket_username'
BITBUCKET_PASS = 'bitbucket_pass'
SSH_DIR = 'ssh_dir'
REPO_DIR = 'repo_dir'
# end literals


#Input prompts
questions = [
    {
        'type': 'input',
        'name': BITBUCKET_USERNAME,
        'message': 'What\'s your BitBucket username?'
    },
    {
        'type': 'password',
        'name': BITBUCKET_PASS,
        'message': 'What\'s yout BitBucket password?'
    },
    {
        'type': 'input',
        'name': SSH_DIR,
        'message': 'Where do you want to store the new ssh keys? eg.. /home/<username>/.ssh'
    },
    {
        'type': 'input',
        'name': REPO_DIR,
        'message': 'Where do you want to checkout the twx-scm-monitoring repo? eg.. /home/agoyal/keyrotate/twx-scm-monitoring'
    }
]

def get_answers():
    answers = prompt(questions)
    return answers
