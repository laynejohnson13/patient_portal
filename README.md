# patient_portal

Used GCP

MySQL IP: 35.239.60.174


Issues I ran into:

- when trying to insert fake treatments/procedures I recieved an error stating: 1062, "Duplicate entry '76981' for key 'treatment_procedures.cpt_code'" after I had dropped duplicates.

  These lines were ran to try and overcome error, but with no luck:
- cpt_codes_sample_use = cpt_codes_sample_new_2.drop_duplicates(subset=['Code'], keep='first')
- cpt_codes_sample_use_2 = cpt_codes_sample_new_2.drop_duplicates(subset=['Description'], keep='first')

a new & smaller dataframe was created without duplicates, but error still shows duplicate entries
