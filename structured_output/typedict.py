from typing import TypedDict, Annotated, Optional, Literal
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

class college_details(TypedDict):
    college_name: Annotated[str,"Full name of the college"]
    college_established_year : Annotated[int,"Year of establishment of the college"]
    college_location:Annotated[str,"location of the college, including the distance from the central city"]
    courses_offered:Annotated[list[str],"The list of courses offered in the college"]
    minor_courses:Annotated[Optional[list[str]],"The list of minor courses offered by the college"]
    country:Annotated[Optional[Literal["India","Out side India"]],"The country in which the college is located, in India or Outside India"]

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite"
)

structuerd_model = model.with_structured_output(college_details)

print(structuerd_model.invoke("""The CVR College of Engineering was established in 2000. It is approved by the All India Council for Technical Education and accredited by the National Board of Accreditation, India.
                              
CVR College of Engineering offers B.Tech. courses in Civil, CSBS, CSE, CSE (Artificial Intelligence and Machine Learning), CSE (Cyber Security), CSE (Data Science), ECE, EEE, EE (VLSI), EIE, IT and Mechanical Engineering. One of the recommendations of the National Education Policy 2020 of the Government of India is to offer interdisciplinary courses at all levels of study for comprehensive and far reaching proficiency of students. The AICTE recommends that a student be provided genuine choice in Minor subject.

At CVRCE, all B.Tech. students are provided options to take-up Minor programme in Artificial Intelligence & Machine Learning, Cyber Security, Data Science and Internet of Things from third year.

CVR College of Engineering has been granted autonomous status by UGC and is affiliated with Jawaharlal Nehru Technological University, Hyderabad. The college is located in Mangalpally(V), Ibrahimpatnam(M), Ranga Reddy, 20 km from the center of Hyderabad, India. The college is supported by the Cherabuddi Educational Society."""))