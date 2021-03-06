FOR /F "tokens=* USEBACKQ" %%F IN (`echo %cd%`) DO (SET pwd=%%F)
cd darkspore_server
docker build -t darkspore_server .
cd ..
docker run -it -p 80:80/tcp -p 42127:42127/tcp -v %pwd%\storage:/darkspore_server_storage --name darkspore_server -td darkspore_server
docker exec -it darkspore_server bash /darkspore_server/run-docker.sh
