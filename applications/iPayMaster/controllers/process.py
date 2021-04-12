# -*- coding: utf-8 -*-
from datetime import datetime

def billslip():
    dt=None
    idict=None
    penno=request.args(0)
    activeid=db(db.status.name=="Active").select(db.status.id)
    slip = SQLFORM.grid(
                         db((db.salaryhistory.pen == penno) & (db.salaryhistory.status == activeid[0].id)),
                         fields=[db.salaryhistory.pen,db.salaryhistory.typ,db.salaryhistory.head,db.salaryhistory.amount],
                         user_signature=False
                       )
    empname = db( db.employee.id == penno ).select( db.employee.name )
    gform=FORM(
               LABEL('Generate Salary for %s' % (empname[0].name) ),
               INPUT(_name='ftm',_type='date'),
               LABEL('Event'),
               INPUT(_name='evt',_type='string'),
               INPUT(_name='submit',_value='Process',_type='submit')
              )
    if gform.process().accepted:
        ftm=request.vars['ftm']
        evt=request.vars['evt']
        dt=datetime.strptime(ftm,'%Y-%m-%d')
        hitems = db((db.salaryhistory.pen == penno) & (db.salaryhistory.status == activeid[0].id) & (db.salaryhistory.efrom <= ftm <= db.salaryhistory.eto )).select()
        idict ={}
        grosspay=0
        deduction=0
        for x  in hitems:
            shead = db(db.salaryheads.id == x.head).select(db.salaryheads.name,db.salaryheads.saltype)
            if shead[0].saltype== "Income" :
                grosspay = grosspay + x.amount
            elif    shead[0].saltype== "Deduction" :
                deduction = deduction + x.amount
            idict[ shead[0].name ] = x.amount
        netpay = grosspay - deduction
        #Corrections
        idict['substancivepay']   = idict.get('substancivepay',0)
        idict['floodrelief']      = idict.get('floodrelief',0)
        idict['leavesalary']      = idict.get('leavesalary',0)
        idict['hra']              = idict.get('hra',0)
        idict['specialallowance'] = idict.get('specialallowance',0)
        idict['cpf']              = idict.get('cpf',0)
        idict['cpfrefund']        = idict.get('cpfrefund',0)
        idict['incometax']        = idict.get('incometax',0)
        idict['festivalallowance'] = idict.get('festivalallowance',0)
        idict['festivaladvance']   = idict.get('festivaladvance',0)
        idict['festivaladvancerefund'] = idict.get('festivaladvancerefund',0)
        idict['houseloan']         = idict.get('houseloan',0)
        idict['gpais']             = idict.get('gpais',0)
        idict['basicpay']          = idict.get('basicpay',0)
        idict['da']                = idict.get('da',0)
        idict['totaldeduction']    = idict.get('totaldeduction',deduction)
        idict['grosspay']          = idict.get('grosspay',grosspay)
        idict['netpay']            = idict.get('netpay',netpay)
        #End Corrections
        sts= db(db.status.name == 'Submitted').select(db.status.id).first()
        db.pbr.update_or_insert(   (db.pbr.mnthandyear==str(dt.month)+"_"+str(dt.year)) &  (db.pbr.pen==penno),
                                 pen=penno,
                                 mnthandyear=str(dt.month)+"_"+str(dt.year),
                                 evnt=evt,
                                 dod=ftm,
                                 substancivepay=idict['substancivepay'],
                                 floodrelief=idict['floodrelief'],
                                 leavesalary=idict['leavesalary'],
                                 hra=idict['hra'],
                                 specialallowance=idict['specialallowance'],
                                 cpf=idict['cpf'],
                                 cpfrefund=idict['cpfrefund'],
                                 incometax=idict['incometax'],
                                 festivalallowance=idict['festivalallowance'],
                                 festivaladvance=idict['festivaladvance'],
                                 festivaladvancerefund=idict['festivaladvancerefund'],
                                 houseloan=idict['houseloan'],
                                 gpais=idict['gpais'],
                                 basicpay=idict['basicpay'],
                                 da=idict['da'],
                                 grsstotal=idict['grosspay'],
                                 totaldeduction=idict['totaldeduction'],
                                 netpay=idict['netpay'],
                                 status=sts.id
                               )
        session.flash = "Bill Generated Successfully"
        redirect(URL('default','index'))
    return locals()

def salaryhistory():
    empname = db( db.employee ).select( db.employee.name, db.employee.id )
    sel = SELECT(_id = "emp" ,_name="emp", *[OPTION( empname[ x].name,_value=empname[x].id) for x in range(len(empname)) ])
    iform=FORM(
               LABEL('Salary history for '),
               sel,
               LABEL('From'),
               INPUT(_name='fdate',_type='date'),
               LABEL('To'),
               INPUT(_name='tdate',_type='date'),
               INPUT(_name='submit',_value='Process',_type='submit')
              )
    empid=None
    frdate=None
    todate=None
    fdate=None
    tdate=None
    hdata=''
    if iform.process().accepted:
        empid=request.vars['emp']
        fdate = request.vars['fdate']
        tdate = request.vars['tdate']
        frdate= str( int(fdate.split("-")[1])) + "_" +  str( int(fdate.split("-")[0]))
        todate= str( int(tdate.split("-")[1])) + "_" +  str( int(tdate.split("-")[0]))
        qry =  db((db.pbr.pen == empid) & ( db.pbr.mnthandyear >= frdate )  & ( db.pbr.mnthandyear <= todate ))
        hdata = SQLFORM.grid( qry,
                             create=False,
                             editable=False,
                             deletable = False,
                             orderby=[~db.pbr.mnthandyear],
                             user_signature=False
                            )
    return locals()

def submitbill():
    id = request.args(0)
    sts= db(db.status.name == 'Submitted').select(db.status.id).first()
    db.pbr.update_or_insert(   (db.pbr.id == id ),
                                 status = sts.id
                               )
    redirect(URL('form','viewbills'))
    return locals()
def approve():
    id = request.args(0)
    sts= db(db.status.name == 'Accepted').select(db.status.id).first()
    db.pbr.update_or_insert(   (db.pbr.id == id ),
                                 status = sts.id
                               )
    redirect(URL('form','pviewbills'))
    return locals()

def recheck():
    id = request.args(0)
    sts= db(db.status.name == 'Recheck').select(db.status.id).first()
    db.pbr.update_or_insert(   (db.pbr.id == id ),
                                 status = sts.id
                               )
    redirect(URL('form','pviewbills'))
    return locals()

def approvelve():
    id = request.args(0)
    sts= db(db.status.name == 'Accepted').select(db.status.id).first()
    db.lve.update_or_insert(   (db.lve.id == id ),
                                 status = sts.id
                               )
    redirect(URL('form','pviewleave'))
    return locals()

def reject():
    id = request.args(0)
    sts= db(db.status.name == 'Rejected').select(db.status.id).first()
    db.lve.update_or_insert(   (db.lve.id == id ),
                                 status = sts.id
                               )
    redirect(URL('form','pviewleave'))
    return locals()
