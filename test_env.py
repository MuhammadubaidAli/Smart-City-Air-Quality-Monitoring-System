from dotenv import load_dotenv
import os

load_dotenv("config/.env")

print("USER:", os.getenv("SNOWFLAKE_USER"))
print("ACCOUNT:", os.getenv("SNOWFLAKE_ACCOUNT"))
print("WAREHOUSE:", os.getenv("SNOWFLAKE_WAREHOUSE"))
print("DATABASE:", os.getenv("SNOWFLAKE_DATABASE"))
print("SCHEMA:", os.getenv("SNOWFLAKE_SCHEMA"))