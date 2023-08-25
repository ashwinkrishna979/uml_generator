
import os
import replicate
from django.conf import settings

def summariser(txt):
    text=[]
    os.environ["REPLICATE_API_TOKEN"]=settings.REPLICATE_KEY
    output = replicate.run(
        "replicate/flan-t5-xl:7a216605843d87f5426a10d2cc6940485a232336ed04d655ef86b91e020e9210",
        #input={"prompt": 'find out the usecase diagram entities in the following statement in a comma seperated form (actor and usecase should be comma separated). System should allow user to send message'}
        input={"prompt": f'remove ambiguity from the text document. {txt}'}

    )

    for item in output:
        # https://replicate.com/replicate/flan-t5-xl/versions/7a216605843d87f5426a10d2cc6940485a232336ed04d655ef86b91e020e9210/api#output-schema
        text.append(item)

    out=['_'.join(text)]
    return out[0]