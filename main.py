import json
import argparse
from modules.extractors import extract_article_data, update_image_urls
from modules.converters import html_to_markdown
from modules.formatters import markdown_formatter, remove_image_line_breaks

def process_articles(json_file_path):
    with open(json_file_path, 'r') as file:
        full_data = json.load(file)
        articles = full_data.get("value", [])
        
        for article in articles:
            title, description, content, article_number, created_on, keywords, knowledge_article_id = extract_article_data(article)
            if not content:
                print(f"Article {title} has no content")
                continue
            
            content = update_image_urls(content)
            markdown_content = html_to_markdown(content)
            markdown_data = markdown_formatter(title, description, markdown_content, article_number, created_on, keywords, knowledge_article_id)
            markdown_data = remove_image_line_breaks(markdown_data)

            markdown_filename = article.get("articlepublicnumber", "Untitled") + ".md"
            with open(markdown_filename, 'w') as md_file:
                md_file.write(markdown_data)

            print(f"Markdown file saved as {markdown_filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert Knowledge Articles to Markdown files.")
    parser.add_argument("json_file_path", help="Path to the JSON file containing Knowledge Articles.")
    args = parser.parse_args()

    process_articles(args.json_file_path)
