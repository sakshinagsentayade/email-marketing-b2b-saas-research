from datetime import date
from youtube_transcript_api import YouTubeTranscriptApi
video_id = "IKG7i0Hvhxg"
yts = YouTubeTranscriptApi()
transcript = yts.fetch(video_id)
text = " ".join([item.text for item in transcript])
print(text)

title="B2B Email Newsletter Strategies for Growth"
source_url="https://www.youtube.com/watch?v=IKG7i0Hvhxg"
date="2025-06-18"