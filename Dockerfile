FROM postgis/postgis
ENV POSTGRES_USER=scotclimpact
ENV POSTGRES_DB=scotclimpact
COPY sql/hazard_data.sql /docker-entrypoint-initdb.d/
