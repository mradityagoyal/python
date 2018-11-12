#!/usr/bin/env python
# -*- coding: utf-8 -*-

from requests_oauthlib import OAuth2Session

class AppPasswords:

    user_id = 'mraditya'
    app_password = ''

import requests as req

def main():
    app_pass = AppPasswords()
    # Fetch a request token
    base_url = 'https://api.bitbucket.org/'
    context_path = '2.0/users/%s/ssh-keys' % app_pass.user_id
    key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCeVU6tNBqtViknp/Xzi/Qi8oYiynCunBXqX7RdrRLHIo8P0jg/wwlsw0tp/pCxiY1ORNKo2+tvRAF4cLVmucxGjhw1TnC3pOgQ0oN0aE2M+hfTaG2gl2NN5Qe9Lnr1QAvLtmHUqmGMDCjhw9Z7BQehGqJn8TuwIZYsrN3sZEIPshs5z1/xtx40Tfmm8nk5quSy2oOSKr8Uy8hv2VYyDuWMX/V+dUsZGaPEejifbOljxNXOrzBkewNS6VaIGEd8iZtqzvqOwTUfKd78Zz29jwfEq+5CpGlzr+Eod3rAQhLhL8Omn/5OkyeUQMERWZmBJkqmAgVYGH0dlE/vdoCXYU41 agoyal@AddyP7520"
    label = "Label1"
    # request_body = request_body_template % (key, label)
    request_body = {
    "key": key,
    "label": label,
    "type": "ssh_key"
}
    print(request_body)


    # r = req.get("%s%s" % (base_url, context_path), auth=(app_pass.user_id, app_pass.app_password))
    r = req.post("https://api.bitbucket.org/2.0/users/mraditya/ssh-keys", data = request_body, auth=(app_pass.user_id, app_pass.app_password))
    print(r.content)


if __name__ == '__main__':
    main()