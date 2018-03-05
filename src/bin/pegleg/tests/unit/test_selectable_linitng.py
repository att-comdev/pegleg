# Copyright 2018 AT&T Intellectual Property.  All other rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from mock import patch

from pegleg import config
from pegleg.engine import lint


def test_lint_excludes():
    exclude_lint = ['P001', 'P002', 'P003']

    # For P002
    with patch.object(lint,'_verify_deckhand_render') as mock_method:
        lint.full(False, exclude_lint,[])
    mock_method.assert_not_called()

    # For P003
    with patch.object(lint,'_verify_no_unexpected_files') as mock_method:
        lint.full(False, exclude_lint,[])
    mock_method.assert_not_called()

def test_lint_warns():
    warn_lint = ['P001', 'P002', 'P003']
    # TODO: need to set priary repo
    config.set_primary_repo(primary_repo)
    #For P002
    with patch.object(lint,'_verify_deckhand_render') as mock_method:
        lint.full(False, [], warn_lint)
    mock_method.assert_called()
