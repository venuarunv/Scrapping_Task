from lxml import etree
from bs4 import BeautifulSoup
import requests,json
rs=requests.get('''https://www.booking.com/hotel/de/kempinskibristolberlin.html''')
#print(rs)
##print(rs.content)
#f=open('kem.html','w+',encoding='utf-8')
#f.write((rs.content).decode("utf-8",errors="ignore"))
#exit()
json_string={}
path = '(//*[@id="hp_hotel_name"]//text())[3]'
address='//*[@id="showMap2"]/span[1]'
review='''//*[@id="js--hp-gallery-scorecard"]/a/div/div/div/div/div[1]'''
room_categories='''//div[@class="room-info"]/a'''
review_count='''//*[@id="js--hp-gallery-scorecard"]/a/div/div/div/div/div[2]/div[2]/text()'''
star_class='''//span[@class="_bebcf8d60 _00b78c844"]/span'''

#soup = BeautifulSoup(open('task 1 - Kempinski Hotel Bristol Berlin, Germany - Booking.com.html',encoding='utf-8'),'html.parser')
soup=BeautifulSoup(rs.content,'html.parser')
dom = etree.HTML(str(soup))
hotel_name=dom.xpath(path)
json_string["hotel_name"]=hotel_name[0].replace("\n","")
#print(hotel_name)
alt=dom.xpath('''//li[@class="bui-list__item"]/div/div[1]''')
alt_desc=""
for i in alt:
    if (alt_desc==""):
        alt_desc=alt_desc+" "+i.xpath("string()")
    else:
        alt_desc=alt_desc+" , "+i.xpath("string()")
hotel_desc=alt_desc

#print(alt);
#print(alt_desc);
json_string["Hotel Surrounding"]=alt_desc.replace("\n","");
address=dom.xpath(address)[0].text
json_string["hotel_address"]=address.replace("\n","")

desc=dom.xpath('//*[@id="property_description_content"]//p')

desc_str=""
for i in desc:
    if(desc_str==""):
        desc_str=desc_str+" "+i.xpath("string()")
    else:
        desc_str=desc_str+" , "+i.xpath("string()")
        
hotel_desc=desc_str
json_string["hotel_description"]=hotel_desc

review=dom.xpath(review)[0].text
json_string["hotel_review"]=review

room_categories=dom.xpath(room_categories)
room_categories_str=""
for i in room_categories:
    if(room_categories_str==""):
        room_categories_str=room_categories_str+" "+i.xpath("string()")
    else:
        room_categories_str=room_categories_str+" , "+i.xpath("string()")
    
json_string["hotel_room_categories"]=room_categories_str.replace("\n","")

review_count=dom.xpath(review_count)
#print(review_count)
json_string["hotel_review_count"]=review_count
star_hotel=dom.xpath('''//span[@class="_bebcf8d60 _00b78c844"]/span''')
#print(star_hotel)
if(len(star_hotel)==5):
    rating=5;
#print(rating)
star_classification=rating
#print(json_string)
print(json.dumps(json_string, indent = 3))
