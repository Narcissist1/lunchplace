from .config import QINIU_BUCKET, QINIU_ACCESS_KEY, QINIU_SECRET_KEY
from qiniu import Auth

qiniu_auth = Auth(QINIU_ACCESS_KEY, QINIU_SECRET_KEY)


def get_qiniu_token():
    return qiniu_auth.upload_token(QINIU_BUCKET)