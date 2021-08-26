###############################################
# Base Image
###############################################
FROM python:3.8-slim as python-base

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_VERSION="1.1.8" \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/project" \
    VENV_PATH="/opt/project/.venv"

# prepend poetry and venv to path
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

###############################################
# Builder Image
###############################################
FROM python-base as builder-image

# Update system and install packages
COPY scripts/install-packages.sh /install-packages.sh
RUN chmod +x install-packages.sh
RUN ./install-packages.sh

# install poetry - respects $POETRY_VERSION & $POETRY_HOME
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -

# copy project requirement files here to ensure they will be cached.
WORKDIR $PYSETUP_PATH
COPY ./src $PYSETUP_PATH/src
COPY poetry.lock pyproject.toml $PYSETUP_PATH/

# install runtime deps - uses $POETRY_VIRTUALENVS_IN_PROJECT internally
RUN poetry install

###############################################
# Production Image
###############################################
FROM python-base as runtime-image
COPY --from=builder-image $PYSETUP_PATH $PYSETUP_PATH
WORKDIR $PYSETUP_PATH
