def get_organization_info(organization=None):
    return {"organization_info":organization}

def get_repository_info(repository=None):
    return {"repository_info":repository}

def get_user_info(username=None):
    return {"user_info": username}

def get_commits_info(organization=None, repository=None, user=None, time_range=None):
    return [{"organization_info":organization},{"repository_info":repository},{"user_info":user}, {'commits_count': 10, 'yyyymmdd_date': '20180101'},
            {'commits_count': 10, 'yyyymmdd_date': '20180102'}]

