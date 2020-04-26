FROM ubuntu:20.04

RUN rm -rf /var/lib/apt/lists/*
RUN apt-get update -y
RUN apt-get install -y --no-install-recommends python3-pip=3.8
RUN apt-get install -y --no-install-recommends python3-dev=3.8
RUN apt-get clean -y
RUN rm -Rf /usr/share/doc && rm -Rf /usr/share/man


# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]
