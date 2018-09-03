import logging
def get_user_info(username=None):
    return {"user_info": username}

def get_commits_info(username=None, time_range=None):
    return [{'commits_count': 10, 'yyyymmdd_date': '20180101'},
            {'commits_count': 10, 'yyyymmdd_date': '20180102'}]

def get_commits_infoUser(organization=None, repository=None, usrName=None):
    logging.info('executing get_commits_infoUser method')
    logging.debug('organization=%s', organization)
    logging.debug('repository=%s', repository)
    logging.debug('usrName=%s', usrName)
    return [{'org_info':organization, 'repos_info':repository, 'usr_info':usrName},
            {'org_info':organization, 'repos_info':repository, 'usr_info':usrName}]
