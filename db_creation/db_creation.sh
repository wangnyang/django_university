docker run -d --name university_project -p 5433:5432 \
 -v $HOME/DATABASES/university_project:/var/lib/postresql/university_project \
 -e POSTGRES_PASSWORD=university123 \
 -e POSTGRES_USER=sirius \
 -e POSTGRES_DB=university_db \
 postgres

psql -h 127.0.0.1 -p 5433 -U sirius university_db -f init_db.ddl
