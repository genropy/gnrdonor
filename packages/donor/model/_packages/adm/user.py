# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('user')

        tbl.column('department_id', size='22', name_long='Department').relation('donor.department.id',
                        relation_name='user', mode='foreignkey', onDelete='raise')    
        tbl.column('is_active', dtype='B', name_long='Is active')    