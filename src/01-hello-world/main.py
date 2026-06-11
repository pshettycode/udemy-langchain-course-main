from dotenv import load_dotenv
import os

load_dotenv()

def main():
    print("Hello from 01-hello-world!")
    print(f"Your API key is: {os.getenv('OPENAI_API_KEY')}")


if __name__ == "__main__":
    main()
