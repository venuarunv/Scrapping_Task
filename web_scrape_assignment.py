from lxml import etree
from bs4 import BeautifulSoup
import json
def extract():
    #Documentation
    #Intialising output string for storing the data Extracted
    json_object={}
    #Xpath for fetching relevant fields from html
    path = '//*[@id="hp_hotel_name"]'
    address='//span[@id="hp_address_subtitle"]'
    review='''(//span[@class="rating notranslate"])[1]/span[1]'''
    room_categories='''//table[@id='maxotel_rooms']//td[@class="ftd"]'''
    review_count='''//p[@id="review_list_score_count"]//text()'''
    alternate_hotels='''//td[@class="althotelsCell tracked"]'''
    star_class='''//span[@class="hp__hotel_ratings__stars hp__hotel_ratings__stars__clarification_track"]/i'''
    #Reading data from html with use of html parser of beautifulSoup and then generating tree using lxml functions
    soup = BeautifulSoup(open('task 1 - Kempinski Hotel Bristol Berlin, Germany - Booking.com.html',encoding='utf-8'),'html.parser')
    dom = etree.HTML(str(soup))
    #Extraction : Extracting the needed fields as said in the assignment
    hotel_name=dom.xpath(path)[0].xpath("string()")
    json_object["Hotel Name"]=hotel_name.replace("\n","")
    address=dom.xpath(address)[0].text
    json_object["Address"]=address.replace("\n","")
    start_hotel=dom.xpath(star_class)
    rating=start_hotel[0].get('class').split()
    star_classification=rating[2]
    json_object["Stars"]=star_classification
    desc=dom.xpath('//*[@id="hotel_main_content"]/div[2]/div[1]//p')
    desc_str=""
    review=dom.xpath(review)[0].text
    json_object["Review Points"]=review
    review_count=dom.xpath(review_count)
    json_object["No of Reviews"]=review_count[1]

    #Hotel Description is spread across multiple <p> element . So collected and assigning it as the combined string
    desc=dom.xpath('//*[@id="hotel_main_content"]/div[2]/div[1]//p')
    desc_str=""
    for i in desc:
        desc_str=desc_str+" "+i.xpath("string()")
    hotel_desc=desc_str
    json_object["Description"]=hotel_desc


    #Hotel Room Categories is spread across multiple element . So collected and assigning it as the combined string
    room_categories=dom.xpath(room_categories)
    room_categories_str=""
    for i in room_categories:
        if (room_categories_str==""):
            room_categories_str=room_categories_str+" "+i.xpath("string()")
        else:
            room_categories_str=room_categories_str+" , "+i.xpath("string()")
    json_object["Room Categories"]=room_categories_str.replace("\n"," ")
    review_count=review_count[1]
    #Hotel Alternate is spread across multiple element . So collected and assigning it as the combined string
    alternate_hotels=dom.xpath(alternate_hotels)
    alternate_hotels_str=''
    for i in alternate_hotels:
        if(alternate_hotels_str==""):
            alternate_hotels_str=alternate_hotels_str+" "+i.xpath("string()")
        else:
            alternate_hotels_str=alternate_hotels_str+" , "+i.xpath("string()")
        
    json_object["Alternative Hotels"]=alternate_hotels_str.replace("\n"," ")
    #Extraction is complete.Now converting and print the json_object dictionary to actual string as said in the assignment 
    #print(json_object);
    json_string=json.dumps(json_object)
    #Printing the output in a visually attractive way using intent
    return json.dumps(json_object, indent = 3)
    
if __name__ == '__main__':
    result=extract();
    print(result);