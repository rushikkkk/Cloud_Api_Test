import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def log(response, rq_body=None):
    logger.info(f"REQUEST METHOD: {response.request.method}\n")
    logger.info(f"REQUEST URL: {response.url}\n")
    # logger.info(f"REQUEST BODY: {rq_body}\n")
    logger.info(f"STATUS CODE: {response.status_code}\n")
    logger.info(f"RESPONSE TIME: {response.elapsed.total_seconds() * 1000:.0f} ms\n")
    logger.info(f"RESPONSE HEADERS: {response.headers}\n")
    logger.info(f"RESPONSE BODY: {response.text}\n.\n.")
