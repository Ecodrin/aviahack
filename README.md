Run:
```sh
docker build .
```

Then:
```sh
docker run -p 8080:8080 --name wrpyapi
```

Connect via:
```sh
docker exec -it wrpyapi /bin/bash
```
or via web-browser:
```http
http://127.0.0.1:8080/lab
```