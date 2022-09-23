FROM python:3.9-slim

EXPOSE 8501

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install altair pandas streamlit schedule

ADD ./tunebot.py /app/tunebot.py

ENTRYPOINT ["streamlit", "run", "tunebot.py", "--server.port=8501", "--server.address=0.0.0.0"]
