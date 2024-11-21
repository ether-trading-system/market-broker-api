import logging
from httpx import Response

class HTTPResponseHandler:
    @staticmethod
    def parse_response(response: Response) -> dict:
        """
        HTTP response parsing & 응답 표준화.
        - 성공: header.res_code = 200
        - 실패: header.res_code = 400 또는 HTTP 상태 코드
        """
        try:
            # JSON 응답 시도
            data = response.json()
        except Exception:
            # JSON 파싱 실패 시, 응답 텍스트 사용
            data = {"error_description": response.text, "error_code": "INVALID_JSON_RESPONSE"}

        try:
            if response.status_code == 200:
                if "error_code" in data:
                    # 한투 API 에러 응답 처리
                    return {
                        "header": {"res_code": 400},    # Bad Request
                        "data": data
                    }

                # 성공 응답 처리
                return {
                    "header": {"res_code": 200},        # Success
                    "data": data
                }

            else:
                # HTTP 상태 코드가 200이 아닌 경우
                logging.warning(f"HTTP Error: {response.status_code} - {response.text}")
                return {
                    "header": {"res_code": response.status_code},
                    "data": data  # 여기서 안전하게 초기화된 data 사용
                }

        except Exception as e:
            logging.error(f"Failed to parse response: {e}")
            return {
                "header": {"res_code": 500},
                "data": {"error_description": "Invalid response format", "error_code": "PARSING_ERROR"}
            }
