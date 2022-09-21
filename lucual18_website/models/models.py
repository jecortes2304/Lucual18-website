# -*- coding: utf-8 -*-

from odoo import models, fields


class Services(models.Model):
    _name = 'lucual18_website.services'

    name = fields.Char()
    description = fields.Html()
