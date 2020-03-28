#!/usr/bin/env python3

import stashy

bitbucketserver_url = ''
username = ''
password = ''

stash = stashy.connect(bitbucketserver_url, username, password)

users = stash.admin.users.list()
for user in users:
  print(user['slug'])
#print(stash.admin.groups.list())
#print(stash.projects.list())