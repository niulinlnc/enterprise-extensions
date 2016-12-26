# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2015  ADHOC SA  (http://www.adhoc.com.ar)
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Transindar Personalization',
    'category': 'Stock',
    'version': '9.0.2.0.0',
    'description': """
Transindar Personalization
==========================
    """,
    'author': 'ADHOC SA',
    'website': 'www.adhoc.com.ar',
    'license': 'AGPL-3',
    'depends': [
        'sale_stock_availability',
        'product_brand',
        'product_website_categ_search',
        'product_category_full_name_search',
        'product_internal_code',
        'partner_internal_code',
        'sale_three_discounts',
        'sale_order_validity',
        'sale_global_discount',
        'l10n_ar_account',
        'sale_quotation_products',
        # 'partner_no_auto_search',
        # 'product_no_auto_search',
        # no migrados todavia
        # 'stock_picking_list',
        # 'account_invoice_prices_update',
        # 'product_template_tree_prices',
        # 'account_invoice_control',
        # no se migran
        # 'sale_order_dates',
        # AGREGADOS POR JUAN
        'account_accountant',
        'l10n_ar_afipws_fe',
        'account_debt_management',
        'account_move_helper',
        # si lo queremos hay que agregar repo
        # 'account_multic_fix',
        'account_no_translation',
        'base_currency_inverse_rate',
        'account_clean_cancelled_invoice_number',
        'account_invoice_change_currency',
        'account_invoice_commercial',
        'account_invoice_company_search',
        'account_invoice_journal_group',
        'account_invoice_prices_update',
        'account_invoice_tax_wizard',
        'l10n_ar_aeroo_einvoice',
        'l10n_ar_aeroo_purchase',
        'l10n_ar_aeroo_sale',
        'l10n_ar_aeroo_stock',
        'l10n_ar_aeroo_payment_group',
        'l10n_ar_padron_afip',
        'l10n_ar_bank',
        'product_catalog_aeroo_report_public_categ',
        'product_no_translation',
        'product_price_currency',
        'product_pricelist',
        'product_price_taxes_included',
        'product_sale_price_by_margin',
        'product_template_search_by_barcode',
        'purchase_quotation_products',
        'sale_exception_credit_limit',
        'sale_exception_partner_state',
        'sale_exception_price_security',
        'sale_quotation_products',
        # 'purchase_discount',
        'stock_inventory_preparation_filter',
        'base_state_active',
        # 'sale_procurement_date_confirm',
        # 'hr_attendance',
        'base_technical_features',
    ],
    'data': [
        'security/security.xml',
        'sale_order_view.xml',
        'product_view.xml',
        'account_payment_view.xml',
        'category_public_view.xml',
        'category_public_view.xml',
        'invoice_view.xml',
        # 'res_partner_view.xml',
        'stock_picking_view.xml',
        'res_company_view.xml'
    ],
    'demo': [
        # 'demo/load_es_lang.yml',
    ],
    'test': [],
    'installable': True,
    'auto_install': False,
    'application': False,
}
