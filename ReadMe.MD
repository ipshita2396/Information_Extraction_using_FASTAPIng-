**Objective**

Detect personal information such as Personal names(Indian), email ids , contact numbers from English Language sentences using FastAPI and async API call. 

**Solution** 

1. Extracting Indian  first name and last name : Using a pretrained  NER model using hugging face namely IndiNER
2. Extracting Phone numbers : Using regex 
3. Extracting Email Id : Using Regex 