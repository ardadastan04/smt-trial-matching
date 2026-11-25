# Failure sample: run `main_dev`, key `gpt5_oracle`

Seed 0. A = 15 random *useful, unanswered* questions per policy (informative, but the answer was unknown). B/C = every pair where one policy is right at k=30 and the other is wrong. Criteria lines are a keyword match and can be off. Fill in each **Category:** line.

## A. greedy_smt: useful but unanswered (15 of 424)

### A1. greedy_smt · trec-202113 · turn 14

- **Trial:** NCT02959957, Disturbance of the Intestinal Microbiota by Temocillin vs Cefotaxime in Treatment of Febrile Urinary Tract Infections
- **Question:** Boolean value indicating whether the patient is currently breastfeeding.
- **Variable:** `patient_is_breastfeeding_now`
- **Answer:** unknown (useful_unanswered)
- **Criteria line:** (no matching line found)

<details><summary>patient note</summary>

62 yo male with hx of CVA, neurogenic bladder with indwelling suprapubic catheter with multiple prior admissions for UTIs, altered mental status, and urosepsis presents to the hospital in urosepsis now resolved after treatment with vanc/meropenem. Per CT there is a non-obstructing stone in the L ureter, no evidence of urethral strictures. Significant leaking around suprapubic cath site. Started on ditropan changed over to detrol. Urologist not concerned with leaking and will f/u with pt next week.
s/p CVA
Neurogenic bladder s/p suprapubic cath
Recurrent UTIs with Klebsiella/Pseudomonas
Non-hodgkins Marginal Zone Lymphoma of the left orbit Dx in 03
(s/p R-CHOP x 6 cycles)
Bells Palsy
BPH
Hypertension
Partial Bowel obstruction s/p colostomy
Hepatitis C
Cryoglobulinemia
SLE with transverse myelitis, anti-dsDNA Ab+
Insulin Dependant Diabetic
Fungal Esophagitis Stage IV?
Urinary Tract Infections-pseudomonas & enterococcus

</details>

Category:

### A2. greedy_smt · trec-202121 · turn 9

- **Trial:** NCT01796652, Home Treatment of Acute Pancreatitis
- **Question:** Boolean indicating whether the patient currently has a blood coagulation disorder (coagulopathy).
- **Variable:** `patient_has_finding_of_blood_coagulation_disorder_now`
- **Answer:** unknown (useful_unanswered)
- **Criteria line:** exclusion: “Coagulopathy (international normalized ratio >1, and/or platelet count <50,000/mm3”

<details><summary>patient note</summary>

The patient is a 57-year-old man with abdominal pain and vomiting. The pain started gradually about 20 hours ago in the epigastric and periumbilical regions, radiating to his back. He drinks around 60 units of alcohol per week and smokes 22 cigarettes per day. He is healthy with no history of allergies or using any medications. His family history is positive for type 2 diabetes (his father and sister). He lives alone and has no children. The abdomen is tender and soft. His bowel sounds are normal. His heart rate is 115/min and blood pressure 110/75 mmHg. The lab results are remarkable for leukocytosis (19.5), urea of 8.5, high CRP (145), high amylase (1200) and Glc level of 15. Cross-sectional imaging was negative for obstructive pancreatitis.

</details>

Category:

### A3. greedy_smt · trec-202123 · turn 27

- **Trial:** NCT00287378, Effect of Ozone on Airway Inflammation in Allergic Asthmatics Treated With Omalizumab
- **Question:** patient_has_finding_of_allergy_to_dust_mite_protein_now
- **Variable:** `patient_has_finding_of_allergy_to_dust_mite_protein_now`
- **Answer:** unknown (useful_unanswered)
- **Criteria line:** inclusion: “Evidence of allergy to house dust mite”

<details><summary>patient note</summary>

A 39-year-old man came to the clinic with cough and shortness of breath that was not relieved by  his inhaler. He had these symptoms for 5 days during the past 2 weeks. He doubled his oral corticosteroids in the past week. He is a chef with a  history of asthma for 3 years, suffering from frequent cough, wheezing, and shortness of breath and chest tightness. The symptoms become more bothersome within 1-2 hours of starting work every day and worsen throughout the work week. His symptoms improve within 1-2 hours outside the workplace. Spirometry was performed revealing a forced expiratory volume in the first second (FEV1) of 63% of the predicted. His past medical history is significant for seasonal allergic rhinitis in the summer. He doesn't smoke or use illicit drugs. His family history is significant for asthma in his father and sister.  He currently uses inhaled corticosteroid (ICS) and fluticasone 500 mcg/salmeterol 50 mcg, one puff twice daily.

</details>

Category:

### A4. greedy_smt · trec-202129 · turn 8

- **Trial:** NCT01739283, GIP and GLP-1 in Type 1 Diabetes
- **Question:** Boolean indicating whether the patient currently has anemia.
- **Variable:** `patient_has_finding_of_anemia_now`
- **Answer:** unknown (useful_unanswered)
- **Criteria line:** (no matching line found)

<details><summary>patient note</summary>

The patient is a 24-year-old man who has had type 1 diabetes for 11 years. He presents to the emergency room with hyperglycemia and concern for possible diabetic ketoacidosis after not taking his insulin for 3 days. The patient reports that he is currently homeless and has lost his supply of insulin, syringes, glucometer, and glucose testing supplies. The patient states that at the time of his initial diagnosis with type 1 diabetes he was hospitalized with a glucose value >1000 mg/dL. At the time, he was experiencing polyuria, polydipsia, and polyphagia. He reports that he has been on insulin since the time of his diagnosis, and he has never been prescribed oral agents for diabetes management. Most recently, he has been using insulin glargine 55 units once daily, and insulin aspart sliding scale 3 times daily. The patient has had previous episodes of diabetic ketoacidosis, for which he was hospitalized. With this episode of hyperglycemia, he is not experiencing any nausea, vomiting, or abdominal discomfort, and he appears well. His lab studies showed:
A1c: 11.3%
Creatinine: 0.9 mg/dL with eGFR >60 mL/min
Aspartate aminotransferase (AST): 17 U/L
Alanine aminotransferase (ALT): 14 U/L
Beta-hydroxybutyrate: 0.1 mmol/L
Bicarbonate: 25 mEq/L
Anion Gap: 14 mEq/L

</details>

Category:

### A5. greedy_smt · trec-202132 · turn 4

- **Trial:** NCT01406288, Outbreak of Hemolytic Uremic Syndrome Linked to Escherichia Coli of Serotype O104:H4
- **Question:** Boolean indicating whether the patient is willing to sign informed consent.
- **Variable:** `patient_is_willing_to_sign_informed_consent`
- **Answer:** unknown (useful_unanswered)
- **Criteria line:** exclusion: “Patient not willing to participate or to sign informed consent”

<details><summary>patient note</summary>

A 17 year old boy  complains of vomiting, non-bloody diarrhea, abdominal pain, fever, chills and loss of appetite for the past 3 days. He ate a salad at a restaurant prior to his diarrhea onset. Physical exam was remarkable for pallor, jaundice, and diffuse abdominal tenderness. Lab results were as follows:
Hemoglobin: 9.7 g/dL
Platelet: 110,000 /cu.mm
Creatinine: 3.6 mg/dL
blood urea nitrogen (BUN): 73 mg/dL
direct bilirubin: 2.4 mg/dL
lactate dehydrogenase (LDH): 881 IU/L (normal: 110-265 IU/L)
Peripheral blood smear showed a moderate number of schistocytes and helmet cells.  Shiga-like toxin-producing E. coli (STEC) stx1/stx2 were found in stools. 
He has no other underlying disease and he is not on any medications.

</details>

Category:

### A6. greedy_smt · trec-202133 · turn 1

- **Trial:** NCT01314352, Bioavailability Study of Desloratadine 5 mg Tablet of Dr. Reddy's Under Fed Conditions
- **Question:** Boolean indicating whether the patient's clinically significant laboratory abnormality would interfere with the conduct of the study, would interfere with the interpretation of the study, or would jeopardize the safety of the patient.
- **Variable:** `patient_has_clinically_significant_laboratory_abnormality_now@@would_interfere_with_study_conduct_or_interpretation_or_jeopardize_patient_safety`
- **Answer:** unknown (useful_unanswered)
- **Criteria line:** exclusion: “Does s/he have clinically significant laboratory abnormalities that would interfere with the conduct or interpretation of the study or jeopardize his/her safety?”

<details><summary>patient note</summary>

A 42-year-old healthy woman came to the clinic to have her flu shot in early October. She works in a rehab center and has no underlying disease. It's her first time getting the vaccine  this  year. She is married for 5 years and uses barrier methods of contraception. Her menstrual cycle is irregular. She does not smoke. She is not on any medications. She exercises regularly for 30 minutes a day at least 5 days a week. She has no history of allergies to any food or drugs. Her past surgical history is significant for tonsillectomy and she is otherwise healthy.

</details>

Category:

### A7. greedy_smt · trec-202134 · turn 1

- **Trial:** NCT00641108, Effects of Cognitive Behavioral Therapy on Brain Serotonin Activity in People With Depression
- **Question:** patient_can_undergo_magnetic_resonance_imaging_now
- **Variable:** `patient_can_undergo_magnetic_resonance_imaging_now`
- **Answer:** unknown (useful_unanswered)
- **Criteria line:** exclusion: “Inability to undergo an MRI scan”

<details><summary>patient note</summary>

The patient is a 47-year-old Asian woman complaining of persistent feelings of sadness. She lost interest in activities she used to enjoy. She states that her mood is mostly depressed for the past 3 weeks. She also lost her appetite , which led to about 5kg weight loss. She complains of loss of energy and feelings of worthlessness nearly every day. She is not using any drugs and she does not smoke. She doesn't drink alcohol. She used to exercise every day for at least 30 min. But she doesn't have enough energy to do so for the past 3 weeks. She also has some digestive issues recently. She is married and has 4 children. She is menopausal. Her husband was recently diagnosed with colon cancer and he is starting his chemotherapy. There is nothing remarkable in her past medical history and her drug history is only positive for Vit D3 1000 units daily. Her family history is negative for any psychologic problems. Her HAM-D score is 20.

</details>

Category:

### A8. greedy_smt · trec-202134 · turn 16

- **Trial:** NCT00641108, Effects of Cognitive Behavioral Therapy on Brain Serotonin Activity in People With Depression
- **Question:** patient_has_diagnosis_of_parkinson_s_disease_inthehistory
- **Variable:** `patient_has_diagnosis_of_parkinson_s_disease_inthehistory`
- **Answer:** unknown (useful_unanswered)
- **Criteria line:** exclusion: “History of Parkinson's or other basal ganglia disease”

<details><summary>patient note</summary>

The patient is a 47-year-old Asian woman complaining of persistent feelings of sadness. She lost interest in activities she used to enjoy. She states that her mood is mostly depressed for the past 3 weeks. She also lost her appetite , which led to about 5kg weight loss. She complains of loss of energy and feelings of worthlessness nearly every day. She is not using any drugs and she does not smoke. She doesn't drink alcohol. She used to exercise every day for at least 30 min. But she doesn't have enough energy to do so for the past 3 weeks. She also has some digestive issues recently. She is married and has 4 children. She is menopausal. Her husband was recently diagnosed with colon cancer and he is starting his chemotherapy. There is nothing remarkable in her past medical history and her drug history is only positive for Vit D3 1000 units daily. Her family history is negative for any psychologic problems. Her HAM-D score is 20.

</details>

Category:

### A9. greedy_smt · trec-202137 · turn 3

- **Trial:** NCT04032158, Study of Evobrutinib in Participants With Relapsing Multiple Sclerosis (RMS)
- **Question:** Boolean indicating whether the condition requiring intravenous corticosteroid therapy is not well-controlled type 2 diabetes mellitus or well-controlled thyroid disease.
- **Variable:** `patient_has_condition_requiring_intravenous_corticosteroid_therapy_now@@except_for_well_controlled_type_2_diabetes_mellitus_or_well_controlled_thyroid_disease`
- **Answer:** unknown (useful_unanswered)
- **Criteria line:** exclusion: “Immunologic disorder other than MS, or any other condition requiring oral, intravenous (IV) , intramuscular, or intra-articular corticosteroid therapy, with the exception of well-controlled Type 2 diabetes mellitus or well controlled thyroid disease.”

<details><summary>patient note</summary>

The patient is a 20 year old Caucasian female presents to the clinic with one-sided vision lost and facial weakness, dysarthria and numbness lasting for 1 day. She visited her PCP and underwent brain MRI which revealed a single plaque in the brainstem. After few months, she experienced lower extremities weakness led to balance problem. The second MRI revealed another lesion in the left cerebral hemisphere. The diagnosis of Relapsing Remitting Multiple Sclerosis (RRMS) is confirmed after the second MRI. Her past surgical history is significant for a C-section 2 years ago and she has a one child. She is divorced and is not currently in any sexual relationship. She smokes 10 cigarettes per day and drinks alcohol occasionally. She is working as an editor in a publisher company and she is happy that she can keep working from home most of the time. She is under the treatment of RRMS from 7 months ago.

</details>

Category:

### A10. greedy_smt · trec-202137 · turn 7

- **Trial:** NCT04032158, Study of Evobrutinib in Participants With Relapsing Multiple Sclerosis (RMS)
- **Question:** Boolean indicating whether the patient has been neurologically stable for at least 30 days prior to baseline.
- **Variable:** `patient_is_neurologically_stable_for_at_least_30_days_prior_to_baseline`
- **Answer:** unknown (useful_unanswered)
- **Criteria line:** inclusion: “inclusion criteria: - Participants are diagnosed with RMS (relapsing-remitting multiple sclerosis [RRMS] or secondary progressive multiple sclerosis [SPMS] with relapses) in accordance with 2017 Revised McDonald criteria (Thompson 2018) - Participants with one or more documented relapses within the 2 years before Screening with either: a. one relapse which occurred within the last year prior to randomization, OR b. the presence of at least 1 gadolinium-enhancing (Gd+) T1 lesion within 6 months prior to randomization - Participants have Expanded Disability Status Scale (EDSS) score of 0 to 5.5 at Baseline. Participants with an EDSS score <= 2 at Screening are only eligible for participation if their disease duration (time since onset of symptoms) is no more than 10 years - Participants are neurologically stable for >= 30 days prior to both screening and baseline - Female participants must be neither pregnant nor breast-feeding and must lack child-bearing potential, as defined by either: post-menopausal or surgically sterile or use an effective method of contraception for the duration of the study - Participants have given written informed consent prior to any study-related procedure - Other protocol defined inclusion criteria could apply”

<details><summary>patient note</summary>

The patient is a 20 year old Caucasian female presents to the clinic with one-sided vision lost and facial weakness, dysarthria and numbness lasting for 1 day. She visited her PCP and underwent brain MRI which revealed a single plaque in the brainstem. After few months, she experienced lower extremities weakness led to balance problem. The second MRI revealed another lesion in the left cerebral hemisphere. The diagnosis of Relapsing Remitting Multiple Sclerosis (RRMS) is confirmed after the second MRI. Her past surgical history is significant for a C-section 2 years ago and she has a one child. She is divorced and is not currently in any sexual relationship. She smokes 10 cigarettes per day and drinks alcohol occasionally. She is working as an editor in a publisher company and she is happy that she can keep working from home most of the time. She is under the treatment of RRMS from 7 months ago.

</details>

Category:

### A11. greedy_smt · trec-202137 · turn 18

- **Trial:** NCT04528121, Effect of CoDuSe Balance Training and Step Square Exercises on Risk of Fall in Multiple Sclerosis
- **Question:** Boolean indicating whether the patient currently has hemopoietic disease.
- **Variable:** `patient_has_finding_of_hemopoietic_disease_now`
- **Answer:** unknown (useful_unanswered)
- **Criteria line:** exclusion: “peripheral vestibulopathy, hepatic, renal, hemopoeitic, thyroid and cardiovascular diseases, cognitive dysfunction,”

<details><summary>patient note</summary>

The patient is a 20 year old Caucasian female presents to the clinic with one-sided vision lost and facial weakness, dysarthria and numbness lasting for 1 day. She visited her PCP and underwent brain MRI which revealed a single plaque in the brainstem. After few months, she experienced lower extremities weakness led to balance problem. The second MRI revealed another lesion in the left cerebral hemisphere. The diagnosis of Relapsing Remitting Multiple Sclerosis (RRMS) is confirmed after the second MRI. Her past surgical history is significant for a C-section 2 years ago and she has a one child. She is divorced and is not currently in any sexual relationship. She smokes 10 cigarettes per day and drinks alcohol occasionally. She is working as an editor in a publisher company and she is happy that she can keep working from home most of the time. She is under the treatment of RRMS from 7 months ago.

</details>

Category:

### A12. greedy_smt · trec-202137 · turn 21

- **Trial:** NCT04528121, Effect of CoDuSe Balance Training and Step Square Exercises on Risk of Fall in Multiple Sclerosis
- **Question:** Boolean indicating whether the patient's current musculoskeletal complication is secondary.
- **Variable:** `patient_has_finding_of_musculoskeletal_complication_now@@secondary`
- **Answer:** unknown (useful_unanswered)
- **Criteria line:** exclusion: “secondary musculoskeletal complication”

<details><summary>patient note</summary>

The patient is a 20 year old Caucasian female presents to the clinic with one-sided vision lost and facial weakness, dysarthria and numbness lasting for 1 day. She visited her PCP and underwent brain MRI which revealed a single plaque in the brainstem. After few months, she experienced lower extremities weakness led to balance problem. The second MRI revealed another lesion in the left cerebral hemisphere. The diagnosis of Relapsing Remitting Multiple Sclerosis (RRMS) is confirmed after the second MRI. Her past surgical history is significant for a C-section 2 years ago and she has a one child. She is divorced and is not currently in any sexual relationship. She smokes 10 cigarettes per day and drinks alcohol occasionally. She is working as an editor in a publisher company and she is happy that she can keep working from home most of the time. She is under the treatment of RRMS from 7 months ago.

</details>

Category:

### A13. greedy_smt · trec-202143 · turn 5

- **Trial:** NCT00807326, A Comparison of Three Medications to Treat Diarrhea in Adults.
- **Question:** Boolean indicating whether the patient has ever had a diagnosis of acquired immunodeficiency syndrome (AIDS) in their medical history.
- **Variable:** `patient_has_diagnosis_of_aids_inthehistory`
- **Answer:** unknown (useful_unanswered)
- **Criteria line:** exclusion: “Immunodeficiency (e.g. those with acquired immunodeficiency syndrome [AIDS] or known human immunodeficiency virus [HIV] infection, or undergoing chemotherapy or radiotherapy)”

<details><summary>patient note</summary>

The patient is a 60-year-old woman admitted to the stroke department with a recent history of a second course of intravenous antibiotics for aspiration pneumonia. She is febrile and complained of abdominal pain and diarrhea (bowel movements eight times in 3 hours, large volumes of greenish, liquid stool each time).
The patient's abdomen is generally tender and distend with hyperactive bowel sounds. She is febrile (38.4°C), tachycardic (113/min) and hypotensive (80/40 mmHg). The stool samples must were positive for Clostridium difficile toxin.

</details>

Category:

### A14. greedy_smt · trec-202160 · turn 23

- **Trial:** NCT02220517, Randomized Study Comparing MR-guided in Bore Versus MRI/US Fusion-guided Prostate Biopsy
- **Question:** Boolean indicating whether the patient's current diagnosis of prostate cancer is known (confirmed).
- **Variable:** `patient_has_diagnosis_of_carcinoma_of_prostate_now@@known`
- **Answer:** unknown (useful_unanswered)
- **Criteria line:** exclusion: “Known prostate cancer”

<details><summary>patient note</summary>

The patient is a 63-year-old man presenting to the Emergency Department with a history of acute urinary retention in the past 2 days. Abdominopelvic CT scan revealed a large prostate and a bladder filled with urine. He is a candidate for urethral catheterization and TURP. Further evaluation revealed:
Post-void residual: 71 mL
Prostate volume (TRUS): 63 mL
Prostate-specific antigen (PSA) level: 3.5 ng/mL
His recent blood chemistry (3 days ago) was normal: 
Hgb: 13.6 g/dl
WBC: 133000 /mm3
Plt: 370000 /ml
PT: 12 second
PTT: 34 second
INR: 0.9
Creatinine: 0.5 mg/dl
BUN: 10 mg/dl
U/A:
Color: yellow
Appearance: cloudy
PH: 5.3
Specific gravity: 1.010
Glc: 100
Nitrite: negative
Ketone: none
Leukocyte esterase: negative
RBC: negative
WBC: 2 WBCs/hpf
U/C: negative

</details>

Category:

### A15. greedy_smt · trec-202161 · turn 13

- **Trial:** NCT01816555, Vitamin D3 (Vit D3) Supplementation and T Cell Immunomodulation in Patients With Newly Diagnosed Operative Invasive Ductal Breast Carcinoma
- **Question:** Indicates whether the patient currently has adequate organ function as defined by all the specified laboratory criteria.
- **Variable:** `patient_has_adequate_organ_function_now`
- **Answer:** unknown (useful_unanswered)
- **Criteria line:** inclusion: “Patients must have adequate organ function as defined by:”

<details><summary>patient note</summary>

The patient is a 45-year-old postmenopausal woman with cytologically confirmed breast cancer. A core biopsy revealed a 3 cm invasive ductal breast carcinoma in the left upper outer quadrant. The tumor is  HER2-positive and ER/PR negative. Axillary sampling revealed 5 positive lymph nodes. CXR was remarkable for metastatic lesions. The patient is using multivitamins and iron supplements. She does not smoke or consume alcohol. She is not sexually active and has no children. She is a candidate for tumor resection and agrees to do so prior to chemotherapy.

</details>

Category:

## A. answerable_informative: useful but unanswered (15 of 337)

### A16. answerable_informative · trec-202114 · turn 25

- **Trial:** NCT00147290, ADVANCE CRT - D: Antitachycardia Pacing (ATP) Delivery for Painless Implantable Cardioverter Defibrillator (ICD) Therapy
- **Question:** Boolean indicating whether the patient has ever undergone a cardiac pacing procedure.
- **Variable:** `patient_has_undergone_cardiac_pacing_inthehistory`
- **Answer:** unknown (useful_unanswered)
- **Criteria line:** exclusion: “Patient's life expectancy less than 1 year due to a non cardiac chronic disease”

<details><summary>patient note</summary>

70 y/o with COPD on 2.5-3.5L O2 at baseline, OSA and obesity hypoventilation syndrome, dCHF, discharged [**2132-8-24**] now presents with agitation and altered mental status with hypoxia and O2 sats 70s on BipAp with 5L. Pt agitated then somnolent at initial presentation. Daughter reported increased agitation and altered mental status x 2-3 days with O2 sats 60s-70s at home. Daughter has also noted increased LE edema and weight gain which prompted a phone call to her PCP and increased lasix dose from 80daily to 100mg daily with some mild improvement in edema. She has had decreased appetite, PO intake, energy level at home with difficulty with ADLs. No recent history of fever, cough, chills, sputum production, CP, abd pain, or other complaints other than chronic right thigh pain last 1-2 months. Daughter also reports med compliance and compliance with BiPap at night.
Past Medical History:
- CAD; s/p 4 vessel CABG in [**2119**]
- CHF; EF 55%, mild AS
- obesity hypoventilation syndrome
- obstructive sleep apnea
- DM2
- ventricular tachycardia; s/p ICD in [**2127**]
- hypothyroidism
- schizophrenia
- COPD
- Pneumona treated in [**4-7**] at [**Hospital1 **]

</details>

Category:

### A17. answerable_informative · trec-202115 · turn 15

- **Trial:** NCT02719912, Mitral Valve Replacement With MValve Dock and Lotus
- **Question:** Boolean indicating whether the patient currently has cardiogenic shock.
- **Variable:** `patient_has_finding_of_cardiogenic_shock_now`
- **Answer:** unknown (useful_unanswered)
- **Criteria line:** exclusion: “Hemodynamic instability defined as systolic pressure < 90 mm Hg with or without afterload reduction, cardiogenic shock, or the need for inotropic support or intra-aortic balloon pump or other hemodynamic support device, or any mechanical heart assistance.”

<details><summary>patient note</summary>

70 year-old woman with a history of CAD recently noted abdominal mass who presents with fevers/rigors and bandemia. Over the last few weeks leading up to admission, she has been experiencing mid-abdominal pain, radiating to the left flank. It lasts throughout the day is not increased by eating though there is associated vomiting and is worsened with coughing. CT abdomen without contrast was then performed on [**4-20**] showing a large 9.5 x 7.5 x 6.0-cm heterogeneous left upper abdominal mass. Patient underwent a EUS with biopsy. The results of the biopsy were consistent with pancreatic adenocarcinoma at the head of pancreas. Splenic flecture/pancreatic tail mass was also seen on CT, likely diverticular abscess given the patients recent likely history of diverticulitis this was thought to be an infected fluid collection or abscess. She was treated with IV antibiotics (Zosyn, then ceftriaxone and flagyl) and will continue on them until seen by ID as an outpatient.
Past Medical History:
1. Coronary artery disease with history of angioplasty in [**State 108**] one year ago
2. Mitral valve prolapse
3. Atrial fibrillation
4. Hyperlipemia
5. Hypertension
6. Chronic kidney disease (SCr 2.1 in [**3-17**])
7. Hypothyroidism? (TSH 10 in [**3-17**])
8. Anemia (HCT 30.7 in [**3-17**])

</details>

Category:

### A18. answerable_informative · trec-202115 · turn 17

- **Trial:** NCT02719912, Mitral Valve Replacement With MValve Dock and Lotus
- **Question:** Numeric percentage representing the patient's left ventricular ejection fraction measured within the past 30 days.
- **Variable:** `patient_left_ventricular_ejection_fraction_value_recorded_inthepast30days_withunit_percent`
- **Answer:** unknown (useful_unanswered)
- **Criteria line:** inclusion: “Left Ventricular Ejection Fraction (LVEF) is ≥30% within 30 days prior to the procedure.”

<details><summary>patient note</summary>

70 year-old woman with a history of CAD recently noted abdominal mass who presents with fevers/rigors and bandemia. Over the last few weeks leading up to admission, she has been experiencing mid-abdominal pain, radiating to the left flank. It lasts throughout the day is not increased by eating though there is associated vomiting and is worsened with coughing. CT abdomen without contrast was then performed on [**4-20**] showing a large 9.5 x 7.5 x 6.0-cm heterogeneous left upper abdominal mass. Patient underwent a EUS with biopsy. The results of the biopsy were consistent with pancreatic adenocarcinoma at the head of pancreas. Splenic flecture/pancreatic tail mass was also seen on CT, likely diverticular abscess given the patients recent likely history of diverticulitis this was thought to be an infected fluid collection or abscess. She was treated with IV antibiotics (Zosyn, then ceftriaxone and flagyl) and will continue on them until seen by ID as an outpatient.
Past Medical History:
1. Coronary artery disease with history of angioplasty in [**State 108**] one year ago
2. Mitral valve prolapse
3. Atrial fibrillation
4. Hyperlipemia
5. Hypertension
6. Chronic kidney disease (SCr 2.1 in [**3-17**])
7. Hypothyroidism? (TSH 10 in [**3-17**])
8. Anemia (HCT 30.7 in [**3-17**])

</details>

Category:

### A19. answerable_informative · trec-202115 · turn 19

- **Trial:** NCT02719912, Mitral Valve Replacement With MValve Dock and Lotus
- **Question:** Boolean indicating whether the patient currently needs to undergo intra-aortic balloon pump support.
- **Variable:** `patient_needs_to_undergo_cardioassist_by_aortic_balloon_pump_now`
- **Answer:** unknown (useful_unanswered)
- **Criteria line:** exclusion: “Hemodynamic instability defined as systolic pressure < 90 mm Hg with or without afterload reduction, cardiogenic shock, or the need for inotropic support or intra-aortic balloon pump or other hemodynamic support device, or any mechanical heart assistance.”

<details><summary>patient note</summary>

70 year-old woman with a history of CAD recently noted abdominal mass who presents with fevers/rigors and bandemia. Over the last few weeks leading up to admission, she has been experiencing mid-abdominal pain, radiating to the left flank. It lasts throughout the day is not increased by eating though there is associated vomiting and is worsened with coughing. CT abdomen without contrast was then performed on [**4-20**] showing a large 9.5 x 7.5 x 6.0-cm heterogeneous left upper abdominal mass. Patient underwent a EUS with biopsy. The results of the biopsy were consistent with pancreatic adenocarcinoma at the head of pancreas. Splenic flecture/pancreatic tail mass was also seen on CT, likely diverticular abscess given the patients recent likely history of diverticulitis this was thought to be an infected fluid collection or abscess. She was treated with IV antibiotics (Zosyn, then ceftriaxone and flagyl) and will continue on them until seen by ID as an outpatient.
Past Medical History:
1. Coronary artery disease with history of angioplasty in [**State 108**] one year ago
2. Mitral valve prolapse
3. Atrial fibrillation
4. Hyperlipemia
5. Hypertension
6. Chronic kidney disease (SCr 2.1 in [**3-17**])
7. Hypothyroidism? (TSH 10 in [**3-17**])
8. Anemia (HCT 30.7 in [**3-17**])

</details>

Category:

### A20. answerable_informative · trec-202120 · turn 8

- **Trial:** NCT01000090, Surgical Versus Medical Treatment of Acromegaly
- **Question:** Boolean indicating whether the patient is currently in treatment control.
- **Variable:** `patient_is_in_treatment_control_now`
- **Answer:** unknown (useful_unanswered)
- **Criteria line:** inclusion: “in treatment control”

<details><summary>patient note</summary>

A 35-year-old woman presents with history of acne and mild hirsutism. The primary evaluation revealed elevated testosterone levels. She recently noticed gradual enlargement of her hands and feet and recognized that her ring is getting small for her finger. There is some irregularity in her menstrual cycle as well as some nipple discharge. She also has positive history for snoring and headache. The physical examination revealed subtle facial features of acromegaly and prognathism. Visual fields are normal by confrontation. Hirsutism, soft tissue thickening and diaphoresis of the hands and feet are noted.  Laboratory evaluation in the fasting state reveals IGF-1 of 968 ng/mL and random GH of 19.7 ng/mL. MRI reveals a macroadenoma with no invasion. She is on stable doses of octreotide LAR since her diagnosis was confirmed. She is married and has 2 children. She is using IUD as her contraceptive method.

</details>

Category:

### A21. answerable_informative · trec-202120 · turn 16

- **Trial:** NCT03710499, Rehabilitation Program in Patients With Acromegaly
- **Question:** Boolean indicating whether the patient is currently eligible for the treatment protocol.
- **Variable:** `patient_is_eligible_for_treatment_protocol_now`
- **Answer:** unknown (useful_unanswered)
- **Criteria line:** inclusion: “Patients who present clinical stability and who are eligible for the treatment protocol (patients with hormone deficiency will continue on replacement therapy - SILVA et al., 2013).”

<details><summary>patient note</summary>

A 35-year-old woman presents with history of acne and mild hirsutism. The primary evaluation revealed elevated testosterone levels. She recently noticed gradual enlargement of her hands and feet and recognized that her ring is getting small for her finger. There is some irregularity in her menstrual cycle as well as some nipple discharge. She also has positive history for snoring and headache. The physical examination revealed subtle facial features of acromegaly and prognathism. Visual fields are normal by confrontation. Hirsutism, soft tissue thickening and diaphoresis of the hands and feet are noted.  Laboratory evaluation in the fasting state reveals IGF-1 of 968 ng/mL and random GH of 19.7 ng/mL. MRI reveals a macroadenoma with no invasion. She is on stable doses of octreotide LAR since her diagnosis was confirmed. She is married and has 2 children. She is using IUD as her contraceptive method.

</details>

Category:

### A22. answerable_informative · trec-202129 · turn 12

- **Trial:** NCT02910271, Clinical Features and Prevalence of Asymptomatic Peripheral Artery Disease in Patients With Type 1 Diabetes Mellitus
- **Question:** Boolean indicating whether the patient is currently diagnosed with a terminal illness.
- **Variable:** `patient_has_finding_of_terminal_illness_now`
- **Answer:** unknown (useful_unanswered)
- **Criteria line:** exclusion: “Current pregnancy, institutionalized or terminal illness subjects.”

<details><summary>patient note</summary>

The patient is a 24-year-old man who has had type 1 diabetes for 11 years. He presents to the emergency room with hyperglycemia and concern for possible diabetic ketoacidosis after not taking his insulin for 3 days. The patient reports that he is currently homeless and has lost his supply of insulin, syringes, glucometer, and glucose testing supplies. The patient states that at the time of his initial diagnosis with type 1 diabetes he was hospitalized with a glucose value >1000 mg/dL. At the time, he was experiencing polyuria, polydipsia, and polyphagia. He reports that he has been on insulin since the time of his diagnosis, and he has never been prescribed oral agents for diabetes management. Most recently, he has been using insulin glargine 55 units once daily, and insulin aspart sliding scale 3 times daily. The patient has had previous episodes of diabetic ketoacidosis, for which he was hospitalized. With this episode of hyperglycemia, he is not experiencing any nausea, vomiting, or abdominal discomfort, and he appears well. His lab studies showed:
A1c: 11.3%
Creatinine: 0.9 mg/dL with eGFR >60 mL/min
Aspartate aminotransferase (AST): 17 U/L
Alanine aminotransferase (ALT): 14 U/L
Beta-hydroxybutyrate: 0.1 mmol/L
Bicarbonate: 25 mEq/L
Anion Gap: 14 mEq/L

</details>

Category:

### A23. answerable_informative · trec-202131 · turn 14

- **Trial:** NCT01231945, Low-Cost Molecular Cervical Cancer Screening Study
- **Question:** patient_has_finding_of_finding_of_menstrual_bleeding_now
- **Variable:** `patient_has_finding_of_finding_of_menstrual_bleeding_now`
- **Answer:** unknown (useful_unanswered)
- **Criteria line:** exclusion: “-Women who are currently menstruating at the time of enrollment will be deferred from participating, and will become eligible to participate 7-14 days after menstruation has ended. The menstruating women will be advised to return for the screening 7 to 14 days after their menstrual period has concluded.”

<details><summary>patient note</summary>

The patient is a 37-year-old woman who came to the clinic for a routine Pap smear. The test revealed stage 1B of cervical cancer. The patient tested positive for HPV 16. She has three sexual partners and   four children. She underwent tubal ligation. She smokes 30 packs/year and drinks alcohol frequently. She is otherwise healthy. She was offered a radical hysterectomy.

</details>

Category:

### A24. answerable_informative · trec-202133 · turn 25

- **Trial:** NCT01994343, Pain in Women With Chronic Pelvic Pain
- **Question:** Boolean indicating whether the patient has had pain in their history.
- **Variable:** `patient_has_finding_of_pain_inthehistory`
- **Answer:** unknown (useful_unanswered)
- **Criteria line:** inclusion: “Clinical diagnosis of chronic pelvic pain.”

<details><summary>patient note</summary>

A 42-year-old healthy woman came to the clinic to have her flu shot in early October. She works in a rehab center and has no underlying disease. It's her first time getting the vaccine  this  year. She is married for 5 years and uses barrier methods of contraception. Her menstrual cycle is irregular. She does not smoke. She is not on any medications. She exercises regularly for 30 minutes a day at least 5 days a week. She has no history of allergies to any food or drugs. Her past surgical history is significant for tonsillectomy and she is otherwise healthy.

</details>

Category:

### A25. answerable_informative · trec-202134 · turn 11

- **Trial:** NCT00976560, Clinical Study to Test a New Drug to Treat Major Depression
- **Question:** Boolean indicating whether the patient has had a positive hepatitis C antibody test in the past 3 months.
- **Variable:** `patient_has_undergone_hepatitis_c_antibody_measurement_inthepast3months_outcome_is_positive`
- **Answer:** unknown (useful_unanswered)
- **Criteria line:** exclusion: “History of liver disease or positive hepatitis B surface antigen or hepatitis C antibody in the last 3 months”

<details><summary>patient note</summary>

The patient is a 47-year-old Asian woman complaining of persistent feelings of sadness. She lost interest in activities she used to enjoy. She states that her mood is mostly depressed for the past 3 weeks. She also lost her appetite , which led to about 5kg weight loss. She complains of loss of energy and feelings of worthlessness nearly every day. She is not using any drugs and she does not smoke. She doesn't drink alcohol. She used to exercise every day for at least 30 min. But she doesn't have enough energy to do so for the past 3 weeks. She also has some digestive issues recently. She is married and has 4 children. She is menopausal. Her husband was recently diagnosed with colon cancer and he is starting his chemotherapy. There is nothing remarkable in her past medical history and her drug history is only positive for Vit D3 1000 units daily. Her family history is negative for any psychologic problems. Her HAM-D score is 20.

</details>

Category:

### A26. answerable_informative · trec-202143 · turn 26

- **Trial:** NCT02112279, Reduction of C-Difficile Infection Using Stool Transplant
- **Question:** Boolean indicating whether the antibiotic therapy undergone by the patient in the past was appropriate for Clostridioides difficile infection.
- **Variable:** `patient_has_undergone_antibiotic_therapy_inthehistory@@appropriate_for_clostridioides_difficile_infection`
- **Answer:** unknown (useful_unanswered)
- **Criteria line:** exclusion: “Less than two courses of appropriate antibiotic therapy for C. difficile infection”

<details><summary>patient note</summary>

The patient is a 60-year-old woman admitted to the stroke department with a recent history of a second course of intravenous antibiotics for aspiration pneumonia. She is febrile and complained of abdominal pain and diarrhea (bowel movements eight times in 3 hours, large volumes of greenish, liquid stool each time).
The patient's abdomen is generally tender and distend with hyperactive bowel sounds. She is febrile (38.4°C), tachycardic (113/min) and hypotensive (80/40 mmHg). The stool samples must were positive for Clostridium difficile toxin.

</details>

Category:

### A27. answerable_informative · trec-202152 · turn 23

- **Trial:** NCT00807326, A Comparison of Three Medications to Treat Diarrhea in Adults.
- **Question:** Boolean indicating whether the patient has ever had a diagnosis of acquired immunodeficiency syndrome (AIDS) in their medical history.
- **Variable:** `patient_has_diagnosis_of_aids_inthehistory`
- **Answer:** unknown (useful_unanswered)
- **Criteria line:** exclusion: “Immunodeficiency (e.g. those with acquired immunodeficiency syndrome [AIDS] or known human immunodeficiency virus [HIV] infection, or undergoing chemotherapy or radiotherapy)”

<details><summary>patient note</summary>

A 34 year old man comes to the clinic complaining of dizziness and severe diarrhea since yesterday. He has returned from an international trip few days ago and was living in a camp in Sudan for a month. He developed abdominal pain followed by bloating and nausea as well as loose bowel movements. Soon he was having profuse watery diarrhea without odor. The stool is watery and white but the patient has no fever. Blood pressure is 95/62 lying down and drops to 75/40 standing. The skin turgor has reduced. HR is 110 and he looks ill with dry mucosa. V. cholerae was seen in dark-field microscopy of a fresh stool specimen. The lab study is as bellow:
Sodium                           137 meq/L
Potassium                      2 meq/L
Chloride                         94meq/L
CO2                                 15 meq/L
Fecal leukocytes           None seen
Fecal occult blood        Negative

</details>

Category:

### A28. answerable_informative · trec-202157 · turn 30

- **Trial:** NCT04196504, Prevalence of Echocardioghraphic and ECG Changes in Patients With Acute Pancreatitis and Its Impact on Outcome.
- **Question:** Boolean indicating whether the patient's chronic pancreatitis is an underlying condition.
- **Variable:** `patient_has_finding_of_chronic_pancreatitis_now@@underlying`
- **Answer:** unknown (useful_unanswered)
- **Criteria line:** exclusion: “patients with underlying chronic pancreatitis”

<details><summary>patient note</summary>

The patient is a 41-year-old obese woman coming to the emergency room with abdominal pain and vomiting. The pain that started gradually yesterday is located in the epigastric and periumbilical regions, radiating to her back. She drinks alcohol frequently and does not smoke. She has no history of allergies and uses only multivitamins daily. Her family history is positive for hypertension (her mother). She lives with her husband and has 3 children. The abdomen is tender and soft. Her bowel sounds are normal. Her heart rate is 115/min and blood pressure 110/75 mmHg. The lab studies are remarkable for leukocytosis (19.5), urea of 8.5, high CRP (145), high amylase (1200) and Glucose level of 15. Her abdominal CT scan revealed acute edematous interstitial pancreatitis with enlarged common bile duct and intrahepatic duct confirming gall stone pancreatitis. Her pregnancy test is negative and she is not breastfeeding.

</details>

Category:

### A29. answerable_informative · trec-202161 · turn 19

- **Trial:** NCT03992521, Breast Cancer Liquid Biopsy Stratification
- **Question:** Boolean indicating whether both plasma and deoxyribonucleic acid are currently available from the patient.
- **Variable:** `patient_has_plasma_dna_available_now`
- **Answer:** unknown (useful_unanswered)
- **Criteria line:** inclusion: “Histological diagnosis of breast cancer, availability of primary tumor tissue and plasma DNA with a high ctDNA content.”

<details><summary>patient note</summary>

The patient is a 45-year-old postmenopausal woman with cytologically confirmed breast cancer. A core biopsy revealed a 3 cm invasive ductal breast carcinoma in the left upper outer quadrant. The tumor is  HER2-positive and ER/PR negative. Axillary sampling revealed 5 positive lymph nodes. CXR was remarkable for metastatic lesions. The patient is using multivitamins and iron supplements. She does not smoke or consume alcohol. She is not sexually active and has no children. She is a candidate for tumor resection and agrees to do so prior to chemotherapy.

</details>

Category:

### A30. answerable_informative · trec-202164 · turn 3

- **Trial:** NCT00039962, Thymosin Plus PEG-Interferon in Hepatitis C Patients With Cirrhosis Who Did Not Respond to Interferon or Interferon Plus Ribavirin
- **Question:** Boolean indicating whether the liver biopsy occurred at least 6 months after the end of the prior failed therapy.
- **Variable:** `patient_has_undergone_biopsy_of_liver_inthehistory@@temporalcontext_atleast6months_after_prior_failed_therapy`
- **Answer:** unknown (useful_unanswered)
- **Criteria line:** inclusion: “Liver biopsy consistent with cirrhosis or progression to cirrhosis (METAVIR fibrosis score 3 to 4) due to chronic hepatitis C within the last 12 months before treatment starts, and at least 6 months after the end of the prior failed therapy.”

<details><summary>patient note</summary>

The patient is a 55-year-old man diagnosed with HCV 2 years ago and the recent coinfection with HBV. His past medical history is non-significant. He is on IFN, RBV and direct antiviral drugs for the past 6 months. The patient takes no other medications. His medical records show previous positive HCV RNA tests and a positive enzyme immunoassay for anti-HCV-antibodies. The recent biopsy was negative for hepatocellular carcinoma and was only remarkable for chronic inflammation compatible with a chronic viral hepatitis. There is no evidence of alcoholic liver disease, bleeding from esophageal varices, hemochromatosis, autoimmune hepatitis, or metabolic liver disease. He is an alert male with no acute distress. His BP: 130/75, HR: 90/min and BMI: 27. His abdomen is soft with no ascites or tenderness. The lower extremities are normal with no edema.

</details>

Category:

## B. answerable_informative wrong, greedy_smt right at k=30 (8 pairs)

### B1. trec-202114 × NCT00394225

- **Trial:** Helium-Hyperoxia and 6MWT Distance in COPD
- **Gold:** ineligible; at k=30: greedy_smt → ineligible, answerable_informative → eligible
- **greedy_smt asked on this trial (7):**
  - turn 5: Boolean indicating whether the patient has had an acute exacerbation of chronic obstructive pulmonary disease in the past 4 weeks. → unknown (useful_unanswered)
    criteria line: exclusion: “Recent exacerbation (< 4 wks)”
  - turn 6: Boolean indicating whether the patient's current cardiovascular system abnormalities are significant. → unknown (useful_unanswered)
    criteria line: exclusion: “Significant cardiovascular/musculoskeletal abnormalities”
  - turn 7: patient_has_finding_of_chronic_obstructive_pulmonary_disease_now → true (useful_answered)
    criteria line: (no matching line found)
  - turn 8: Boolean indicating whether the patient currently has a disability affecting daily living (activity limitation). → true (useful_answered)
    criteria line: (no matching line found)
  - turn 9: Boolean indicating whether the patient currently has exertional dyspnea (dyspnea on exertion). → unknown (useful_unanswered)
    criteria line: (no matching line found)
  - turn 10: Boolean indicating whether the patient's current musculoskeletal system abnormalities are significant. → unknown (useful_unanswered)
    criteria line: exclusion: “Significant cardiovascular/musculoskeletal abnormalities”
  - turn 11: Boolean indicating whether the patient is currently undergoing oxygen therapy. → true (useful_answered)
    criteria line: (no matching line found)
- **answerable_informative asked on this trial (3):**
  - turn 9: patient_has_finding_of_chronic_obstructive_pulmonary_disease_now → true (useful_answered)
    criteria line: (no matching line found)
  - turn 21: Boolean indicating whether the patient currently has exertional dyspnea (dyspnea on exertion). → unknown (useful_unanswered)
    criteria line: (no matching line found)
  - turn 24: Boolean indicating whether the patient currently has a disability affecting daily living (activity limitation). → true (useful_answered)
    criteria line: (no matching line found)

<details><summary>patient note</summary>

70 y/o with COPD on 2.5-3.5L O2 at baseline, OSA and obesity hypoventilation syndrome, dCHF, discharged [**2132-8-24**] now presents with agitation and altered mental status with hypoxia and O2 sats 70s on BipAp with 5L. Pt agitated then somnolent at initial presentation. Daughter reported increased agitation and altered mental status x 2-3 days with O2 sats 60s-70s at home. Daughter has also noted increased LE edema and weight gain which prompted a phone call to her PCP and increased lasix dose from 80daily to 100mg daily with some mild improvement in edema. She has had decreased appetite, PO intake, energy level at home with difficulty with ADLs. No recent history of fever, cough, chills, sputum production, CP, abd pain, or other complaints other than chronic right thigh pain last 1-2 months. Daughter also reports med compliance and compliance with BiPap at night.
Past Medical History:
- CAD; s/p 4 vessel CABG in [**2119**]
- CHF; EF 55%, mild AS
- obesity hypoventilation syndrome
- obstructive sleep apnea
- DM2
- ventricular tachycardia; s/p ICD in [**2127**]
- hypothyroidism
- schizophrenia
- COPD
- Pneumona treated in [**4-7**] at [**Hospital1 **]

</details>

Category:

### B2. trec-202114 × NCT00871962

- **Trial:** Long-term Oxygen Treatment (LTOT) in Chronic Obstructive Pulmonary Disease: Factors Influencing Survival
- **Gold:** ineligible; at k=30: greedy_smt → ineligible, answerable_informative → eligible
- **greedy_smt asked on this trial (2):**
  - turn 15: Boolean indicating whether the patient currently has a diagnosis of chronic obstructive pulmonary disease. → true (useful_answered)
    criteria line: inclusion: “Patients treated by LTOT, with or without clinically fulfilled criteria for LTOT, with PaO2<55mmHg or less at rest or during sleeping or less during exercise, if supplemental oxygen is demonstrated to improve the exercise-associated hypoxia. Patients with PaO2 56-59mmHg if they also have dependent edema, pulmonary hypertension or hematocrit higher than 56%”
  - turn 16: Boolean indicating whether the patient currently has a diagnosis of obstructive sleep apnea syndrome. → true (useful_answered)
    criteria line: exclusion: “Patient with obstructive sleep apnea or overlap syndrome”
- **answerable_informative asked on this trial (1):**
  - turn 2: Boolean indicating whether the patient currently has a diagnosis of chronic obstructive pulmonary disease. → true (useful_answered)
    criteria line: inclusion: “Patients treated by LTOT, with or without clinically fulfilled criteria for LTOT, with PaO2<55mmHg or less at rest or during sleeping or less during exercise, if supplemental oxygen is demonstrated to improve the exercise-associated hypoxia. Patients with PaO2 56-59mmHg if they also have dependent edema, pulmonary hypertension or hematocrit higher than 56%”

<details><summary>patient note</summary>

70 y/o with COPD on 2.5-3.5L O2 at baseline, OSA and obesity hypoventilation syndrome, dCHF, discharged [**2132-8-24**] now presents with agitation and altered mental status with hypoxia and O2 sats 70s on BipAp with 5L. Pt agitated then somnolent at initial presentation. Daughter reported increased agitation and altered mental status x 2-3 days with O2 sats 60s-70s at home. Daughter has also noted increased LE edema and weight gain which prompted a phone call to her PCP and increased lasix dose from 80daily to 100mg daily with some mild improvement in edema. She has had decreased appetite, PO intake, energy level at home with difficulty with ADLs. No recent history of fever, cough, chills, sputum production, CP, abd pain, or other complaints other than chronic right thigh pain last 1-2 months. Daughter also reports med compliance and compliance with BiPap at night.
Past Medical History:
- CAD; s/p 4 vessel CABG in [**2119**]
- CHF; EF 55%, mild AS
- obesity hypoventilation syndrome
- obstructive sleep apnea
- DM2
- ventricular tachycardia; s/p ICD in [**2127**]
- hypothyroidism
- schizophrenia
- COPD
- Pneumona treated in [**4-7**] at [**Hospital1 **]

</details>

Category:

### B3. trec-202123 × NCT00287378

- **Trial:** Effect of Ozone on Airway Inflammation in Allergic Asthmatics Treated With Omalizumab
- **Gold:** ineligible; at k=30: greedy_smt → ineligible, answerable_informative → eligible
- **greedy_smt asked on this trial (19):**
  - turn 12: individual_symptom_scores_value_recorded_now_all_scores_leq_3 → unknown (useful_unanswered)
    criteria line: inclusion: “Symptom Score (defined in section f) no greater than 20 (out of a possible 60) for total symptom score with a value no greater than 3 for any one score. No more than one score may be greater or equal than 3.”
  - turn 13: patient_has_allergy_to_acetaminophen_containing_product_now → unknown (useful_unanswered)
    criteria line: exclusion: “Allergy to any medications which may be used in the course of this study (albuterol, acetaminophen, aspirin or non-steroidal anti-inflammatory agents, corticosteroids, lactose, polyethylene glycol)”
  - turn 14: patient_has_allergy_to_albuterol_containing_product_now → unknown (useful_unanswered)
    criteria line: exclusion: “Allergy to any medications which may be used in the course of this study (albuterol, acetaminophen, aspirin or non-steroidal anti-inflammatory agents, corticosteroids, lactose, polyethylene glycol)”
  - turn 15: patient_has_allergy_to_aspirin_containing_product_now → unknown (useful_unanswered)
    criteria line: exclusion: “Allergy to any medications which may be used in the course of this study (albuterol, acetaminophen, aspirin or non-steroidal anti-inflammatory agents, corticosteroids, lactose, polyethylene glycol)”
  - turn 16: patient_has_allergy_to_corticosteroid_and_corticosteroid_derivative_containing_product_now → unknown (useful_unanswered)
    criteria line: exclusion: “Allergy to any medications which may be used in the course of this study (albuterol, acetaminophen, aspirin or non-steroidal anti-inflammatory agents, corticosteroids, lactose, polyethylene glycol)”
  - turn 17: patient_has_allergy_to_lactose_containing_product_now → unknown (useful_unanswered)
    criteria line: exclusion: “Allergy to any medications which may be used in the course of this study (albuterol, acetaminophen, aspirin or non-steroidal anti-inflammatory agents, corticosteroids, lactose, polyethylene glycol)”
  - turn 18: patient_has_allergy_to_medication_used_in_study_now → unknown (useful_unanswered)
    criteria line: exclusion: “Allergy to any medications which may be used in the course of this study (albuterol, acetaminophen, aspirin or non-steroidal anti-inflammatory agents, corticosteroids, lactose, polyethylene glycol)”
  - turn 19: patient_has_allergy_to_non_steroidal_anti_inflammatory_agent_now → unknown (useful_unanswered)
    criteria line: exclusion: “Allergy to any medications which may be used in the course of this study (albuterol, acetaminophen, aspirin or non-steroidal anti-inflammatory agents, corticosteroids, lactose, polyethylene glycol)”
  - turn 20: patient_has_allergy_to_polyethylene_glycol_containing_product_now → unknown (useful_unanswered)
    criteria line: exclusion: “Allergy to any medications which may be used in the course of this study (albuterol, acetaminophen, aspirin or non-steroidal anti-inflammatory agents, corticosteroids, lactose, polyethylene glycol)”
  - turn 21: patient_has_diagnosis_of_autoimmune_disease_inthehistory@@significant_and_chronic → false (useful_answered)
    criteria line: exclusion: “A history of significant chronic illnesses (to include diabetes, autoimmune diseases, immunodeficiency state, known ischemic heart disease, chronic respiratory diseases such as chronic obstructive pulmonary disease or severe asthma, hypertension)”
  - turn 22: patient_has_diagnosis_of_chronic_obstructive_lung_disease_inthehistory@@excluded_unless_lung_function_criteria_met → false (useful_answered)
    criteria line: exclusion: “Acute, non-chronic, medical conditions, including (but not limited to) pneumonia or bronchitis requiring antibiotics, febrile illnesses, flu-like symptoms must be totally resolved symptomatically for 2 weeks. Documentation of normal lung function (as defined in Specific inclusion criteria) must be met.”
  - turn 23: patient_has_diagnosis_of_diabetes_mellitus_inthehistory@@significant_and_chronic → false (useful_answered)
    criteria line: exclusion: “A history of significant chronic illnesses (to include diabetes, autoimmune diseases, immunodeficiency state, known ischemic heart disease, chronic respiratory diseases such as chronic obstructive pulmonary disease or severe asthma, hypertension)”
  - turn 24: patient_has_diagnosis_of_hypertension_inthehistory@@uncontrolled_or_poorly_controlled → unknown (useful_unanswered)
    criteria line: exclusion: “A history of significant chronic illnesses (to include diabetes, autoimmune diseases, immunodeficiency state, known ischemic heart disease, chronic respiratory diseases such as chronic obstructive pulmonary disease or severe asthma, hypertension)”
  - turn 25: patient_has_diagnosis_of_immunodeficiency_disorder_inthehistory@@significant_and_chronic → false (useful_answered)
    criteria line: exclusion: “A history of significant chronic illnesses (to include diabetes, autoimmune diseases, immunodeficiency state, known ischemic heart disease, chronic respiratory diseases such as chronic obstructive pulmonary disease or severe asthma, hypertension)”
  - turn 26: patient_has_diagnosis_of_severe_asthma_inthehistory@@excluded_unless_lung_function_criteria_met → unknown (useful_unanswered)
    criteria line: exclusion: “Acute, non-chronic, medical conditions, including (but not limited to) pneumonia or bronchitis requiring antibiotics, febrile illnesses, flu-like symptoms must be totally resolved symptomatically for 2 weeks. Documentation of normal lung function (as defined in Specific inclusion criteria) must be met.”
  - turn 27: patient_has_finding_of_allergy_to_dust_mite_protein_now → unknown (useful_unanswered)
    criteria line: inclusion: “Evidence of allergy to house dust mite”
  - turn 28: patient_has_finding_of_illness_now@@increases_risk_of_ozone_inhalation_challenge_investigator_judgment → unknown (useful_unanswered)
    criteria line: exclusion: “Unspecified illnesses, which in the judgment of the investigator increase the risk associated with ozone inhalation challenge, will be a basis for exclusion.”
  - turn 29: patient_has_positive_pregnancy_test_at_initial_screening → false (useful_answered)
    criteria line: exclusion: “Positive pregnancy test at time of initial screening”
  - turn 30: patient_has_undergone_administration_of_steroid_inthepast12months → true (useful_answered)
    criteria line: exclusion: “Allergy to any medications which may be used in the course of this study (albuterol, acetaminophen, aspirin or non-steroidal anti-inflammatory agents, corticosteroids, lactose, polyethylene glycol)”
- **answerable_informative asked on this trial (1):**
  - turn 25: patient_is_taking_antibiotic_now → false (useful_answered)
    criteria line: exclusion: “Medications which may impact the results of the ozone challenge, interfere with any other medications potentially used in the study (to include steroids, beta antagonists, non-steroidal anti-inflammatory agents) or suggest an ongoing illness (such as antibiotics)”

<details><summary>patient note</summary>

A 39-year-old man came to the clinic with cough and shortness of breath that was not relieved by  his inhaler. He had these symptoms for 5 days during the past 2 weeks. He doubled his oral corticosteroids in the past week. He is a chef with a  history of asthma for 3 years, suffering from frequent cough, wheezing, and shortness of breath and chest tightness. The symptoms become more bothersome within 1-2 hours of starting work every day and worsen throughout the work week. His symptoms improve within 1-2 hours outside the workplace. Spirometry was performed revealing a forced expiratory volume in the first second (FEV1) of 63% of the predicted. His past medical history is significant for seasonal allergic rhinitis in the summer. He doesn't smoke or use illicit drugs. His family history is significant for asthma in his father and sister.  He currently uses inhaled corticosteroid (ICS) and fluticasone 500 mcg/salmeterol 50 mcg, one puff twice daily.

</details>

Category:

### B4. trec-202129 × NCT03775733

- **Trial:** Efficacy and Safety of Hydrolysed Red Ginseng Extract on Improvement of Hyperglycemia
- **Gold:** eligible; at k=30: greedy_smt → eligible, answerable_informative → ineligible
- **greedy_smt asked on this trial (0):** nothing
- **answerable_informative asked on this trial (1):**
  - turn 17: Boolean indicating whether the patient has undergone any laboratory test now. → true (useful_answered)
    criteria line: exclusion: “Laboratory test by show the following results”

<details><summary>patient note</summary>

The patient is a 24-year-old man who has had type 1 diabetes for 11 years. He presents to the emergency room with hyperglycemia and concern for possible diabetic ketoacidosis after not taking his insulin for 3 days. The patient reports that he is currently homeless and has lost his supply of insulin, syringes, glucometer, and glucose testing supplies. The patient states that at the time of his initial diagnosis with type 1 diabetes he was hospitalized with a glucose value >1000 mg/dL. At the time, he was experiencing polyuria, polydipsia, and polyphagia. He reports that he has been on insulin since the time of his diagnosis, and he has never been prescribed oral agents for diabetes management. Most recently, he has been using insulin glargine 55 units once daily, and insulin aspart sliding scale 3 times daily. The patient has had previous episodes of diabetic ketoacidosis, for which he was hospitalized. With this episode of hyperglycemia, he is not experiencing any nausea, vomiting, or abdominal discomfort, and he appears well. His lab studies showed:
A1c: 11.3%
Creatinine: 0.9 mg/dL with eGFR >60 mL/min
Aspartate aminotransferase (AST): 17 U/L
Alanine aminotransferase (ALT): 14 U/L
Beta-hydroxybutyrate: 0.1 mmol/L
Bicarbonate: 25 mEq/L
Anion Gap: 14 mEq/L

</details>

Category:

### B5. trec-202143 × NCT00304369

- **Trial:** Response of Clostridium Difficile Infection to Metronidazole Therapy
- **Gold:** ineligible; at k=30: greedy_smt → ineligible, answerable_informative → eligible
- **greedy_smt asked on this trial (1):**
  - turn 1: Boolean indicating whether the patient has ever received treatment for Clostridium difficile colitis with oral metronidazole at any time in the past. → false (useful_answered)
    criteria line: inclusion: “records of patients who have a fecal sample positive for C. difficile toxin and who are then treated for C. difficile colitis with oral metronidazole will be included in this study.”
- **answerable_informative asked on this trial (1):**
  - turn 14: Boolean indicating whether the patient has ever undergone a collection of stool specimen (fecal sample) at any time in the past. → true (useful_answered)
    criteria line: (no matching line found)

<details><summary>patient note</summary>

The patient is a 60-year-old woman admitted to the stroke department with a recent history of a second course of intravenous antibiotics for aspiration pneumonia. She is febrile and complained of abdominal pain and diarrhea (bowel movements eight times in 3 hours, large volumes of greenish, liquid stool each time).
The patient's abdomen is generally tender and distend with hyperactive bowel sounds. She is febrile (38.4°C), tachycardic (113/min) and hypotensive (80/40 mmHg). The stool samples must were positive for Clostridium difficile toxin.

</details>

Category:

### B6. trec-202143 × NCT00807326

- **Trial:** A Comparison of Three Medications to Treat Diarrhea in Adults.
- **Gold:** ineligible; at k=30: greedy_smt → ineligible, answerable_informative → eligible
- **greedy_smt asked on this trial (24):**
  - turn 2: Boolean indicating whether the patient currently has clinical signs of orthostatic hypotension. → unknown (useful_unanswered)
    criteria line: exclusion: “Signs or symptoms of orthostatic hypotension”
  - turn 3: Boolean indicating whether the patient currently has any condition that, in the opinion of the investigator, would compromise the well-being of the subject or would compromise the study. → unknown (useful_unanswered)
    criteria line: exclusion: “Any condition that, in the opinion of the investigator, would compromise the well-being of the subject or the study”
  - turn 4: Boolean indicating whether the determination is made in the opinion of the investigator. → unknown (useful_unanswered)
    criteria line: exclusion: “Any condition that, in the opinion of the investigator, would compromise the well-being of the subject or the study”
  - turn 5: Boolean indicating whether the patient has ever had a diagnosis of acquired immunodeficiency syndrome (AIDS) in their medical history. → unknown (useful_unanswered)
    criteria line: exclusion: “Immunodeficiency (e.g. those with acquired immunodeficiency syndrome [AIDS] or known human immunodeficiency virus [HIV] infection, or undergoing chemotherapy or radiotherapy)”
  - turn 6: Boolean indicating whether the patient has ever been diagnosed with a chronic digestive system disorder. → unknown (useful_unanswered)
    criteria line: exclusion: “History of chronic gastrointestinal disease, hepatic or renal insufficiency, or other significant medical condition that could be aggravated by untreated acute diarrhea”
  - turn 7: Boolean indicating whether the disease condition (medical condition) could be aggravated by untreated acute diarrhea. → unknown (useful_unanswered)
    criteria line: exclusion: “History of chronic gastrointestinal disease, hepatic or renal insufficiency, or other significant medical condition that could be aggravated by untreated acute diarrhea”
  - turn 8: Boolean indicating whether the patient has ever been diagnosed with hepatic failure. → unknown (useful_unanswered)
    criteria line: exclusion: “History of chronic gastrointestinal disease, hepatic or renal insufficiency, or other significant medical condition that could be aggravated by untreated acute diarrhea”
  - turn 9: Boolean indicating whether the patient has ever had a diagnosis of human immunodeficiency virus (HIV) infection in their medical history. → unknown (useful_unanswered)
    criteria line: exclusion: “Immunodeficiency (e.g. those with acquired immunodeficiency syndrome [AIDS] or known human immunodeficiency virus [HIV] infection, or undergoing chemotherapy or radiotherapy)”
  - turn 10: Boolean indicating whether the patient has ever had a diagnosis of immunodeficiency disorder in their medical history. → unknown (useful_unanswered)
    criteria line: exclusion: “Immunodeficiency (e.g. those with acquired immunodeficiency syndrome [AIDS] or known human immunodeficiency virus [HIV] infection, or undergoing chemotherapy or radiotherapy)”
  - turn 11: Boolean indicating whether the patient has ever been diagnosed with renal insufficiency. → unknown (useful_unanswered)
    criteria line: exclusion: “History of chronic gastrointestinal disease, hepatic or renal insufficiency, or other significant medical condition that could be aggravated by untreated acute diarrhea”
  - turn 12: patient_has_finding_of_acute_diarrhea_now → true (useful_answered)
    criteria line: inclusion: “Acute diarrhea illness with symptoms onset within 48 hours of study entry”
  - turn 13: patient_has_finding_of_acute_diarrhea_now@@symptom_onset_within_48_hours_before_study_entry → unknown (useful_unanswered)
    criteria line: inclusion: “Acute diarrhea illness with symptoms onset within 48 hours of study entry”
  - turn 14: Boolean indicating whether the patient's history of hematochezia (gross blood in stool) occurred during the current illness. → unknown (useful_unanswered)
    criteria line: exclusion: “History or clinical evidence of gross blood or pus in stool in current illness”
  - turn 15: Boolean indicating whether the patient's current hematochezia (gross blood in stool) is present during the current illness. → unknown (useful_unanswered)
    criteria line: exclusion: “History or clinical evidence of gross blood or pus in stool in current illness”
  - turn 16: Boolean indicating whether the patient's current hypersensitivity condition is to any component of the study formulations. → unknown (useful_unanswered)
    criteria line: exclusion: “Intake of antibiotics, oral antifungals, quinidine or ritonavir within 7 days, antidiarrhoeal, promotility drugs (e.g., metoclopramide, domperidone), antiflatulents (e.g., simeticone, activated charcoal) or probiotics or bismuth salts within 48 hours, or any analgesic within 6 hours prior to study entry Hypersensitivity to loperamide, yeast, or any component of study formulations”
  - turn 17: Boolean indicating whether the patient's current hypersensitivity condition is to loperamide. → unknown (useful_unanswered)
    criteria line: exclusion: “Intake of antibiotics, oral antifungals, quinidine or ritonavir within 7 days, antidiarrhoeal, promotility drugs (e.g., metoclopramide, domperidone), antiflatulents (e.g., simeticone, activated charcoal) or probiotics or bismuth salts within 48 hours, or any analgesic within 6 hours prior to study entry Hypersensitivity to loperamide, yeast, or any component of study formulations”
  - turn 18: Boolean indicating whether the patient's current hypersensitivity condition is to yeast. → unknown (useful_unanswered)
    criteria line: exclusion: “Intake of antibiotics, oral antifungals, quinidine or ritonavir within 7 days, antidiarrhoeal, promotility drugs (e.g., metoclopramide, domperidone), antiflatulents (e.g., simeticone, activated charcoal) or probiotics or bismuth salts within 48 hours, or any analgesic within 6 hours prior to study entry Hypersensitivity to loperamide, yeast, or any component of study formulations”
  - turn 19: Boolean indicating whether the patient's history of pus in stool occurred during the current illness. → unknown (useful_unanswered)
    criteria line: exclusion: “History or clinical evidence of gross blood or pus in stool in current illness”
  - turn 20: Boolean indicating whether the patient's current pus in stool is present during the current illness. → unknown (useful_unanswered)
    criteria line: exclusion: “History or clinical evidence of gross blood or pus in stool in current illness”
  - turn 21: Boolean indicating whether the patient currently has symptoms of orthostatic hypotension. → unknown (useful_unanswered)
    criteria line: exclusion: “Signs or symptoms of orthostatic hypotension”
  - turn 22: Boolean indicating whether the patient is currently breast-feeding. → unknown (useful_unanswered)
    criteria line: exclusion: “Pregnant or breast-feeding”
  - turn 23: Boolean indicating whether the patient has been exposed to activated charcoal in the 48 hours prior to now. → unknown (useful_unanswered)
    criteria line: exclusion: “Intake of antibiotics, oral antifungals, quinidine or ritonavir within 7 days, antidiarrhoeal, promotility drugs (e.g., metoclopramide, domperidone), antiflatulents (e.g., simeticone, activated charcoal) or probiotics or bismuth salts within 48 hours, or any analgesic within 6 hours prior to study entry Hypersensitivity to loperamide, yeast, or any component of study formulations”
  - turn 24: Boolean indicating whether the patient has been exposed to any analgesic in the 6 hours prior to now. → unknown (useful_unanswered)
    criteria line: exclusion: “Intake of antibiotics, oral antifungals, quinidine or ritonavir within 7 days, antidiarrhoeal, promotility drugs (e.g., metoclopramide, domperidone), antiflatulents (e.g., simeticone, activated charcoal) or probiotics or bismuth salts within 48 hours, or any analgesic within 6 hours prior to study entry Hypersensitivity to loperamide, yeast, or any component of study formulations”
  - turn 25: Boolean indicating whether the patient has been exposed to any antibiotics in the 7 days prior to now. → true (useful_answered)
    criteria line: exclusion: “Requiring hospital admission, parenteral hydration or antibiotic therapy Axillary temperature >38.2°C or oral temperature >38.6°C”
- **answerable_informative asked on this trial (7):**
  - turn 8: Boolean indicating whether the patient's current pus in stool is present during the current illness. → unknown (useful_unanswered)
    criteria line: exclusion: “History or clinical evidence of gross blood or pus in stool in current illness”
  - turn 9: patient_has_finding_of_acute_diarrhea_now@@symptom_onset_within_48_hours_before_study_entry → unknown (useful_unanswered)
    criteria line: inclusion: “Acute diarrhea illness with symptoms onset within 48 hours of study entry”
  - turn 11: Boolean indicating whether the patient's history of pus in stool occurred during the current illness. → unknown (useful_unanswered)
    criteria line: exclusion: “History or clinical evidence of gross blood or pus in stool in current illness”
  - turn 13: Boolean indicating whether the patient's current hematochezia (gross blood in stool) is present during the current illness. → unknown (useful_unanswered)
    criteria line: exclusion: “History or clinical evidence of gross blood or pus in stool in current illness”
  - turn 16: Boolean indicating whether the patient's history of hematochezia (gross blood in stool) occurred during the current illness. → unknown (useful_unanswered)
    criteria line: exclusion: “History or clinical evidence of gross blood or pus in stool in current illness”
  - turn 21: patient_has_finding_of_acute_diarrhea_now → true (useful_answered)
    criteria line: inclusion: “Acute diarrhea illness with symptoms onset within 48 hours of study entry”
  - turn 29: Boolean indicating whether the patient currently has symptoms of orthostatic hypotension. → unknown (useful_unanswered)
    criteria line: exclusion: “Signs or symptoms of orthostatic hypotension”

<details><summary>patient note</summary>

The patient is a 60-year-old woman admitted to the stroke department with a recent history of a second course of intravenous antibiotics for aspiration pneumonia. She is febrile and complained of abdominal pain and diarrhea (bowel movements eight times in 3 hours, large volumes of greenish, liquid stool each time).
The patient's abdomen is generally tender and distend with hyperactive bowel sounds. She is febrile (38.4°C), tachycardic (113/min) and hypotensive (80/40 mmHg). The stool samples must were positive for Clostridium difficile toxin.

</details>

Category:

### B7. trec-202143 × NCT02112279

- **Trial:** Reduction of C-Difficile Infection Using Stool Transplant
- **Gold:** ineligible; at k=30: greedy_smt → ineligible, answerable_informative → eligible
- **greedy_smt asked on this trial (4):**
  - turn 26: Boolean indicating whether the patient currently has symptoms of Clostridioides difficile infection. → true (useful_answered)
    criteria line: inclusion: “Continued symptoms of c-difficile infection”
  - turn 27: Boolean indicating whether the patient has ever undergone antibiotic therapy in their history. → true (useful_answered)
    criteria line: inclusion: “Patients must have failed at least two courses of appropriate antibiotic therapy for C. diff to be a candidate for this procedure”
  - turn 28: Boolean indicating whether the antibiotic therapy undergone by the patient in the past was appropriate for Clostridioides difficile infection. → unknown (useful_unanswered)
    criteria line: exclusion: “Less than two courses of appropriate antibiotic therapy for C. difficile infection”
  - turn 29: Boolean indicating whether the patient has failed at least two courses of antibiotic therapy in the past. → false (useful_answered)
    criteria line: inclusion: “Patients must have failed at least two courses of appropriate antibiotic therapy for C. diff to be a candidate for this procedure”
- **answerable_informative asked on this trial (4):**
  - turn 6: Boolean indicating whether the patient has ever undergone antibiotic therapy in their history. → true (useful_answered)
    criteria line: inclusion: “Patients must have failed at least two courses of appropriate antibiotic therapy for C. diff to be a candidate for this procedure”
  - turn 18: Boolean indicating whether the patient currently has symptoms of Clostridioides difficile infection. → true (useful_answered)
    criteria line: inclusion: “Continued symptoms of c-difficile infection”
  - turn 22: Boolean indicating whether the patient has ever undergone a Clostridioides difficile assay (test) with a positive result at any time in the past. → true (useful_answered)
    criteria line: inclusion: “Patient must have a positive C. difficile test within the 10 days prior to the procedure”
  - turn 26: Boolean indicating whether the antibiotic therapy undergone by the patient in the past was appropriate for Clostridioides difficile infection. → unknown (useful_unanswered)
    criteria line: exclusion: “Less than two courses of appropriate antibiotic therapy for C. difficile infection”

<details><summary>patient note</summary>

The patient is a 60-year-old woman admitted to the stroke department with a recent history of a second course of intravenous antibiotics for aspiration pneumonia. She is febrile and complained of abdominal pain and diarrhea (bowel movements eight times in 3 hours, large volumes of greenish, liquid stool each time).
The patient's abdomen is generally tender and distend with hyperactive bowel sounds. She is febrile (38.4°C), tachycardic (113/min) and hypotensive (80/40 mmHg). The stool samples must were positive for Clostridium difficile toxin.

</details>

Category:

### B8. trec-202164 × NCT00230854

- **Trial:** Study in Non-responder Hepatitis C Genotype 1 Patients With EMZ702, Pegylated Interferon and Ribavirin
- **Gold:** ineligible; at k=30: greedy_smt → ineligible, answerable_informative → eligible
- **greedy_smt asked on this trial (4):**
  - turn 23: Boolean indicating whether the patient's current human immunodeficiency virus infection diagnosis is present as a coinfection. → false (useful_answered)
    criteria line: inclusion: “Hepatitis C virus (HCV) genotype 1”
  - turn 24: Boolean indicating whether the patient currently has a diagnosis of malignant neoplasm of the liver (liver cancer). → false (useful_answered)
    criteria line: exclusion: “Other unrelated liver diseases”
  - turn 25: Boolean indicating whether the patient currently has a diagnosis of any other liver disease that is unrelated to the primary condition of interest. → false (useful_answered)
    criteria line: exclusion: “Other unrelated liver diseases”
  - turn 26: Boolean indicating whether the patient's current hepatitis B diagnosis is present as a coinfection. → true (useful_answered)
    criteria line: exclusion: “Coinfection with hepatitis B or HIV”
- **answerable_informative asked on this trial (3):**
  - turn 7: Boolean indicating whether the patient currently has hepatitis C virus infection. → true (useful_answered)
    criteria line: inclusion: “Hepatitis C virus (HCV) genotype 1”
  - turn 27: Boolean indicating whether the patient currently has a diagnosis of any other liver disease that is unrelated to the primary condition of interest. → false (useful_answered)
    criteria line: exclusion: “Other unrelated liver diseases”
  - turn 28: Boolean indicating whether the patient has ever had a determination of outcome unsuccessful (treatment failure) at any time in the past. → unknown (useful_unanswered)
    criteria line: (no matching line found)

<details><summary>patient note</summary>

The patient is a 55-year-old man diagnosed with HCV 2 years ago and the recent coinfection with HBV. His past medical history is non-significant. He is on IFN, RBV and direct antiviral drugs for the past 6 months. The patient takes no other medications. His medical records show previous positive HCV RNA tests and a positive enzyme immunoassay for anti-HCV-antibodies. The recent biopsy was negative for hepatocellular carcinoma and was only remarkable for chronic inflammation compatible with a chronic viral hepatitis. There is no evidence of alcoholic liver disease, bleeding from esophageal varices, hemochromatosis, autoimmune hepatitis, or metabolic liver disease. He is an alert male with no acute distress. His BP: 130/75, HR: 90/min and BMI: 27. His abdomen is soft with no ascites or tenderness. The lower extremities are normal with no edema.

</details>

Category:

## C. greedy_smt wrong, answerable_informative right at k=30 (27 pairs)

### C1. trec-202112 × NCT01029561

- **Trial:** Impact of Obstructive Sleep Apnea Syndrome on Metabolic Syndrome in Severe Obesity
- **Gold:** ineligible; at k=30: greedy_smt → eligible, answerable_informative → ineligible
- **greedy_smt asked on this trial (0):** nothing
- **answerable_informative asked on this trial (2):**
  - turn 1: Boolean indicating whether the patient is currently included in the obesity surgery program. → false (not_useful)
    criteria line: inclusion: “Patients who are included in the obesity surgery program will be recruited if they fulfill the following criteria:”
  - turn 2: patient_is_included_in_obesity_surgery_program → false (useful_answered)
    criteria line: inclusion: “Patients who are included in the obesity surgery program will be recruited if they fulfill the following criteria:”

<details><summary>patient note</summary>

34 year old woman with Marfan's syndrome and known severe mitral valve prolapse with regurgitation, who was planned for a MV repair but was lost to follow-up. She remains symptomatic and is now prepared to undergo mitral valve repair/replacement surgery. EF of 65% on TTE. 
Past Medical History:
Marfans Syndrome
MVP with severe mitral regurgitation
Gastric reflux disease
History of gestational diabetes mellitus
Hypertension with pregnancy
Obesity
c-section x 2
laser eye surgery
cataract surgery
foot surgery (shorten bone length)

</details>

Category:

### C2. trec-202113 × NCT02305342

- **Trial:** Sensitivity of Antibiotics for Urinary Tract Infections Patients Attending Family Physicians
- **Gold:** ineligible; at k=30: greedy_smt → eligible, answerable_informative → ineligible
- **greedy_smt asked on this trial (0):** nothing
- **answerable_informative asked on this trial (2):**
  - turn 2: Boolean indicating whether the patient currently has symptoms of urinary tract infection. → true (useful_answered)
    criteria line: inclusion: “Samples from primary care clinics from patients who reports UTI symptoms and in which uropathogens are isolated will be included.”
  - turn 7: Boolean indicating whether the patient is currently being seen in a primary health care clinic. → false (useful_answered)
    criteria line: inclusion: “Samples from primary care clinics from patients who reports UTI symptoms and in which uropathogens are isolated will be included.”

<details><summary>patient note</summary>

62 yo male with hx of CVA, neurogenic bladder with indwelling suprapubic catheter with multiple prior admissions for UTIs, altered mental status, and urosepsis presents to the hospital in urosepsis now resolved after treatment with vanc/meropenem. Per CT there is a non-obstructing stone in the L ureter, no evidence of urethral strictures. Significant leaking around suprapubic cath site. Started on ditropan changed over to detrol. Urologist not concerned with leaking and will f/u with pt next week.
s/p CVA
Neurogenic bladder s/p suprapubic cath
Recurrent UTIs with Klebsiella/Pseudomonas
Non-hodgkins Marginal Zone Lymphoma of the left orbit Dx in 03
(s/p R-CHOP x 6 cycles)
Bells Palsy
BPH
Hypertension
Partial Bowel obstruction s/p colostomy
Hepatitis C
Cryoglobulinemia
SLE with transverse myelitis, anti-dsDNA Ab+
Insulin Dependant Diabetic
Fungal Esophagitis Stage IV?
Urinary Tract Infections-pseudomonas & enterococcus

</details>

Category:

### C3. trec-202114 × NCT01029561

- **Trial:** Impact of Obstructive Sleep Apnea Syndrome on Metabolic Syndrome in Severe Obesity
- **Gold:** ineligible; at k=30: greedy_smt → eligible, answerable_informative → ineligible
- **greedy_smt asked on this trial (0):** nothing
- **answerable_informative asked on this trial (2):**
  - turn 14: Boolean indicating whether the patient is currently included in the obesity surgery program. → false (not_useful)
    criteria line: inclusion: “Patients who are included in the obesity surgery program will be recruited if they fulfill the following criteria:”
  - turn 15: patient_is_included_in_obesity_surgery_program → false (useful_answered)
    criteria line: inclusion: “Patients who are included in the obesity surgery program will be recruited if they fulfill the following criteria:”

<details><summary>patient note</summary>

70 y/o with COPD on 2.5-3.5L O2 at baseline, OSA and obesity hypoventilation syndrome, dCHF, discharged [**2132-8-24**] now presents with agitation and altered mental status with hypoxia and O2 sats 70s on BipAp with 5L. Pt agitated then somnolent at initial presentation. Daughter reported increased agitation and altered mental status x 2-3 days with O2 sats 60s-70s at home. Daughter has also noted increased LE edema and weight gain which prompted a phone call to her PCP and increased lasix dose from 80daily to 100mg daily with some mild improvement in edema. She has had decreased appetite, PO intake, energy level at home with difficulty with ADLs. No recent history of fever, cough, chills, sputum production, CP, abd pain, or other complaints other than chronic right thigh pain last 1-2 months. Daughter also reports med compliance and compliance with BiPap at night.
Past Medical History:
- CAD; s/p 4 vessel CABG in [**2119**]
- CHF; EF 55%, mild AS
- obesity hypoventilation syndrome
- obstructive sleep apnea
- DM2
- ventricular tachycardia; s/p ICD in [**2127**]
- hypothyroidism
- schizophrenia
- COPD
- Pneumona treated in [**4-7**] at [**Hospital1 **]

</details>

Category:

### C4. trec-202114 × NCT02682251

- **Trial:** Engaging Patients in Heart Failure Management
- **Gold:** ineligible; at k=30: greedy_smt → eligible, answerable_informative → ineligible
- **greedy_smt asked on this trial (0):** nothing
- **answerable_informative asked on this trial (1):**
  - turn 1: Boolean indicating whether the patient has ever had a diagnosis of heart failure with reduced ejection fraction in their medical history. → false (useful_answered)
    criteria line: inclusion: “History of HFrEF (heart failure in the setting of reduced ejection fraction)”

<details><summary>patient note</summary>

70 y/o with COPD on 2.5-3.5L O2 at baseline, OSA and obesity hypoventilation syndrome, dCHF, discharged [**2132-8-24**] now presents with agitation and altered mental status with hypoxia and O2 sats 70s on BipAp with 5L. Pt agitated then somnolent at initial presentation. Daughter reported increased agitation and altered mental status x 2-3 days with O2 sats 60s-70s at home. Daughter has also noted increased LE edema and weight gain which prompted a phone call to her PCP and increased lasix dose from 80daily to 100mg daily with some mild improvement in edema. She has had decreased appetite, PO intake, energy level at home with difficulty with ADLs. No recent history of fever, cough, chills, sputum production, CP, abd pain, or other complaints other than chronic right thigh pain last 1-2 months. Daughter also reports med compliance and compliance with BiPap at night.
Past Medical History:
- CAD; s/p 4 vessel CABG in [**2119**]
- CHF; EF 55%, mild AS
- obesity hypoventilation syndrome
- obstructive sleep apnea
- DM2
- ventricular tachycardia; s/p ICD in [**2127**]
- hypothyroidism
- schizophrenia
- COPD
- Pneumona treated in [**4-7**] at [**Hospital1 **]

</details>

Category:

### C5. trec-202114 × NCT03184727

- **Trial:** Pulmonary Vasculature and Right Heart Dysfunction in Chronic Obstructive Pulmonay Disease
- **Gold:** ineligible; at k=30: greedy_smt → eligible, answerable_informative → ineligible
- **greedy_smt asked on this trial (0):** nothing
- **answerable_informative asked on this trial (2):**
  - turn 4: Boolean indicating whether the patient currently has a diagnosis of chronic obstructive pulmonary disease (COPD), regardless of stability. → true (useful_answered)
    criteria line: exclusion: “patents with other respiratory diseases and pulmonary hypertension other than group 3 PH;”
  - turn 11: patient_has_diagnosis_of_chronic_obstructive_pulmonary_disease_now@@stable → false (useful_answered)
    criteria line: exclusion: “patents with other respiratory diseases and pulmonary hypertension other than group 3 PH;”

<details><summary>patient note</summary>

70 y/o with COPD on 2.5-3.5L O2 at baseline, OSA and obesity hypoventilation syndrome, dCHF, discharged [**2132-8-24**] now presents with agitation and altered mental status with hypoxia and O2 sats 70s on BipAp with 5L. Pt agitated then somnolent at initial presentation. Daughter reported increased agitation and altered mental status x 2-3 days with O2 sats 60s-70s at home. Daughter has also noted increased LE edema and weight gain which prompted a phone call to her PCP and increased lasix dose from 80daily to 100mg daily with some mild improvement in edema. She has had decreased appetite, PO intake, energy level at home with difficulty with ADLs. No recent history of fever, cough, chills, sputum production, CP, abd pain, or other complaints other than chronic right thigh pain last 1-2 months. Daughter also reports med compliance and compliance with BiPap at night.
Past Medical History:
- CAD; s/p 4 vessel CABG in [**2119**]
- CHF; EF 55%, mild AS
- obesity hypoventilation syndrome
- obstructive sleep apnea
- DM2
- ventricular tachycardia; s/p ICD in [**2127**]
- hypothyroidism
- schizophrenia
- COPD
- Pneumona treated in [**4-7**] at [**Hospital1 **]

</details>

Category:

### C6. trec-202123 × NCT00042705

- **Trial:** Asthma Severity in Children and Environmental Agents
- **Gold:** ineligible; at k=30: greedy_smt → eligible, answerable_informative → ineligible
- **greedy_smt asked on this trial (4):**
  - turn 8: Boolean indicating whether the patient currently has a diagnosis of asthma. → true (useful_answered)
    criteria line: inclusion: “Physician diagnosed asthma”
  - turn 9: Boolean indicating whether the patient's current diagnosis of asthma was made by a physician. → true (useful_answered)
    criteria line: inclusion: “Physician diagnosed asthma”
  - turn 10: patient_is_sibling_of_birth_cohort_recruited_1997_1999 → unknown (useful_unanswered)
    criteria line: inclusion: “Siblings of a birth cohort recruited 1997-1999”
  - turn 11: patient_meets_inclusion_symptoms_or_medication_inthepast12months → true (useful_answered)
    criteria line: inclusion: “Active symptoms (wheeze, persistent cough, chest tightness, shortness of breath) or medication use in the 12 months prior to enrollment.”
- **answerable_informative asked on this trial (1):**
  - turn 1: Numeric value indicating the patient's current age in years. → 39.0 (useful_answered)
    criteria line: inclusion: “Age less than 11 years”

<details><summary>patient note</summary>

A 39-year-old man came to the clinic with cough and shortness of breath that was not relieved by  his inhaler. He had these symptoms for 5 days during the past 2 weeks. He doubled his oral corticosteroids in the past week. He is a chef with a  history of asthma for 3 years, suffering from frequent cough, wheezing, and shortness of breath and chest tightness. The symptoms become more bothersome within 1-2 hours of starting work every day and worsen throughout the work week. His symptoms improve within 1-2 hours outside the workplace. Spirometry was performed revealing a forced expiratory volume in the first second (FEV1) of 63% of the predicted. His past medical history is significant for seasonal allergic rhinitis in the summer. He doesn't smoke or use illicit drugs. His family history is significant for asthma in his father and sister.  He currently uses inhaled corticosteroid (ICS) and fluticasone 500 mcg/salmeterol 50 mcg, one puff twice daily.

</details>

Category:

### C7. trec-202123 × NCT00971035

- **Trial:** A Study to Evaluate Lebrikizumab (MILR1444A) in Adult Patients With Asthma Who Are Not Taking Inhaled Corticosteroids
- **Gold:** ineligible; at k=30: greedy_smt → eligible, answerable_informative → ineligible
- **greedy_smt asked on this trial (0):** nothing
- **answerable_informative asked on this trial (1):**
  - turn 9: Boolean indicating whether the patient has ever undergone a chest radiograph (plain x-ray of chest) in the past. → false (useful_answered)
    criteria line: inclusion: “Chest radiograph within 12 months of Visit 1 without evidence of a clinically significant abnormality”

<details><summary>patient note</summary>

A 39-year-old man came to the clinic with cough and shortness of breath that was not relieved by  his inhaler. He had these symptoms for 5 days during the past 2 weeks. He doubled his oral corticosteroids in the past week. He is a chef with a  history of asthma for 3 years, suffering from frequent cough, wheezing, and shortness of breath and chest tightness. The symptoms become more bothersome within 1-2 hours of starting work every day and worsen throughout the work week. His symptoms improve within 1-2 hours outside the workplace. Spirometry was performed revealing a forced expiratory volume in the first second (FEV1) of 63% of the predicted. His past medical history is significant for seasonal allergic rhinitis in the summer. He doesn't smoke or use illicit drugs. His family history is significant for asthma in his father and sister.  He currently uses inhaled corticosteroid (ICS) and fluticasone 500 mcg/salmeterol 50 mcg, one puff twice daily.

</details>

Category:

### C8. trec-202123 × NCT01144910

- **Trial:** The Long-term Prognosis of Moderate to Severe Bronchial Hyperresponsiveness (BHR) in Asthmatic Preschool Children
- **Gold:** ineligible; at k=30: greedy_smt → eligible, answerable_informative → ineligible
- **greedy_smt asked on this trial (0):** nothing
- **answerable_informative asked on this trial (1):**
  - turn 2: Numeric value indicating the patient's current age in years. → 39.0 (useful_answered)
    criteria line: inclusion: “age 3 to 6 years”

<details><summary>patient note</summary>

A 39-year-old man came to the clinic with cough and shortness of breath that was not relieved by  his inhaler. He had these symptoms for 5 days during the past 2 weeks. He doubled his oral corticosteroids in the past week. He is a chef with a  history of asthma for 3 years, suffering from frequent cough, wheezing, and shortness of breath and chest tightness. The symptoms become more bothersome within 1-2 hours of starting work every day and worsen throughout the work week. His symptoms improve within 1-2 hours outside the workplace. Spirometry was performed revealing a forced expiratory volume in the first second (FEV1) of 63% of the predicted. His past medical history is significant for seasonal allergic rhinitis in the summer. He doesn't smoke or use illicit drugs. His family history is significant for asthma in his father and sister.  He currently uses inhaled corticosteroid (ICS) and fluticasone 500 mcg/salmeterol 50 mcg, one puff twice daily.

</details>

Category:

### C9. trec-202123 × NCT01772147

- **Trial:** Efficacy and Safety of the Addition of Fluticasone Propionate/Salmeterol (250/50mcg) Twice-daily to 2 Doses of Umeclidinium Bromide Inhalation Powder (62.5 or 125mcg) Once-daily Over 12 Weeks.
- **Gold:** ineligible; at k=30: greedy_smt → eligible, answerable_informative → ineligible
- **greedy_smt asked on this trial (0):** nothing
- **answerable_informative asked on this trial (1):**
  - turn 7: Boolean indicating whether the patient has a clinical history of chronic obstructive pulmonary disease (COPD). → false (useful_answered)
    criteria line: exclusion: “Other Respiratory Disorders: Known α-1 antitrypsin deficiency, active lung infections (such as tuberculosis), and lung cancer are absolute exclusionary conditions. A subject who, in the opinion of the investigator, has any other significant respiratory conditions in addition to COPD should be excluded. Examples may include clinically significant bronchiectasis, pulmonary hypertension, sarcoidosis, or interstitial lung disease.”

<details><summary>patient note</summary>

A 39-year-old man came to the clinic with cough and shortness of breath that was not relieved by  his inhaler. He had these symptoms for 5 days during the past 2 weeks. He doubled his oral corticosteroids in the past week. He is a chef with a  history of asthma for 3 years, suffering from frequent cough, wheezing, and shortness of breath and chest tightness. The symptoms become more bothersome within 1-2 hours of starting work every day and worsen throughout the work week. His symptoms improve within 1-2 hours outside the workplace. Spirometry was performed revealing a forced expiratory volume in the first second (FEV1) of 63% of the predicted. His past medical history is significant for seasonal allergic rhinitis in the summer. He doesn't smoke or use illicit drugs. His family history is significant for asthma in his father and sister.  He currently uses inhaled corticosteroid (ICS) and fluticasone 500 mcg/salmeterol 50 mcg, one puff twice daily.

</details>

Category:

### C10. trec-202123 × NCT02040766

- **Trial:** A Safety and Efficacy Study of Beclomethasone Dipropionate Delivered Via Breath-Actuated Inhaler (BAI) or Metered-Dose Inhaler (MDI) in Participants Ages 4-11 Years Old With Persistent Asthma
- **Gold:** ineligible; at k=30: greedy_smt → eligible, answerable_informative → ineligible
- **greedy_smt asked on this trial (0):** nothing
- **answerable_informative asked on this trial (3):**
  - turn 6: Boolean indicating whether the patient has a diagnosis of asthma at any point in their history. → true (useful_answered)
    criteria line: inclusion: “Asthma diagnosis: The patient has a diagnosis of asthma as defined by the National Institute of Health (NIH). The asthma diagnosis has been present for a minimum of 3 months and has been stable (defined as no exacerbations and no changes in medication) for at least 30 days before screening visit”
  - turn 8: Boolean indicating whether the patient's asthma diagnosis has been present for at least 3 months. → true (useful_answered)
    criteria line: inclusion: “Asthma diagnosis: The patient has a diagnosis of asthma as defined by the National Institute of Health (NIH). The asthma diagnosis has been present for a minimum of 3 months and has been stable (defined as no exacerbations and no changes in medication) for at least 30 days before screening visit”
  - turn 11: Boolean indicating whether the patient's asthma diagnosis stability is defined as no exacerbations and no changes in medication. → false (useful_answered)
    criteria line: inclusion: “Asthma diagnosis: The patient has a diagnosis of asthma as defined by the National Institute of Health (NIH). The asthma diagnosis has been present for a minimum of 3 months and has been stable (defined as no exacerbations and no changes in medication) for at least 30 days before screening visit”

<details><summary>patient note</summary>

A 39-year-old man came to the clinic with cough and shortness of breath that was not relieved by  his inhaler. He had these symptoms for 5 days during the past 2 weeks. He doubled his oral corticosteroids in the past week. He is a chef with a  history of asthma for 3 years, suffering from frequent cough, wheezing, and shortness of breath and chest tightness. The symptoms become more bothersome within 1-2 hours of starting work every day and worsen throughout the work week. His symptoms improve within 1-2 hours outside the workplace. Spirometry was performed revealing a forced expiratory volume in the first second (FEV1) of 63% of the predicted. His past medical history is significant for seasonal allergic rhinitis in the summer. He doesn't smoke or use illicit drugs. His family history is significant for asthma in his father and sister.  He currently uses inhaled corticosteroid (ICS) and fluticasone 500 mcg/salmeterol 50 mcg, one puff twice daily.

</details>

Category:

### C11. trec-202123 × NCT03952286

- **Trial:** ED-Initiated School-based Asthma Medication Supervision
- **Gold:** ineligible; at k=30: greedy_smt → eligible, answerable_informative → ineligible
- **greedy_smt asked on this trial (0):** nothing
- **answerable_informative asked on this trial (1):**
  - turn 3: Numeric value indicating the patient's current age in years. → 39.0 (useful_answered)
    criteria line: inclusion: “Children 6-12 years of age; AND”

<details><summary>patient note</summary>

A 39-year-old man came to the clinic with cough and shortness of breath that was not relieved by  his inhaler. He had these symptoms for 5 days during the past 2 weeks. He doubled his oral corticosteroids in the past week. He is a chef with a  history of asthma for 3 years, suffering from frequent cough, wheezing, and shortness of breath and chest tightness. The symptoms become more bothersome within 1-2 hours of starting work every day and worsen throughout the work week. His symptoms improve within 1-2 hours outside the workplace. Spirometry was performed revealing a forced expiratory volume in the first second (FEV1) of 63% of the predicted. His past medical history is significant for seasonal allergic rhinitis in the summer. He doesn't smoke or use illicit drugs. His family history is significant for asthma in his father and sister.  He currently uses inhaled corticosteroid (ICS) and fluticasone 500 mcg/salmeterol 50 mcg, one puff twice daily.

</details>

Category:

### C12. trec-202123 × NCT04326530

- **Trial:** Use of a Modern Breath Sampling System (the Pneumopipe® Combined With an Array of E-nose Sensors) for the Prediction of Treatment Response in Persistent Asthmatic Children
- **Gold:** ineligible; at k=30: greedy_smt → eligible, answerable_informative → ineligible
- **greedy_smt asked on this trial (0):** nothing
- **answerable_informative asked on this trial (1):**
  - turn 4: Numeric value indicating the patient's current age in years. → 39.0 (useful_answered)
    criteria line: inclusion: “age between 6 and 16 years”

<details><summary>patient note</summary>

A 39-year-old man came to the clinic with cough and shortness of breath that was not relieved by  his inhaler. He had these symptoms for 5 days during the past 2 weeks. He doubled his oral corticosteroids in the past week. He is a chef with a  history of asthma for 3 years, suffering from frequent cough, wheezing, and shortness of breath and chest tightness. The symptoms become more bothersome within 1-2 hours of starting work every day and worsen throughout the work week. His symptoms improve within 1-2 hours outside the workplace. Spirometry was performed revealing a forced expiratory volume in the first second (FEV1) of 63% of the predicted. His past medical history is significant for seasonal allergic rhinitis in the summer. He doesn't smoke or use illicit drugs. His family history is significant for asthma in his father and sister.  He currently uses inhaled corticosteroid (ICS) and fluticasone 500 mcg/salmeterol 50 mcg, one puff twice daily.

</details>

Category:

### C13. trec-202123 × NCT04448002

- **Trial:** AIM2ACT: A Mobile Health Tool to Help Adolescents Self-Manage Asthma
- **Gold:** ineligible; at k=30: greedy_smt → eligible, answerable_informative → ineligible
- **greedy_smt asked on this trial (0):** nothing
- **answerable_informative asked on this trial (1):**
  - turn 5: Numeric value indicating the patient's current age in years. → 39.0 (useful_answered)
    criteria line: (no matching line found)

<details><summary>patient note</summary>

A 39-year-old man came to the clinic with cough and shortness of breath that was not relieved by  his inhaler. He had these symptoms for 5 days during the past 2 weeks. He doubled his oral corticosteroids in the past week. He is a chef with a  history of asthma for 3 years, suffering from frequent cough, wheezing, and shortness of breath and chest tightness. The symptoms become more bothersome within 1-2 hours of starting work every day and worsen throughout the work week. His symptoms improve within 1-2 hours outside the workplace. Spirometry was performed revealing a forced expiratory volume in the first second (FEV1) of 63% of the predicted. His past medical history is significant for seasonal allergic rhinitis in the summer. He doesn't smoke or use illicit drugs. His family history is significant for asthma in his father and sister.  He currently uses inhaled corticosteroid (ICS) and fluticasone 500 mcg/salmeterol 50 mcg, one puff twice daily.

</details>

Category:

### C14. trec-202127 × NCT01687257

- **Trial:** Sofosbuvir and Ribavirin in Patients With Chronic HCV With Cirrhosis and Portal Hypertension With or Without Liver Decompensation
- **Gold:** ineligible; at k=30: greedy_smt → eligible, answerable_informative → ineligible
- **greedy_smt asked on this trial (0):** nothing
- **answerable_informative asked on this trial (1):**
  - turn 1: Boolean indicating whether the patient currently has cirrhosis of the liver. → false (useful_answered)
    criteria line: inclusion: “Individuals with cirrhosis with Child-Pugh score < 10”

<details><summary>patient note</summary>

A 53-year-old man presents with chronic HCV infection for the past 2 years. His past medical history is only significant for inguinal hernia surgery when he was 20 years old. He is on IFN (100 mg/week) plus RBV (400 mg/day) combination therapy for the past 9 months. Direct antiviral drugs were added to his treatment 6 months ago. His medical record shows previous positive HCV RNA tests as well as positive enzyme immunoassay for anti-HCV-antibodies. The recent biopsy was negative for hepatocellular carcinoma and was only remarkable for chronic inflammation compatible with a chronic viral hepatitis. There is no evidence of alcoholic liver disease, bleeding from esophageal varices, hemochromatosis, autoimmune hepatitis or metabolic liver disease. He is an alert male with no acute distress. His BP: 130/75, HR: 90/min and BMI: 27. His abdomen is soft with no ascites or tenderness. The lower extremities are normal with no edema.

</details>

Category:

### C15. trec-202127 × NCT02517528

- **Trial:** ABT-450/Ritonavir/ ABT-267 (ABT-450/r/ABT-267) and ABT-333 Co-Administered With Ribavirin (RBV) in Treatment Naïve and Treatment Experienced Asian Adults With Genotype 1b Chronic Hepatitis C Virus (HCV) Infection and Compensated Cirrhosis
- **Gold:** ineligible; at k=30: greedy_smt → eligible, answerable_informative → ineligible
- **greedy_smt asked on this trial (0):** nothing
- **answerable_informative asked on this trial (1):**
  - turn 2: Boolean indicating whether the patient currently has cirrhosis of the liver. → false (useful_answered)
    criteria line: inclusion: “Compensated cirrhosis defined as a Child-Pugh Score of less than or equal to 6 at Screening.”

<details><summary>patient note</summary>

A 53-year-old man presents with chronic HCV infection for the past 2 years. His past medical history is only significant for inguinal hernia surgery when he was 20 years old. He is on IFN (100 mg/week) plus RBV (400 mg/day) combination therapy for the past 9 months. Direct antiviral drugs were added to his treatment 6 months ago. His medical record shows previous positive HCV RNA tests as well as positive enzyme immunoassay for anti-HCV-antibodies. The recent biopsy was negative for hepatocellular carcinoma and was only remarkable for chronic inflammation compatible with a chronic viral hepatitis. There is no evidence of alcoholic liver disease, bleeding from esophageal varices, hemochromatosis, autoimmune hepatitis or metabolic liver disease. He is an alert male with no acute distress. His BP: 130/75, HR: 90/min and BMI: 27. His abdomen is soft with no ascites or tenderness. The lower extremities are normal with no edema.

</details>

Category:

### C16. trec-202127 × NCT02993250

- **Trial:** A Study to Investigate the Safety, Pharmacokinetics, and Efficacy of Combination Treatment of AL-335, Odalasvir, and Simeprevir in Japanese Participants With Chronic Hepatitis C Genotype 1 or 2 Virus Infection, With or Without Compensated Cirrhosis Who Are Direct Acting Antiviral Treatment-naive
- **Gold:** ineligible; at k=30: greedy_smt → eligible, answerable_informative → ineligible
- **greedy_smt asked on this trial (0):** nothing
- **answerable_informative asked on this trial (4):**
  - turn 14: Boolean indicating whether the patient currently has a positive hepatitis B surface antigen (i.e., hepatitis B infection). → unknown (useful_unanswered)
    criteria line: exclusion: “Co-infection with human immunodeficiency virus (HIV 1 or HIV 2 antibody positive) or hepatitis B virus (HBV) (hepatitis B surface antigen [HBsAg] positive)”
  - turn 18: Boolean indicating whether the patient currently has cirrhosis of the liver. → false (not_useful)
    criteria line: exclusion: “Any evidence of liver disease of non-HCV etiology. This includes, but is not limited to, acute hepatitis A infection (immunoglobulin M), drug or alcohol related liver disease, autoimmune hepatitis, hemochromatosis, Wilson's disease, alpha 1 antitrypsin deficiency, primary biliary cirrhosis, or any other non-HCV liver disease that is considered clinically significant by the investigator”
  - turn 19: Boolean indicating whether the patient has ever had a diagnosis of acute type A viral hepatitis (acute hepatitis A) in their medical history. → false (useful_answered)
    criteria line: exclusion: “Any evidence of liver disease of non-HCV etiology. This includes, but is not limited to, acute hepatitis A infection (immunoglobulin M), drug or alcohol related liver disease, autoimmune hepatitis, hemochromatosis, Wilson's disease, alpha 1 antitrypsin deficiency, primary biliary cirrhosis, or any other non-HCV liver disease that is considered clinically significant by the investigator”
  - turn 20: Boolean indicating whether the patient has ever been exposed to a direct-acting antiviral for hepatitis C virus at any time in the past. → true (useful_answered)
    criteria line: inclusion: “Direct-acting antiviral (DAA)-naive participants, defined as not having received treatment with any approved or investigational DAA drug for chronic HCV infection; prior HCV therapy consisting of interferon (IFN, pegylated or nonpegylated) with or without ribavirin (RBV) is allowed”

<details><summary>patient note</summary>

A 53-year-old man presents with chronic HCV infection for the past 2 years. His past medical history is only significant for inguinal hernia surgery when he was 20 years old. He is on IFN (100 mg/week) plus RBV (400 mg/day) combination therapy for the past 9 months. Direct antiviral drugs were added to his treatment 6 months ago. His medical record shows previous positive HCV RNA tests as well as positive enzyme immunoassay for anti-HCV-antibodies. The recent biopsy was negative for hepatocellular carcinoma and was only remarkable for chronic inflammation compatible with a chronic viral hepatitis. There is no evidence of alcoholic liver disease, bleeding from esophageal varices, hemochromatosis, autoimmune hepatitis or metabolic liver disease. He is an alert male with no acute distress. His BP: 130/75, HR: 90/min and BMI: 27. His abdomen is soft with no ascites or tenderness. The lower extremities are normal with no edema.

</details>

Category:

### C17. trec-202131 × NCT01051895

- **Trial:** Colposcopy Versus HPV Testing to Identify Persistent Cervical Precancers
- **Gold:** ineligible; at k=30: greedy_smt → eligible, answerable_informative → ineligible
- **greedy_smt asked on this trial (7):**
  - turn 13: Boolean indicating whether there is a strong probability that the patient will not come to appointments. → unknown (useful_unanswered)
    criteria line: exclusion: “There is a strong probability that the participant will not follow the procedures of study, will not come to its appointment, or plans a delocalization throughout study.”
  - turn 14: Boolean indicating whether there is a strong probability that the patient will not follow the procedures of the study. → unknown (useful_unanswered)
    criteria line: exclusion: “There is a strong probability that the participant will not follow the procedures of study, will not come to its appointment, or plans a delocalization throughout study.”
  - turn 15: Boolean indicating whether the patient has received immunosuppressive therapy in the three months prior to enrollment. → unknown (useful_unanswered)
    criteria line: exclusion: “Immunosuppressive therapy in the three months prior to enrollment”
  - turn 16: Boolean indicating whether the patient is receiving immunosuppressive therapy in the three months prior to enrollment. → unknown (useful_unanswered)
    criteria line: exclusion: “Immunosuppressive therapy in the three months prior to enrollment”
  - turn 17: Boolean indicating whether the patient plans a delocalization throughout the study. → unknown (useful_unanswered)
    criteria line: exclusion: “There is a strong probability that the participant will not follow the procedures of study, will not come to its appointment, or plans a delocalization throughout study.”
  - turn 18: Boolean value indicating whether the patient's current sex is female. → true (useful_answered)
    criteria line: (no matching line found)
  - turn 29: Numeric value indicating the patient's current age in years. → 37.0 (useful_answered)
    criteria line: (no matching line found)
- **answerable_informative asked on this trial (6):**
  - turn 5: Boolean value indicating whether the patient's current sex is female. → true (useful_answered)
    criteria line: (no matching line found)
  - turn 20: Boolean indicating whether the patient is scheduled to undergo a hysterectomy in the future. → true (not_useful)
    criteria line: inclusion: “Understands English or French (for sites where French speaking coordinator is available)”
  - turn 21: Boolean indicating whether the patient meets the age/location inclusion logic for inclusion. → unknown (useful_unanswered)
    criteria line: (no matching line found)
  - turn 22: Boolean indicating whether the corticosteroid therapy taken excludes inhalation, nasal, or topical forms. → unknown (useful_unanswered)
    criteria line: exclusion: “Two or more courses of corticosteroids (orally or parenterally) lasting at least one week in duration in the year prior to enrollment (inhalation, nasal or topical corticosteroids are permitted)”
  - turn 23: Boolean indicating whether the patient received two or more courses of corticosteroids, each at least one week, orally or parenterally, in the year prior to enrollment. → unknown (useful_unanswered)
    criteria line: exclusion: “Two or more courses of corticosteroids (orally or parenterally) lasting at least one week in duration in the year prior to enrollment (inhalation, nasal or topical corticosteroids are permitted)”
  - turn 24: Boolean indicating whether the scheduled future hysterectomy is planned. → true (useful_answered)
    criteria line: inclusion: “Understands English or French (for sites where French speaking coordinator is available)”

<details><summary>patient note</summary>

The patient is a 37-year-old woman who came to the clinic for a routine Pap smear. The test revealed stage 1B of cervical cancer. The patient tested positive for HPV 16. She has three sexual partners and   four children. She underwent tubal ligation. She smokes 30 packs/year and drinks alcohol frequently. She is otherwise healthy. She was offered a radical hysterectomy.

</details>

Category:

### C18. trec-202134 × NCT01314352

- **Trial:** Bioavailability Study of Desloratadine 5 mg Tablet of Dr. Reddy's Under Fed Conditions
- **Gold:** ineligible; at k=30: greedy_smt → eligible, answerable_informative → ineligible
- **greedy_smt asked on this trial (0):** nothing
- **answerable_informative asked on this trial (2):**
  - turn 4: Boolean indicating whether the patient has ever had a finding of hepatitis B infection (positive screen). → unknown (useful_unanswered)
    criteria line: exclusion: “Does s/he have a positive urine drug screen or a positive HIV-1, or hepatitis B or C screen, or a positive pregnancy test?”
  - turn 6: Numeric value indicating the patient's current age in years. → 47.0 (useful_answered)
    criteria line: inclusion: “Is s/he within 18 and 45 years of age, inclusive?”

<details><summary>patient note</summary>

The patient is a 47-year-old Asian woman complaining of persistent feelings of sadness. She lost interest in activities she used to enjoy. She states that her mood is mostly depressed for the past 3 weeks. She also lost her appetite , which led to about 5kg weight loss. She complains of loss of energy and feelings of worthlessness nearly every day. She is not using any drugs and she does not smoke. She doesn't drink alcohol. She used to exercise every day for at least 30 min. But she doesn't have enough energy to do so for the past 3 weeks. She also has some digestive issues recently. She is married and has 4 children. She is menopausal. Her husband was recently diagnosed with colon cancer and he is starting his chemotherapy. There is nothing remarkable in her past medical history and her drug history is only positive for Vit D3 1000 units daily. Her family history is negative for any psychologic problems. Her HAM-D score is 20.

</details>

Category:

### C19. trec-202134 × NCT01506050

- **Trial:** Bioequivalence Study for Desloratadine OD Tablets 5 mg Under Fasting Condition
- **Gold:** ineligible; at k=30: greedy_smt → eligible, answerable_informative → ineligible
- **greedy_smt asked on this trial (0):** nothing
- **answerable_informative asked on this trial (3):**
  - turn 3: Boolean indicating whether the patient currently has the clinical finding of hepatitis B infection. → unknown (useful_unanswered)
    criteria line: exclusion: “Does s/he have significant history or clinical evidence of auto-immune, cardiovascular, gastrointestinal, hematological, hematopoietic, hepatic, neurological, ongoing infection, pancreatic, or renal disease that would interfere with the conduct or interpretation of the study or jeopardize his/her safety?”
  - turn 5: Boolean indicating whether the patient currently has the clinical finding of hepatitis C infection. → unknown (useful_unanswered)
    criteria line: exclusion: “Does s/he have significant history or clinical evidence of auto-immune, cardiovascular, gastrointestinal, hematological, hematopoietic, hepatic, neurological, ongoing infection, pancreatic, or renal disease that would interfere with the conduct or interpretation of the study or jeopardize his/her safety?”
  - turn 7: Numeric value indicating the patient's current age in years. → 47.0 (useful_answered)
    criteria line: inclusion: “Is s/he within 18 to 45 years of age, inclusive?”

<details><summary>patient note</summary>

The patient is a 47-year-old Asian woman complaining of persistent feelings of sadness. She lost interest in activities she used to enjoy. She states that her mood is mostly depressed for the past 3 weeks. She also lost her appetite , which led to about 5kg weight loss. She complains of loss of energy and feelings of worthlessness nearly every day. She is not using any drugs and she does not smoke. She doesn't drink alcohol. She used to exercise every day for at least 30 min. But she doesn't have enough energy to do so for the past 3 weeks. She also has some digestive issues recently. She is married and has 4 children. She is menopausal. Her husband was recently diagnosed with colon cancer and he is starting his chemotherapy. There is nothing remarkable in her past medical history and her drug history is only positive for Vit D3 1000 units daily. Her family history is negative for any psychologic problems. Her HAM-D score is 20.

</details>

Category:

### C20. trec-202139 × NCT03599258

- **Trial:** Comparison of Phototherapy Using Neolight Skylife Versus Standardized Phototherapy for Hyperbilirubinemia in Newborns
- **Gold:** ineligible; at k=30: greedy_smt → eligible, answerable_informative → ineligible
- **greedy_smt asked on this trial (1):**
  - turn 30: patient_has_finding_of_hyperbilirubinemia_now → true (useful_answered)
    criteria line: inclusion: “Infants who developed significant hyperbilirubinemia Infants who developed significant hyperbilirubinemia per BiliToolTM plot requiring phototherapy as determined by the attending neonatologist utilizing the American Academy of Pediatrics'”
- **answerable_informative asked on this trial (1):**
  - turn 3: patient_is_undergoing_light_therapy_now → false (useful_answered)
    criteria line: (no matching line found)

<details><summary>patient note</summary>

A 3-day-old Asian female infant presents with jaundice that started a day ago. She was born at 38w3d of gestation, after an uncomplicated pregnancy. The family history is unremarkable. The baby is breastfed.
Vital signs are reported as: axillary temperature: 36.3°C, heart rate: 154 beats/min, respiratory rate: 37 breaths/min, and blood pressure: 65/33 mm Hg. Her weight is 3.2 kg, length is 53 cm, and head circumference 36 cm. Her sclera are yellow and her body is icteric. No murmurs or any other abnormalities are  detected in the heart and lung auscultation. Her liver and spleen are normal on palpation.
Laboratory results are as follows: 
Serum total bilirubin: 21.02 mg/dL
Direct bilirubin of 2.04 mg/dL
AST: 37 U/L
ALT: 20 U/L
GGT: 745 U/L
Alkaline phosphatase: 531 U/L
Creatinine: 0.3 mg/dL
Urea: 29 mg/dL
Na: 147 mEq/L
K: 4.5 mEq/L
CRP: 3 mg/L
Complete blood cell count within the normal range.
She is diagnosed with uncomplicated neonatal jaundice that may require phototherapy.

</details>

Category:

### C21. trec-20215 × NCT00464594

- **Trial:** Japan Early Diabetes Intervention Study
- **Gold:** ineligible; at k=30: greedy_smt → eligible, answerable_informative → ineligible
- **greedy_smt asked on this trial (0):** nothing
- **answerable_informative asked on this trial (7):**
  - turn 5: Boolean indicating whether the patient is currently undergoing administration of steroids. → unknown (useful_unanswered)
    criteria line: exclusion: “Undergoing treatment with steroids”
  - turn 9: Boolean indicating whether the patient currently has a diagnosis of secondary diabetes mellitus. → false (useful_answered)
    criteria line: exclusion: “Secondary diabetes mellitus”
  - turn 12: Boolean indicating whether the patient currently has a diagnosis of chronic renal failure. → unknown (useful_unanswered)
    criteria line: exclusion: “Liver cirrhosis or chronic hepatic, chronic renal failure”
  - turn 14: Boolean indicating whether the patient has ever undergone an oral glucose tolerance test (OGTT). → unknown (useful_unanswered)
    criteria line: inclusion: “Results of 75-g oral glucose tolerance test (75 g OGTT)will be used to confirm FPG <= 125 mg/dL, 2-h PG >= 200 mg/dL and HbA1c <= 6.9%”
  - turn 18: Boolean indicating whether the patient currently has a diagnosis of chronic hepatic failure. → false (useful_answered)
    criteria line: exclusion: “Liver cirrhosis or chronic hepatic, chronic renal failure”
  - turn 20: Boolean indicating whether the patient currently has a diagnosis of type 1 diabetes mellitus. → false (useful_answered)
    criteria line: exclusion: “Type 1 diabetes mellitus”
  - turn 22: Boolean indicating whether the patient currently has anemia. → true (useful_answered)
    criteria line: (no matching line found)

<details><summary>patient note</summary>

74M hx of CAD s/p CABG, EF 60% prior CVA (no residual deficits), HTN, HL, DMII, Moderate to Severe PVD was referred to cardiology for evaluation of PVD, and on examination patient was found to have carotid bruits. Upon further review of symptoms the pt reports + Occasional dizziness, no prior syncope occasional HA, Denies CP/SOB. No sensory or motor defects. He recalls that he might have had a stroke 10-15 years ago without any residual deficit. Prior to CABG he only had diaphoresis.
Further review of systems is notable for absence of chest pain, dyspnea on exertion, paroxysmal nocturnal dyspnea, orthopnea, palpitations, syncope or presyncope. He underwent Carotid U/S that showed significant bilateral carotid stenosis, L>R. Angiography revealed an 80% stenosis of the R ICA and a 90% L ICA stenosis. Cerebral angiography further revealed patent right ACA and MCA and patent left ACA and left MCA.
Past Medical History:
CAD s/p CABG in [**2154**] ([**Hospital1 112**])
Prior CVA
Bilateral carotid artery disease
Anemia
PVD
Hypertension
Diabetes c/b retinopathy and peripheral neuropathy
Cataracts s/p surgery
Thyroid nodule
Colon polyps s/p resection
Intermittent Lower back pain
Proteinuria
s/p right elbow fracture as a child
Arthritis

</details>

Category:

### C22. trec-20215 × NCT01274676

- **Trial:** Carotid Stenting in Patients With High Risk Carotid Stenosis (Soft Plaque)
- **Gold:** ineligible; at k=30: greedy_smt → eligible, answerable_informative → ineligible
- **greedy_smt asked on this trial (0):** nothing
- **answerable_informative asked on this trial (3):**
  - turn 10: Boolean indicating whether the patient currently has carotid stenosis. → true (useful_answered)
    criteria line: inclusion: “-patients with monolateral, significant, soft carotid stenosis”
  - turn 15: Boolean indicating whether the patient's current carotid stenosis is significant (meets the clinical threshold for significance). → true (useful_answered)
    criteria line: inclusion: “-patients with monolateral, significant, soft carotid stenosis”
  - turn 25: Boolean indicating whether the patient's current carotid stenosis is monolateral (affecting only one side). → false (useful_answered)
    criteria line: inclusion: “-patients with monolateral, significant, soft carotid stenosis”

<details><summary>patient note</summary>

74M hx of CAD s/p CABG, EF 60% prior CVA (no residual deficits), HTN, HL, DMII, Moderate to Severe PVD was referred to cardiology for evaluation of PVD, and on examination patient was found to have carotid bruits. Upon further review of symptoms the pt reports + Occasional dizziness, no prior syncope occasional HA, Denies CP/SOB. No sensory or motor defects. He recalls that he might have had a stroke 10-15 years ago without any residual deficit. Prior to CABG he only had diaphoresis.
Further review of systems is notable for absence of chest pain, dyspnea on exertion, paroxysmal nocturnal dyspnea, orthopnea, palpitations, syncope or presyncope. He underwent Carotid U/S that showed significant bilateral carotid stenosis, L>R. Angiography revealed an 80% stenosis of the R ICA and a 90% L ICA stenosis. Cerebral angiography further revealed patent right ACA and MCA and patent left ACA and left MCA.
Past Medical History:
CAD s/p CABG in [**2154**] ([**Hospital1 112**])
Prior CVA
Bilateral carotid artery disease
Anemia
PVD
Hypertension
Diabetes c/b retinopathy and peripheral neuropathy
Cataracts s/p surgery
Thyroid nodule
Colon polyps s/p resection
Intermittent Lower back pain
Proteinuria
s/p right elbow fracture as a child
Arthritis

</details>

Category:

### C23. trec-202152 × NCT00807326

- **Trial:** A Comparison of Three Medications to Treat Diarrhea in Adults.
- **Gold:** eligible; at k=30: greedy_smt → ineligible, answerable_informative → eligible
- **greedy_smt asked on this trial (1):**
  - turn 10: Boolean indicating whether the patient currently has clinical signs of orthostatic hypotension. → true (useful_answered)
    criteria line: exclusion: “Signs or symptoms of orthostatic hypotension”
- **answerable_informative asked on this trial (19):**
  - turn 1: patient_has_finding_of_acute_diarrhea_now@@symptom_onset_within_48_hours_before_study_entry → true (useful_answered)
    criteria line: inclusion: “Acute diarrhea illness with symptoms onset within 48 hours of study entry”
  - turn 4: Boolean indicating whether the 24-hour window for counting loose (unformed) stools is the 24 hours immediately before study entry. → unknown (useful_unanswered)
    criteria line: inclusion: “Minimum of 3 unformed stools in 24 hours before study entry”
  - turn 6: patient_has_finding_of_acute_diarrhea_now → true (useful_answered)
    criteria line: inclusion: “Acute diarrhea illness with symptoms onset within 48 hours of study entry”
  - turn 9: Boolean indicating whether the patient has ever used opiates at any time in the past, regardless of context (including as recreational drugs or as painkillers). → unknown (useful_unanswered)
    criteria line: exclusion: “Use of opiates (as 'recreational' drugs and as painkillers)”
  - turn 10: Boolean indicating whether the patient currently requires antibiotic therapy. → unknown (useful_unanswered)
    criteria line: exclusion: “Requiring hospital admission, parenteral hydration or antibiotic therapy Axillary temperature >38.2°C or oral temperature >38.6°C”
  - turn 11: Boolean indicating whether the patient is currently undergoing chemotherapy. → unknown (useful_unanswered)
    criteria line: exclusion: “Immunodeficiency (e.g. those with acquired immunodeficiency syndrome [AIDS] or known human immunodeficiency virus [HIV] infection, or undergoing chemotherapy or radiotherapy)”
  - turn 13: Boolean indicating whether the patient currently has symptoms of orthostatic hypotension. → unknown (useful_unanswered)
    criteria line: exclusion: “Signs or symptoms of orthostatic hypotension”
  - turn 14: Boolean indicating whether the patient is currently producing or exposed to feces (stool) now. → unknown (useful_unanswered)
    criteria line: (no matching line found)
  - turn 15: Boolean indicating whether the patient currently requires hospital admission. → unknown (useful_unanswered)
    criteria line: exclusion: “Requiring hospital admission, parenteral hydration or antibiotic therapy Axillary temperature >38.2°C or oral temperature >38.6°C”
  - turn 16: Boolean indicating whether the patient is currently undergoing radiotherapy. → unknown (useful_unanswered)
    criteria line: exclusion: “Immunodeficiency (e.g. those with acquired immunodeficiency syndrome [AIDS] or known human immunodeficiency virus [HIV] infection, or undergoing chemotherapy or radiotherapy)”
  - turn 17: Numeric variable representing the number of loose (unformed) stools the patient had in the past 24 hours. → unknown (useful_unanswered)
    criteria line: inclusion: “Minimum of 3 unformed stools in 24 hours before study entry”
  - turn 21: Boolean indicating whether the patient currently requires parenteral rehydration therapy. → unknown (useful_unanswered)
    criteria line: exclusion: “Requiring hospital admission, parenteral hydration or antibiotic therapy Axillary temperature >38.2°C or oral temperature >38.6°C”
  - turn 22: Boolean indicating whether the patient has ever been diagnosed with renal insufficiency. → unknown (useful_unanswered)
    criteria line: exclusion: “History of chronic gastrointestinal disease, hepatic or renal insufficiency, or other significant medical condition that could be aggravated by untreated acute diarrhea”
  - turn 23: Boolean indicating whether the patient has ever had a diagnosis of acquired immunodeficiency syndrome (AIDS) in their medical history. → unknown (useful_unanswered)
    criteria line: exclusion: “Immunodeficiency (e.g. those with acquired immunodeficiency syndrome [AIDS] or known human immunodeficiency virus [HIV] infection, or undergoing chemotherapy or radiotherapy)”
  - turn 24: Boolean indicating whether the patient is currently breast-feeding. → unknown (useful_unanswered)
    criteria line: exclusion: “Pregnant or breast-feeding”
  - turn 25: Boolean indicating whether the patient has been exposed to any antibiotics in the 7 days prior to now. → unknown (useful_unanswered)
    criteria line: exclusion: “Requiring hospital admission, parenteral hydration or antibiotic therapy Axillary temperature >38.2°C or oral temperature >38.6°C”
  - turn 26: Boolean indicating whether the variable refers to the most recent stool (feces) produced by the patient. → unknown (useful_unanswered)
    criteria line: inclusion: “Most recent stool is unformed”
  - turn 29: Boolean indicating whether the patient currently has any condition that, in the opinion of the investigator, would compromise the well-being of the subject or would compromise the study. → unknown (useful_unanswered)
    criteria line: exclusion: “Any condition that, in the opinion of the investigator, would compromise the well-being of the subject or the study”
  - turn 30: Boolean indicating whether the stool (feces) is unformed. → unknown (useful_unanswered)
    criteria line: inclusion: “Minimum of 3 unformed stools in 24 hours before study entry”

<details><summary>patient note</summary>

A 34 year old man comes to the clinic complaining of dizziness and severe diarrhea since yesterday. He has returned from an international trip few days ago and was living in a camp in Sudan for a month. He developed abdominal pain followed by bloating and nausea as well as loose bowel movements. Soon he was having profuse watery diarrhea without odor. The stool is watery and white but the patient has no fever. Blood pressure is 95/62 lying down and drops to 75/40 standing. The skin turgor has reduced. HR is 110 and he looks ill with dry mucosa. V. cholerae was seen in dark-field microscopy of a fresh stool specimen. The lab study is as bellow:
Sodium                           137 meq/L
Potassium                      2 meq/L
Chloride                         94meq/L
CO2                                 15 meq/L
Fecal leukocytes           None seen
Fecal occult blood        Negative

</details>

Category:

### C24. trec-202158 × NCT02029781

- **Trial:** The Laparoscopic Appendicitis Score; a Multicenter Validation Study
- **Gold:** ineligible; at k=30: greedy_smt → eligible, answerable_informative → ineligible
- **greedy_smt asked on this trial (6):**
  - turn 5: patient_has_refused_written_informed_consent_now → unknown (useful_unanswered)
    criteria line: inclusion: “Written informed consent”
  - turn 6: patient_has_suspicion_of_acute_appendicitis_now → true (useful_answered)
    criteria line: inclusion: “Patients operated for the clinical suspicion of acute appendicitis that will undergo a diagnostic laparoscopy.”
  - turn 7: patient_is_able_to_give_written_informed_consent_now → unknown (useful_unanswered)
    criteria line: exclusion: “Not able to give informed consent (for example language barrier or legally incapable).”
  - turn 8: patient_is_able_to_give_written_informed_consent_now@@inability_due_to_language_barrier → unknown (useful_unanswered)
    criteria line: exclusion: “Not able to give informed consent (for example language barrier or legally incapable).”
  - turn 9: patient_is_able_to_give_written_informed_consent_now@@inability_due_to_legal_incapacity → unknown (useful_unanswered)
    criteria line: exclusion: “Not able to give informed consent (for example language barrier or legally incapable).”
  - turn 10: patient_is_primarily_chosen_for_open_appendectomy_now → false (useful_answered)
    criteria line: exclusion: “Primarily chosen for an open appendectomy.”
- **answerable_informative asked on this trial (4):**
  - turn 5: patient_has_suspicion_of_acute_appendicitis_now → true (useful_answered)
    criteria line: inclusion: “Patients operated for the clinical suspicion of acute appendicitis that will undergo a diagnostic laparoscopy.”
  - turn 12: patient_is_primarily_chosen_for_open_appendectomy_now → false (useful_answered)
    criteria line: exclusion: “Primarily chosen for an open appendectomy.”
  - turn 22: patient_has_refused_written_informed_consent_now → unknown (useful_unanswered)
    criteria line: inclusion: “Written informed consent”
  - turn 23: patient_age_value_recorded_now_in_years → 17.0 (useful_answered)
    criteria line: inclusion: “Age ≥ 18 years.”

<details><summary>patient note</summary>

The patient is a 17-year-old boy complaining of severe migratory pain in the right lower quadrant of his abdomen that started four days ago. The pain is accompanied by nausea and vomiting. He was febrile with tenderness, rebound tenderness and guarding on palpation. His WBC was elevated with dominant neutrophils. CT scan showed evidence of acute perforated appendicitis with free fluid in the pelvis. Diagnostic laparoscopy revealed phlegmon with no other abdominal abnormalities. He is now a candidate for emergent laparoscopic appendectomy under general anesthesia.

</details>

Category:

### C25. trec-202158 × NCT02789865

- **Trial:** Clinical Trial Comparing ERAT vs Antibiotic Therapy vs Appendectomy for Treatment of Uncomplicated Acute Appendicitis
- **Gold:** ineligible; at k=30: greedy_smt → eligible, answerable_informative → ineligible
- **greedy_smt asked on this trial (5):**
  - turn 16: Boolean indicating whether the patient currently has any contraindication for colonoscopy. → unknown (useful_unanswered)
    criteria line: exclusion: “contraindications for colonoscopy”
  - turn 17: Boolean indicating whether the patient currently has a periappendiceal abscess (abscess of appendix). → false (useful_answered)
    criteria line: inclusion: “patients with Alvarado scores ≥7 (with or without US/CT) diagnosed of uncomplicated acute appendicitis”
  - turn 18: Boolean value indicating whether the patient is currently pregnant. → false (useful_answered)
    criteria line: (no matching line found)
  - turn 19: Boolean indicating whether the patient is unable to cooperate. → unknown (useful_unanswered)
    criteria line: exclusion: “unable to cooperate or provide informed consent”
  - turn 20: Boolean indicating whether the patient is unable to provide informed consent. → unknown (useful_unanswered)
    criteria line: exclusion: “unable to cooperate or provide informed consent”
- **answerable_informative asked on this trial (3):**
  - turn 11: Boolean indicating whether the patient currently has a periappendiceal abscess (abscess of appendix). → false (useful_answered)
    criteria line: inclusion: “patients with Alvarado scores ≥7 (with or without US/CT) diagnosed of uncomplicated acute appendicitis”
  - turn 16: Boolean indicating whether the patient is currently diagnosed with uncomplicated acute appendicitis (acute appendicitis without peritonitis). → false (not_useful)
    criteria line: inclusion: “patients with Alvarado scores ≥7 (with or without US/CT) diagnosed of uncomplicated acute appendicitis”
  - turn 17: Boolean indicating whether the patient's current appendicitis diagnosis is perforated. → true (useful_answered)
    criteria line: inclusion: “patients with Alvarado scores ≥7 (with or without US/CT) diagnosed of uncomplicated acute appendicitis”

<details><summary>patient note</summary>

The patient is a 17-year-old boy complaining of severe migratory pain in the right lower quadrant of his abdomen that started four days ago. The pain is accompanied by nausea and vomiting. He was febrile with tenderness, rebound tenderness and guarding on palpation. His WBC was elevated with dominant neutrophils. CT scan showed evidence of acute perforated appendicitis with free fluid in the pelvis. Diagnostic laparoscopy revealed phlegmon with no other abdominal abnormalities. He is now a candidate for emergent laparoscopic appendectomy under general anesthesia.

</details>

Category:

### C26. trec-202158 × NCT03380793

- **Trial:** A Trial to Assess the Efficacy and Safety of Morinidazole in Patients With Appendicitis
- **Gold:** ineligible; at k=30: greedy_smt → eligible, answerable_informative → ineligible
- **greedy_smt asked on this trial (10):**
  - turn 21: Boolean indicating whether the patient cannot evaluate the efficacy of treatment. → unknown (useful_unanswered)
    criteria line: exclusion: “patients who can not evaluate the efficacy or difficult to complete the desired course of treatment”
  - turn 22: Boolean indicating whether the patient currently has any condition (other than suppurative or gangrenous appendicitis) likely to require broad spectrum antibiotic therapy. → unknown (useful_unanswered)
    criteria line: exclusion: “patients with any condition likely to require broad spectrum antibiotics”
  - turn 23: Boolean indicating whether the patient currently has an allergy to nitroimidazole. → unknown (useful_unanswered)
    criteria line: exclusion: “patients with an allergy to nitroimidazole”
  - turn 24: Boolean indicating whether the patient currently has a cardiovascular abnormality. → unknown (useful_unanswered)
    criteria line: exclusion: “patients with severe systemic diseases likely to affect therapy (e.g., cardiovascular abnormalities, unstable angina, high blood pressure, severe neuropathy, or epilepsy)”
  - turn 25: Boolean indicating whether the patient currently has epilepsy. → unknown (useful_unanswered)
    criteria line: exclusion: “patients with severe systemic diseases likely to affect therapy (e.g., cardiovascular abnormalities, unstable angina, high blood pressure, severe neuropathy, or epilepsy)”
  - turn 26: Boolean indicating whether the patient currently has high blood pressure. → unknown (useful_unanswered)
    criteria line: exclusion: “patients with severe systemic diseases likely to affect therapy (e.g., cardiovascular abnormalities, unstable angina, high blood pressure, severe neuropathy, or epilepsy)”
  - turn 27: Boolean indicating whether the patient currently has severe neuropathy. → unknown (useful_unanswered)
    criteria line: exclusion: “patients with severe systemic diseases likely to affect therapy (e.g., cardiovascular abnormalities, unstable angina, high blood pressure, severe neuropathy, or epilepsy)”
  - turn 28: Boolean indicating whether the patient currently has another systemic disease that may interfere with the efficacy of the study drug. → unknown (useful_unanswered)
    criteria line: exclusion: “patients with other diseases or use other drugs which may interfere with the efficacy or safety of the drug”
  - turn 29: Boolean indicating whether the patient currently has another systemic disease that may interfere with the safety of the study drug. → unknown (useful_unanswered)
    criteria line: exclusion: “patients with other diseases or use other drugs which may interfere with the efficacy or safety of the drug”
  - turn 30: Boolean indicating whether the patient currently has unstable angina. → unknown (useful_unanswered)
    criteria line: exclusion: “patients with severe systemic diseases likely to affect therapy (e.g., cardiovascular abnormalities, unstable angina, high blood pressure, severe neuropathy, or epilepsy)”
- **answerable_informative asked on this trial (1):**
  - turn 9: Numeric value indicating the patient's current age in years. → 17.0 (useful_answered)
    criteria line: exclusion: “Pregnant women, breastfeeding women, women of childbearing age without effective contraceptive”

<details><summary>patient note</summary>

The patient is a 17-year-old boy complaining of severe migratory pain in the right lower quadrant of his abdomen that started four days ago. The pain is accompanied by nausea and vomiting. He was febrile with tenderness, rebound tenderness and guarding on palpation. His WBC was elevated with dominant neutrophils. CT scan showed evidence of acute perforated appendicitis with free fluid in the pelvis. Diagnostic laparoscopy revealed phlegmon with no other abdominal abnormalities. He is now a candidate for emergent laparoscopic appendectomy under general anesthesia.

</details>

Category:

### C27. trec-202158 × NCT03750032

- **Trial:** Technical Modifications of Appendicular Stump Closure During Laparoscopic Appendectomy
- **Gold:** ineligible; at k=30: greedy_smt → eligible, answerable_informative → ineligible
- **greedy_smt asked on this trial (0):** nothing
- **answerable_informative asked on this trial (4):**
  - turn 2: Boolean indicating whether the patient has undergone laparoscopy at any time up to and including now. → true (useful_answered)
    criteria line: (no matching line found)
  - turn 8: Boolean indicating whether the patient currently has acute appendicitis. → true (useful_answered)
    criteria line: exclusion: “- necrosis or advanced inflammatory changes in the area of appendicular stump”
  - turn 18: Boolean indicating whether the patient's tissue necrosis is located in the area of the appendicular stump. → unknown (useful_unanswered)
    criteria line: exclusion: “- necrosis or advanced inflammatory changes in the area of appendicular stump”
  - turn 24: Numeric value indicating the patient's current age in years. → 17.0 (useful_answered)
    criteria line: inclusion: “age ≥18 years”

<details><summary>patient note</summary>

The patient is a 17-year-old boy complaining of severe migratory pain in the right lower quadrant of his abdomen that started four days ago. The pain is accompanied by nausea and vomiting. He was febrile with tenderness, rebound tenderness and guarding on palpation. His WBC was elevated with dominant neutrophils. CT scan showed evidence of acute perforated appendicitis with free fluid in the pelvis. Diagnostic laparoscopy revealed phlegmon with no other abdominal abnormalities. He is now a candidate for emergent laparoscopic appendectomy under general anesthesia.

</details>

Category:
