FROM continuumio/anaconda3
WORKDIR /usr/app/
COPY . .
EXPOSE 5000
RUN pip install -r requirements.txt 
CMD python flask_api.py