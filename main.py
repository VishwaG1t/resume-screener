import os
import warnings
from dotenv import load_dotenv
from langchain_core.tracers.context import tracing_v2_enabled
from chains.pipeline import pipeline

warnings.filterwarnings("ignore", category=UserWarning, module="pydantic")

# Load environment variables (API keys)
load_dotenv()

def load_text(filepath):
    with open(filepath, "r") as f:
        return f.read()

def main():
    print("Loading Data...")
    job_description = load_text("data/job_description.txt")
    
    candidates = ["strong", "average", "weak"]
    
    for candidate in candidates:
        print(f"\n{'='*40}")
        print(f"Evaluating {candidate.upper()} Candidate...")
        print(f"{'='*40}")
        
        resume_text = load_text(f"data/resumes/{candidate}.txt")
        
        # Enable LangSmith tracing with custom tags for sorting in the dashboard
        with tracing_v2_enabled(project_name=os.getenv("LANGCHAIN_PROJECT"), tags=[f"candidate_{candidate}"]):
            
            # .invoke() executes the full LCEL pipeline
            result = pipeline.invoke({
                "resume": resume_text,
                "job_description": job_description
            })
            
            print(f"Score: {result.score} / 100")
            print(f"Explanation:\n{result.explanation}")

if __name__ == "__main__":
    main()