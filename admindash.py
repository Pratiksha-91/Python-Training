#admin dashboard

from fastapi import FastAPI, HTTPException,Form
from pymongo import MongoClient
from datetime import datetime
from fastapi.responses import JSONResponse
from bson import ObjectId

app = FastAPI()


#MongoDB COnnectivity
client = MongoClient("mongodb://localhost:27017")
db = client["Demo"]
collection = db["jobDesc"]
usercollection = db["users"]
jobapplicationCollection = db["japplication"]

#to posting new job in system 
@app.post("/Post New Job/")
async def posNewJob(title:str= Form(...),description:str= Form(...),department:str= Form(...),location:str= Form(...),employment_type:str= Form(...),salary:str= Form(...),appdeadline:str= Form(...),reSkils:str= Form(...),additional_Info:str= Form(...)):

    job_data ={"title":title,
               "description":description,
               "department":department,
               "location":location,
               "employment_type":employment_type,
               "salary":salary,
               "appdeadline":appdeadline,
               "reskills":reSkils,
               "additionalInfo":additional_Info,
               "Status":"Open",
               "created_at":datetime.today().strftime("%Y-%m-%d")
               }
    result = collection.insert_one(job_data)
    
    if not result.acknowledged:
            raise HTTPException(status_code=500, detail="Failed to insert user into database")

    return {"Job Posted Successfully!!!"}
   
#To see all candidates
@app.get("/get all candidates/")
async def getallcandidates():
    data = usercollection.find()
    result = []
    for doc in data:
        
        doc.pop('_id', None)
        if doc.get('user_type')=="Candidate":
            result.append(doc)
    return {"candidate_data": result}


#get candidate by their email
@app.get("/get candidate by id/")
async def candidatebyId(email:str):
     
     candidate = usercollection.find_one({"mail":email})
     if candidate:
          candidate['_id'] = str(candidate['_id'])
          return candidate
     else:
          raise HTTPException(status_code=404,detail="Candidate Not found!")



#get all jobs whoes status is open
@app.get("/GetAllOpenJobs/")
async def Jobs():
    data = collection.find({"Status":"Open"}, {"_id": 1, "title": 1, "department": 1, "location": 1, "ReSkills": 1,"created_at":1})
    result = []
    for doc in data:
        doc['_id'] = str(doc['_id'])
        result.append(doc)
    return {"job_data": result}

#get all jobs whoes status is Filled
@app.get("/GetAllFilledJobs/")
async def Jobs():
    data = collection.find({"Status":"Filled"}, {"_id": 1, "title": 1, "department": 1, "location": 1, "ReSkills": 1,"created_at":1})
    result = []
    for doc in data:
        doc['_id'] = str(doc['_id'])
        result.append(doc)
    return {"job_data": result}


#Update existing job whith jobid
@app.put("/job/{_id}/update/")

async def updatingJob(jodId:str,updates:dict):
     job = collection.find_one({"_id":jodId})
     if job:
          
          update_job = collection.update_one({"_id":jodId},{"$set":updates})
          if update_job.modified_count == 1:
               return{"message":"Job update successfully"}
          else:
               raise HTTPException(status_code=500, detail="Failed to update job")
     else:
          raise HTTPException(status_code=404, detail="Job not found")
          
 #Updating status of jobs
     
@app.put("/jobStatus/{_id}/update/")
async def updateStatus(jobId:str,status:str):
    id = {"_id": ObjectId(jobId)}  
    update = {"$set": {"Status": status}}  
    st = collection.update_one(id, update)


    
    if st.modified_count == 1:
          return {"Message":"Status updated!!!"}
    else:
          raise HTTPException(status_code=500, detail="Failed to update job")
    

#See application of any job 
@app.get("/see job applications/{JobID}/")
async def fetchJobApplications(jobId:str):
     id = {"JobID": ObjectId(jobId)}
     application = jobapplicationCollection.find(id,{"_id": 1,"JobID":1,"Candidate_Id":1}) 

     application_List = []
     
     for a in application:
         a['_id'] = str(a['_id'])
         a['JobID'] = str(a['JobID'])
         a['Candidate_Id'] = str(a['Candidate_Id'])
         application_List.append(a)
     
     if application_List:
            return application_List
     
     else:
          raise HTTPException(status_code=404,detail="No applications for this Job ")
     
     
     
