import logging
from httpx import Response

class HTTPResponseHandler:
    @staticmethod
    def parse_response(response: Response) -> dict:
        """
        HTTP response parsing & 응답 표준화.
        - 성공: `header.res_code = 200`
        - 실패: `header.res_code = 400`
        """
        try:
            if response.status_code == 200:
                data = response.json()

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
                logging.error(f"HTTP Error: {response.status_code} - {response.text}")
                return {
                    "header": {"res_code": response.status_code},
                    "data": {data}
                }

        except Exception as e:
            logging.error(f"Failed to parse response: {e}")
            return {
                "header": {"res_code": 500},
                "data": {"error_description": "Invalid response format", "error_code": "PARSING_ERROR"}
            }
