import pandas as pd
import csv

print("🚀 Creating comprehensive LPU dataset...")

dataset = []

# Helper function
def add_questions(qa_list, mode):
    for q, a in qa_list:
        dataset.append([q, a, mode])
    print(f"✓ Added {len(qa_list)} {mode} questions")

# ACADEMIC (already have 30, keeping them)
academic = pd.read_csv('data/dataset_advanced.csv')
dataset = academic.values.tolist()

# ADMISSIONS AND ADMINISTRATION (25 questions)
admissions_qa = [
    ("What is the LPU admission process?", "LPU admission process: 1) Visit lpu.in and click 'Apply Online', 2) Fill application form with personal/academic details, 3) Pay application fee ₹1000 (non-refundable), 4) Appear for LPUNEST (LPU National Entrance and Scholarship Test) or submit JEE/NEET scores, 5) Check merit list on portal, 6) If selected, pay admission fee, 7) Submit documents: 10th/12th mark sheets, transfer certificate, migration certificate, Aadhar card, photos, 8) Complete biometric registration. Admission confirmed after document verification and full fee payment."),
    
    ("What is the fee structure for B.Tech?", "B.Tech fee structure (2024-25): Tuition fee ₹1,60,000 per year (₹80,000 per semester), Hostel AC: ₹1,15,000/year, Non-AC: ₹95,000/year, Mess: ₹45,000/year, Onetotime charges: ₹25,000 (admission + alumni + ID card + medical). Total: Approx ₹3,45,000/year for AC hostel, ₹3,25,000/year for non-AC. Scholarships available based on rank. Fee payable semester-wise. EMI options available."),
    
    ("What documents are required for admission?", "Required documents for LPU admission: 1) Class 10th mark sheet + certificate (original + 1 copy), 2) Class 12th mark sheet + certificate (original + 1 copy), 3) Transfer Certificate from last institution (original), 4) Migration Certificate from previous board (original), 5) Character Certificate (original), 6) Passport size photographs (10 copies), 7) Aadhar Card (copy), 8) Caste certificate (for SC/ST/OBC, original), 9) Income certificate (for scholarships, if applicable), 10) Gap affidavit (if gap year taken, notarized). Documents verified during admission."),
    
    ("What scholarships are available?", "LPU Scholarships 2024: 1) LPUNEST-based: Rank 1-500: 100% tuition waiver, 501-2000: 75%, 2001-5000: 50%, 5001-10000: 30%, 10001-25000: 20%. 2) Board-based (12th): 90%+: ₹1,00,000/year, 80-90%: ₹75,000/year, 70-80%: ₹50,000/year. 3) JEE Advanced: Rank 1-10000: 100%, 10001-20000: 50%. 4) JEE Main: Percentile 90+: ₹1,00,000. 5) Sports/Cultural: National level: 100%, State level: 50%. 6) Need-based: Up to 25% for financial hardship. Scholarships renewable based on CGPA 7.5+."),
    
    ("What is LPUNEST exam pattern?", "LPUNEST (LPU National Entrance and Scholarship Test) Pattern: Duration: 2 hours (120 minutes), Questions: 120 MCQs (4 options), Marking: +1 for correct, -0.25 for wrong, Sections: English (30), Mathematics (60), General Knowledge (30) for Engineering. For Management: Logical Reasoning, English, Maths, GK. Mode: Online (CBT - Computer Based Test). Conducted: 5-6 times annually (Jan, Feb, Apr, May, Jun, Jul). Registration: Free online. Used for: Admission + Scholarship eligibility + Seat allotment."),
    
   ("Can I get admission without entrance exam?", "Yes, admission without entrance exam possible through: 1) JEE Main/Advanced scores (B.Tech), 2) NEET scores (MBBS/BDS/Pharmacy), 3) CAT/MAT/XAT scores (MBA), 4) Board percentage (for some programs), 5) Direct admission for top board scorers (95%+ in 12th). However, LPUNEST recommended for scholarship opportunities. Scholarship eligibility requires LPUNEST or national test scores. Direct admission fee usually higher than scholarship routes."),
    
    ("What is the last date for admission?", "LPU Admission deadlines: Engineering/Technology: July 31st, Management courses: June 30th, Agriculture/Hotel Management: July 15th, Design/Architecture: June 15th, Law/Pharmacy: July 31st. However, seats on first-come-first-serve basis. Early birds get better hostel rooms + scholarship opportunities. Late admissions (August) subject to seat availability. International students: Rolling admissions till semester start. Spot admissions during July-August at campus."),
    
    ("How to pay fees online?", "Online fee payment: Login to UMS portal → Student Finance → Fee Payment → Select semester + components (tuition + hostel + mess), View total amount, Choose payment mode: Credit/Debit card, Net Banking, UPI, Education loan, Pay and download receipt. Fee breakdown visible before payment. Partial payments allowed (installments). Late fee: ₹500 after due date. Refund: Within 30 days after deduction of processing charges. Payment helpline: +91-1824-517000."),
    
    ("What is the hostel allocation process?", "Hostel allocation: After admission confirmation, hostel form online on UMS, Preference: AC/Non-AC, Single/Double/Triple sharing, Block preference (Boys: 30-41, Girls: 14-28), Allocation: Based on payment date (first come first serve), Fee payment: Advance hostel fee with admission, Allotment: Room number sent via SMS + Email, Check-in: During admission days with parents, Room change: Only first 2 weeks of semester, Refund: If cancelled before semester start (processing charges apply)."),
    
    ("Is there any age limit for admission?", "Age criteria: No maximum age limit for undergraduate/postgraduate programs. Minimum age: 17 years as on December 31 of admission year for UG programs, 21 years for PG programs. For diploma courses: 15+ years. PhD: No age limit. Foreign students: Follow respective country norms. Gap years: Acceptable with valid reason, Gap affidavit required if gap >1 year. Relaxation for reserved categories as per GoI norms."),
    
    ("Can I change my course after admission?", "Course change policy: Allowed within first 15 days of semester start, Conditions: Eligibility criteria of new course must be met, Seat availability in new course, No refund of fees paid, Pay difference if new course fee higher, Approval from both departments + Dean Academics required, Form: Download from UMS → Academic Affairs, Processing fee: ₹5000. Not allowed: After 15 days, Between different schools (Engineering to Management), If scholarship holder. Final decision by Academic Committee."),
    
    ("What is the refund policy?", "LPU Fee Refund Policy: Cancelled before semester start: 90% refund (10% processing), Withdrawal in first week: 80% refund, Withdrawal in second week: 60% refund, After 2 weeks: No refund of tuition fee, Hostel/Mess: Prorated refund after deduction, Refund process: Submit application→Dean approval→Accounts clearance→15-30 days, One-time charges (admission fee): Non-refundable, Security deposit: Full refund after course completion + no dues certificate. Medical emergency: Special consideration on case basis."),
    
    ("How to apply for education loan?", "Education Loan for LPU: Partner banks: SBI, PNB, HDFC, ICICI, Axis Bank, Loan amount: Up to ₹20 lakhs (₹30L for foreign studies), Interest rate: 8-12% (girl students get 0.5% rebate), Processing: Collateral required above ₹7.5L, Documents: Admission letter, Fee structure, Mark sheets, Parents' income proof, Collateral documents. Process: Apply at bank→Submit documents→Valuation→Approval (7-15 days)→Loan disbursal to university directly. LPU Loan Cell: Block-5, ext 2222. Scholar scheme: Central govt subsidy on interest for economically weaker sections."),
    
    ("What is the seat reservation policy?", "LPU Reservation: SC: 15%, ST: 7.5%, OBC (Non-creamy layer): 27%, EWS (Rs<8L income): 10%, Persons with Disability (PwD): 5%, Kashmiri Migrants: 1%, Defense personnel children: 5%. Relaxation: 5% marks or one grade point, Age relaxation: 5 years, Scholarship priority. Documents required: Caste certificate from SDM/Tehsildar, Income certificate for EWS, Disability certificate from medical board. Verification at admission time. False certificate: Cancellation + police case."),
    
    ("How to transfer to LPU from another university?", "Lateral entry/migration to LPU: Eligibility: Similar program at previous university, Minimum 60% marks in previous semesters, No backlogs, Admission: Apply through lateral entry form, Submit: All previous semester mark sheets, Syllabus comparison, Transfer certificate, Migration certificate, Credit transfer: Possible if 70%+ syllabus match, Evaluation: By Academic Committee, Credit exemption maximum: 60% of total credits, Hostel: Fresh allocation needed, Fee: Current batch fees applicable. Processing time: 2-3 weeks. Applications accepted: May-June for odd semester."),
    
    ("What is the dress code policy?", "LPU Dress Code (Academics): Monday-Friday: Formal wear mandatory - Boys: Full pants + formal shirt + shoes (no t-shirts/jeans), Girls: Formal suit/kurti + pants/skirt + formal footwear (no leggings/shorts). Saturday: Casual allowed (no shorts/sleeveless/torn jeans). PhD scholars/Faculty: Always formal. ID Card: Mandatory to display. Violations: Warning→Attendance marked absent→Parents notification→Disciplinary action. Relaxation: During exams week, On specific event days with prior permission. Hostels: No dress code inside hostel premises."),
    
    ("Can international students apply?", "Yes! LPU welcomes international students from 60+ countries. Eligibility: Equivalent to Indian 10+2 (UG) or Bachelor's (PG), IELTS/TOEFL for English proficiency, Valid passport + Student visa, Minimum 60% aggregate, Medical fitness certificate. Admission: Apply online→Document verification→Visa assistance→Arrival support. Fee: Same as Indian students (foreign students can't avail merit scholarships but can get percentage-based). Services: Airport pickup, Orientation, Local guardian arrangement, International Student Office: Block-34. Documents legalization: From MEA/Indian Embassy required. Over 3000 international students currently enrolled."),
    
    ("What is the migration process after admission?", "Course migration: Not allowed in first semester, From 2nd semester onwards: Apply with 8+ CGPA, Subject to seat availability, Pay differential fee if any, Department approvals required. Institute migration (between LPU campuses): Not applicable (only one main campus). Semester migration (shift timing change): Possible with 75%+ attendance, Pay ₹2000 shift change fee, Subject availability in new shift. Physical documents migration: Submit original TC + Migration at admission, Certificates verified + returned with degree, Migration certificate needed from previous university board for inter-university admissions."),
    
    ("How to get admission fee receipt?", "Fee receipt: Auto-generated after successful payment in UMS, Download: Login UMS→Finance→Fee Receipt→Select semester→Download PDF, Contains: Receipt number, Date, Student details, Fee breakdown, Payment mode, Official seal (digitally signed). Uses: Loan processing, Income tax rebate (80C), Scholarship application, Verification purposes. Lost receipt: Reprint from UMS anytime, Physical copy: Accounts department (₹100 duplicate charges), Email: finance@lpu.co.in with request. Receipt number needed for all fee-related queries."),
    
    ("What is the admission cancellation process?", "Admission cancellation: Submit written application to Dean Student Welfare→ Clearance from library, hostel, accounts→No dues certificate→Refund processing as per policy. Online: UMS→Withdrawal request→Upload reason→Department approval. Timeline: Before semester: 15 days processing, After start: 30 days processing. Refund: As per refund policy (90%-0% based on timing). Documents returned: All original documents except TC/Migration (kept for records). Re-admission: Possible in next session with fresh application. Blacklisting: None unless disciplinary issues. Health emergency: Special fast-track process with medical proof."),
    
    ("What is semester exchange program?", "LPU Student Exchange Program: Duration: One semester (4-6 months), Partner Universities: 200+ in USA, Canada, UK, Australia, Europe, Eligibility: Minimum 7.5 CGPA, No backlogs, Good conduct, English proficiency, Application: 4-6 months before exchange (January/July), Process: Apply→Selection→Visa assistance→Pre-departure orientation. Cost: Flight + living expenses (student bears), Tuition: Waived under exchange agreement, Credits: Transferred back to LPU, Scholarship: Limited scholarships available. Hosting family: Arranged by partner university. Contact: International Affairs, Block-34, +91-1824-517851."),
    
    ("How to update personal details after admission?", "Personal details update: Name/DOB change: Submit: Gazette notification + newspaper ad + affidavit + updated mark sheets→Dean approval→University records update (₹5000 processing), Address/Phone/Email: Update directly in UMS→Student Profile→Edit→No approval needed, Parents' details: Submit request with proof→Dean approval, Category change (SC/ST or others): Not allowed after admission, Photo update: Upload in UMS (size: 50KB, JPEG). Name correction (spelling): Simple affidavit + proof→Dean approval (₹1000). Processing: 7-15 working days. Affects: ID card, credentials, degree (if name change)."),
    
    ("What is the difference between regular and distance mode?", "LPU offers only REGULAR mode for UG/PG: Full-time on-campus programs, Daily classes, Mandatory attendance (75%), Practical labs, Industry projects, Complete campus facilities, Placements assistance. Distance/Online: LPU does NOT offer UG in distance mode (UGC restrictions), But offers: Online MBA, Online MA, PG Diplomas through online mode, Classes: Weekend live + recorded, Exams: At designated centers or online proctored. Difference summary: Regular = Full campus experience + better placements, Online = Working professional friendly + lower cost. Choose based on: Career goals, Time availability, Budget, Job status."),
    
    ("How to check admission status?", "Admission status tracking: Login: lpu.in/admission-portal using mobile/email used during application, Status shows: Application submitted→Document verification pending→Entrance test scheduled→Test completed→Merit list→Provisional admission→Fee payment pending→Admitted, SMS/Email: Sent at each stage, Helpline: +91-1824-517000 (9 AM - 6 PM), Check directly: Visit admissions office with application number. Merit list: Published on website + SMS to registered mobile, Admission letter: Downloaded from portal after fee payment. Waiting list: If not in first merit list, subsequent lists released weekly. Final status: Admitted/Not selected/Waiting.")
]

add_questions(admissions_qa, "Admissions and Administration")

# Save
df = pd.DataFrame(dataset, columns=['Question', 'Answer', 'Mode'])
df.to_csv('data/dataset.csv', index=False, quoting=csv.QUOTE_ALL)
print(f"\n✅ Total dataset: {len(df)} Q&A pairs")
print(f"📁 Saved to: data/dataset.csv")
print("\n📊 Mode distribution:")
print(df['Mode'].value_counts())
