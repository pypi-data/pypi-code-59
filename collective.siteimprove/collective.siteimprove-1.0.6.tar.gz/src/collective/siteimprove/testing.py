# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import collective.siteimprove


class CollectiveSiteimproveLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=collective.siteimprove)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.siteimprove:default')


COLLECTIVE_SITEIMPROVE_FIXTURE = CollectiveSiteimproveLayer()


COLLECTIVE_SITEIMPROVE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_SITEIMPROVE_FIXTURE,),
    name='CollectiveSiteimproveLayer:IntegrationTesting',
)


COLLECTIVE_SITEIMPROVE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_SITEIMPROVE_FIXTURE,),
    name='CollectiveSiteimproveLayer:FunctionalTesting',
)


COLLECTIVE_SITEIMPROVE_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_SITEIMPROVE_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='CollectiveSiteimproveLayer:AcceptanceTesting',
)
