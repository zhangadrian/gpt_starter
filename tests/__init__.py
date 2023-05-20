import json
import os

import pytest

import sys
sys.path.insert(0,'/home/lighthouse/bowen/codes/gpt_starter/')

from app import create_app
from app.api.cms.model.group import Group
from app.api.cms.model.group_permission import GroupPermission
from app.api.cms.model.permission import Permission
from app.api.cms.model.user import User
from app.api.cms.model.user_group import UserGroup
from app.api.cms.model.user_identity import UserIdentity

from config import password, username

app = create_app(
    group_model=Group,
    user_model=User,
    group_permission_model=GroupPermission,
    permission_model=Permission,
    identity_model=UserIdentity,
    user_group_model=UserGroup,
)

app.config['REDIS_HOST'] = "127.0.0.1" # redis数据库地址
app.config['REDIS_PORT'] = 6379 # redis 端口号
app.config['REDIS_DB'] = 0 # 数据库名
app.config['REDIS_EXPIRE'] = 600 # redis 过期时间600秒

@pytest.fixture()
def fixtureFunc():
    with app.test_client() as c:
        rv = c.post(
            "/cms/user/login",
            headers={"Content-Type": "application/json"},
            json={"username": username, "password": password},
        )
        json_data = rv.get_json()
        assert json_data.get("access_token") != None
        assert rv.status_code == 200
        write_token(json_data)


def get_file_path():
    pytest_cache_dir_path = os.getcwd() + os.path.sep + ".pytest_cache"
    if not os.path.exists(pytest_cache_dir_path):
        os.makedirs(pytest_cache_dir_path)
    json_file_path = pytest_cache_dir_path + os.path.sep + "test.json"
    return json_file_path


def write_token(data):
    obj = json.dumps(data)
    with open(get_file_path(), "w") as f:
        f.write(obj)


def get_token(key="access_token"):
    with open(get_file_path(), "r") as f:
        obj = json.loads(f.read())
        return obj[key]
