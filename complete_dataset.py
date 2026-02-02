import pandas as pd
import csv

# Load existing dataset
df = pd.read_csv('data/dataset.csv')
dataset = df.values.tolist()

# Add Rules Safety and Grievance mode (20 questions)
rules_data = [
    ["What is the dress code policy?", "Formal dress mandatory Mon-Fri: Boys: Full pants + formal shirt + shoes (NO jeans/t-shirts). Girls: Formal suit/kurti + formal pants (NO leggings/shorts). Saturday: Smart casuals. ID card mandatory. Violations: Attendance marked absent, fine Rs.500. Hostel: No dress code inside.", "Rules Safety and Grievance"],
    ["What is LPU anti-ragging policy?", "ZERO tolerance. Punishment: Immediate suspension, police complaint, expulsion. 24/7 helpline: 1800-180-5522. Email: antiragging@lpu.co.in. Anti-ragging squad regular checks. Affidavit from students and parents mandatory. Complainant identity protected.", "Rules Safety and Grievance"],
    ["What is the attendance policy?", "Minimum 75% mandatory in each subject. Below 75%: Warning. 50-65%: Detained. Below 50%: Repeat semester. Medical leave with certificate counted as absent. Biometric attendance. Daily SMS to parents if absent. No proxy allowed.", "Rules Safety and Grievance"],
    ["How to file a grievance?", "Online: UMS → Grievance portal. Offline: Written complaint, Drop box. Categories: Academic, Administrative, Harassment. Timeline: Acknowledgment 24hrs, Resolution 7 days. Escalation: HOD → Dean → Proctor → VC. Anonymous option available.", "Rules Safety and Grievance"],
    ["What happens with prohibited items?", "Alcohol/Drugs: Immediate expulsion + police case. Smoking: Fine Rs.5000. Detection: Random hostel checks, CCTV, security scanning. Room search without consent if suspicious. Strict disciplinary action.", "Rules Safety and Grievance"],
    ["What is mobile phone policy?", "Allowed with restrictions. Not in classrooms during lectures. Banned in exam halls (UFM case if found). Hostels: Free usage. Library: Silent mode. Photography needs permission. Cyberbullying serious offence.", "Rules Safety and Grievance"],
    ["What safety measures exist?", "24/7 security guards. Biometric entry/exit. 2000+ CCTV cameras. Emergency helpline: 181. Campus police station. 24/7 hospital. Women safety: Separate security, panic buttons, self-defense training. Fire safety: Detectors, drills, trained staff.", "Rules Safety and Grievance"],
    ["What is sexual harassment policy?", "ICC (Internal Complaints Committee) active. Email: icc@lpu.co.in. Confidential proceedings. Inquiry within 90 days. Punishment: Suspension, expulsion, police case. POSH training for all. Well-lit campus, CCTV monitoring.", "Rules Safety and Grievance"],
    ["Can I leave campus anytime?", "Day scholars: Free with ID card. Hostellers: Outpass from warden. Same day till 8PM boys, 7PM girls. Overnight needs parent permission. Biometric tracking. Late entry needs explanation. Local guardian required for hostellers.", "Rules Safety and Grievance"],
    ["Mess food complaint procedure?", "Daily feedback forms. Online: UMS → Mess Complaint. Mess committee meetings. Same day acknowledgment. Quality checks. FSSAI inspections. Can subscribe/unsubscribe mess. Multiple cafeterias alternative.", "Rules Safety and Grievance"],
    ["Policy on strikes and protests?", "Peaceful dissent allowed with permission. Designated areas. No disruption of academics. No violence/property damage. Unauthorized protest: Disciplinary action. Student council for representation. Dialogue encouraged before protest.", "Rules Safety and Grievance"],
    ["Political activities policy?", "Student elections allowed annually. External party politics banned. Academic discussions permitted. No disruption, division, unauthorized rallies. Violations: Immediate action. Focus on education maintained.", "Rules Safety and Grievance"],
    ["What if theft in hostel?", "Report to warden immediately. Register with security. FIR if valuable. CCTV checked. Use lockers for valuables. University not liable. Personal insurance recommended. Keep valuables minimal.", "Rules Safety and Grievance"],
    ["Examination malpractice policy?", "Copying, mobile, chits, talking: Paper cancelled, one-year ban. Repeat: Possible expulsion. Evidence collected, disciplinary hearing. CCTV in halls. Not worth risking career. Extra time for disabled students.", "Rules Safety and Grievance"],
    ["Substance abuse policy?", "Absolute ban on alcohol, drugs, smoking, tobacco. Random checks. Drugs: FIR + expulsion. Alcohol: Suspension. De-addiction support available. Counseling services. Parents notified. Criminal case for drugs.", "Rules Safety and Grievance"],
    ["Cyber safety policy?", "Prohibited: Cyberbullying, obscene content, fake profiles, morphed images. Report: cyber@lpu.co.in. Action: Warning to expulsion. Victim support provided. Cyber safety workshops. Think before posting online.", "Rules Safety and Grievance"],
    ["Accommodation change policy?", "Allowed first 2 weeks only. Genuine reasons: Medical, compatibility issues. Written application to warden. Availability checked. Mid-semester changes not allowed. Emergency immediate shift possible.", "Rules Safety and Grievance"],
    ["Damage to property policy?", "Accidental: Report, repair cost charged. Intentional: Cost + penalty + discipline. Security deposit deducted. Full replacement if serious. Lost library book: Cost + Rs.500. Fair assessment for accidents.", "Rules Safety and Grievance"],
    ["Discipline and conduct policy?", "Expected: Respect, punctuality, honesty. Prohibited: Violence, harassment, ragging. Minor violations: Warning. Serious: Suspension, expulsion. Parents informed. Record maintained. Impacts character certificate.", "Rules Safety and Grievance"],
    ["Disability support services?", "Equal opportunity cell. Ground floor hostel. Wheelchair accessibility. Scribes, extra time in exams. Assistive technology. Ramps, lifts throughout. Special transport. Scholarship available. Inclusive culture, anti-discrimination strict.", "Rules Safety and Grievance"]
]

# Add to dataset
for row in rules_data:
    dataset.append(row)

# Save final dataset
df_final = pd.DataFrame(dataset, columns=['Question', 'Answer', 'Mode'])
df_final.to_csv('data/dataset.csv', index=False, quoting=csv.QUOTE_ALL)

print(f"✅ FINAL DATASET COMPLETE!")
print(f"Total Q&A pairs: {len(df_final)}")
print("\nMode Distribution:")
print(df_final['Mode'].value_counts())
