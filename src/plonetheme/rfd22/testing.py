# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    applyProfile,
    FunctionalTesting,
    IntegrationTesting,
    PloneSandboxLayer,
)
from plone.testing import z2

import plonetheme.rfd22


class PlonethemeRfd22Layer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=plonetheme.rfd22)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'plonetheme.rfd22:default')


PLONETHEME_RFD22_FIXTURE = PlonethemeRfd22Layer()


PLONETHEME_RFD22_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PLONETHEME_RFD22_FIXTURE,),
    name='PlonethemeRfd22Layer:IntegrationTesting',
)


PLONETHEME_RFD22_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PLONETHEME_RFD22_FIXTURE,),
    name='PlonethemeRfd22Layer:FunctionalTesting',
)


PLONETHEME_RFD22_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PLONETHEME_RFD22_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='PlonethemeRfd22Layer:AcceptanceTesting',
)
