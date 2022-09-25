FROM python:3.10

# install PDM
RUN pip install -U pip setuptools wheel
RUN pip install pdm

# install make
RUN apt-get install make

# copy files
COPY . /app
WORKDIR /app

# environment variables
ENV DB_USER user
ENV DB_PASS password
ENV DB_HOST database
ENV DB_PORT 5432
ENV DB_NAME url_shortener
ENV JWT_SECRET secret


CMD ["make", "serve"]
