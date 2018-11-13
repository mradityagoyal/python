from keyrotate import constants


def create_backup(ssh_dir: str):
    """
    Create backup zip of private and public keys found in the ssh_dir

    :param ssh_dir: the directory where the id_rsa and id_rsa pub files reside.
    """
    # create old key backup
    files = ['%s/id_rsa' % ssh_dir, '%s/id_rsa.pub' % ssh_dir]

    backup_dir = "%s/key_backup" % ssh_dir
    import os
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
        print("new directory for backups created:- %s" % backup_dir)

    import zipfile, datetime
    now = datetime.datetime.utcnow().strftime("%a %b %d %H:%M:%S UTC %Y")
    zipFileName = '%s/KeysBackup-%s.zip' % (backup_dir, now)
    with zipfile.ZipFile(zipFileName, 'w') as z:
        for f in files:
            z.write(f)
    print('Created backup of keys:- %s' % zipFileName)

    # delte old key
    for f in files:
        os.remove(f)
        print('Removed old key file:- %s' % f)


def create_key_pair(ssh_dir: str):
    """
    Creates a new id_rsa and id_rsa.pub file in the ssh_dir

    :param ssh_dir: the directory where the id_rsa and id_rsa pub files will reside.
    """
    pk_fileName = '%s/id_rsa' % ssh_dir
    pubk_filename = '%s/id_rsa.pub' % ssh_dir
    # create new key .
    from Crypto.PublicKey import RSA
    key = RSA.generate(2048)
    # write private key
    with open(pk_fileName, 'wb+') as private_key:
        private_key.write(key.exportKey('PEM'))
        import os
        os.chmod(pk_fileName, 0o600)
        print('Created Private key:- %s' % pk_fileName)
    # write public key
    with open(pubk_filename, 'wb+') as public_key:
        public_key.write(key.publickey().exportKey('OpenSSH'))
        print('Created Public key:- %s' % pubk_filename)

def run_ssh_add():
    import os
    print('Running ssh-add command')
    os.system('ssh-add')

def delete_key():
    #TODO
    raise Exception('Not Implemented')
