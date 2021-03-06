import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)
print(dirname)
try:
    load_dotenv(dotenv_path=os.path.join(dirname, ".env"))
except FileNotFoundError:
    pass

bodypart_file = os.getenv("bodypart_file")
stretch_file = os.getenv("stretch_file")
