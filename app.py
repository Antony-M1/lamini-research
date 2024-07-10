# flake8: noqa
import os
import lamini
from dotenv import load_dotenv

load_dotenv()

lamini.api_key = os.environ.get('LAMINI_API_KEY')

def get_start():
    """
        This is the function is a starting point of the application
    """
    llm = lamini.Lamini("meta-llama/Meta-Llama-3-8B-Instruct")
    print(llm.generate("How are you?"))


def main():
    get_start()


if __name__ == '__main__':
    main()
