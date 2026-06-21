from youtube_transcript_api import YouTubeTranscriptApi
video_id = "LBJ6Bl7Smkw"
yts = YouTubeTranscriptApi()
transcript = yts.fetch(video_id)
text = " ".join([item.text for item in transcript])
print(text)

title="The Ultimate Step-By-Step Guide to Cold Emailing in 2026"
source_url="https://www.youtube.com/watch?v=LBJ6Bl7Smkw&list=PL6bZK00b2D3HEzpnmU7a26pVd9djPQzAL"
date="2025-10-20"