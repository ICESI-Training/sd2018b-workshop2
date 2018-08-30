def get_user_info(username=None):
    return {"user_info": username}

def get_commits_info(username=None, time_range=None):
    return {"time_range": time_range, "commits_count": 100}
