FROM continuumio/miniconda3

ADD docker-entrypoint.sh ./
ADD testmodule.py ./
ADD requirements.txt ./
RUN chmod 777 ./docker-entrypoint.sh
RUN pip install -r requirements.txt

CMD ["./docker-entrypoint.sh"]
