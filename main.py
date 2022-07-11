import requests

data = {
    'username': 'name',
    'embeds': [{
        'title': 'title',
        'description': "desc"
    }]
}
webhookurl = "urlhere"
result = requests.post(webhookurl,json=data)
try:
    
    result.raise_for_status()
except:
    pass