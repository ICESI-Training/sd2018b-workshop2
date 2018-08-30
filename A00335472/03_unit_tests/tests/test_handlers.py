import pytest
import connexion
import mock
import pdb
from gm_analytics import handlers

flask_app = connexion.FlaskApp(__name__)
# flask_app.add_api('swagger.yml')
flask_app.add_api('/home/pi/so-microservices-python-part2/03_unit_tests/gm_analytics/swagger/indexer.yaml')


@pytest.fixture(scope='module')
def client():
    with flask_app.app.test_client() as c:
        yield c

# @pytest.fixture
# def client():
    # flask_app = connexion.FlaskApp(__name__)
    # flask_app.add_api('/home/pi/so-microservices-python-part2/03_unit_tests/gm_analytics/swagger/indexer.yaml')
#     return flask_app.app.test_client()


@pytest.fixture
def user_info():
    return {'user_info': 'dummy.user'}


def test_get_user_info(mocker, client, user_info):
    # GIVEN not query parameters or payload
    # WHEN I access to the url GET /users/daniel.barragan
    # THEN the information for an user must be returned
    mocker.patch.object(handlers, 'get_user_info', return_value=user_info)
    response = client.get('/users/daniel.barragan')
    pdb.set_trace()
    assert {"user_info": "dummy.user"} in response.data
    assert response.status_code == 200

#  https://stackoverflow.com/questions/42934525/how-to-test-a-connexion-flask-app
# https://github.com/pallets/flask/tree/1.0.2/examples/tutorial/tests
