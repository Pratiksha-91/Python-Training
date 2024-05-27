#Candidate Dashboard


from fastapi import FastAPI,HTTPException, UploadFile, File
from pymongo import MongoClient
from datetime import datetime
import gridfs

#MongoDb connectivity 
client = MongoClient("mongodb://localhost:27017")
db = client["Demo"]

collection = db["jobDesc"]
usercollection = db["users"]
jobapplicationCollection = db["japplication"]

fs = gridfs.GridFS(db)

app = FastAPI()

#FastAPI to see all jobs
@app.get("/Get_all_jobs/")

async def Get_all_jobs():

    jobs = collection.find({"Status":"Open"},{"_id":1,"title":1,"department":1,"location":1,"ReSkills":1,"created_at":1})

    result = []

    for j in jobs:
        j['_id'] = str(j['_id'])
        result.append(j)
    return {"All Jobs":result}


#API For searching particular job
@app.get("/search job/")
async def searchJob(title:str):

   
    jobs = collection.find({"title":title,"Status":"Open"},{"_id":1,"title":1,"department":1,"location":1,"ReSkills":1,"created_at":1})

    jobsList = []

    for job in jobs:
         job['_id'] = str(job["_id"]),
         jobsList.append(job )

    if jobsList:
        return {"Current openings":jobsList}        
    else:
        raise HTTPException(status_code=500,detail="No Job vacancy now!!")
    
#Fast API for applying job with uploading resume 
@app.post("/apply-to-job/")
async def applyJob(email: str, jobId: str , resume: UploadFile = File(...)):
    
    candidate = usercollection.find_one({"mail": email})
    
    if candidate:
        
        resume_data = await resume.read()

        resume_id = fs.put(resume_data, filename=resume.filename, contentType=resume.content_type)
 
        job_application = {
            "JobID": jobId,
            "Candidate_Id": str(candidate["_id"]),
            "resume_id": resume_id,
            "resume_filename": resume.filename,
            "resume_content_type": resume.content_type,
            "created_at": datetime.today().strftime("%Y-%m-%d")
        }        
        application = jobapplicationCollection.insert_one(job_application)
        if application.acknowledged:
            return {"Message": "Applied Successfully!"}
        else:
            raise HTTPException(status_code=500, detail="Application not applied")
    else:
        raise HTTPException(status_code=404, detail="Sign up to apply for the job")
