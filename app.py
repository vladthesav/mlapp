from flask import Flask, render_template, request

from pymongo import MongoClient

client = MongoClient("mongodb+srv://admin:HACKRUpassword@cluster0-d2rxd.gcp.mongodb.net/test?retryWrites=true&w=majority")

db = client.test