from fastapi import FastAPI,HTTPException,File,UploadFile,Form
import pdfplumber
import re
import os
import requests
from fastapi.middleware.cors import CORSMiddleware




import os
HF_TOKEN = os.getenv("HF_TOKEN")

url="https://router.huggingface.co/hf-inference/models/facebook/bart-large-cnn"

headers = {
    "Authorization": f"Bearer {HF_TOKEN} ",
}




def get_summary(text):
    payload={
        "inputs":text,
        "parameters":{"max_new_tokens":200}
    }
    response=requests.post(url,headers=headers,json=payload)
    if response.status_code==200:
        return response.json()[0]['summary_text']
    else:
        return f"error:{response.status_code,response.text}"


def chunktext(text,max_chars=1000):
    chunks=[]
    current_chunk=""
    for line in text.split("/n"):
        if len(current_chunk) + len(line) + 1 > max_chars:
            chunks.append(current_chunk.strip())
            current_chunk = line + "\n"
        else:
            current_chunk += line + "\n"

   
    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks

textapp=FastAPI(title="pdf text extractor")

textapp.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_methods=["*"],
    allow_headers=["*"],
)






allowed_content_types={"application/pdf", "application/octet-stream"}
MAX_FILE_SIZE = 10 * 1024 * 1024

@textapp.post("/upload_file")
async def uploadfile(file: UploadFile = File()):
    
    
    

    try:
        with pdfplumber.open(file.file) as pdf:
            text_pages=[]
            for page_number,page in enumerate(pdf.pages,start=1):
                try:
                    text=page.extract_text()
                   
                    if not text:
                        words=page.extract_words()
                        text=" ".join(w['text'] for w in words)
                    if text:
                        
                        text_pages.append(text)

                except Exception as e:
                    print(f"Page number {page_number} extraction failed:{e}")
                    continue
            fulltext="\n\n".join(text_pages).strip()
      

        if not fulltext:
            return {"ok":False,"message":"no extractable text found","text":""}
        else:
            summary=get_summary(fulltext)

        
        
        
    except Exception as e:
        raise HTTPException(status_code=500,detail="failed to process pdf")
    
    
    return {
        "ok":True,
        "full_text":fulltext,
        "summary":summary
        
       
    }

    

        	
