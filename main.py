import re
import requests
from fastapi import FastAPI
import logging
import uvicorn
import extraction
app = FastAPI()




@app.post("/info/{personal_information_string}")
async def personal_information_extraction(personal_information_string):

    #storing the text
    string_data=personal_information_string

    try:
        person = ",".join(extraction.extract_names(personal_information_string))
        phone_number = ",".join(extraction.extract_phone_numbers(personal_information_string))
        email = ",".join(extraction.extract_email_addresses(personal_information_string))

        #dictionary personal information extraction
        result ={
            "Personal Information String": string_data,
            "Person Names": person,

            "Phone Number": phone_number,
            "Email": email
        }

    except Exception as e:
            logging.info(e)

    return result

# Press the green button in the gutter to run the script.
@app.get("/")
async def root():
    return {"message": "This is a simple get request"}



if __name__ =="__main__":
    uvicorn.run(app)
