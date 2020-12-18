FROM python:3.8

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip \ 
  && pip install --user --no-cache-dir -r requirements.txt \
  && rm requirements.txt

ENV PATH="~/.local/bin/:$PATH"