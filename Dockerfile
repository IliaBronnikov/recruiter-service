FROM python:3.9-slim
WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE 1 \
    PYTHONUNBUFFERED 1 \
    PYTHONPATH=$WORKDIR \
    PATH=.venv/bin:$PATH



COPY requirements.txt /code
#COPY ["requirements.txt", "requirements-dev.txt"] ./code

#RUN pip install -r requirements.txt && rm -rf /root/.cache/pip
RUN pip install  -r requirements.txt && rm -rf /root/.cache/pip

COPY . /code