FROM python:3.9
WORKDIR /app

COPY requirements.txt ./requirements.txt
COPY data data

RUN pip install -r requirements.txt
EXPOSE 8080
COPY . .
CMD streamlit run main.py --server.port 8080
