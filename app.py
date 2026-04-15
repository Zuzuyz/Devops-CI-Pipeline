import logging

logging.basicConfig(level=logging.INFO)

def add(a, b):
    logging.info("Adding two numbers")
    return a + b

if __name__ == "__main__":
    result = add(2, 3)
    logging.info(f"Result is {result}")