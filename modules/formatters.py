import re

def markdown_formatter(title, description, content, article_number, created_on, keywords, knowledge_article_id):
    """Format data into markdown. Must be updated with your own base URL and table GUID."""
    return f"""# {title}

**Article Number:** {article_number}
**Created On:** {created_on}
**Knowledge Article ID:** {knowledge_article_id} [(Link to Dynamics)]( ### ADD YOUR BASE URL AND TABLE GUID HERE FROM BROWSER URL ### &pagetype=entityrecord&etn=knowledgearticle&id={knowledge_article_id})
**Keywords:** {', '.join(keywords)}

---

##### {description}

{content}
    """

def remove_image_line_breaks(content):
    """Remove line breaks related to images in markdown content."""
    content = re.sub(r'(!\[[^\]]*?\]\([^\)]*?\))\n', r'\1', content)
    content = re.sub(r'(!\[[^\]]*?)\n([^\]]*?\]\([^\)]*?)\n([^\)]*?\))', r'\1\2\3', content)
    return content

