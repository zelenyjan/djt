from __future__ import annotations

import multiprocessing

module = "djt"
name = module
bind = "0.0.0.0:8080"
workers = multiprocessing.cpu_count() * 2 + 1
accesslog = "-"
errorlog = "-"
loglevel = "debug"
worker_tmp_dir = "/dev/shm"  # noqa: S108
timeout = 120
