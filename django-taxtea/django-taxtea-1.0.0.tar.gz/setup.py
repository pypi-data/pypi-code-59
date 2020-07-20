# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['taxtea', 'taxtea.migrations', 'taxtea.services']

package_data = \
{'': ['*'], 'taxtea': ['fixtures/*']}

install_requires = \
['django-localflavor>=3.0.1,<4.0.0',
 'django>=3.0.5,<4.0.0',
 'httpx>=0.13.3,<0.14.0',
 'xmltodict>=0.12.0,<0.13.0']

entry_points = \
{'console_scripts': ['build_docs = docs:makedocs']}

setup_kwargs = {
    'name': 'django-taxtea',
    'version': '1.0.0',
    'description': 'Django TaxTea - A Django app that provides up-to-date tax rates for SaaS.',
    'long_description': '# Django TaxTea\n\nDjango App that calculates tax rates for SaaS products\n\nTaxes are hard. That shouldn\'t stop you from building your dreams. TaxTea does the heavy lifting and tells you exactly what sales tax, if any, you need to be charging your customers.\n\n> Currently only supporting US 🇺🇸\n\n## Installation\n\n```bash\npip install django-taxtea\n```\n\n## Getting Started\n\nAdd the following to your Django settings:\n\n```python\nTAXTEA_USPS_USER = "XXXXXXXX"           # required\nTAXTEA_AVALARA_USER = "XXXXXXXX"        # required\nTAXTEA_AVALARA_PASSWORD = "XXXXXXXX"    # required\nTAXTEA_NEXUSES = [("AZ", "12345"),]     # required\nTAXTEA_TAX_RATE_INVALIDATE_INTERVAL = 7 # optional, default is 7 (days)\n```\n\n## Required Accounts & Information\n\n### USPS\n\nTaxTea uses the USPS web service API to find states for Zip Codes. You\'ll need to register for a free account [here.](https://www.usps.com/business/web-tools-apis/)\n\n**NOTE: TaxTea only needs the USPS user, not the password.**\n\n### Avalara\n\nTaxTea relies on Avalara for getting up-to-date tax rates for Zip Codes. The Avalara website can be confusing, but to register simply hit the API endpoint documented [here.](https://developer.avalara.com/api-reference/avatax/rest/v2/methods/Free/RequestFreeTrial/)\n\n### Nexuses\n\nYour `TAXTEA_NEXUSES` are any place where your company has a presence. For example, every company has a nexus where they incorporated. We require there to be at least one item in this list, which is your physical incorporation state/zip.\n\nNexuses are part of the equation of how TaxTea calculates sales tax.\n\nThe determination of [sales tax sourcing](https://www.avalara.com/us/en/blog/2019/02/sales-tax-sourcing-how-to-find-the-right-rule-for-every-transaction.html) is predicated on whether a given state\'s model for taxation is:\n\n- Origin-based, or\n- Destination-based\n\nFor example, if your incorporation state is an _Origin-based_ state and a customer purchases your product who also lives in that state, it is the nexus\' Zip Code that is used to determine the tax rate, not the customer\'s location.\n\n_Destination-based_ sales tax means that the sales tax will be charged at the rate of the customer location. This is applicable for out of state transactions and transactions within a state that is not an Origin-based.\n\nWant to learn more? Here\'s a great article about [Origin vs. Destination-based Sales tax](https://blog.taxjar.com/charging-sales-tax-rates/) from Tax Jar.\n\n## Usage\n\nAdd to `INSTALLED_APPS`:\n\n```python\nINSTALLED_APPS = [\n    ...,\n    "taxtea"\n]\n```\n\nRun migrations:\n\n```python\npython manage.py migrate\n```\n\n## Getting Tax Rates\n\nImport the ZipCode model:\n\n```python\nfrom taxtea.models import ZipCode\n\n# Get the ZipCode Object from the database\n# If no object exists for this Zip Code, it will create one by\n# fetching data from the USPS API and storing it in the database.\n# At this point, there will be no `tax_rate` associated with it.\n\nzip_code = ZipCode.get("90210")\n\n# The `applicable_tax_rate` property is the workhorse of TaxTea.\n# It will fetch & store a tax rate from the Avalara API and then\n# use your tax nexuses to determine which tax rate is applicable.\n\ntax_rate = zip_code.applicable_tax_rate\n# Returns a Decimal object that will look like `0.0625`\n\n# For convenience, there is a classmethod to convert to a percent.\n\npercentage = ZipCode.tax_rate_to_percentage(tax_rate)\n# Returns a Decimal object that will look like `6.25`\n\n```\n\n## Docs\n\nRead the [docs](https://www.djangotaxtea.com).\n\n\n## Resources\n\nTaxTea uses a list provided by taxjar to populate the states and their tax collection methods.\n\n- [SaaS Sales Tax](https://blog.taxjar.com/saas-sales-tax/)\n- [Origin / Destination States](https://blog.taxjar.com/charging-sales-tax-rates/)\n',
    'author': 'Matt Strayer',
    'author_email': 'git@mattstrayer.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/lowercase-app/django-taxtea',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8.0,<4.0.0',
}


setup(**setup_kwargs)
