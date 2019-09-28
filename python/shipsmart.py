#!/usr/bin/python3
import cgi,cgitb
import gspread
import pprint
#from google.auth import compute_engine
from oauth2client.service_account import ServiceAccountCredentials

cgitb.enable()
print("Content-Type: text/html;charset=utf-8")
print()

#creds = compute_engine.Credentials()
scope = ["https://spreadsheets.google.com/feeds"]
creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
client = gspread.authorize(creds)
sheet = client.open_by_url('https://docs.google.com/spreadsheets/d/1Qr5FG_-Qpd3mR2aXCafsMKr8NB5C3HI4vij6T6m0PIk/edit#gid=1976283364').sheet1
list_data = sheet.get_all_records()
dic = list_data[-1]
#print(type(list_data))
#print(list_data)


form = cgi.FieldStorage()
name = form.getvalue('form_type')
#print("test form type: {0}".format(name))

if name == "coo":
    seller_name=str(dic["Shipper's Name and Address"])
    buyer_name=str(dic["Consignee Name and Address"])
    container=str(dic["Number of Container(s)"])
    packages=str(dic["Number of Packages"])
    weight=str(dic["Total Weight"])
    volume=str(dic["Total Volume"])
    amount= int(dic['Price per unit (in Euros)']) * int(dic["Total Volume"])
    destination=str(dic["Port of Discharge"])
    port_discharge=str(dic["Port of Discharge"])
    co_sheet=client.open_by_url('https://docs.google.com/spreadsheets/d/12hBaMGdjGEC1Fbu0oXy0AFRSE90f5zygEiaCH6n7R6g/edit?ts=5d8f6916#gid=0').sheet1
    co_sheet.update_acell('A2',seller_name)
    co_sheet.update_acell('B2',buyer_name)
    co_sheet.update_acell('C2',container)
    co_sheet.update_acell('D2',packages)
    co_sheet.update_acell('G2',weight)
    co_sheet.update_acell('H2',volume)
    co_sheet.update_acell('I2',amount)
    co_sheet.update_acell('J2', port_discharge)
    co_sheet.update_acell('K2',destination)
    print("<a href='https://docs.google.com/spreadsheets/d/12hBaMGdjGEC1Fbu0oXy0AFRSE90f5zygEiaCH6n7R6g/edit?ts=5d8f6916#gid=0'>Redirect to Edit/View Form sheet</a>")
    #print(seller_name, buyer_name, container, packages, weight, volume, amount, destination)

elif name == "invoice":
    seller_name=str(dic["Shipper's Name and Address"])
    buyer_name=str(dic["Consignee Name and Address"])
    destination=str(dic["Port of Discharge"])
    port_discharge=str(dic["Port of Discharge"])
    amount= int(dic['Price per unit (in Euros)']) * int(dic["Total Volume"])
    volume=str(dic["Total Volume"])
    price=str(dic["Price per unit (in Euros)"])
    co_sheet=client.open_by_url('https://docs.google.com/spreadsheets/d/1MciiIe-J7qgnVoP1NifSRxhQrKQuV0FbvT11ZVziS7A/edit?ts=5d8f699a#gid=0').sheet1
    #print(seller_name, buyer_name, destination, port_discharge,amount, volume,price)
    co_sheet.update_acell('A2',seller_name)
    co_sheet.update_acell('B2',buyer_name)
    co_sheet.update_acell('C2',destination)
    co_sheet.update_acell('D2', port_discharge)
    co_sheet.update_acell('E2',amount)
    co_sheet.update_acell('G2',volume)
    print("<a href='https://docs.google.com/spreadsheets/d/1MciiIe-J7qgnVoP1NifSRxhQrKQuV0FbvT11ZVziS7A/edit?ts=5d8f699a#gid=0'>Redirect to Edit/View Form sheet</a>")
