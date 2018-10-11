def test_get_user_info():
    assert 1==1

def get_commits_info():
    assert 1==1

import pytest
import mock
from op_stats.app import app
from op_stats.stats import Stats

@pytest.fixture
def client():
  return app.test_client()

@pytest.fixture
def cpu_percent():
    return 32.5

def test_get_cpuinfo(mocker, client, cpu_percent):
  # GIVEN not query parameters or payload
  # WHEN I access to the url GET /stats/cpu
  # THEN user must obtain the cpu consumption as a percentage
  mocker.patch.object(Stats, 'get_cpu_percent', return_value=cpu_percent)
  response = client.get('/v1/stats/cpu')
  assert '{"cpu_percent": 32.5}' in response.data.decode("utf-8")
assert response.status_code == 200
