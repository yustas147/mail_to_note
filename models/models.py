# -*- coding: utf-8 -*-
#from openerp.osv import osv
from openerp import api, models, fields
#from datetime import datetime
#from openerp import tools
#import logging

#_mylog = logging.getLogger('YUSTAS#################################################')


class note_note(models.Model):
    _inherit = 'note.note'
    
    mess_id = fields.Many2one('mail.message', string='Created from:')
    
    @api.multi
    def open_mess(self):
        if self.mess_id:
#            _mylog.info("Mess id is %s" % (self.mess_id.id))
            return {
                'type': 'ir.actions.client',
                'tag': 'mail.wall',
                'res_model': 'mail.message',
                'params': {
                            'domain':[('id','=',self.mess_id.id)],
                            'truncate_limit':10,
                            'display_intended_thread':1,
                           },
               } 
    

class mail_message(models.Model):

    _inherit = 'mail.message'
    
    @api.multi
    def create_note(self):
#        _mylog.info('Need to create NOTE!')
        self.res_id = self.env['note.note'].create({'name':self.subject, 'memo':self.body, 'mess_id':self.id})
