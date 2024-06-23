from fastapi import FastAPI, File, UploadFile
import whisper  
from transformers import pipeline  


app = FastAPI()


def save_results(filename, transcript, summary, timestamps):
    try:
        
        with open(filename, "w") as f:
            f.write("Transcript:\n")
            f.write(transcript + "\n")
            f.write("Summary:\n")
            f.write(summary + "\n")
            f.write("Timestamps:\n")
            for timestamp, text in timestamps.items():
                f.write("{timestamp}: {text}\n")
        print("Results saved to: {filename}")
    except Exception as e:
        print("Error saving results: {e}")

model = whisper.load_model("base")  

summarizer = pipeline("summarization", model="facebook/bart-base")  

@app.post("/transcribe_and_summarize")
async def transcribe_and_summarize(audio_file: UploadFile = File(...)):
    try:
        content = await audio_file.read()

        result = model.transcribe(content)
        transcript = result["text"]
        timestamps = result["timestamps"]

        summary = summarizer(transcript)["sentences"][0]["summary_text"]

        filename = "transcript_{audio_file.filename}.txt"

        save_results(filename, transcript, summary, timestamps)

        return {"message": "Transcription and summarization successful!"}
    except Exception as e:
        print("Error during processing: {e}")
        return {"error": "An error occurred: {str(e)}"}


