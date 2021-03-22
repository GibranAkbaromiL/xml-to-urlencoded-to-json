# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 02:19:01 2021

@author: OMMIE
"""

import re
import json
import urllib


"""
Contenty-Type: application/x-www-form-urlencoded
Contenty-Type: application/xml
Contenty-Type: application/json

json => url_encoded
json => XML

url_encoded => json
url_encoded => XML

XML => json
XML => url_encoded
"""

def xml_builder(data):
    container = []
    counter = 1
    while counter < len(data):
        check = counter % 2
        if check == 1:
            key = data[counter-1]
            value = data[counter]
            data_xml = "<"+key+">"+value+"</"+key+">"
            container.append(data_xml)
        counter +=1
    return container

def json_builder(data):
    container = {}
    counter = 1
    while counter < len(data):
        check = counter % 2
        if check == 1:
            key = data[counter-1]
            value = data[counter]
            data_json = {key:value}
            container.update(data_json)
        counter +=1
    return container

def url_encoder_builder(data):
    container = []
    counter = 1
    while counter < len(data):
        check = counter % 2
        if check == 1:
            key = data[counter-1]
            value = urllib.parse.quote(data[counter])
            data_url_encoded = key+"="+value
            container.append(data_url_encoded)
        counter +=1
    return container

def remove_duplicate(data):
    container = []
    for i in data:
        if i not in container:
            container.append(i)
    return container

testing = input("Input = ")

if testing[:1] == "{":
    regex = re.findall( r"\w+\s\w+|\w+",testing)
    data = remove_duplicate(regex)
    #===============================JSON ====> XML ============================
    print("\nXML")
    print("<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?>")
    xml = xml_builder(data)
    for i in xml:
        print(i)
    #==========================================================================
    print("\n==================================================================\n")
    
    #=========================JSON ====> url_encoded ==========================
    print("URL_ENCODED")
    url_encoded = url_encoder_builder(data)
    ampersand = "&"
    print_ = ampersand.join(url_encoded)
    print(print_)

elif testing[:1] == "<":
    regex = re.findall( r"\w+\s\w+|\w+",testing)
    data = remove_duplicate(regex)
    #===============================JSON ====> XML ============================
    print("\nJSON")
    json_ = json_builder(data)
    print(json.dumps(json_))
    #==========================================================================
    print("\n==================================================================\n")
    
    #=========================JSON ====> url_encoded ==========================
    print("URL_ENCODED")
    url_encoded = url_encoder_builder(data)
    ampersand = "&"
    print_ = ampersand.join(url_encoded)
    print(print_)
    
else :
    regex = re.findall( r"\w+\s\w+|\w+",testing)
    data = remove_duplicate(regex)
    #===============================JSON ====> XML ============================
    print("\nJSON")
    json_ = json_builder(data)
    print(json.dumps(json_))
    #==========================================================================
    print("\n==================================================================\n")
    
    #=========================JSON ====> url_encoded ==========================
    print("XML")
    print("<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?>")
    xml = xml_builder(data)
    for i in xml:
        print(i)
    
    
    
    
    
    
    
    
    
    
    
    
    