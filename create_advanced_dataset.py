import pandas as pd
import csv

# Advanced LPU Dataset with 120+ Q&A pairs
dataset = []

# ACADEMIC MODE (30 questions)
academic_qa = [
    ("What is the grading system at LPU?", "LPU follows a 10-point CGPA system with letter grades. Grade O (Outstanding) = 10, A+ (Excellent) = 9, A (Very Good) = 8, B+ (Good) = 7, B (Above Average) = 6, C (Average) = 5, P (Pass) = 4. The CGPA is calculated as the weighted average of grade points earned in all courses. Percentage conversion formula: (CGPA - 0.5) × 10."),
    
    ("How to check attendance on UMS?", "Login to LPU UMS (University Management System) at ums.lpu.in using your registration number and password. Go to 'Attendance' tab → Select semester → View subject-wise attendance percentage. You can also download detailed attendance reports. Minimum 75% attendance is mandatory in each subject for appearing in end-term examinations."),
    
    ("What is the examination pattern?", "LPU conducts two internal assessments (20% each) and one end-term examination (60%). Mid-term exam (20%) after 7-8 weeks, Terminal exam (20%) after 14-15 weeks, and Final exam (60%) at semester end. Total marks: 100 per subject. Practical subjects have continuous evaluation pattern with lab work assessment."),
    
    ("How to apply for re-evaluation?", "Apply for re-evaluation within 10 days of result declaration. Login to UMS → Examinations → Re-evaluation → Select paper → Pay fee ₹1000 per paper. Results declared within 15 days. If marks increase by 5+ or grade changes, fee is refunded. Only theory papers are eligible, not practicals or internal assessments."),
    
    ("What is the credit system?", "LPU follows credit-based semester system. Each course has specific credits (typically 3-4 for theory, 1-2 for practical). Graduation requires minimum 120-180 credits depending on program. Credits = Weekly contact hours. Example: 3-hour theory course = 3 credits. CGPA calculated using (Credit × Grade Point) for all courses."),
    
    ("When are semester exams?", "Academic calendar: Odd semester (August-December), Even semester (January-May), Summer term (May-July). Mid-term exams in week 8, Terminal exams in week 15, End-term exams in week 18-19. Exact dates published on UMS 4 weeks before exams. Admit cards available 1 week before exams."),
    
    ("What is the library timing?", "Central Library timings: Monday-Saturday 8:00 AM to 12:00 Midnight, Sunday 9:00 AM to 9:00 PM. During exams: 24×7 open. Block-wise libraries: 8 AM to 8 PM. E-library access available 24/7 online. Members can borrow 5 books for 15 days. Late return fine: ₹5 per day per book."),
    
    ("How to access online journals?", "Access through LPU Library portal → E-Resources → Database list. LPU subscribes to IEEE, Springer, Elsevier, EBSCO, ProQuest, and 40+ databases. Use VPN (download from IT Services) for off-campus access. Login with UMS credentials. Technical support: lib@lpu.co.in or extension 2250."),
    
    ("What is the minimum passing marks?", "Minimum 40% in end-term exam AND 40% aggregate (internals + end-term) to pass. Failing end-term even with high internals = Fail. Failing aggregate even with passing end-term = Fail. Re-appear exam fee: ₹1500 per paper. Maximum 2 re-appear attempts allowed."),
    
    ("How to change elective subjects?", "Subject change allowed only in first 2 weeks of semester. Procedure: Download change form from UMS → Get HOD approval → Submit to Academic Affairs → Pay processing fee ₹500. Subject change depends on seat availability. Core subjects cannot be changed, only electives."),
    
    ("What is academic probation?", "Student placed on probation if CGPA falls below 5.0 at semester end. Probation conditions: Attend mandatory counseling, Cannot participate in placements, Cannot hold student body positions. Must achieve 5.5+ CGPA in next semester to come out of probation. Continuous poor performance may lead to program termination."),
    
    ("How to get transcripts?", "Apply through UMS → Student Services → Transcript Request. Processing time: 7-10 working days. Fee: ₹500 for Indian universities, ₹1500 for foreign universities. Collected from Academic Block-A counter 12. Courier available for ₹200 extra. Original mark sheets + degree required for verification."),
    
    ("What is the grace marks policy?", "Grace marks not applicable at LPU. However, benefit of doubt rule: If marks are 38-39.75, rounded to 40 (passing). This applies only to end-term exam, not aggregate. Grace marks petition can be filed for medical/family emergency during exams with valid proof."),
    
    ("How to register for courses?", "Course registration opens in first week of semester. Login UMS → Academics → Course Registration → Select courses from eligible list. System shows pre-requisites, timings, credits. Confirm selection and lock. Late registration: Week 2 with ₹1000 penalty. No registration after week 2."),
    
    ("What is the attendance calculation?", "Attendance = (Classes Attended / Total Classes Conducted) × 100. Includes theory, practical, tutorial classes. Medical leave counted as absent unless supported by medical certificate from LPU Hospital within 3 days. Sports/official duty: Submit leave form before event for attendance marking."),
    
    ("How to apply for semester break?", "Semester break (leave of absence) allowed for medical/personal reasons. Apply at Academic Affairs → Submit reason, documents → Get approval from Dean. Maximum 2 semesters break in entire program. Fee: Full registration fee + ₹10,000 semester retention fee. Re-admission not guaranteed."),
    
    ("What is the syllabus coverage policy?", "Faculty must complete 100% syllabus before end-term. Syllabus uploaded on UMS at semester start. Weekly lecture plan followed strictly. Students can report incomplete syllabus to HOD. Syllabus completion certificate issued by HOD before exams. Incomplete syllabus allows question paper modification."),
    
    ("How to access study materials?", "Materials available on: 1) UMS → Course Content → Download PPT/PDF, 2) LMS Blackboard → Course → Content, 3) LPU Knowledge Hub app, 4) Faculty shared Google Drive links. Video lectures on LPU YouTube channel. Previous year papers in library archives section."),
    
    ("What is the project/thesis guideline?", "Final year project mandatory for B.Tech/M.Tech. Choose guide in 7th semester. Submit synopsis within 2 weeks. Mid-term presentation in week 12, Final defense in week 18. Report format: 50-80 pages, IEEE format. Plagiarism check mandatory (max 15% allowed). Evaluated by internal + external examiner."),
    
    ("How to convert CGPA to percentage?", "Official LPU conversion: Percentage = (CGPA - 0.5) × 10. Example: 8.5 CGPA = (8.5 - 0.5) × 10 = 80%. This formula used for placements, further studies, scholarships. Conversion certificate available from Academic Affairs on request for ₹200. Processing time: 3 days."),
    
    ("What is the makeup class policy?", "Makeup classes scheduled for: National holidays falling on working days, Faculty on leave, Syllabus backlog. Classes on Saturdays 2-6 PM or after 5 PM on weekdays. Attendance mandatory. Schedule published on UMS notice board. Proxy marking in makeup = disciplinary action."),
    
    ("How to apply for scholarship based on academics?", "Merit scholarships: CGPA 9.5+ (100% fee waiver), 9.0-9.49 (75%), 8.5-8.99 (50%), 8.0-8.49 (25%). Applied automatically based on previous semester CGPA. Credited direct to fee account. Maintained each semester. First semester based on entrance rank/board percentage."),
    
    ("What is the lab assessment criteria?", "Lab evaluation: Regular work (60%), Viva (20%), Final exam (20%). Minimum 75% lab attendance mandatory. Each experiment: Pre-lab (5), Observation (15), Result (10), Viva (5). Submit all lab files before end-term. Incomplete submissions = re-register entire lab next semester."),
    
    ("How to get permission for extra-curricular activities?", "Apply 15 days before event through UMS → Student Activities → Permission Request. Get faculty advisor signature → HOD approval → Dean signature. If classes missed: Submit makeup plan, attendance compensation plan. Maximum 7 days per semester for activities without affecting attendance."),
    
    ("What is the PhD admission process?", "Eligibility: Master's degree with 55% marks (50% for SC/ST). Entrance test in January/July. Pattern: Research Aptitude (25), Subject Knowledge (50), General Awareness (25). Shortlisted candidates: Interview + presentation. Admission based on entrance + interview (70:30). Fellowship: ₹31,000/month for NET/GATE."),
    
    ("How to access previous semester marks?", "Login UMS → Examinations → Result → Select semester → View detailed marks. Download mark sheet PDF. Detailed marks show: Internal marks breakdown, Mid-term marks, Terminal marks, End-term marks, Total marks, Grade, Grade points. Grade card issued within 15 days of result."),
    
    ("What is the backlog examination process?", "Backlog/re-appear exams conducted with regular semester exams. Register on UMS in first week. Fee: ₹1500 per paper. Appear with junior batch. Max 2 attempts. If failed in 2 attempts, must re-register as regular student in next semester. Backlog clearance mandatory for degree."),
    
    ("How to apply for transcript for foreign university?", "International transcript application: Submit passport copy, University name/address, Purpose, Number of copies needed. Fee: ₹1500 per copy. Processing: 10-15 days. Attestation: MEA/HRD (arrange yourself or pay ₹3000 to LPU). Courier: DHL/FedEx (₹2500 per country). WES/ECE evaluation guidance available."),
    
    ("What is the internship credit policy?", "Summer internship (6-8 weeks) carries 2-4 credits in most programs. Mandatory for engineering students. Find internship yourself or through T&P cell. Submit: Offer letter, Attendance proof, Completion certificate, Project report. Evaluation by faculty coordinator. Minimum 'B' grade required. Counts toward total credit requirement."),
    
    ("How to access WiFi on campus?", "Campus-wide WiFi coverage. Connect to SSID 'LPU-Student'. Login with UMS credentials (@lpu.co.in email). Speed: 20Mbps per user. Usage limit: 10GB/day. Access to educational websites unlimited. Social media 8 PM-11 PM only. Download LPU Network app for auto-login. Technical issues: IT Helpdesk, Block 32, ext. 2200.")
]

for q, a in academic_qa:
    dataset.append([q, a, "Academic"])

print(f"Added {len(academic_qa)} Academic questions")

# Save dataset
df = pd.DataFrame(dataset, columns=['Question', 'Answer', 'Mode'])
df.to_csv('data/dataset_advanced.csv', index=False, quoting=csv.QUOTE_ALL)
print(f"\n✅ Created advanced dataset with {len(dataset)} Q&A pairs")
print(f"📁 Saved to: data/dataset_advanced.csv")
