FROM python:3.8
WORKDIR /home
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN pip install pandas numpy Flask folium
EXPOSE 5000
COPY . .
CMD ["flask", "run"]