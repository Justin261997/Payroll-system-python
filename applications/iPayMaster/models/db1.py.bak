# -*- coding: utf-8 -*-

db.define_table('designation',
                Field('name','string',label='Designation'),
                fake_migrate = True,
                format='%(name)s'
               )

db.define_table('employee',
                Field('pen','integer',requires=IS_NOT_EMPTY(),unique=True,label='PEN'),
                Field('name','string',requires=IS_NOT_EMPTY(),label='Name of Employee'),
                Field('dob','date',label='Date of Birth'),
                Field('bloodgroup',requires=IS_IN_SET(['A+','A-','B+','B-','AB+','AB-','O+','O-']),label='Blood Group'),
                Field('mob','string',label='Mobile'),
                Field('religion',requires=IS_IN_SET(['Hindu','Christian','Muslim','Other']),label='Religion'),
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
                Field('fbsno','integer',label='FBS Number'),
                Field('licno','integer',label='LIC Number'),
                Field('slino','integer',label='SLI Number'),
                Field('plino','integer',label='PLI Number'),
                Field('serviceverified',requires=IS_IN_SET(['Yes','No']),label='Service Verified'),
                Field('honorarium',requires=IS_IN_SET(['Yes','No']),label='Honorarium'),
                fake_migrate = True,
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
                fake_migrate = True,
               )

db.define_table('bank',
                Field('pen','reference employee'),
                Field('acchldname','string',label='Account Holder Name'),
                Field('accno','integer',requires=IS_NOT_EMPTY(),label='Account Number'),
                Field('ifsc','string',requires=IS_NOT_EMPTY(),label='IFS Code'),
                Field('pan','string',label='PAN Number'),
                Field('mob','string',label='Mobile'),
                Field('aadhaar','string',label='Aadhaar'),
                fake_migrate = True,
                )

db.define_table('status',
                Field('name','string',label='Status Values'),
                fake_migrate = True,
                format='%(name)s'
                )

db.define_table('pbr',
                Field('pen','reference employee'),
                Field('billno','integer',requires=IS_NOT_EMPTY(),label='Bill Number'),
                Field('mnthandyear','string',label='Month and Year'),
                Field('evnt','string',label='Event'),
                Field('basicpay','integer',requires=IS_NOT_EMPTY(),label='Basic Pay'),
                Field('dod','date',label='Date of Draw'),
                Field('floodrelief','integer',label='Flood Relief'),
                Field('substancivepay','integer',label='Sub Stancive Pay'),
                Field('leavesalary','integer',label='Leave Salary'),
                Field('da','integer',label='DA'),
                Field('hra','integer',label='HRA'),
                Field('specialallowance','integer',label='Special Allowance'),
                Field('cpf','integer',label='CPF Subscription'),
                Field('cpfrefund','integer',label='CPF Refund '),
                Field('incometax','integer',label='Income Tax'),
                Field('festivalallowance','integer',label='Festival Allowance'),
                Field('festivaladvance','integer',label='Festival Advance'),
                Field('festivaladvancerefund','integer',label='Festival Advance Refund'),
                Field('houseloan','integer',label='Housing Loan Refund'),
                Field('gpais','integer',label='GPAIS'),
                Field('grsstotal','integer',label='Gross Total'),
                Field('totaldeduction','integer',label='Total Deduction'),
                Field('netpay','integer',label='Netpay'),
                Field('status','reference status'),
                Field('created_on', 'datetime', default=request.now),
                Field('created_by', 'reference auth_user', default=auth.user_id),
                fake_migrate = True,
                format='%(pen)s'
               )
#compute=lambda r: r['basicpay'] + r['floodrelief'] + r['substancivepay'] + r['leavesalary'] + r['da'] + r['hra'] + r['specialallowance'] + r['festivalallowance']
#compute=lambda r: r['cpfrefund'] + r['incometax'] + r['festivaladvancerefund'] + r['houseloan'] + r['gpais']
#compute=lambda r: r['grsstotal']  -  r['totaldeduction']
db.define_table('lve',
                Field('name','reference employee'),
                Field('applydate','date',requires=IS_NOT_EMPTY(),label='Apply Date'),
                Field('typ',requires=IS_IN_SET(['Duty leave','Casual leave','Halfpay leave','Commuted leave','Earned leave']),label='Leave Type'),
                Field('frmdate','date',requires=IS_NOT_EMPTY(),label='From Date'),
                Field('todate','date',requires=IS_NOT_EMPTY(),label='To Date'),
                Field('ttllvs','integer',label='Total Leaves'),
                Field('reason','string',label='Reason'),
                Field('status','reference status'),
                fake_migrate = True,
                format='%()s'
               )

db.define_table('salaryheads',
                Field('name','string',label='Salary Heads'),
                Field('saltype',requires=IS_IN_SET(['Income','Deduction']),label='Type'),
                fake_migrate = True,
                format='%(name)s'
               )

db.define_table('salaryhistory',
                Field('pen','reference employee'),
                Field('historyid','integer',label='History ID'),
                Field('efrom','date',label='From date'),
                Field('eto','date',label='To Date'),
                Field('typ',requires=IS_IN_SET(['Income','Dedction']),label='Type'),
                Field('head','reference salaryheads',label='Head'),
                Field('amount','integer',label='Amount'),
                Field('status','reference status'),
                fake_migrate = True,
                format='%()s'
               )
