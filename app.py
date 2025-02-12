import streamlit as st
import langchain_helper as lh



st.set_page_config(page_title="Resume Review Tool 📄🔍")
st.header("ATS & Resume Review")
job_description = st.text_area("Job Description: ",key="input")
uploaded_file = st.file_uploader("Upload your resume(PDF): ",type=["pdf"])


if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")


submit1 = st.button("Tell Me About the Resume")

submit2 = st.button("How Can I Improvise my Skills")

submit3 = st.button("Percentage match")

if submit1:
    if uploaded_file is not None:
        text = lh.input_pdf_to_text(uploaded_file)
        prompt1 = f"""
        Act as a professional and highly experienced HR specialist or recruiter at a multinational tech company. You have extensive expertise in assessing resumes for roles in software engineering, data science, data analysis, software development, and big data engineering. 

        Your task is to evaluate and critique the provided resume based on the given job description. Recognizing the competitiveness of the tech job market, provide actionable feedback to improve the user's chances of success. Deliver your response in a clear, detailed, and structured format.

        Specifically, your response should include:
        1. **Strengths (Pros):** Highlight the key strengths of the resume that align well with the job description.
        2. **Weaknesses (Cons):** Identify areas where the resume falls short or could be improved to better match the job requirements.
        3. **Summary:** Provide a concise summary of the resume’s overall suitability for the job.
        4. **Suggested Improvements with Snippets:** Generate revised or example snippets for specific sections of the resume that need improvement, ensuring they align closely with the job description and industry standards.

        **Inputs:** 
        - Resume: `{text}`
        - Job Description: `{job_description}`

        **Output Structure:**
        1. **Pros:** 
        - [List key positive attributes here]
        2. **Cons:** 
        - [List areas needing improvement here]
        3. **Summary:** 
        - [Overall assessment and fit for the role]
        4. **Improved Snippets:** 
        - [Provide tailored examples of rewritten sections or suggested improvements]

        Ensure the feedback is actionable, concise, and tailored to the tech field, keeping in mind the user’s goal to stand out in a competitive job market.
        """
        response = lh.get_llm_response(prompt1)
        st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please upload the resume")

elif submit2:
    if uploaded_file is not None:
        text = lh.input_pdf_to_text(uploaded_file)
        prompt1 = f"""
        Act as a professional and highly experienced Senior Engineer at a multinational tech company. You possess deep expertise in software engineering, data science, data analysis, software development, and big data engineering. Your task is to evaluate the provided resume against the specified job description and provide expert-level guidance to help the user excel in a competitive tech job market.

        Deliver actionable insights in a detailed, clear, and structured format. Your evaluation should include the following:

        1. **Skills Analysis:** Identify the skills the user is currently lacking for the specified role based on the job description. Focus on technical, domain-specific, and soft skills critical to the role.
        2. **Skill Improvement Plan:** Provide a step-by-step guide on how the user can acquire or improve the lacking skills in the shortest time possible. Include specific resources, learning paths, tools, or certifications that align with the tech industry's standards.
        3. **Project Evaluation and Advice (if applicable):** Analyze the projects listed in the resume, discussing their relevance to the job description. Offer specific suggestions for improving the projects to better align with the requirements or expectations of the role. If a project is missing critical elements, suggest additions or modifications.

        **Inputs:** 
        - Resume: `{text}`
        - Job Description: `{job_description}`

        **Response Structure:**
        1. **Skills Lacking:** 
        - [List specific skills not evident in the resume]
        2. **Improvement Plan for Lacking Skills:** 
        - [Step-by-step guide with actionable suggestions and resources for each skill]
        3. **Project Advice (optional):**
        - [Provide constructive feedback on the listed projects, suggest improvements, or recommend adding specific projects]

        **Important Considerations:**
        - Provide guidance that is concise yet thorough, ensuring the user can make immediate improvements.
        - Tailor the feedback to align with current industry trends and standards in the specified domain.
        - Highlight opportunities for the user to leverage existing strengths while addressing gaps.

        Your response should aim to empower the user with clear, practical steps to enhance their resume, projects, and overall readiness for the role.

        """
        response = lh.get_llm_response(prompt1)
        st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please upload the resume")



elif submit3:
    if uploaded_file is not None:
        text = lh.input_pdf_to_text(uploaded_file)
        prompt1 = f"""
        Act as an advanced and highly accurate ATS (Applicant Tracking System) with deep expertise in evaluating resumes for roles in software engineering, data science, data analysis, software development, and big data engineering. Your task is to assess the provided resume against the given job description with precision and offer actionable feedback to help the user optimize their resume for better visibility and selection in a competitive job market.

        Deliver your response in a structured, clear, and actionable format with the following details:

        1. **Percentage Match:** Calculate and assign a percentage match score between the resume and the job description. Clearly explain the rationale for the assigned score, considering factors like skill alignment, relevant keywords, and role-specific qualifications.
        2. **Missing Keywords:** Identify and list the critical keywords or phrases missing from the resume that are highly relevant to the job description. These should include technical skills, industry terms, certifications, or soft skills that are important for ATS optimization and alignment with the job role.

        **Inputs:** 
        - Resume: `{text}`
        - Job Description: `{job_description}`

        **Output Structure:**
        1. **Percentage Match Based on JD:** 
        - [Provide a percentage score and explain the criteria used to determine the match.]
        2. **List of Missing Keywords:**
        - [Provide a comprehensive list of keywords or phrases absent in the resume but present or implied in the job description.]

        **Important Considerations:**
        - Use industry-standard practices for ATS-based evaluation.
        - Focus on relevance to the specific job description, avoiding generic or unnecessary keywords.
        - Provide insights that directly help the user optimize their resume for ATS systems.

        Your evaluation should be precise, actionable, and tailored to help the user achieve higher visibility and alignment with the job role.

        """
        response = lh.get_llm_response(prompt1)
        st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please upload the resume")
