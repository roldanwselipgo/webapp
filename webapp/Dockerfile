FROM python:3.9.2
WORKDIR /app
COPY ./requirements.txt ./

RUN apt-get update && \
      apt-get -y install nmap

RUN pip install --no-cache-dir -r requirements.txt
COPY ./ ./
EXPOSE 8000
#CMD flask run --host=0.0.0.0
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" , "--insecure" ]