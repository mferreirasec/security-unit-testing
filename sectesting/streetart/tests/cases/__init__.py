# -*- coding: utf-8 -*-
from __future__ import absolute_import

from .auth import (
    AuthenticationEnforcementTestCase,
)

from .dos import (
    AdminViewRequestIsSuccessfulTestCase,
    RegularViewRequestIsSuccessfulTestCase,
)

from .headers import (
    HeaderKeyExistsTestCase,
    HeaderKeyNotExistsTestCase,
    HeaderValueAccurateTestCase,
)

from .hidden import (
    RegularUnknownMethodsTestCase,
)

from .requestor import (
    ViewHasRequestorTestCase,
)
