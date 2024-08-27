import os
import argparse
import glob

parser = argparse.ArgumentParser()
parser.add_argument("files", help="File names")
parser.add_argument("--text", help="Text to search for")
args = parser.parse_args()


def get_context(line_content, text, window=5):
    words = line_content.split()
    index = words.index(text)
    start = max(0, index - window)
    end = min(len(words), index + window + 1)
    return " ".join(words[start:end])


log_files = glob.glob(os.path.join(args.files, "*.log"))

for file_path in log_files:
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            for line_number, line in enumerate(file):
                if args.text and args.text in line:
                    context = get_context(line, args.text)
                    print(f"File: {file_path}, Line: {line_number}")
                    print(context)
    else:
        print(f"File not found: {file_path}")
