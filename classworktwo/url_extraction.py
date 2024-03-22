import requests

url = 'https://media.licdn.com/media/AAYQAgTPAAgAAQAAAAAAADVuOvKzTF-3RD6j-qFPqhubBQ.png'
home = requests.get(url)
with open('test_for_me.png', mode=cub) as mf:
    mf.write(home.content)
