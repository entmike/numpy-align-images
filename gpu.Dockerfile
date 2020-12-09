FROM datmo/keras-tensorflow:gpu-py35

ADD models /models
ADD app /app

WORKDIR /app

ENTRYPOINT [ "python", "./go.py" ]