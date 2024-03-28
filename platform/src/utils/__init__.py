import os


def get_database_uri():
    host = os.environ.get("POSTGRES_HOST")
    password = os.environ.get("POSTGRES_PASSWORD")
    database = os.environ.get("POSTGRES_DB")

    return f"postgresql://postgres:{password}@{host}/{database}"


def get_redis_uri():
    host = os.environ.get("REDIS_HOST")
    password = os.environ.get("REDIS_PASSWORD")
    port = int(os.environ.get("REDIS_PORT", 6379))

    return f"redis://:{password}@{host}:{port}"
