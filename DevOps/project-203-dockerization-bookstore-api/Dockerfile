FROM python:alpine
COPY . /app
WORKDIR /app 
RUN pip install -r requirements.txt
EXPOSE 80
CMD python ./app.py

#workdir = cd
#-r = read only
#cmd runs the app
#expose 80 is default for this app (this port is container's port)


