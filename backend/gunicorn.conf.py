import multiprocessing

bind = "0.0.0.0:8000"
# bind = "unix:/run/justhighlight.sock"
workers = multiprocessing.cpu_count() * 2 + 1
reload_engine = "inotify"
group = "justhighlight"
user = "justhighlight"
reload = True

# logs
loglevel = "debug"
accesslog = "logs/gunicorn/justhighlight.access"
errorlog = "logs/gunicorn/justhighlight.error"