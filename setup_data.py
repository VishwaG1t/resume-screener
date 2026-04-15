import os

os.makedirs("data/resumes", exist_ok=True)

job_description = """
Role: Data Scientist
Requirements:
- 3+ years of experience in Data Science or Machine Learning.
- Proficient in Python, SQL, and Pandas.
- Experience with Machine Learning frameworks like Scikit-Learn and TensorFlow.
- Strong communication skills.
"""

resumes = {
    "strong": "Experienced Data Scientist with 4 years in the industry. Expert in Python, SQL, Pandas, Scikit-Learn, and PyTorch. Deployed multiple predictive models into production. Excellent presenter and communicator.",
    "average": "Data Analyst with 2 years of experience. Knows Python and SQL well. Uses Pandas for data manipulation. Familiar with basic machine learning concepts but has not used TensorFlow or Scikit-Learn in a professional setting.",
    "weak": "Recent graduate with a degree in Biology. Took one introductory course in Java. Proficient in Microsoft Excel and Word. Hard worker and eager to learn."
}

with open("data/job_description.txt", "w") as f:
    f.write(job_description)

for name, content in resumes.items():
    with open(f"data/resumes/{name}.txt", "w") as f:
        f.write(content)

print("Data files created successfully in the 'data/' folder!")