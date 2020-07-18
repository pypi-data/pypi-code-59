# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['impersonate_permissions', 'impersonate_permissions.migrations']

package_data = \
{'': ['*'], 'impersonate_permissions': ['templates/impersonate_permissions/*']}

install_requires = \
['django-impersonate>=1.5.1,<2.0.0', 'django>=2.2,<4.0']

setup_kwargs = {
    'name': 'django-impersonate-permissions',
    'version': '0.3',
    'description': 'Django app that tracks user permssions when using django-impersonate.',
    'long_description': '# Django Impersonate Permissions\n\nAdd ability to control impersonate permissions.\n\nImpersonate is a powerful Django app that allow site admins to log in to a user\'s account, and take\nactions on their behalf. This can be invalulable in providing technical support. However, with great\npower comes great responsiblity, and operationally you should **never** impersonate a user without\ntheir explicit consent.\n\nThis app provides a mechanism for recording user consent, and enforcing it.\n\n## How it works\n\nThe core concept is the "permission window". This is a time period during which the user has granted\naccess to their account. How you determine when to ask for access is up to you - this library makes\nno assumptions about that.\n\nThe starting point is saving a new `PermissionWindow` object:\n\n```python\n# views.py\ndef grant_permission(request):\n    """Create a new PermissionWindow, allowing the user to be impersonated."""\n    window = PermissionWindow.objects.create(user=request.user)\n    return HttpResponse("OK")\n```\n\nOnce you have an active PermissionWindow, the user will appear in the `users_impersonable` queryset.\nWhilst you are impersonating a user, the middleware will check that the permissions window is still\nvalid. If it expires (or is disabled), the middleware will redirect the request to the\n`impersonate-stop` URL, effectively logging the impersonator out of the impersonation session.\n\n## Use\n\nThe app itself contains a model, `PermissionWindow`, that is use to record a user\'s permission, and\na middleware class, `ImpersonatePermissionsMiddleware` that is used to enforce it.\n\nYou will need to add the middleware to your `MIDDLEWARE` Django settings. It also contains a\nfunction `users_impersonable` that you should set to the as the impersonate `CUSTOM_USER_QUERYSET`\nfunction:\n\n```python\n# settings.py\nINSTALLED_APPS = (\n    "django.contrib.admin",\n    "django.contrib.auth",\n    "django.contrib.contenttypes",\n    "django.contrib.sessions",\n    "django.contrib.messages",\n    "django.contrib.staticfiles",\n    "django.contrib.humanize",\n    "impersonate",\n    "impersonate_permissions",\n    ...\n)\n\nMIDDLEWARE = (\n    "django.contrib.sessions.middleware.SessionMiddleware",\n    "django.middleware.common.CommonMiddleware",\n    "django.middleware.csrf.CsrfViewMiddleware",\n    "django.contrib.auth.middleware.AuthenticationMiddleware",\n    "django.contrib.messages.middleware.MessageMiddleware",\n    "impersonate.middleware.ImpersonateMiddleware",\n    "impersonate_permissions.middleware.ImpersonatePermissionsMiddleware",\n    ...\n)\n\nIMPERSONATE = {\n    "CUSTOM_USER_QUERYSET": "impersonate_permissions.models.users_impersonable"\n}\n```\n\n## Settings\n\nThe following settings can be set in the Django settings module, as part of the `IMPERSONATE`\ndictionary.\n\n**DEFAULT_PERMISSION_EXPIRY**\n\nAn integer value that defines the default length of a permission \'window\', in minutes, thereby\nsetting its expiry.\n\nDefault value is 60 - which equates to a one hour window.\n\n**DISPLAY_PERMISSION_MESSAGES**\n\nA bool value that controls whether the middleware should add messages using the Django messages\nframework. If True, a message is set whilst impersonating, and another is set when a\nPermissionWindow has expired, and the impersonation session cut.\n\nDefault value is `True`\n\n**PERMISSION_EXPIRY_WARNING_INTERVAL**\n\nAn integer value which is used to turn the impersation message level from `INFO` to `WARNING`. Value\nis in minutes.\n\nDefault value is 10, which means that the message will change 10 minutes before the session expires.\n\n## License\n\nMIT.\n\n## Contributing\n\nIf you want to contribute, add features, fix bugs - thank you.\n\nThe project uses Poetry to handle dependencies, and it comes will a working Django project that you\ncan use for testing.\n\n### Tests\n\nTo begin, it\'s best to install the virtualenv and check that the tests run:\n\n```shell\n$ poetry install\n$ poetry run pytest\n```\n\nOnce you have a working test run, you can set up the project locally (it uses SQLite), create a\nsuperuser account, and spin up the site:\n\n```shell\n$ poetry shell\n(venv) $ python manage.py migrate\n(venv) $ python manage.py createsuperuser\n(venv) $ python manage.py runserver\n```\n\n### Code style\n\nThe project contains a `pre-commit` config, and you should set this up before committing any code:\n\n```shell\n$ pre-commit install\n```\n\nCode must be formatted using `isort` and `black`.\n\nAll new code should use type hints.\n\n### CI\n\nThe project contains a `.travis.yml` config, and the tests will run on any new PR. This config runs\nthe tests and a suite of linting / formatting tools: `isort`, `black`, `pylint`, `flake8` (with\n`bandit` and `pydocstyle`) and `mypy`.\n',
    'author': 'YunoJuno',
    'author_email': 'code@yunojuno.com',
    'maintainer': 'YunoJuno',
    'maintainer_email': 'code@yunojuno.com',
    'url': 'https://github.com/yunojuno/django-impersonate-permissions',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
