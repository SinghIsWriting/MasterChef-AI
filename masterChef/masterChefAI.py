from boltiotai import openai
import os
import sys
from decouple import config

try:
  openai.api_key = config('API_KEY')
except:
  sys.stderr.write("""
  You haven't set up your API key yet.

  If you don't have an API key yet, visit:

  https://platform.openai.com/signup

  1. Make an account or sign in
  2. Click "View API Keys" from the top right menu.
  3. Click "Create new secret key"

  Then, open the Secrets Tool and add OPENAI_API_KEY as a secret.
  """)
  

def masterChef(components):
  if openai.api_key == "":
    sys.stderr.write("""
    You haven't set up your API key yet.
    
    If you don't have an API key yet, visit:
    
    https://platform.openai.com/signup
  
    1. Make an account or sign in
    2. Click "View API Keys" from the top right menu.
    3. Click "Create new secret key"
  
    Then, open the Secrets Tool and add OPENAI_API_KEY as a secret.
    """)
    return False
  else:
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "system",
            "content": "You are a helpful and intelligen master chef. Fist introduce yourself as Master Chef. You can write any type of food recipes which can be cooked or prepare.You can use relevant emoticons in your recipes to make it interactive to user. You are only allowed to answer food related queries. If you do not know the answer then simply tell the user that you have not cooked or prepare the food asked by the user in a gentle manner."
        },
        {
            "role": "user",
            "content": f"Tell me a recipe of {components}. Make sure you have a nice name for this recipe listed at the start. Then share the recipe in step-by-step manner. In the end, write a fact about the recipe or any of the item used in the recipe."
        }])
    return response['choices'][0]['message']['content']

def masterChefPro(components):
  if openai.api_key == "":
    sys.stderr.write("""
    You haven't set up your API key yet.
    
    If you don't have an API key yet, visit:
    
    https://platform.openai.com/signup
  
    1. Make an account or sign in
    2. Click "View API Keys" from the top right menu.
    3. Click "Create new secret key"
  
    Then, open the Secrets Tool and add OPENAI_API_KEY as a secret.
    """)
    return False
  else:
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "system",
            "content": "You are a helpful and intelligen master chef. Fist introduce yourself as Master Chef. You can write any type of food recipes which can be cooked or prepare using ingredients provided by user. You can use relevant emoticons in your recipes to make it interactive to user. You are only allowed to answer food related queries. If you do not know the answer then simply tell the user that you have not cooked or prepare the food using ingredients given by the user in a gentle manner."
        },
        {
            "role": "user",
            "content": f"Tell me a recipe using the item listed as available. Make sure you have a nice name for this recipe listed at the start. Then share the recipe in step-by-step manner. In the end, write a fact about the recipe or any of the item used in the recipe. The items are available: {components}"
        }])
    return response['choices'][0]['message']['content']
