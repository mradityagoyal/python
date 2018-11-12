
def create_backup(root_dir: str):
    #create old key backup
    backup_dir = "%s/key_backup" % root_dir
    import os
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
        print("new directory %s created" % backup_dir)
    import shutil
    shutil.copy('%s/id_rsa' % root_dir, '%s/id_rsa' % backup_dir )
    shutil.copy('%s/id_rsa.pub' % root_dir, '%s/id_rsa.pub' % backup_dir)

    #delte old key
    os.remove('%s/id_rsa.pub' % root_dir)
    os.remove('%s/id_rsa' % root_dir)



def create_key_pair(root_dir: str):
    # create new key .
    from Crypto.PublicKey import RSA

    key = RSA.generate(2048)
    #write private key
    with open('%s/id_rsa' % root_dir, 'wb+') as private_key:
        # chmod("/tmp/private.key", 0o0600)
        private_key.write(key.exportKey('PEM'))
    #write public key
    pubkey = key.publickey()
    with open('%s/id_rsa.pub' % root_dir, 'wb+') as public_key:
        # chmod("/tmp/private.key", 0o0600)
        public_key.write(pubkey.exportKey('OpenSSH'))


#read new key and upload to bitbucket.
def upload_key(pub_key : str, key_label: str, user_id: str, password : str):
    import requests as req
    base_url = 'https://api.bitbucket.org/'
    context_path = '2.0/users/%s/ssh-keys' % user_id
    key = pub_key
    label = key_label
    # request_body = request_body_template % (key, label)
    request_body = {
        "key": key,
        "label": label,
        "type": "ssh_key"
    }
    r = req.post("https://api.bitbucket.org/2.0/users/mraditya/ssh-keys", data = request_body, auth=(user_id, password))
    return r

def update_repo_time(repo_dir: str, username: str):
    import datetime
    # put current date in keys-last-changed file.
    now = datetime.datetime.utcnow().strftime("%a %b %d %H:%M:%S UTC %Y")
    with open('%s/%s/keys-last-changed' % (repo_dir, username),  'w') as keys_last_changed:
        keys_last_changed.write(now)
    with open('%s/%s/password-last-changed' % (repo_dir, username),  'w') as pass_last_changed:
        pass_last_changed.write(now)

    from git import Repo

    # rorepo is a Repo instance pointing to the git-python repository.
    # For all you know, the first argument to Repo is a path to the repository
    # you want to work with
    repo = Repo(path=repo_dir)
    assert not repo.bare
    repo.git.add('%s/%s/keys-last-changed' % (repo_dir, username))
    repo.git.add('%s/%s/password-last-changed' % (repo_dir, username))

    repo.git.commit('-m "Update Key and pass"', author='agoyal@ptc.com')
    repo.git.push('origin')

USERNAME = "mraditya"
APP_PASS = ''
ROOT_DIR = "/home/agoyal/.ssh"
REPO_DIR = '/home/agoyal/keyrotate/twx-scm-monitoring'
#create backup
create_backup(ROOT_DIR)
print('backup created')
#create new keys
create_key_pair(ROOT_DIR)
print('new keys created')
with open('%s/id_rsa.pub' % ROOT_DIR, 'r') as pub_key_file:
    pub_key = pub_key_file.read()
    #upload the keys
    upload_key(pub_key, key_label= "for desktop", user_id= USERNAME, password=APP_PASS)
print('keys uploaded')
update_repo_time(repo_dir=REPO_DIR, username=USERNAME)
print('git repo updated and pushed')



#commit and push git to rotate key.