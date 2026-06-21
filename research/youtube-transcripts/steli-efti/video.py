from datetime import date
from youtube_transcript_api import YouTubeTranscriptApi
video_id = "Rfh8BRrqmhU"
yts = YouTubeTranscriptApi()
transcript = yts.fetch(video_id)
text = " ".join([item.text for item in transcript])
print(text)

title="Close CEO Steli Efti im Interview"
source_url="https://www.youtube.com/watch?v=Rfh8BRrqmhU"
date="2024-07-11"