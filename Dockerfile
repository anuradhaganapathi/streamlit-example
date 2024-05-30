FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt ./requirements.txt

RUN apt-get update && apt-get install -y --no-install-recommends \
        ca-certificates \
        netbase \
        && rm -rf /var/lib/apt/lists/*

RUN pip3 install -r requirements.txt

#RUN  pip3 install --no-cache-dir awscli==1.14.5 s3cmd==2.0.1 boto3 pyyaml

RUN pip3 install nltk

RUN python -m nltk.downloader -d /usr/share/nltk_data all


ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY 
ARG AWS_DEFAULT_REGION="eu-north-1"

EXPOSE 8501

COPY . .

ENTRYPOINT ["streamlit", "run"]

CMD ["streamlit_app.py"]
