from __future__ import print_function, unicode_literals
from PyInquirer import prompt, print_json
from keyrotate import constants


def get_answers(defaults: dict):
    # Input prompts
    questions = [
        {
            'type': 'password',
            'name': constants.BITBUCKET_PASS,
            'message': 'What\'s yout BitBucket password?'
        },
        {
            'type': 'input',
            'name': constants.BITBUCKET_USERNAME,
            'message': 'What\'s your BitBucket username?',
            'default': defaults.get(constants.BITBUCKET_USERNAME, '')
        },
        {
            'type': 'input',
            'name': constants.SSH_DIR,
            'message': 'Where do you want to store the new ssh keys? eg.. /home/<username>/.ssh',
            'default': defaults.get(constants.SSH_DIR, '')
        },
        {
            'type': 'input',
            'name': constants.REPO_DIR,
            'message': 'Where do you want to checkout the twx-scm-monitoring repo? eg.. /home/<username>/repo',
            'default': defaults.get(constants.REPO_DIR, '')
        },
        {
            'type': 'input',
            'name': constants.BRANCH_NAME,
            'message': 'What is your branch name in twx-scm-monitoring repo?',
            'default': defaults.get(constants.BRANCH_NAME, '')
        },
        {
            'type': 'input',
            'name': constants.EMAIL,
            'message': 'What is your Email id?',
            'default': defaults.get(constants.EMAIL, '')
        }
    ]
    answers = prompt(questions)
    return answers


def save_user_input(input: dict):
    import json
    with open(constants.SETTINGS_FILE, 'w+') as settings_file:
        json.dump(input, settings_file)


def read_settings() -> dict:
    import os.path
    import json
    if os.path.isfile(constants.SETTINGS_FILE):
        with open(constants.SETTINGS_FILE) as f:
            data = json.load(f)
            return data
    return {}
