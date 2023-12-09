FROM python:3.11-bullseye

ENV SHELL=/bin/bash
EXPOSE 8080

RUN apt update && apt install -y \ 
    vim \
    git \
    gcc \
    make

WORKDIR /app/

COPY . /app/

#building WaveRange
RUN ./wrbuild.sh

#installing jupyter
RUN pip install --upgrade pip && pip install \
    jupyterlab \
    jupyter -U  

#installing dependencies
RUN pip install -r requirements.txt

#running jupyter at init
ENTRYPOINT jupyter lab \
    --notebook-dir=/app/ \
    --ip=0.0.0.0 \
    --no-browser \
    --allow-root \
    --port=8080 \
    --NotebookApp.token='' \
    --NotebookApp.password='' \
    --FileContentsManager.delete_to_trash=True