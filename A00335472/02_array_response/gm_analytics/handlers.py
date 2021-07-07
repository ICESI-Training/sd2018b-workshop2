import logging

def get_user_info(username=None):
    return {"user_info": username}

def get_commits_info(organization=None, repository=None,  username=None, time_range=None):    
    logging.info('executing get_commits_info method')
    logging.debug('organization=%s', organization)
    logging.debug('repository=%s', repository)
    logging.debug('username=%s', username)
    return [{'commits_count': 10, 'yyyymmdd_date': '20180101'},
            {'commits_count': 10, 'yyyymmdd_date': '20180102'}]
