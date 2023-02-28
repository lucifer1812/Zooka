from enum import auto
from turtle import width
import requests
import tkinter as tk
from tkinter import *




url = "https://weatherapi-com.p.rapidapi.com/current.json"

querystring = {"q":"SW1"}

headers = {
    "X-RapidAPI-Key": "ebf40647c0msh0a4d28506aa8d50p1e05f0jsn0637ba971d03",
    "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

# print(response.text)
s=response.text
s=str(s)
# type(s)
import json
t=json.loads(s)
q=t['current']
print(q)
r=q['condition']
print(r)
