
import replicate
import os

replicate_api="r8_OrRqvrgfeX5WMfdLitY4NP74oNKH00X4cEfI7"
os.environ['REPLICATE_API_TOKEN'] = replicate_api


import replicate
output = replicate.run(
    "meta/llama-2-70b-chat:35042c9a33ac8fd5e29e27fb3197f33aa483f72c2ce3b0b9d201155c7fd2a287",
    input={"prompt": "You are a bad language detector. You will analize the text and find out if there is any bad language. If there is any bad language you will answer with: 'KO.', else you will answer 'OK'. You won't ever say anything else "}
)
# The meta/llama-2-70b-chat model can stream output as it's running.
# The predict method returns an iterator, and you can iterate over that output.
for item in output:
    # https://replicate.com/meta/llama-2-70b-chat/versions/35042c9a33ac8fd5e29e27fb3197f33aa483f72c2ce3b0b9d201155c7fd2a287/api#output-schema
    print(item, end="")