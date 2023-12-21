import re
import sys


def count_fullwidth_text(text):
    # コメントアウトした文字は数えない
    text = re.sub(r"<!--.*?-->", "", text)

    # ルビは数えないので削除
    text = re.sub(r"<rt>.*?</rt>", "", text)

    # 見出しは数えない
    text = re.sub(r"^#.*$", "", text, flags=re.MULTILINE)

    # 半角文字は数えない
    text = re.sub(r"[\x00-\x7F]", "", text)

    return len(text)


def read_markdown_file(file_path):
    try:
        with open(file_path, "r", encoding="utf=8") as file:
            return file.read()
    except Exception as e:
        return str(e)


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    markdown_content = read_markdown_file(file_path)

    if isinstance(markdown_content, str):
        text_count = count_fullwidth_text(markdown_content)
        print(f"ファイルの文字数は {text_count} です．")
    else:
        print("Error reading file")


if __name__ == "__main__":
    main()
