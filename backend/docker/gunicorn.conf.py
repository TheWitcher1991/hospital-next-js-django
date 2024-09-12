import multiprocessing

name = "wsgi"

bind = "0.0.0.0:5000"

loglevel = "warning"

workers = multiprocessing.cpu_count() * 2

threads = multiprocessing.cpu_count()

max_requests = 1000
max_requests_jitter = 50

timeout = 30
graceful_timeout = 30

accesslog = "-"
errorlog = "-"

preload_app = True

reload = False
