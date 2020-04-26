FROM ubuntu:20.04

RUN apt-get update -y \
&& apt-get install -y --no-install-recommends python3-pip=20.0.2-5ubuntu1 \
&& apt-get install -y --no-install-recommends python3-dev=3.8.2-0ubuntu2 \
&& apt-get clean \
&& rm -rf /var/lib/apt/lists/* \
&& rm -Rf /usr/share/doc && rm -Rf /usr/share/man

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]
