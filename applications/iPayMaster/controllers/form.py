# -*- coding: utf-8 -*-
from datetime import datetime,date
import os
ones = ["", "one ","two ","three ","four ", "five ","six ","seven ","eight ","nine "]
tens = ["ten ","eleven ","twelve ","thirteen ", "fourteen ","fifteen ","sixteen ","seventeen ","eighteen ","nineteen "]
twenties = ["","","twenty ","thirty ","forty ","fifty ","sixty ","seventy ","eighty ","ninety "]
thousands = ["","thousand ","million ", "billion ", "trillion ", "quadrillion ", "quintillion ", "sextillion ", "septillion ","octillion ",    "nonillion ", "decillion ", "undecillion ", "duodecillion ", "tredecillion ",    "quattuordecillion ", "quindecillion", "sexdecillion ","septendecillion ", 	"octodecillion ", "novemdecillion ", "vigintillion "]

def designations():
    desform=SQLFORM.smartgrid(db.designation,deletable=True,editable=True,_class='form-style-9',user_signature=False)
    return locals()

def employees():
    empform=SQLFORM.smartgrid(db.employee,deletable=True,editable=True,_class='form-style-9',user_signature=False)
    return locals()

def leaves():
    lveform=SQLFORM.smartgrid(db.lve,deletable=True,editable=True,_class='form-style-9',user_signature=False)
    return locals()

def salaries():
    salaryform=SQLFORM.smartgrid(db.pbr,deletable=True,editable=True,_class='form-style-9',user_signature=False)
    return locals()

def remitence():
    remform=SQLFORM.smartgrid(db.remitence,deletable=True,editable=True,_class='form-style-9',user_signature=False)
    return locals()

def bank():
    bankform=SQLFORM.smartgrid(db.bank,deletable=True,editable=True,_class='form-style-9',user_signature=False)
    return locals()

def salaryhistories():
    shform=SQLFORM.smartgrid(db.salaryhistory,deletable=True,editable=True,_class='form-style-9',user_signature=False)
    return locals()

def salaryheads():
    sheadform=SQLFORM.smartgrid(db.salaryheads,deletable=True,editable=True,_class='form-style-9',user_signature=False)
    return locals()

def statuses():
    statusform=SQLFORM.smartgrid(db.status,deletable=True,editable=True,_class='form-style-9',user_signature=False)
    return locals()

def salaryhistemp():
    x=request.args(0)
    shform=SQLFORM.smartgrid(
                             db.salaryhistory,constraints={'salaryhistory':db.salaryhistory.pen==x},
                             deletable=True,
                             editable=True,
                             _class='form-style-9',
                             user_signature=False
                           )
    return locals()

def paybillgenerator():
    generateform=SQLFORM.grid(
                                  db.employee,
                                  orderby=db.employee.name,
                                  fields=[db.employee.pen,db.employee.name, ],
                                  deletable=False,
                                  editable=False,
                                  _class='form-style-9',
                                  links=[
                                         lambda r:  A(T('Generate'),
                                                    _href=URL('process','billslip',args=[r.id] ),
                                                    _class='btn btn-primary',
                                                    _name='btgen'),
                                         ],
                                  user_signature=False,
                             )
    return locals()

def viewbills():
    bills = db(db.pbr)
    sts= db(db.status.name == 'Accepted').select(db.status.id).first()
    url = os.path.join(request.folder, 'static', 'images/ihrdlogo.png')
    chart = IMG(_src=url, _width="250", _height="100")
    vbillsgrid = SQLFORM.grid( bills, fields=[db.pbr.pen, db.pbr.mnthandyear, db.pbr.status ], _class='form-style-9', links=[
                                         lambda r:  A(T('Show'),
                                                    _href=URL('form','viewslip',args=[r.pen, r.mnthandyear] ),
                                                    _class='btn btn-primary',
                                                    _name='btshow'),
                                         lambda r:  A(T('PDF'),
                                                    _href=URL('form','viewslippdf',args=[r.pen, r.mnthandyear] ) ,
                                                    _class='btn btn-primary',
                                                    _name='btnpdf')  if r.status == sts.id else A(T('Submit'),
                                                    _href=URL('process','submitbill',args=[r.id]) ,
                                                    _class='btn btn-warning',
                                                    _name='btnpdf') ,
                                         ],
                                         create = False
                             )
    return locals()

def int2word(n):
    """
    convert an integer number n into a string of english words
    """
    # break the number into groups of 3 digits using slicing
    # each group representing hundred, thousand, million, billion, ...
    n3 = []
    r1 = ""
    # create numeric string
    ns = str(n)
    for k in range(3, 33, 3):
        r = ns[-k:]
        q = len(ns) - k
        # break if end of ns has been reached
        if q < -2:
            break
        else:
            if  q >= 0:
                n3.append(int(r[:3]))
            elif q >= -1:
                n3.append(int(r[:2]))
            elif q >= -2:
                n3.append(int(r[:1]))
        r1 = r

    #print n3  # test

    # break each group of 3 digits into
    # ones, tens/twenties, hundreds
    # and form a string
    nw = ""
    for i, x in enumerate(n3):
        b1 = x % 10
        b2 = (x % 100)//10
        b3 = (x % 1000)//100
        #print b1, b2, b3  # test
        if x == 0:
            continue  # skip
        else:
            t = thousands[i]
        if b2 == 0:
            nw = ones[b1] + t + nw
        elif b2 == 1:
            nw = tens[b1] + t + nw
        elif b2 > 1:
            nw = twenties[b2] + ones[b1] + t + nw
        if b3 > 0:
            nw = ones[b3] + "hundred " + nw
    return nw

def viewslip():
    vpen = request.args(0)
    mny  = request.args(1)
    mn   = mny
    mn   = mn.replace("_","/")
    slip = db( (db.pbr.pen == vpen) & ( db.pbr.mnthandyear == mny )).select().first()
    empdata = db(db.employee.id == vpen ).select(db.employee.name,db.employee.designation).first()
    empdesig = db(db.designation.id == empdata.designation).select(db.designation.name).first()
    wrd = int2word(slip.netpay)
    return locals()

def viewslippdf():
    vpen = request.args(0)
    mny  = request.args(1)
    mn   = mny
    mn   = mn.replace("_","/")
    slip = db( (db.pbr.pen == vpen) & ( db.pbr.mnthandyear == mny )).select().first()
    empdata = db(db.employee.id == vpen ).select(db.employee.name,db.employee.designation).first()
    empdesig = db(db.designation.id == empdata.designation).select(db.designation.name).first()
    acc = db(db.bank.id == vpen).select().first()
    wrd = int2word(slip.netpay)
    sliphtml = DIV(_style="border: 1px solid black;")
    sliphtml.insert(0,H3('To,'))
    sliphtml.insert(1,H3('Sri/Smt. %s' % ( empdata.name )))
    sliphtml.insert(2,H4(empdesig.name))
    sliphtml.insert(3,H3('Payslip for the month and year %s' % (mn) )   )
    tbl = TABLE(_class='table table-bordered')
    tbl.insert(0,TR(TH('Income'),TH('Amount'),TH('Deduction'),TH('Amount')))
    tbl.insert(1,TR(TD( 'Basic Salary'),TD( slip.basicpay),TD( 'CPF Contribution'),TD( slip.cpf)))
    tbl.insert(2,TR(TD( 'DA'),TD( slip.da),TD( 'CPF Loan Refund'),TD( slip.cpfrefund)))
    tbl.insert(3,TR(TD( 'HRA'),TD( slip.hra),TD( 'Festival Advance Refund'),TD( slip.festivaladvancerefund)))
    tbl.insert(4,TR(TD( 'Special Allowance'),TD( slip.specialallowance),TD( 'House Loan Refund'),TD( slip.houseloan)))
    tbl.insert(5,TR(TD( 'Flood Relief'),TD( slip.floodrelief),TD( 'Income Tax'),TD( slip.incometax)))
    tbl.insert(6,TR(TD( 'Substancive Pay'),TD( slip.substancivepay),TD( 'GPAIS'),TD( slip.gpais)))
    tbl.insert(7,TR(TD( 'Leave Salary'),TD( slip.leavesalary),TD( ),TD( )))
    tbl.insert(8,TR(TD( 'Festival Allowance'),TD( slip.festivalallowance),TD( ),TD( )))
    tbl.insert(9,TR(TD( 'Festival Advance'),TD( slip.festivaladvance),TD( ),TD( )))
    tbl.insert(10,TR(HR()))
    tbl.insert(11,TR(TD( 'Gross Total'),TD( slip.grsstotal),TD('Total Deduction' ),TD(slip.totaldeduction)))
    tbl.insert(12,TR(HR()))
    jump=0
    for th in tbl.elements('th'):
        if jump % 2 == 0:
            th.attributes['_width'] = '30%'
        else:
            th.attributes['_width'] = '15%'
            th.attributes['_align'] = 'right'
        jump=jump+1
    jump=0
    for td in tbl.elements('td'):
        if jump % 2 == 0:
            td.attributes['_width'] = '30%'
        else:
            td.attributes['_width'] = '15%'
            td.attributes['_align'] = 'right'
        jump=jump+1
    sliphtml.insert(4,tbl)
    sliphtml.insert(5,H4('Net Pay : %s' % ( slip.netpay )))
    sliphtml.insert(6,'Rs. ')
    sliphtml.insert(7,wrd)
    sliphtml.insert(8,' Only')
    sliphtml.insert(9,BR())
    sliphtml.insert(10,H4('Account Details'))
    sliphtml.insert(11,BR())
    sliphtml.insert(12,'Transfered to ')
    sliphtml.insert(13,'Account number :')
    sliphtml.insert(14,acc.accno)
    sliphtml.insert(15,BR())
    sliphtml.insert(16,'IFSC code :')
    sliphtml.insert(17,acc.ifsc)
    sliphtml.insert(18,BR())
    sliphtml.insert(19,HR())
    sliphtml.insert(20,BR())
    sliphtml.insert(21,BR())
    sliphtml.insert(22,BR())
    sliphtml.insert(23,BR())
    sliphtml.insert(24,BR())
    sliphtml.insert(25,BR())
    sliphtml.insert(26,BR())
    sliphtml.insert(27,BR())
    sliphtml.insert(28,'                         PRINCIPAL                                                                            ')
    sliphtml.insert(29,'CASHIER')
    from gluon.contrib.pyfpdf import FPDF, HTMLMixin
        # create a custom class with the required functionality
    class MyFPDF(FPDF, HTMLMixin):
        def header(self):
            "hook to draw custom page header (logo and title)"
            self.set_font('Arial', 'B', 15)
            self.cell(65) # padding
            self.cell(80, 10, "CAS Payyappady PaySlip", 1, 0, 'C')
            self.ln(20)
        def footer(self):
            "hook to draw custom page footer (printing page numbers)"
            self.set_y(-15)
            self.set_font('Arial', 'I', 8)
            txt = 'Page %s of %s' % (self.page_no(), self.alias_nb_pages())
            self.cell(0, 10, txt, 0, 0, 'C')
    pdf = MyFPDF()

    # create a page and serialize/render HTML objects
    pdf.add_page()

    pdf.write_html(str(sliphtml))
    # prepare PDF to download:
    response.headers['Content-Type'] = 'application/pdf'

    return pdf.output(dest='S')

def pviewbills():
    x= db(db.status.name == 'Submitted').select(db.status.id).first()
    pvbillsgrid = SQLFORM.smartgrid( db.pbr,constraints={'pbr':db.pbr.status==x}, fields=[db.pbr.pen, db.pbr.billno, db.pbr.mnthandyear, db.pbr.evnt, db.pbr.basicpay, db.pbr.dod, db.pbr.floodrelief, db.pbr.substancivepay, db.pbr.leavesalary, db.pbr.da, db.pbr.hra, db.pbr.specialallowance,	db.pbr.cpf,	db.pbr.cpfrefund,	db.pbr.incometax, db.pbr.festivalallowance,	db.pbr.festivaladvance,	db.pbr.festivaladvancerefund, db.pbr.houseloan,	db.pbr.gpais,	db.pbr.grsstotal, db.pbr.totaldeduction, db.pbr.netpay,	db.pbr.status ], _class='form-style-9',
                               links=[
                                         lambda r:  A(T('Approve'),
                                                    _href=URL('process','approve',args=[r.id] ),
                                                    _class='btn btn-primary',
                                                    _name='btapve'),
                                         lambda r:  A(T('Recheck'),
                                                    _href=URL('process','recheck',args=[r.id] ),
                                                    _class='btn btn-primary',
                                                    _name='btrch'),
                                         ],
                                         create = False,
                                         deletable=False,
                                         editable=False,
                                         user_signature=False
                             )
    return locals()

def pviewleave():
    x= db(db.status.name == 'Submitted').select(db.status.id).first()
    pvlvegrid= SQLFORM.smartgrid( db.lve,constraints={'lve':db.lve.status == x}, fields=[db.lve.name, db.lve.applydate, db.lve.typ,
                                         db.lve.frmdate,db.lve.todate,db.lve.ttllvs, db.lve.reason, db.lve.status
                                                                                         ],
                                      _class='form-style-9',
                               links=[
                                         lambda r:  A(T('Approve'),
                                                    _href=URL('process','approvelve',args=[r.id] ),
                                                    _class='btn btn-primary',
                                                    _name='btapve'),
                                         lambda r:  A(T('Reject'),
                                                    _href=URL('process','reject',args=[r.id] ),
                                                    _class='btn btn-primary',
                                                    _name='btrch'),
                                         ],
                                         create = False,
                                         deletable=False,
                                         editable=False,
                                         user_signature=False
                             )
    return locals()

def signup():
    empname = db( db.employee ).select( db.employee.name, db.employee.id )
    sel = SELECT(_id = "emp" ,_name="emp", *[OPTION( empname[x].name,_value=empname[x].name) for x in range(len(empname)) ])
    authform=FORM(
               LABEL('Sign up for'),
               sel,
               BR(),
               LABEL('Email      '),
               INPUT(_name='email',_type='string'),
               BR(),
               LABEL('Password   '),
               INPUT(_name='password',_type='string'),
               BR(),
               INPUT(_name='submit',_value='Process',_type='submit')
              )
    if authform.process().accepted:
        emp = request.vars['emp']
        db.auth_user.update_or_insert(
                                        first_name=emp,
                                        email=request.vars['email'],
                                        password=db.auth_user.password.validate(request.vars['password'])[0],
                                        user_type='Ordinary',
                                     )
    return locals()

def eviewleave():
    emp = db(db.auth_user.id == auth.user_id).select(db.auth_user.first_name).first()
    empid = db(db.employee.name == emp.first_name).select(db.employee.id).first()
    evlvegrid= SQLFORM.smartgrid(
                                         db.lve,constraints={'lve':db.lve.name == empid.id},fields=[db.lve.name, db.lve.applydate,db.lve.typ,db.lve.frmdate,db.lve.todate,db.lve.ttllvs, db.lve.reason, db.lve.status],
                                         _class='form-style-9',
                                         orderby=[~db.lve.applydate],
                                         create = False,
                                         deletable=False,
                                         editable=False,
                                         user_signature=False
                                 )
    return locals()

def applylve():
    emp = db(db.auth_user.id == auth.user_id).select(db.auth_user.first_name).first()
    empid = db(db.employee.name == emp.first_name).select(db.employee.id).first()
    today = datetime.date(datetime.now())
    submitid=db(db.status.name=="Submitted").select(db.status.id)
    lvetyp = ['Duty leave','Casual leave','Halfpay leave','Commuted leave','Earned leave']
    sel = SELECT(_id = "typ" ,_name="typ", *[OPTION(lvetyp[x],_value=lvetyp[x]) for x in range(len(lvetyp)) ])
    applyform=FORM(
                    LABEL('Leave type'),
                    sel,
                    BR(),
                    LABEL('From Date'),
                    INPUT(_name='fdate',_type='date'),
                    BR(),
                    LABEL('To Date'),
                    INPUT(_name='tdate',_type='date'),
                    BR(),
                    LABEL('Number of days'),
                    INPUT(_name='totaldays',_type='integer'),
                    BR(),
                    LABEL('Reason'),
                    INPUT(_name='reason',_type='string'),
                    BR(),
                    INPUT(_name='submit',_value='Process',_type='submit')
                  )
    if applyform.process().accepted:
        db.lve.update_or_insert(
                                        name=empid,
                                        applydate=today,
                                        typ=request.vars['typ'],
                                        frmdate=request.vars['fdate'],
                                        todate=request.vars['tdate'],
                                        ttllvs=request.vars['totaldays'],
                                        reason=request.vars['reason'],
                                        status=submitid[0].id,
                                )
        redirect(URL('form','eviewleave'))
    return locals()
