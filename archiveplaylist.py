import requests
import time
from bs4 import BeautifulSoup
YOUR_PLAYLIST_ID = ""
YOUR_API_KEY = ""
WebArchiveURLSave = "https://web.archive.org/save/"
def archive_videos(pageToken=None):
    url = f"https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=50&playlistId={YOUR_PLAYLIST_ID}&key={YOUR_API_KEY}"
    if pageToken:
        url += f"&pageToken={pageToken}"
    response = requests.get(url)
    data = response.json()
    for item in data["items"]:
        title = item["snippet"]["title"]
        video_url = "https://www.youtube.com/watch?v=" + item["snippet"]["resourceId"]["videoId"]
        Theme_RefreshURL = video_url + "&themeRefresh=1"
        print("Getting: " + Theme_RefreshURL)
        print("Title: " + title)
        try:
            response = requests.get(WebArchiveURLSave + Theme_RefreshURL)
            if response.status_code == 200:
                print("Successfully archived the link: " + Theme_RefreshURL)
            else:
                print("ERROR The link: " + Theme_RefreshURL + " wasn't archived or occurred an error with connection. Or this capture was already saved.")
        except Exception as e:
            print("ERROR The link: " + Theme_RefreshURL + " wasn't archived or occurred an error with connection.")
            print("Exception: ", e)
            time.sleep(1)
    if "nextPageToken" in data:
        archive_videos(data["nextPageToken"])

archive_videos()
