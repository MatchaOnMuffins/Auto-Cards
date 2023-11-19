FROM python:3.10

COPY requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

COPY install_nlp.sh /tmp/install_nlp.sh

RUN /tmp/install_nlp.sh

COPY . /app

WORKDIR /app

CMD ["streamlit", "run", "main.py"]