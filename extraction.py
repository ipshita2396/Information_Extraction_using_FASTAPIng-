import re
import requests

def extract_names(string):

    #using https://huggingface.co/ai4bharat/IndicNER for extracting Indian names from text

    response = requests.post("https://ai4bharat-indicner.hf.space/run/predict", json={
        "data": [string
                 ]}).json()

    data = response["data"]

    full_name = []
    for j, i in enumerate(data[0]):

        if j == len(data[0]) - 1:
            continue
    #extracting First name
        if i[1] == 'B-PER':

            #extracting last name for the first name
            if data[0][j + 1][1] == 'I-PER':
                name = i[0] + " " + data[0][j + 1][0]
            else:
                name = i[0]
            full_name.append(name)

    return full_name


#using regex to extract phone numbers

def extract_phone_numbers(string):
    r = re.compile(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')
    phone_numbers = r.findall(string)
    return [re.sub(r'\D', '', number) for number in phone_numbers]

#using regex to extract phone numbers

def extract_email_addresses(string):
    r = re.compile(r'[\w\.-]+@[\w\.-]+')
    return r.findall(string)
