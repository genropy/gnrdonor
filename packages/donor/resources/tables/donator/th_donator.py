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
        top = bc.borderContainer(region='top', height='40%', datapath='.record', margin='10px')
        fb = top.contentPane(region='left', width='900px').formbuilder(cols=3, border_spacing='4px')
        fb.field('user_id' )
        fb.field('name' )
        fb.field('surname' )
        fb.field('birthplace_id' )
        fb.field('birthdate' )
        fb.field('gender', tag='filteringSelect', values='M:Male,F:Female' )
        fb.field('job' )
        fb.field('telephone' )
        fb.field('email' )
        fb.field('address' )
        fb.field('city_id' )
        fb.field('fiscal_code' )
        fb.field('blood_group_code' )
        fb.field('department_id' )
        fb.br()
        fb.field('journal_request' )
        fb.field('news_request' )
        fb.br()
        fb.simpleTextArea('^.notes', lbl='Notes', colspan=3, width='100%', height='20px')

        right = top.contentPane(region='center')
        right.img(src='^.photo', border='2px dotted silver',
                    crop_width='150px',crop_height='150px',
                    edit=True, 
                    placeholder=True,
                    upload_filename='=#FORM.record.id', 
                    upload_folder='site:donators')

        tc = bc.tabContainer(region='center')
        tc.contentPane(title='Donations').dialogTableHandler(relation='@donations')
        tc.contentPane(title='Analysis').dialogTableHandler(relation='@analysis')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px' )
