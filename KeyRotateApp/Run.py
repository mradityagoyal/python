from keyrotate import input_service as in_s
from keyrotate import keys_service as ks
from keyrotate import constants
from keyrotate import bitbucket_service as bbs
from keyrotate import git_service as gs
import datetime

#read answers json file if exists.
answers = in_s.read_settings()

#prompt user for input
answers = in_s.get_answers(answers)
password = answers[constants.BITBUCKET_PASS]
answers.pop(constants.BITBUCKET_PASS) # remove password from answers. to avoid saving to file.

#save input for future.
in_s.save_user_input(answers)

username = answers[constants.BITBUCKET_USERNAME]
bbs.validate_login(username, password) #TODO; termiate program if auth fails.


#create backup of old keys
ssh_dir = answers[constants.SSH_DIR]
ks.create_backup(ssh_dir)

#create new key pair.
ks.create_key_pair(ssh_dir)

#run ssh-add
ks.run_ssh_add()

public_key_file = '%s/id_rsa.pub' % ssh_dir
now = datetime.datetime.utcnow().strftime("%a %b %d %H:%M:%S")
key_label = 'Key rotated on %s' % now

#upload keys to bitbucket
bbs.upload_key(public_key_file, key_label, username, password)

#TODO: delete old keys from bitbucket.

#update the timestamps in the twx-scm-monitoring repo and push.
repo_dir = answers[constants.REPO_DIR]
branch = answers[constants.BRANCH_NAME]
email = answers[constants.EMAIL]
gs.update_twx_scm_monitoring(repo_dir, branch, email)




