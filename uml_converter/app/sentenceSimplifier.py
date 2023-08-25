import openai
from django.shortcuts import render
from django.conf import settings

def reformat(sentence):

  openai.api_key =settings.OPENAI_API_KEY 


  response = openai.Completion.create(
      model="text-davinci-003",
      prompt=f"{sentence}.make this suitable for a usecase diagram statement in the format actor (replace with the actor in this specific case) should be able to do usecase(replace with use case in this specific case). answer in a single sentence without any formatting. example answer: user should be able to play cricket."
  )

  return response['choices'][0]['text']
#reformat('abs')