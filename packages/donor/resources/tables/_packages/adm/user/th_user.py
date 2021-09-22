# -*- coding: utf-8 -*-

# th_user.py
# Created by Saverio Porcari on 2011-03-13.
# Copyright (c) 2011 Softwell. All rights reserved.

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method


class View(BaseComponent):
    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('is_active', semaphore=True)
        r.fieldcell('department_id')
        r.fieldcell('username',name='Username',width='10em')
        r.fieldcell('fullname',name='Fullname',width='20em')
        r.fieldcell('group_code')
        r.fieldcell('email',name='Email',width='20em')
        r.fieldcell('@tags.@tag_id.code',name='Tags',width='100%')
        r.fieldcell('auth_tags',name='Old tags',width='15em')
        
        
    def th_order(self):
        return 'department_id'
        
    def th_query(self):
        return dict(column='username',op='contains', val='')