# -*_ coding: utf-8 -*-
"""
Created on Apr 14 10:21:00 2019
@author: Youngmi Huang
@email: cyeninesky3@gmail.com

"""

def _categ_addr(i):
    if i in ['NV','SD','OK','AL','LA','AK']:
        ind = 'addr_high'
    elif i in ['ND', 'NH', 'VT', 'ME']:
        ind = 'addr_low'
    else:
        ind = 'addr_mid'
    return ind

def _categ_date_quarter(i):
    if i in [1,2,3]:
        ind = 'Q1'
    elif i in [4,5,6]:
        ind = 'Q2'
    elif i in [7,8,9]:
        ind = 'Q3' 
    else:
        ind = 'Q4'
    return ind

def _categ_purpose(i):
    if i in ['small_business', 'renewable_energy', 'house']:
        ind = 'purpose_high'
    elif i in ['moving', 'medical', 'vacation', 'other', 'debt_consolidation', 'major_purchase']:
        ind = 'purpose_mid'
    else:
        ind = 'purpose_low'
    return ind

def _categ_emp_title(i):
    if i in ['assembler', 'Customer Service Representative', 'warehouse', 'cna',
       'Owner ', 'service tech', 'Admin Assistant', 'operator', 'DRIVER',
       'foreman', 'Delivery Driver', 'custodian', 'correctional officer',
       'Machine Operator', 'general manager', 'bus driver',
       'Truck driver', 'LVN', 'driver', 'welder', 'Machinist', 'cashier',
       'Installer', 'technician', 'Sales Consultant', 'Material Handler',
       'machine operator', 'Salesman', 'Dental Assistant', 'bartender',
       'Conductor', 'Pharmacy Technician', 'Assembler', 'server',
       'Security Officer', 'account manager', 'supervisor',
       'truck driver', 'medical assistant', 'HR Director', 'accountant',
       'laborer', 'Technician ', 'machinist', 'Program Analyst',
       'Insurance Agent', 'OWNER', 'Project Coordinator',
       'Logistics Manager', 'Cashier', 'Security', 'Sales Associate',
       'IT Consultant', 'Captain', 'Customer service', 'Stylist']:
        
        ind = 'emp_title_high'
        
    elif i in ['police officer', 'Customer Service Manager', 'store manager',
       'Manufacturing Engineer', 'SALES', 'Customer Service Rep',
       'sales manager', 'Customer Service', 'Purchasing Manager',
       'Warehouse', 'sales', 'Production Supervisor', 'cook', 'Laborer',
       'Foreman', 'office manager', 'chef', 'Accounts Payable', 'IT',
       'Supervisor ', 'Banker', 'Dental Hygienist', 'Tech', 'Secretary',
       'sales associate', 'Warehouse Manager', 'Driver',
       'Correction Officer', 'Manager ', 'Bus Driver', 'Store Manager',
       'Welder', 'production', 'manager', 'operations manager', 'Plumber',
       'engineer', 'CSR', 'mechanic', 'Truck Driver', 'customer service',
       'GM', 'Maintenance ', 'Server', 'Admin', 'tech', 'paralegal',
       'CNA', 'Budget Analyst', 'Inspector', 'Service Technician',
       'Driver ', 'Cook', 'director', 'Courier', 'MANAGER', 'Educator',
       'Mechanic', 'Operations manager', 'Inside Sales', 'clerk', 'Nurse',
       'Sales', 'Legal Assistant', 'maintenance', 'Paramedic',
       'Assistant Manager', 'CEO', 'Accounting', 'Realtor', 'Electrician',
       'Department Manager', 'Executive Chef', 'Practice Manager',
       'Owner', 'Social Worker', 'Service Manager', 'president',
       'Team Leader', 'Technician', 'Assistant manager', 'Teller',
       'Plant Manager', 'Trainer', 'Personal Banker', 'Store manager',
       'nurse', 'Property Manager', 'Medical Assistant',
       'Business Development Manager', 'Dispatcher',
       'Administrative Assistant', 'Operator', 'Bartender', 'Management',
       'LPN', 'Legal Secretary', 'Supervisor', 'other', 'electrician',
       'Account Manager', 'IT Specialist', 'Sales ', 'General manager',
       'analyst', 'REGISTERED NURSE', 'Correctional Officer',
       'Business Development', 'Letter Carrier', 'Chef', 'Marketing',
       'rn', 'Paralegal', 'Police officer', 'Recruiter', 'owner',
       'Registered nurse', 'Manager', 'Sales Rep', 'Service Tech',
       'Human Resources', 'Receptionist', 'Nurse Manager', 'Case Manager',
       'General Manager', 'Bus Operator', 'Registered Nurse ',
       'Project manager', 'teacher', 'Web Developer', 'COO', 'Programmer',
       'Deputy', 'Specialist', 'Therapist', 'Consultant',
       'District Manager', 'carpenter', 'Radiologic Technologist',
       'Area Manager', 'RN', 'Superintendent ', 'letter carrier',
       'Network Engineer', 'IT Analyst', 'Carpenter', 'project manager',
       'School Psychologist', 'Program Specialist',
       'Relationship Manager', 'Sales Executive', 'Parts Manager',
       'Coordinator', 'President', 'Auditor', 'Program Coordinator',
       'Caregiver', 'Sales Manager', 'Administration', 'Office Manager',
       'Instructor', 'registered nurse', 'Sales manager', 'Clerk',
       'Custodian', 'Chemist', 'Managing Partner', 'Deputy Sheriff',
       'Accountant', 'Registered Nurse', 'Senior Associate',
       'Credit Analyst', 'IT Project Manager', 'Account Executive',
       'Project Manager', 'Production', 'Assistant Director',
       'System Engineer', 'Marketing Director', 'Analyst',
       'Contract Specialist', 'Rn', 'Executive Assistant', 'Firefighter',
       'Flight Attendant', 'Officer', 'Senior Financial Analyst',
       'Assistant Store Manager', 'Operations Manager', 'Buyer',
       'Financial Analyst', 'Sergeant', 'Office manager', 'Teacher ',
       'Quality Manager', 'Engineer', 'Administrator', 'Office Assistant',
       'Agent', 'Finance Manager', 'Underwriter',
       'Special Education Teacher', 'Bookkeeper', 'Director', 'Designer',
       'Controller', 'Maintenance', 'Assistant Vice President',
       'Medical Technologist', 'Investigator', 'Regional Manager']:
        ind = 'emp_title_mid'
    else:
        ind = 'emp_title_low'
    return ind

def _categ_emp_length(i):
    if i in ['< 1 year', '1 year', '2 years', '3 years']:
        ind = 'emp_length_class1'
    elif i in ['4 years', '5 years', '6 years', '7 years']:
        ind = 'emp_length_class2'
    else:
        ind = 'emp_length_class3'
    return ind

def _categ_revol(i):
    if i <30:
        ind = 'revol_less_than_30'
    elif 30 <= i < 80:
        ind = 'revol_betwwwn_30_80'
    else:
        ind = 'revol_over_80'
    return ind

def preprocess(df):
    drop_feats= ['id', 'member_id', 'funded_amnt', 'funded_amnt_inv', 'int_rate', 'installment','grade', 'sub_grade', 
                 'initial_list_status', 'out_prncp', 'out_prncp_inv','total_pymnt', 'total_pymnt_inv', 
                 'collection_recovery_fee', 'last_pymnt_d','last_pymnt_amnt', 'next_pymnt_d', 'last_credit_pull_d', 
                 'last_fico_range_high', 'last_fico_range_low', 'collections_12_mths_ex_med', 'mths_since_last_major_derog',
                 'policy_code', 'application_type','fico_range_low', 'fico_range_high', 'open_il_6m']
    df_cols = [i for i in df.columns if i not in drop_feats]
    df = df.copy()
    df = df[~df['loan_status'].isin(['Late (31-120 days)', 'In Grace Period', 'Late (16-30 days)', 'Default'])]
    df = df[df_cols]
    df['label'] = df.loc[:, 'loan_status'].apply(lambda x: 1 if x == 'Charged Off' else 0)
    
    df_categ = df.select_dtypes(include=["object"])
    df_categ['addr_state'] = df_categ['addr_state'].apply(_categ_addr)
    df_categ['issue_d'] = [datetime.datetime.strptime(i, '%b-%Y').date().month for i in df_categ['issue_d']]
    df_categ['issue_d'] = df_categ['issue_d'].apply(_categ_date_quarter)
    df_categ['issue_d'] = ['issue_d_'+i for i in df_categ['issue_d']]
    df_categ['emp_title'] = df_categ['emp_title'].apply(_categ_emp_title)
    df_categ['emp_length'] = df_categ['emp_length'].apply(_categ_emp_length)
    df_categ['purpose'] = df_categ['purpose'].apply(_categ_purpose)
    df_categ['home_ownership'] = [i.replace('other', 'MORTGAGE') for i in df_categ['home_ownership']]
    df_categ['earliest_cr_line'] = [datetime.datetime.strptime(i, '%b-%Y').date().month for i in df_categ['earliest_cr_line']]
    df_categ['earliest_cr_line'] = df_categ['earliest_cr_line'].apply(_categ_date_quarter)
    df_categ['earliest_cr_line'] = ['earliest_cr_line_'+i for i in df_categ['earliest_cr_line']]
    df_categ['revol_util'] = [float(str(i).replace('%','')) for i in df_categ['revol_util']]
    df_categ['revol_util'] = df_categ['revol_util'].apply(_categ_revol)

    categ_cols = ['term', 'verification_status', 'addr_state', 'issue_d', 'purpose', 'emp_title', 'emp_length', 
                 'home_ownership', 'earliest_cr_line', 'revol_util']
    df_categ = df_categ[categ_cols]
    print('len categ: {}'.format(len(df_categ)))

    # 先處理 numerical 的部分
    df_numeric = df.select_dtypes(exclude=["object"])
    df_numeric = df_numeric.fillna(0)
    num_cols = [i for i in df_numeric.columns if i not in ['label']]
    
    # 標準化
    scaler = StandardScaler()
    df_numeric[num_cols] = scaler.fit_transform(df_numeric[num_cols])
    print('len numeric: {}'.format(len(df_numeric)))
    
    combine = pd.concat([df_numeric, df_categ], axis=1).reset_index(drop=True)
    return combine