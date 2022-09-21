# -*- coding: utf-8 -*-
from odoo import http


class Lucual18Website(http.Controller):

    @http.route('/home', auth='public', website=True)
    def home(self, **kw):
        return http.request.render('lucual18_website.home', {})

    @http.route('/', auth='public', website=True)
    def index(self, **kw):
        return http.request.render('lucual18_website.home', {})

    @http.route('/erp', auth='public', website=True)
    def erp(self, **kw):
        return http.request.render('lucual18_website.erp', {})

    @http.route('/outsourcing', auth='public', website=True)
    def outsourcing(self, **kw):
        return http.request.render('lucual18_website.outsourcing', {})

    @http.route('/software-dev', auth='public', website=True)
    def software_dev(self, **kw):
        return http.request.render('lucual18_website.software_dev', {})

    @http.route('/corporative-image-design', auth='public', website=True)
    def corporative_image_design(self, **kw):
        return http.request.render('lucual18_website.corp_design', {})

    @http.route('/scraping-web', auth='public', website=True)
    def scraping_web(self, **kw):
        return http.request.render('lucual18_website.scraping_web', {})

    @http.route('/automation', auth='public', website=True)
    def automation(self, **kw):
        return http.request.render('lucual18_website.automation', {})

    @http.route('/about', auth='public', website=True)
    def about(self, **kw):
        return http.request.render('lucual18_website.about', {})

    @http.route('/contact', auth='public', website=True)
    def contact(self, **kw):
        return http.request.render('lucual18_website.contact', {})


    @http.route('/thanks-contact', auth='public', website=True)
    def thanks_contact(self, **kw):
        return http.request.render('lucual18_website.thanks_contact', {})
