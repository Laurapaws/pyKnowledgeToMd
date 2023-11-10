import html2text

def html_to_markdown(html_content):
    """Convert HTML content to markdown."""
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.body_width = 0
    return h.handle(html_content)
