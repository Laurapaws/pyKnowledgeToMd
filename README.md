# pyKnowledgeToMd (for Dataverse/Dynamics 365)
 A little tool to extract knowledge articles into markdown from the Dynamics API

Made for myself, but feel free to use it if you want to. Be sure to update formatters.py to refer to the base URL and GUID table reference for your instance. Just visit the entity in Dynamics and check the URL.

Doesn't make its own api call to save having to bother with auth. Just use a call like this in your browser and download the JSON.
https://YOUR BASE URL.crm.dynamics.com/api/data/v9.1/knowledgearticles

There are lots of improvements that could be made but it would be a case of making them for the sake of making them. If you want to do it for fun, try:
- Improving command line args to give more options.
- Built a templating system so you can customise the output format.
- Download Dataverse-hosted images locally so they can be embedded in the markdown.
- Improving the mess of regex.