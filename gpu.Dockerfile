FROM datmo/keras-tensorflow:gpu-py35

RUN pip install dlib

ADD models /models
ADD app /app

WORKDIR /app

ENTRYPOINT [ "python", "./go.py" ]