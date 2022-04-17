    FROM python:3.8
    ENV PYTHONUNBUFFERED 1
    EXPOSE 8000
    EXPOSE 8080
    RUN mkdir code
    COPY requirements.txt code/
    WORKDIR code
    RUN pip3 install --upgrade pip setuptools wheel && pip3 install -r requirements.txt




