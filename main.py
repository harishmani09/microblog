from flask import Flask, render_template,request
from time import localtime, strftime
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()


def create_app():


    app = Flask(__name__)

    client = MongoClient(os.getenv("MONGODB_URI"))
    app.db = client.microblog



    @app.route('/', methods=['GET','POST'])
    def home():
        
        if request.method == 'POST':
            entry_content  =request.form.get('content')
            formatted_date = strftime("%d %b %Y",localtime())
            new_entry = {"content":entry_content,"date":formatted_date}
            # entries.append(new_entry)
            app.db.entries.insert_one(new_entry)
        
        all_entries = app.db.entries.find({})
        return render_template('home.html', posts=all_entries)
        # return render_template('home.html',posts=all_entries)





    # if __name__=="__main__":
    #     app.run(debug=True)
        
    return app