import requests as req
base_url = 'https://api.bitbucket.org/'

def upload_key(pub_key: str, key_label: str, user_id: str, password: str):
    """
    Adds the key as a new key in bitbucket.

    :param pub_key: the location of the publickey
    :param key_label: the label to use for the key in bitbucket
    :param user_id: bitbucket user id
    :param password: bitbucket password
    :return:
    """

    context_path = '2.0/users/%s/ssh-keys' % user_id
    # request_body = request_body_template % (key, label)
    with open(pub_key , 'r') as f:
        key_data = f.read()
    request_body = {
        "key": key_data,
        "label": key_label,
        "type": "ssh_key"
    }
    # print(request_body)
    r = req.post(base_url + context_path, data=request_body, auth=(user_id, password))
    if r.status_code == 201:
        print('Successfully uploaded key to bitbucket.')
    else:
        print('Failed to upload key. something went wrong.')
        raise Exception('Failed to upload public key to bitbucket. Http status code: %s' % r.status_code)

def validate_login(user_id: str, password: str):
    context_path = '2.0/users/%s/ssh-keys' % user_id
    url = base_url+context_path
    r = req.get(url, auth=(user_id, password))
    if r.status_code != 200:
        raise Exception('Authentication failed for user:- %s , HTTP status code:- ' % (user_id, r.status_code))
    else: print('Authentication passed for user:- %s' % user_id)