from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import pickle

def upload_to_youtube(file_path, title="Daily Kids Story", privacy="unlisted"):
    with open("secrets/token.pickle", "rb") as token:
        credentials = pickle.load(token)

    youtube = build("youtube", "v3", credentials=credentials)

    request_body = {
        'snippet': {
            'title': title,
            'description': 'A fun AI-generated kids story.',
            'tags': ['kids', 'story', 'fun'],
            'categoryId': '1'
        },
        'status': {
            'privacyStatus': privacy
        }
    }

    media = MediaFileUpload(file_path, resumable=True)
    video = youtube.videos().insert(part="snippet,status", body=request_body, media_body=media)
    response = video.execute()

    print(f"Video uploaded: https://www.youtube.com/watch?v={response['id']}")
