import re

def extract_article_data(data):
    """Extract data from article."""
    title = data.get("title", "Untitled")
    description = data.get("description", "")
    content = data.get("content", "")
    article_number = data.get("articlepublicnumber", "")
    created_on = data.get("createdon", "")
    keywords_data = data.get("keywords", "")
    keywords = keywords_data.split(", ") if keywords_data else []
    knowledge_article_id = data.get("knowledgearticleid", "")
    return title, description, content, article_number, created_on, keywords, knowledge_article_id

def update_image_urls(content):
    """Update image URLs in content."""
    def replace_image_url(match):
        guid = match.group(2)
        return f"./images/{guid}.png"
    
    return re.sub(r'/api/data/v9\.0/msdyn_knowledgearticleimages(%28|\()(\w{8}-\w{4}-\w{4}-\w{4}-\w{12})(%29|\))\/msdyn_blobfile/\$value', replace_image_url, content)
