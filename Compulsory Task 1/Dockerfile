FROM pypy:latest
RUN pip install tabulate
WORKDIR /app
COPY . /app
CMD python -u inventory.py