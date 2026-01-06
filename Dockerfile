FROM postgis/postgis
ENV POSTGRES_USER=scotclimpact
ENV POSTGRES_DB=scotclimpact
COPY sql/hazard_data.sql.gz /docker-entrypoint-initdb.d/
#RUN 'gunzip /docker-entrypoint-initdb.d/hazard_data.sql.gz'
