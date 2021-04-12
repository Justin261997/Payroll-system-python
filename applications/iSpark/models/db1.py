# -*- coding: utf-8 -*-

from gluon.contrib.appconfig import AppConfig
from gluon.tools import Auth

db.define_table('designation',
                Field('name','string',label='Designation'),
                format='%(name)s'
               )

db.define_table('employee',
                Field('pen','integer',requires=IS_NOT_EMPTY(),label='PEN'),
                Field('name','string',requires=IS_NOT_EMPTY(),label='Name of Employee'),
                Field('dob','date',label='Date of Birth'),
                Field('bloodgroup',requires=IS_IN_SET(['A+','A-','B+','B-','AB+','AB-','O+','O-']),label='Blood Group'),
                Field('mob','string',label='Mobile'),
                Field('religion','string',label='Religion'),
                Field('caste','string',label='Caste'),
                Field('voterid','string',label='Voter ID'),
                Field('designation','reference designation'),
                Field('scaleofpay','string',label='Scale of Pay'),
                Field('curntbasicpay','integer',label='Current Basic Pay'),
                Field('doj','date',label='Date of Join'),
                Field('docp','date',label='Date of Completion Probation'),
                Field('maritalstatus',requires=IS_IN_SET(['Married','Not married','Widower']),label='Marital Status'),
                Field('doi','date',label='Date of Increment'),
                Field('gpfaccno','integer',label='GPF Account Number'),
                Field('category',requires=IS_IN_SET(['Officiating','Temporary']),label='Job Category'),
                Field('fpsno','integer',label='FPS Number'),
                Field('licno','integer',label='LIC Number'),
                Field('slino','integer',label='SLI Number'),
                Field('plino','integer',label='PLI Number'),
                Field('serviceverified',requires=IS_IN_SET(['Yes','No']),label='Service Verified'),
                Field('honorarium',requires=IS_IN_SET(['Yes','No']),label='Honorarium'),
                format='%(name)s'
               )

db.define_table('remitence',
                Field('pen','reference employee'),
                Field('dte','date',label='Date'),
                Field('amtdbt','integer',label='Amount Debited'),
                Field('chqdetails','string',label='Cheque Details'),
                Field('chqno','integer',label='Cheque Number'),
                Field('chqd','date',label='Cheque Date'),
                Field('typ',requires=IS_IN_SET(['Bank','Cheque','Cash']),label='Type'),
                Field('amount','integer',label='Amount'),
               )

db.define_table('bank',
                Field('pen','reference employee'),
                Field('acchldname','string',label='Account Holder Name'),
                Field('accno','integer',label='Account Number'),
                Field('ifsc','string',label='IFS Code'),
                Field('pan','string',label='PAN Number'),
                Field('mob','string',label='Mobile'),
                Field('aadhaar','string',label='Aadhaar'),
                )

db.define_table('status',
                Field('name','string',label='Status Values'),
                format='%(name)s'
                )

db.define_table('pbr',
                Field('pen','reference employee'),
                Field('billno','integer',requires=IS_NOT_EMPTY(),label='Bill Number'),
                Field('fbs','integer',label='FBS'),
                Field('mnthandyear','date',label='Month and Year'),
                Field('evnt','string',label='Event'),
                Field('officiatepay','string',label='Officiating Pay'),
                Field('dod','date',label='Date of Draw'),
                Field('fldrf','integer',label='Flood Relief'),
                Field('substanpay','integer',label='Sub Stancive Pay'),
                Field('accdetails','string',label='Account Details'),
                Field('lvesalry','integer',label='Leave Salary'),
                Field('da','integer',label='DA'),
                Field('hra','integer',label='HRA'),
                Field('spclalwnc','integer',label='Special Allowance'),
                Field('gps','integer',label='GPS Sub'),
                Field('grsstotl','integer',label='Gross Total'),
                Field('gpfadv','integer',label='GPF Advanced'),
                Field('houserent','integer',label='House Rent'),
                Field('incometax','integer',label='Income Tax'),
                Field('festallow','integer',label='Festival Allowance'),
                Field('housebld','integer',label='House Build Allowance'),
                Field('gpas','integer',label='GPAS'),
                Field('ttlddn','integer',label='Total Deduction'),
                Field('netpay','integer',label='Net Pay'),
                Field('status','reference status'),
                Field('created_on', 'datetime', default=request.now),
                Field('created_by', 'reference auth_user', default=auth.user_id),
                format='%(pen)s'
               )

db.define_table('lve',
                Field('name','reference employee'),
                Field('applydate','date',label='Apply Date'),
                Field('typ',requires=IS_IN_SET(['Duty leave','Other']),label='Leave Type'),
                Field('frmdate','date',label='From Date'),
                Field('todate','date',label='To Date'),
                Field('ttllvs','integer',label='Total Leaves'),
                Field('reason','string',label='Reason'),
                Field('lveid','integer',label='Leave ID'),
                Field('status','date',label='Status'),
                format='%()s'
               )

#db.define_table('advances',
#                Field('gpf','integer',label='GPF'),
#                Field('cyclic_mc','date',label='Cyclic MC'),
#                Field('fest_allo','integer',label='Festival allowance'),
#                Field('h_l_mna','integer',label=''),
#                Field('no_date','integer',label='Number of dates'),
#                format='%(gpf)s'
#               )

#db.define_table('govtres',
#                Field('dooc','date',label='Date of occupied'),
#                Field('dov','date',label='Date of vaccated'),
#                format='%(dooc,dov)s'
#               )

#db.define_table('salary',
#                Field('employee','reference employee'),
#                Field('b_acc','integer',label='Bank account'),
#                Field('lve','reference lve',label='Total leaves'),
#                Field('cu_bp','integer',label='Current basic pay'),
#                Field('sc_of_pay','integer',label='Scale of pay'),
#                format='%(cu_bp)s'
#               )
