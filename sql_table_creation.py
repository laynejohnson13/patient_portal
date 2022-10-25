import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
import dbm

load_dotenv()

GCP_MYSQL_HOSTNAME = os.getenv('GCP_MYSQL_HOSTNAME')
GCP_MYSQL_USER = os.getenv('GCP_MYSQL_USER')
GCP_MYSQL_PASSWORD = os.getenv('GCP_MYSQL_PASSWORD')
GCP_MYSQL_DATABASE = os.getenv('GCP_MYSQL_DATABASE')

connection_string = f'mysql+pymysql://{GCP_MYSQL_USER}:{GCP_MYSQL_PASSWORD}@{GCP_MYSQL_HOSTNAME}:3306/{GCP_MYSQL_DATABASE}'
gc_engine = create_engine(connection_string)

##show databases
tablenames_gcp= gc_engine.table_names()


##creating tables

production_patients = """
create table if not exists production_patients (
    id int auto_increment,
    mrn varchar(255) default null unique,
    first_name varchar(255) default null,
    last_name varchar(255) default null,
    zip_code varchar(255) default null,
    dob varchar(255) default null,
    gender varchar(255) default null,
    contact_mobile varchar(255) default null,
    contact_home varchar(255) default null,
    PRIMARY KEY (id) 
); 
"""

medications = """
create table if not exists medications (
    id int auto_increment,
    med_ndc varchar(255) default null unique,
    med_human_name varchar(255) default null,
    med_is_dangerous varchar(255) default null,
    PRIMARY KEY (id)
); 
"""

conditions = """
create table if not exists conditions (
    id int auto_increment,
    icd10_code varchar(255) default null unique,
    icd10_description varchar(255) default null,
    PRIMARY KEY (id) 
); 
"""

treatment_procedures = """
create table if not exists treatment_procedures (
    id int auto_increment,
    cpt_code varchar(255) default null unique,
    cpt_description varchar(255) default null,
    PRIMARY KEY (id) 
); 
"""



patients_medications = """
create table if not exists patient_medications (
    id int auto_increment,
    mrn varchar(255) default null,
    med_ndc varchar(255) default null,
    PRIMARY KEY (id),
    FOREIGN KEY (mrn) REFERENCES production_patients(mrn) ON DELETE CASCADE,
    FOREIGN KEY (med_ndc) REFERENCES production_medications(med_ndc) ON DELETE CASCADE
); 
"""


patient_conditions = """
create table if not exists patient_conditions (
    id int auto_increment,
    mrn varchar(255) default null,
    icd10_code varchar(255) default null,
    PRIMARY KEY (id),
    FOREIGN KEY (mrn) REFERENCES production_patients(mrn) ON DELETE CASCADE,
    FOREIGN KEY (icd10_code) REFERENCES conditions(icd10_code) ON DELETE CASCADE
); 
"""
patient_treatment_procedures = """
create table if not exists patient_treatment_procedures (
    id int auto_increment,
    mrn varchar(255) default null,
    cpt_code varchar(255) default null,
    PRIMARY KEY (id),
    FOREIGN KEY (mrn) REFERENCES production_patients(mrn) ON DELETE CASCADE,
    FOREIGN KEY (cpt_code) REFERENCES treatments_procedures(cpt_code) ON DELETE CASCADE
); 
"""

gc_engine.execute(production_patients)
gc_engine.execute(medications)
gc_engine.execute(patients_medications)
gc_engine.execute(conditions)
gc_engine.execute(patient_conditions)
gc_engine.execute(treatment_procedures)
