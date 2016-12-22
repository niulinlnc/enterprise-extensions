# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in module root
# directory
##############################################################################
from openerp import fields, models, api
from openerp.osv import expression


class ProductTemplate(models.Model):

    _inherit = 'product.template'

    supplier_code = fields.Char(
        related='seller_ids.product_code', string="Supplier Code")
    location_1 = fields.Char(String='Location 1')
    location_2 = fields.Char(String='Location 2')
    quantity_per_pack = fields.Char(String='Cantidad por Pack')
    stk_tmp_ros = fields.Char('S. Rosario')
    stk_tmp_sfe = fields.Char('S. Santa Fe')
    stk_tmp_raf = fields.Char('S. Rafaela')
    next_deactivate = fields.Date('Next Deactivate')

    @api.model
    def name_search(
            self, name, args=None, operator='ilike', limit=100):
        recs = self.search(self._get_search_domain(
            name, args=args, operator=operator, limit=limit), limit=limit)
        return recs.name_get()

    @api.model
    def _get_search_domain(
            self, name, args=None, operator='ilike', limit=100):
        if not args:
            args = []
        if name:
            # if we found exact internal_code we return it
            if self.search(
                    [('internal_code', '=ilike', name)], limit=limit):
                return [('internal_code', '=ilike', name)] + args

            # if we found exact default_code we return it
            elif self.search(
                    [('default_code', '=ilike', name)], limit=limit):
                return [('default_code', '=ilike', name)] + args

            # else we return custom search
            else:
                return [
                    '|', '|', ('name', 'ilike', name),
                    ('product_brand_id.name', 'ilike', name),
                    ('supplier_code', 'ilike', name)] + args
        return args

    @api.model
    def _search_custom_search(self, operator, value):
        # base_domain = args or []
        # base_domain = []
        # name = value
        fields_names = ['name', 'product_brand_id', 'supplier_code']
        exact_fields_names = ['internal_code', 'default_code']
        # if we found exact default_code we return it
        for exact_field_name in exact_fields_names:
            recs = self.search([(exact_field_name, '=ilike', value)])
            # TODO que hacemos, buscamos tmb por estos si no esexato igual?
            if recs:
                return [(exact_field_name, '=ilike', value)]


        # if len(fields_names) > 1:
        #     word_domain = ['|']
        # else:
        #     word_domain = []

        # words = value.split(',')
        # if len(words) > 1:
        #     domain = ['&']
        # else:
        #     domain = []

        # Try regular search on each additional search field
        # for rec_name in all_names[1:]:
        #     domain = [(rec_name, operator, name)]
        #     res = base_domain + domain
        #     print 'res1', res
        # # Try ordered word search on each of the search fields
        # for rec_name in all_names:
        #     domain = [(rec_name, operator, name.replace(' ', '%'))]
        #     res = base_domain + domain
        #     print 'res3', res
        # Try unordered word search on each of the search fields
        domain = []
        for word in value.split(','):
            word_domain = []
            # domain = [(word, operator, x) for x in all_names]
            for field_name in fields_names:
                # word_domain = [(word, operator, field_name)]
                word_domain = (
                    word_domain and ['|'] + word_domain or word_domain
                ) + [(field_name, operator, word)]
            print 'res3', word_domain
            # for x in range(len(domain) - 1):
            #     domain = ['|'] + domain
            # if base_domain
            # domain = domain + word_domain
            domain = (domain and ['&'] + domain or domain) + word_domain
            print 'res3', domain
        print 'res', domain


        # for rec_name in all_names:
        #     domain = [(rec_name, operator, x)
        #               for x in name.split() if x]
        #     print 'res3', domain
        #     for x in range(len(domain)-1):
        #         domain = ['&'] + domain
        #     # if base_domain
        #     base_domain = (base_domain and ['|'] + base_domain or base_domain) + domain
        #     print 'res3', base_domain
        # print 'res', base_domain


            # for x in range(len(domain)-1):
            #     domains += ['&'] + domain
        # recs = ['|', '|', ('name', 'ilike', value),
        #         ('product_brand_id.name', 'ilike', value),
        #         ('supplier_code', 'ilike', value)]
        return domain

    @api.multi
    def _get_custom_search(self):
        return False

    custom_search = fields.Char(
        compute='_get_custom_search',
        string='Busqueda Inteligente',
        search='_search_custom_search'
    )

    @api.multi
    def get_invoice_analisis(self):
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'account.invoice.line.report',
            'view_mode': 'tree,graph',
            'view_type': 'form',
            'context': {
                'search_default_product_id': self.product_variant_ids[0].id},
        }


class ProductProduct(models.Model):
    _inherit = 'product.product'

    supplier_code = fields.Char(
        related='seller_ids.product_code', string="Supplier Code")
    location_1 = fields.Char(
        related='product_tmpl_id.location_1', String='Location 1')
    location_2 = fields.Char(
        related='product_tmpl_id.location_2', String='Location 2')

    @api.multi
    def get_invoice_analisis(self):
        context = {
            'search_default_product_id': self.id,
            'search_default_partner_id': self._context.get(
                'partner_id', False)}

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'account.invoice.line.report',
            'view_mode': 'tree,graph',
            'view_type': 'form',
            'context': context,
        }

    @api.model
    def name_search(
            self, name, args=None, operator='ilike', limit=100):
        recs = self.search(self._get_search_domain(
            name, args=args, operator=operator, limit=limit), limit=limit)
        return recs.name_get()

    @api.model
    def _get_search_domain(
            self, name, args=None, operator='ilike', limit=100):
        if not args:
            args = []
        if name:
            # if we found exact internal_code we return it
            if self.search(
                    [('internal_code', '=ilike', name)], limit=limit):
                return [('internal_code', '=ilike', name)] + args

            # if we found exact default_code we return it
            elif self.search(
                    [('default_code', '=ilike', name)], limit=limit):
                return [('default_code', '=ilike', name)] + args

            # else we return custom search
            else:
                return [
                    '|', '|', ('name', 'ilike', name),
                    ('product_brand_id.name', 'ilike', name),
                    ('supplier_code', 'ilike', name)] + args

        return args

    @api.model
    def _search_custom_search(self, operator, value):
        recs = ['|', '|', ('name', 'ilike', value),
                ('product_brand_id.name', 'ilike', value),
                ('supplier_code', 'ilike', value)]
        return recs

    @api.multi
    def _get_custom_search(self):
        return False

    custom_search = fields.Char(
        compute='_get_custom_search',
        string='Busqueda Inteligente',
        search='_search_custom_search'
    )
