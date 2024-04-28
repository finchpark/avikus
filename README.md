## 준비

- docker 가 설치돼 있어야 한다.


## 빌드

```sh
docker compose up
```

위 명령을 통해 빌드가 되고 아래 docker container가 생성된다.

- avikus-db-1: PostgreSQL DB
- avikus-server-1: 실행할 수 있는 서버
- avikus-test-server-1: 테스트를 수행하는 서버


## 실행

container가 정상적으로 실행되었다면, 브라우저에서 주소창에 아래 주소를 입력하면 Swagger UI를 확인할 수 있다.

```sh
http://localhost:8000/docs
```


## 테스트

테스트는 `docker compose up`을 통해 자동으로 실행된다.

로그는 다음 명령을 통해 확인할 수 있다.

```sh
docker logs avikus-test-server-1
```