import argparse
import logging
import os
import time

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def log_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f"Error in {func.__name__}: {e}")
            raise
    return wrapper

def time_execution(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logger.info(f"Execution time for {func.__name__}: {end_time - start_time} seconds")
        return result
    return wrapper

@log_exceptions
def read_file(file_path):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"No such file: {file_path}")
    with open(file_path, 'r') as file:
        return file.read()

@log_exceptions
def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

@time_execution
def process_content(content):
    # Example processing: count word frequency
    words = content.split()
    word_count = {}
    for word in words:
        word = word.lower().strip('.,!?')
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

def main():
    parser = argparse.ArgumentParser(description='Process a text file and output the result to another file.')
    parser.add_argument('input_file', help='The path to the input text file')
    parser.add_argument('output_file', help='The path to the output text file')
    args = parser.parse_args()

    try:
        logger.info(f"Reading from {args.input_file}")
        content = read_file(args.input_file)
        
        logger.info("Processing content")
        processed_content = process_content(content)
        
        processed_content_str = '\n'.join([f"{word}: {count}" for word, count in processed_content.items()])
        
        logger.info(f"Writing to {args.output_file}")
        write_file(args.output_file, processed_content_str)
        
        logger.info("Processing complete")
    except Exception as e:
        logger.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
