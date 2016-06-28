# coding: utf-8
import os
from fabric.api import *
from fabric.decorators import hosts

env.user = 'bxzz'
env.code_base = ''
env.dir_name = 'lunchplace'

TEST_CONN = 'dongsheng@yun.zhiyoujy.com'


@hosts(TEST_CONN)
def deploy():
    HOME_DIR = '/home/dongsheng'
    env_prefix = 'source '+os.path.join(HOME_DIR, 'python_env/work/bin/activate')
    proj_dir = os.path.join(HOME_DIR, env.dir_name)
    with cd(proj_dir):
        run('git pull --ff')
        with prefix(env_prefix):
            run('supervisorctl  -c '+os.path.join(HOME_DIR, '.supervisord.ini'+' restart bx-wechatapi:*'))
