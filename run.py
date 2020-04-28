# run.py
import os
import sqlite3
import random
from flask import Flask
import werkzeug.utils
from app import app

#db = sqlite3.connect("database.db")
con = sqlite3.connect("database.db") 
#con.row_factory = sqlite3.Row 
#print("Database opened successfully")  
#con.execute("create table Users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email TEXT UNIQUE NOT NULL, address TEXT NOT NULL)")  
#print("Table created successfully")

if __name__ == '__main__':
    app.run()
