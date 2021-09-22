#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('fullname')
        r.fieldcell('birthplace_id')
        r.fieldcell('gender')
        r.fieldcell('birthdate')
        r.fieldcell('telephone')
        r.fieldcell('email')
        r.fieldcell('job')
        r.fieldcell('journal_request', semaphore=True)
        r.fieldcell('news_request', semaphore=True)
        r.fieldcell('address')
        r.fieldcell('city_id')
        r.fieldcell('fiscal_code')
        r.fieldcell('blood_group_code', width='8em')
        r.fieldcell('department_id')
        r.fieldcell('first_donation_date')
        r.fieldcell('last_donation_date')
        r.fieldcell('is_active', semaphore=True)
        r.fieldcell('donations_number')
        r.fieldcell('notes')

    def th_order(self):
        return 'fullname'

    def th_query(self):
        return dict(column='id', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        bc = form.center.borderContainer()
        fb = bc.contentPane(region='top', height='50%', datapath='.record').formbuilder(cols=2, border_spacing='4px')
        fb.field('name' )
        fb.field('surname' )
        fb.field('birthplace_id' )
        fb.field('gender', tag='filteringSelect', values='M:Male,F:Female' )
        fb.field('birthdate' )
        fb.field('telephone' )
        fb.field('email' )
        fb.field('job' )
        fb.field('journal_request' )
        fb.field('news_request' )
        fb.field('address' )
        fb.field('city_id' )
        fb.field('fiscal_code' )
        fb.field('blood_group_code' )
        fb.field('department_id' )
        fb.field('notes' )

        tc = bc.tabContainer(region='center')
        tc.contentPane(title='Donations').dialogTableHandler(relation='@donations')
        tc.contentPane(title='Analysis').dialogTableHandler(relation='@analysis')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px' )
