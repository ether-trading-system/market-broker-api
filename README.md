# market-broker-api

> 증권사, 거래소 연동 API

## Getting Started

`env.template` 파일을 복사하여 `.env.local` 파일을 생성하고, 환경변수를 설정합니다.

```bash
poetry install
export ENV=local
poetry run start
```

## DB Migration (Alembic)

`env` 파일에 등록한 DB 정보를 읽어 마이그레이션을 실행합니다.

```ini
DB_HOST
DB_PORT
DB_NAME
DB_USER
DB_PASS
```

다음 명령어로 마이그레이션 Model 기준 마이그레이션 파일을 생성합니다.

```bash
alembic revision --autogenerate -m "파일명"
```

다음 명령어로 마이그레이션을 실행합니다.

```bash
alembic upgrade head
```

다른 명령어는 [Alembic 공식 문서](https://alembic.sqlalchemy.org/en/latest/api/commands.html)를 참고하세요.