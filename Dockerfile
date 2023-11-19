FROM python:3.10

COPY requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

COPY install_nlp.sh /tmp/install_nlp.sh

RUN chmod +x /tmp/install_nlp.sh

RUN /tmp/install_nlp.sh

COPY . /app

WORKDIR /app

COPY main.py /app/main.py

HEALTHCHECK CMD curl --fail http://localhost:8080/_stcore/health

ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8080", "--server.address=0.0.0.0"]
