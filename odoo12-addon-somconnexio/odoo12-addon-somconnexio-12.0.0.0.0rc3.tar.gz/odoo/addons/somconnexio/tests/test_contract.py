from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError


class TestContract(TransactionCase):

    def setUp(self, *args, **kwargs):
        super().setUp(*args, **kwargs)
        self.Contract = self.env['contract.contract']
        self.product_1 = self.env.ref('product.product_product_1')

    def test_create_mobile_contract_with_mobile_service(self):
        self.product_1.categ_id = self.ref("somconnexio.mobile_service")

        vals_contract = {
            'name': 'Test Contract Mobile',
            'partner_id': self.ref("easy_my_coop.res_partner_cooperator_1_demo"),
            'invoice_partner_id': self.ref(
                "easy_my_coop.res_partner_cooperator_1_demo"
            ),
            'contract_category_id': self.ref("somconnexio.mobile"),
            'contract_line_ids': [
                (
                    0,
                    0,
                    {
                        'product_id': self.product_1.id,
                        'name': 'Services from #START# to #END#',
                        'quantity': 1,
                        'recurring_rule_type': 'monthly',
                        'recurring_interval': 1,
                        'date_start': '2018-02-15',
                        'recurring_next_date': '2018-02-22',
                    },
                )
            ],
        }

        contract = self.Contract.create(vals_contract)

        self.assertEqual(contract.contract_category_id.name, 'Mobile')

    def test_create_mobile_contract_with_broadband_service_raise_ValidationError(self):
        self.product_1.categ_id = self.ref("somconnexio.broadband_service")

        vals_contract = {
            'name': 'Test Contract Mobile',
            'partner_id': self.ref("easy_my_coop.res_partner_cooperator_1_demo"),
            'invoice_partner_id': self.ref(
                "easy_my_coop.res_partner_cooperator_1_demo"
            ),
            'contract_category_id': self.ref("somconnexio.mobile"),
            'contract_line_ids': [
                (
                    0,
                    0,
                    {
                        'product_id': self.product_1.id,
                        'name': 'Services from #START# to #END#',
                        'quantity': 1,
                        'recurring_rule_type': 'monthly',
                        'recurring_interval': 1,
                        'date_start': '2018-02-15',
                        'recurring_next_date': '2018-02-22',
                    },
                )
            ],
        }

        self.assertRaises(ValidationError, self.Contract.create, vals_contract)

    def test_more_than_one_invoice_contact_same_parent(self):
        partner_id = self.ref('easy_my_coop.res_partner_cooperator_2_demo')

        invoice_partner_1_args = {
            'name': 'Partner for invoice 1',
            'type': 'invoice'
        }
        invoice_partner_2_args = {
            'name': 'Partner for invoice 2',
            'type': 'invoice'
        }
        self.assertRaises(
            ValidationError,
            self.env['res.partner'].browse(partner_id).write,
            {
                'child_ids': [
                    (0, False, invoice_partner_1_args),
                    (0, False, invoice_partner_2_args)
                ]
            }
        )

    def test_one_invoice_contact_per_partner(self):
        partner_id = self.ref('easy_my_coop.res_partner_cooperator_2_demo')

        invoice_partner_args = {
            'name': 'Partner for invoice 1',
            'type': 'invoice'
        }
        self.assertTrue(
            self.env['res.partner'].browse(partner_id).write({
                'child_ids': [
                    (0, False, invoice_partner_args),
                ]
            })
        )

    def test_service_contact_wrong_type(self):
        partner_id = self.ref('easy_my_coop.res_partner_cooperator_2_demo')
        service_partner = self.env['res.partner'].create({
            'parent_id': partner_id,
            'name': 'Partner not service'
        })
        vals_contract = {
            'name': 'Test Contract Broadband',
            'partner_id': partner_id,
            'service_partner_id': service_partner.id,
            'invoice_partner_id': partner_id,
            'contract_category_id': self.ref("somconnexio.broadband")
        }
        self.assertRaises(
            ValidationError,
            self.env['contract.contract'].create,
            (vals_contract,)
        )

    def test_service_contact_right_type(self):
        partner_id = self.ref('easy_my_coop.res_partner_cooperator_2_demo')
        service_partner = self.env['res.partner'].create({
            'parent_id': partner_id,
            'name': 'Partner service OK',
            'type': 'service'
        })
        vals_contract = {
            'name': 'Test Contract Broadband',
            'partner_id': partner_id,
            'service_partner_id': service_partner.id,
            'invoice_partner_id': partner_id,
            'contract_category_id': self.ref("somconnexio.broadband")
        }
        self.assertTrue(self.env['contract.contract'].create(vals_contract))

    def test_service_contact_wrong_parent(self):
        partner_id = self.ref('easy_my_coop.res_partner_cooperator_2_demo')
        service_partner = self.env['res.partner'].create({
            'parent_id': self.ref('easy_my_coop.res_partner_cooperator_3_demo'),
            'name': 'Partner wrong parent',
            'type': 'service'
        })
        vals_contract = {
            'name': 'Test Contract Broadband',
            'partner_id': partner_id,
            'service_partner_id': service_partner.id,
            'invoice_partner_id': partner_id,
            'contract_category_id': self.ref("somconnexio.broadband")
        }
        self.assertRaises(
            ValidationError,
            self.env['contract.contract'].create,
            (vals_contract,)
        )

    def test_service_contact_wrong_parent_not_broadband(self):
        partner_id = self.ref('easy_my_coop.res_partner_cooperator_2_demo')
        service_partner = self.env['res.partner'].create({
            'parent_id': self.ref('easy_my_coop.res_partner_cooperator_3_demo'),
            'name': 'Partner wrong parent',
            'type': 'service'
        })
        vals_contract = {
            'name': 'Test Contract Broadband',
            'partner_id': partner_id,
            'service_partner_id': service_partner.id,
            'invoice_partner_id': partner_id,
            'contract_category_id': self.ref("somconnexio.mobile")
        }
        self.assertTrue(self.env['contract.contract'].create(vals_contract))

    def test_service_contact_wrong_type_not_broadband(self):
        partner_id = self.ref('easy_my_coop.res_partner_cooperator_2_demo')
        service_partner = self.env['res.partner'].create({
            'parent_id': partner_id,
            'name': 'Partner not service'
        })
        vals_contract = {
            'name': 'Test Contract Broadband',
            'partner_id': partner_id,
            'service_partner_id': service_partner.id,
            'invoice_partner_id': partner_id,
            'contract_category_id': self.ref("somconnexio.mobile")
        }
        self.assertTrue(self.env['contract.contract'].create(vals_contract))
