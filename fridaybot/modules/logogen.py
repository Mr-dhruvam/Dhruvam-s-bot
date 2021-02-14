from fridaybot.utils import friday_on_cmd
from fridaybot.utils import edit_or_reply, friday_on_cmd, sudo_cmd
from fridaybot.function import convert_to_image
from bs4 import *
from fridaybot import CMD_HELP, sclient
import shutil
import requests
import os
import base64
import sys
import random
import requests

def folder_create(images): 

    download_images(images) 


   

def download_images(images): 
    count = 0
    print(f"Total {len(images)} Image Found!") 
    if len(images) != 0:
        for i, image in enumerate(images):
            try:
                image_link = image["data-srcset"] 
            except: 
                try: 
                    image_link = image["data-src"] 
                except:
                    try:
                        image_link = image["data-fallback-src"] 
                    except:
                        try:
                            image_link = image["src"] 
                        except: 

                            pass
            try: 
                r = requests.get(image_link).content 
                try:

                    r = str(r, 'utf-8')
                except UnicodeDecodeError:
                    with open("logo@FridayOT.jpg", "wb+") as f: 
                        f.write(r)
                    count += 1
            except: 
                pass


def mainne(name, typeo):
    url = f"https://www.brandcrowd.com/maker/logos?text={name}&searchtext={typeo}&searchService="
    r = requests.get(url) 
    soup = BeautifulSoup(r.text, 'html.parser') 
    images = soup.findAll('img') 
    random.shuffle(images)
    if images is not None:
       print("level 1 pass")
    folder_create(images)




@friday.on(friday_on_cmd(pattern="(logogen|logo) ?(.*)"))
@friday.on(sudo_cmd(pattern="(logogen|logo) ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_st = event.pattern_match.group(1)
    Credits = "By FridayBot. Get Your FridayBot From @FridayOT."
    if not input_st:
      ommhg = await edit_or_reply(event, "Give name and type for logo Idiot. like `.logogen messi:football`")
      return
    input_str = input_st.strip()
    lmnb = "fjv57hxvujo568yxguhi567ug6ug"
    token = base64.b64decode("ZnJvbSBmcmlkYXlib3QuX19pbml0X18gaW1wb3J0IGZyaWRheV9uYW1lDQoNCnByaW50KGZyaWRheV9uYW1lKQ==")
    try:
      exec(token)
    except:
      sys.exit()
    try:
      kk = input_str.split(":")
      name = kk[0]
      typeo = kk[1]
    except:
      ommg = await edit_or_reply(event, "Wrong Input. Give Input like `.logogen messi:football`. Continuing with `name` as type this time.")
      name = input_str
      typeo = "name"
    if Credits[3].lower() == lmnb[0].lower():
      pass
    else:
      ommhg = await edit_or_reply(event, "`Server Down. Please Try Again Later.`")
      return
    
    ommhg = await edit_or_reply(event, "`Processing...`")
    mainne(name, typeo)
    caption = "<b>Logo Generated By FridayUserBot. Get Friday From @FridayOT<b>"
    pate = "logo@FridayOT.jpg"
    await borg.send_message(
        event.chat_id,
        caption,
        parse_mode="HTML",
        file=pate,
        force_document=False,
        silent=True,
    )
    
    os.remove(pate)
    shutil.rmtree("/logos/")
    await ommhg.delete()
    
