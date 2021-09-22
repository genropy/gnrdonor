# encoding: utf-8


class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('donator',pkey='id',name_long='Donator',name_plural='Donators',caption_field='fullname')
        self.sysFields(tbl)
        tbl.column('name',name_long='Name')
        tbl.column('surname',name_long='Surname')
        tbl.column('birthplace_id',size='22',name_long='Birthplace').relation('glbl.comune.id',relation_name='donators_by_birthplace', mode='foreignkey', onDelete='raise')
        tbl.column('gender',name_long='Gender', values='M:Male,F:Female')
        tbl.column('birthdate',dtype='D',name_long='Birthdate')
        tbl.column('telephone',name_long='Telephone')
        tbl.column('email',name_long='E-mail')
        tbl.column('job',name_long='Job')
        tbl.column('journal_request',dtype='B',name_long='Journal request')
        tbl.column('news_request',dtype='B',name_long='News request')
        tbl.column('address',name_long='Address')
        tbl.column('city_id',size='22',name_long='City').relation('glbl.comune.id',relation_name='donators_by_city', mode='foreignkey', onDelete='raise')
        tbl.column('fiscal_code',size='16',name_long='Fiscal code')
        tbl.column('blood_group_code',size=':3',name_long='Blood Group').relation('donator_blood_group.code',relation_name='donators', mode='foreignkey', onDelete='raise')
        tbl.column('department_id',size='22',name_long='Department').relation('department.id',relation_name='donators', mode='foreignkey', onDelete='raise')
        tbl.column('notes',name_long='Notes')

        tbl.formulaColumn('fullname', "$surname||' '||$name", name_long='Fullname')
        tbl.formulaColumn('first_donation_date', select=dict(table='donor.donation', columns='$date',
                                                                where='$donator_id=#THIS.id',
                                                                order_by='$date ASC', limit=1),
                                                                dtype='D', name_long='First donation date')
        tbl.formulaColumn('last_donation_date', select=dict(table='donor.donation', columns='$date',
                                                                where='$donator_id=#THIS.id',
                                                                order_by='$date DESC', limit=1),
                                                                dtype='D', name_long='Last donation date')
        tbl.formulaColumn('is_active', "CASE WHEN $last_donation_date > NOW() - INTERVAL '365 DAYS' THEN TRUE ELSE FALSE END",
                                                                dtype='B', name_long='Is active')
        tbl.formulaColumn('donations_number', select=dict(table='donor.donation', columns='COUNT(*)',
                                                                where='$donator_id=#THIS.id'),
                                                                dtype='I', name_long='Donations number')                                                        
        