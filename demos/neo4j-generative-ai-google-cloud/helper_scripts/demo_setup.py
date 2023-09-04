#! /usr/bin/env python3

import os
import sys

from github import Github
from github import Auth

gitrepo_dir = "/Users/lrazo/Frigomex Dropbox/Lee Razo/__professional/_documents_neo4j/git_repos/"
#github_user = 'leerazo'
github_user = 'neo4j-partners'
repo_path = os.path.dirname(__file__).split(os.path.sep)
repo_name = "intelligent-app-google-generativeai-neo4j"
full_repo_name = os.path.join(github_user, repo_name)

access_token = "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"

""" Utlility to add backslashes to pathnames where needed for executing shell commands """
def backslash_escape(string):
        special_characters = [' ',"^","$","|","?","*","+","(",")"]

        # Remove any existing backslashes
        no_slash = string.replace("\\", "")
        new_string = no_slash

        # Replace any special characters with escape slash
        for i in special_characters:
            new_string = new_string.replace(i,"\\"+i)
        return new_string


""" Authenticate in github and return instance """
def github_auth(access_token):
    # using an access token
    auth = Auth.Token(access_token)
    g = Github(auth=auth)
    return g

def gh_repo_exists(full_repo_name, g):
    try:
        repo = g.get_repo(full_repo_name)
        print('repo:', repo)
        repo_exists = True
    except Exception as e:
        print(e) 
        repo_exists = False

    return repo_exists

def main():
    print('full_repo_name:', full_repo_name)
    g = github_auth(access_token)

    if gh_repo_exists(full_repo_name, g):
         print('Repo {} exists!'.format(full_repo_name))
         clone_dir = backslash_escape(os.path.join(gitrepo_dir, repo_name))
         print('clone_dir:', clone_dir)
         git_clone_cmd = 'git clone https://github.com/' + full_repo_name + '.git ' + clone_dir
         print(git_clone_cmd)
         os.system(git_clone_cmd)
    else:
         print('Sorry, repo {} does not yet exist.'.format(full_repo_name))

if __name__ == '__main__':
    main()
