from datetime import date
from youtube_transcript_api import YouTubeTranscriptApi
video_id = "XLsAAnNaFOc"
yts = YouTubeTranscriptApi()
transcript = yts.fetch(video_id)
text = " ".join([item.text for item in transcript])
print(text)

title="Interview with Connor Murray"
source_url="https://www.youtube.com/watch?v=XLsAAnNaFOc"
date="2025-06-08"