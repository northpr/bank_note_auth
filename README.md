Source: [Github](https://github.com/DARK-art108/Bank-Note-Authentication)

# Docker
1. Create an `app` directory and move `app.py`, `requirements.txt`, and `rfc.pkl` into `app`
2. Create `Dockerfile`
3. Build the docker image
```
docker build -t bank_auth .
```
4. Run it
```
docker run bank_auth
```
5. Go to `http://127.0.0.1:8000/docs` and this is the Swagger UI of FastAPI.