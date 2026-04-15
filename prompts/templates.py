from langchain_core.prompts import PromptTemplate

# Step 1: Extraction Prompt
EXTRACTION_TEMPLATE = """You are an expert technical recruiter. Your task is to extract information from the following resume.

CRITICAL RULES:
- Do NOT assume or hallucinate skills, tools, or experience not explicitly present in the resume.
- If a section is missing, return empty lists or "None".

Resume:
{resume}
"""
extraction_prompt = PromptTemplate.from_template(EXTRACTION_TEMPLATE)

# Step 2: Evaluation Prompt
EVALUATION_TEMPLATE = """You are an expert technical recruiter evaluating a candidate for a role.
Compare the candidate's extracted details against the job description.

Job Description:
{job_description}

Candidate Extracted Details:
{extracted_details}

CRITICAL RULES:
- Calculate a strict fit score (0-100).
- Be objective. Penalize heavily if core requirements (like years of experience or key frameworks) are missing.
- Provide a clear, step-by-step explanation for the score.
"""
evaluation_prompt = PromptTemplate.from_template(EVALUATION_TEMPLATE)