FROM python:3.8
COPY ./setup.py /app/setup.py
COPY ./requirements.txt /app/requirements.txt
COPY ./run.sh /app/run.sh
COPY ./src /app/src

WORKDIR /app
RUN pip install -e .
RUN chmod +x /app/run.sh
CMD /app/run.sh
