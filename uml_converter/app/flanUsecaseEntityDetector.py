
import os
import replicate
from django.conf import settings
    
def getUsecaseEntity(sentence):



        os.environ["REPLICATE_API_TOKEN"]=settings.REPLICATE_KEY

        entity=[]
        actors=[]
        usecases=[]
        actor = replicate.run(
            "replicate/flan-t5-xl:7a216605843d87f5426a10d2cc6940485a232336ed04d655ef86b91e020e9210",
            #input={"prompt": 'find out the usecase diagram entities in the following statement in a comma seperated form (actor and usecase should be comma separated). System should allow user to send message'}
            input={"prompt": f'find out the usecase diagram actor  in the following sentence. {sentence}'}

        )




        entities=replicate.run(
            "replicate/flan-t5-xl:7a216605843d87f5426a10d2cc6940485a232336ed04d655ef86b91e020e9210",
            #input={"prompt": 'find out the usecase diagram entities in the following statement in a comma seperated form (actor and usecase should be comma separated). System should allow user to send message'}
            input={"prompt": f'find out the action in the following sentence. {sentence}'}

        )


        # The replicate/flan-t5-xl model can stream output as it's running.
        # The predict method returns an iterator, and you can iterate over that output.
        for item in entities:
            # https://replicate.com/replicate/flan-t5-xl/versions/7a216605843d87f5426a10d2cc6940485a232336ed04d655ef86b91e020e9210/api#output-schema
            entity.append(item.lower())


        for item in actor:
        #     # https://replicate.com/replicate/flan-t5-xl/versions/7a216605843d87f5426a10d2cc6940485a232336ed04d655ef86b91e020e9210/api#output-schema
        #     if item  in entity:
            actors.append(item.lower())

            
            
        act_out='_'.join(actors)
        # use_out=['_'.join(usecases)]
        entity_out='_'.join(entity)

        return act_out, entity_out #,act_out,use_out,



#print(getUsecaseEntity('The system should allow user to send message'))


