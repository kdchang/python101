from .settings import *
import dj_database_url
# 把 debug 模式關掉
DEBUG = False
# 遵守 HTTPS 連線中的 "X-Forwarded-Proto" header
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# 設定靜態檔位置
STATIC_ROOT = 'staticfiles'
# 設定資料庫
DATABASES = {
	'default': dj_database_url.config()
}
# 允許所有網址連⾄至網站
ALLOWED_HOSTS = ['*']