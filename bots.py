"""
This bot listens to port 5002 for incoming connections from Facebook. It takes
in any messages that the bot receives and echos it back.
"""
import os
from flask import Flask, request
from pymessenger.bot import Bot
import json


app =  Flask(__name__)
PAT = "EAAdGfq5c0sQBABeCdZC1yPfodlelFzO2vT3JZCua81ABlE4LilswQXiXWNZBz59ICIC79vyzbsd18djPmoNZAMdlEox7JwKr8zmoiyzCGeDgHh1NR7dahMoTJ8eqgmnZC40C13hLCxsAgsAQBgm16ER9ItqkyrkUcMZCOFxg3LuwZDZD"
VT = "90293269"
bot = Bot(PAT)

@app.route("/", methods=['GET', 'POST'])

def hello():
    if request.method == 'GET':
        if request.args.get("hub.verify_token") == VT:
                return request.args.get("hub.challenge")
        else:
            return 'Invalid verification token'
    if request.method == 'POST':
      output = request.get_json()
      for event in output['entry']:
        messaging = event['messaging']
        for x in messaging:
          if x.get('message'):
            recipient_id = x['sender']['id']
            if x['message'].get('text'):
              elements = [{"title" : "Hello Wandering Stranger, Press play to see what the night holds...",
                                     "image_url" : "https://ak1.picdn.net/shutterstock/videos/6963970/thumb/8.jpg",
                                     "buttons" : [
                                      {
                                        "type" : "postback",
                                        "title" : "Play",
                                        "payload" : "BEGIN"
                                      },{
                                        "type" : "postback",
                                        "title" : "I am not curious",
                                        "payload" : "END"
                                      }
                                                    ]}]
              bot.send_generic_message(recipient_id, elements)       
          elif x.get('postback'):
            recipient_id = x['sender']['id']
            if x.get('postback').get('payload') == 'BEGIN':
              message0 = "You are stranded in a forest and your flashlight flickers out..." 
              bot.send_text_message(recipient_id,message0)
              url1 = "http://ak6.picdn.net/shutterstock/videos/5566106/thumb/8.jpg"
              bot.send_image_url(recipient_id,url1)
              message1 = "Suddenly, you hear a deep growl coming from behind you..."
              bot.send_text_message(recipient_id,message1)
              message2 = "What do you do? ..."
              bot.send_text_message(recipient_id,message2)
              
              elements = [{"title" : "Choose or die",
                                "image_url" : "https://ak1.picdn.net/shutterstock/videos/6963970/thumb/8.jpg",
                                "buttons" : [
                                {
                                  "type" : "postback",
                                  "title" : "Run for my life!",
                                  "payload" : "RUN1"
                                },
                                {
                                  "type" : "postback",
                                  "title" : "Freeze",
                                  "payload" : "FR"
                                }
                              ]}
                          ]
              bot.send_generic_message(recipient_id, elements)
            elif x.get('postback').get('payload') == 'RUN1':
              message3 = "You fall and instead of falling to the ground, you sink into a deep hole... You feel like Alice, down the rabbit hole..."
              bot.send_text_message(recipient_id,message3)
              message4 = "You land softly on a bundle of something. Your eye's take some time to adjust... You suddenly see thousands of red eyes as a deafening screech fills the air..."
              url0 = "https://i0.wp.com/ap-pics.gotpoem.com/ap-pics/item/10472/975.jpg?w=520&ssl=1"
              bot.send_image_url(recipient_id,url0)
              bot.send_text_message(recipient_id,message4)
              message5 = "Suddenly, the screeching stops and a bright light shines ... You see thousands of Rabbits, but something about them looks Evil.. you spot one seated on some kind of throne... What do you do?"
              elements = [{"title" : "Time is ticking...",
                              "image_url" : "https://careerleadershipalignment.com/wp-content/uploads/2017/09/falling-into-a-black-hole-by-Aisha-ashscrapyard.wordpress.com_.jpg",
                              "buttons" : [
                                {
                                "type" : "postback",
                                "title" : "Fight the Rabbits",
                                "payload" : "FIGHT"
                                },
                              {
                              "type": "postback",
                              "title": "Talk to their leader",
                              "payload": "TALK"
                              }
                            ]}]
              bot.send_generic_message(recipient_id, elements)  
            elif x.get('postback').get('payload') == 'END' :
              message6 = "You will never know what awaits in the wonders of adventure! And in the weird roads yet travelled..."
              bot.send_text_message(recipient_id,message6)
              url2 = "https://www.travelwyoming.com/sites/default/site-files/files/styles/16_9_wide/public/assets/Adventure_hero_image.jpg?itok=fLfNGVXH&timestamp=1461077434"
              bot.send_image_url(recipient_id,url2)
            elif x.get('postback').get('payload') == 'FIGHT' :
              message7 = "Thousands of angry bunnies are staring at you, Gaping with frothing mouths of sharp teeth... You decide to fight them..."
              bot.send_text_message(recipient_id,message7)
              url3 = "https://vignette2.wikia.nocookie.net/villains/images/d/d1/Woundwort_kills_Blackavar.png/revision/latest?cb=20160331063058" 
              bot.send_image_url(recipient_id,url3)
              message8 = "You decided to fight, but you decided to die... Sorry, you get eaten and die. Better luck next time..."
              bot.send_text_message(recipient_id,message8)
              url4 = "https://s3.amazonaws.com/cgmagazine/2016/03/donniedarko.jpg"
              bot.send_image_url(recipient_id,url4)
            elif x.get('postback').get('payload') == 'TALK':
              message9 = "You decide to talk to their leader and to negotiate for your life... The rabbit King summons you"
              bot.send_text_message(recipient_id,message9)
              url5 = "https://cdn.drawception.com/images/panels/2016/7-16/3ZAmPmzmW6-6.png"
              bot.send_image_url(recipient_id, url5)
              message11 = "The king summons you to an inner chamber and you have to make a choice..."
              elements = [{"title" : "Be careful what you do....",
                              "image_url" : "https://vignette3.wikia.nocookie.net/amnesia/images/f/f1/115dd9a41957089ea22cb980dd6f27af.jpg/revision/latest?cb=20110624052932",
                              "buttons" : [
                                {
                                "type" : "postback",
                                "title" : "Enter the room",
                                "payload" : "ENTER"
                                },
                              {
                              "type": "postback",
                              "title": "Ignore the King",
                              "payload": "IGNORE"
                              }
                            ]}]
              bot.send_generic_message(recipient_id, elements)   
            elif x.get('postback').get('payload') == 'FR':
              message10 = "To your surprise a small puppy yelps towards you..."
              bot.send_text_message(recipient_id,message10)
              url6 = "https://c.pxhere.com/photos/ee/72/shih_tzu_dog_pet_animal_cute_puppy_purebred_pedigree-1291548.jpg!d"
              bot.send_image_url(recipient_id,url6)
              message12 = "The puppy is hurt, you were being paranoid. You take it back to your tent and help it just before you sleep..."
              bot.send_text_message(recipient_id,message12)
              url7 = "https://static1.fitbit.com/simple.b-cssdisabled-jpg.hd7d4926725cd53dd676d7fbbe4f27a52.pack?items=%2Fcontent%2Fassets%2Fadventures%2Fimages%2Fgallery%2Fyosemite8.jpg"
              bot.send_image_url(recipient_id,url7)
              

        else:
          break
          pass
    return "Success"
if __name__ == "__main__":
    app.run()