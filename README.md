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



### Access Token 발급&갱신 반환값 예제

{
  "header": {
    "res_code": 403
  },
  "data": {
    "error_description": "접근토큰 발급 잠시 후 다시 시도하세요(1분당 1회)",
    "error_code": "EGW00133"
  }
}



{
  "header": {
    "res_code": 200
  },
  "data": {
    "access_token": "토큰",
    "access_token_token_expired": "만료일자",
    "token_type": "Bearer(고정)",
    "expires_in": 86400(만료시간)
  }
}