# market-broker-api

> 증권사, 거래소 연동 API

## Getting Started

`env.template` 파일을 복사하여 `.env.local` 파일을 생성하고, 환경변수를 설정합니다.

```bash
poetry install
export ENV=local # windows 환경은 set ENV=local
poetry run start
```

--- 

1. clients : 실제 한투에 API 요청을 보낼 기능 정의.
2. services : 비즈니스 로직을 정의. ex) 토큰 발급 or 갱신, 계좌의 일별 or 월별 수익률 조회 등...
3. routers : 클라이언트(member/rebalance/finance data)의 요청 받아서 서비스 레이어 로직 호출/응답 반환, router 내에는 모듈별 폴더로 분리
4. 한투에서 발생하는 공통 예외 처리