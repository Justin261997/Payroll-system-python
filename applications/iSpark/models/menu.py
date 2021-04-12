# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# this is the main application menu add/remove items as required
# ----------------------------------------------------------------------------------------------------------------------

response.menu = [
                    (T('Home'), False, URL('default', 'index'), []),
                    (T('Employee Details'),False,URL('form','employees'),[]),
                    (T('Designation Details'),False,URL('form','designations'),[]),
                    (T('Salary Details'),False,URL('form','salaries'),[]),
                    (T('Apply for leave'),False,URL('form','leaves'),[])
                ]
