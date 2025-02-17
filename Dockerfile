# single point of entry for all docker images
FROM python:3.13-slim-bookworm as python

# export poetry to requirements.txt and create wheels
FROM python as builder
WORKDIR /usr/src/app

# install dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc python3-dev libjpeg-dev libcairo2-dev pkg-config zlib1g-dev && \
    pip install --upgrade pip && \
    rm -rf /var/lib/apt/lists/*

# get requirements.txt from poetry file
RUN pip install --upgrade pip
RUN pip install poetry poetry-plugin-export

COPY ../poetry.lock pyproject.toml ./

# convert poetry to requirements txt
RUN poetry export -f requirements.txt --output requirements.txt
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt


# create system with all dependencies insllated
FROM python as runtime
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update && \
    apt-get install -y --no-install-recommends netcat-openbsd libnss-unknown libmagic1 weasyprint gettext && \
    rm -rf /var/lib/apt/lists/*

# create the appropriate directories
ENV APP_NAME=src
ENV APP_HOME=/home/app/$APP_NAME
RUN mkdir -p $APP_HOME

# copy wheels from builder
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install --no-cache /wheels/*


# final python image
FROM runtime as production

ARG RELEASE_VERSION
ENV RELEASE_VERSION=${RELEASE_VERSION}

WORKDIR $APP_HOME

# copy project
COPY .. $APP_HOME

# modify entrypoint
RUN sed -i 's/\r$//g'  $APP_HOME/entrypoint
RUN chmod +x  $APP_HOME/entrypoint

ENTRYPOINT ["./entrypoint"]
