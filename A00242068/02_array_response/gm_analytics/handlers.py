def get_user_info(username=None):
    return {"user_info": username}

def get_commits_info(username=None, time_range=None):
    return [{'commits_count': 10, 'yyyymmdd_date': '20180101'},
            {'commits_count': 10, 'yyyymmdd_date': '20180102'}]
def get_commits_info(org=none, repos=none, usr=none):
    return [{'org_info':org, 'repos_info':repos, 'usr_info':usr},
            {'org_info':org, 'repos_info':repos, 'usr_info':usr}]
