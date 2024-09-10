FROM python:3.12-slim AS poetry

RUN pip install --upgrade pip \
    && pip install poetry -U

WORKDIR /home/poetry

COPY ./poetry.lock ./pyproject.toml .

RUN poetry export --without-hashes --without dev -f requirements.txt -o requirements.txt