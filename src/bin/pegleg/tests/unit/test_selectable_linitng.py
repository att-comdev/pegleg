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
import click
import mock

from pegleg import config
from pegleg.engine import lint


@mock.patch.object(lint, '_verify_deckhand_render', return_value=[])
def test_lint_excludes_P001(*args):
    exclude_lint = ['P001']
    config.set_primary_repo('../pegleg/site_yamls/deployment_files/')
    results=''
    try:
        results = lint.full(False, exclude_lint,[])
    except click.ClickException as e:
        pass
        # TODO: need to make sure expected error is not in errors list
        # how do I change sorage_policy to cleartext so it will fail?


def test_lint_excludes_P002():
    exclude_lint = ['P002']
    config.set_primary_repo('../pegleg/site_yamls/deployment_files/')
    # For P002
    with mock.patch.object(lint,'_verify_deckhand_render') as mock_method:
        try:
            lint.full(False, exclude_lint,[])
        except click.ClickException:
            pass

    mock_method.assert_not_called()


@mock.patch.object(lint, '_verify_deckhand_render', return_value=[])
def test_lint_excludes_P003(*args):
    exclude_lint = ['P003']
    with mock.patch.object(lint,'_verify_no_unexpected_files') as mock_method:
        try:
            lint.full(False, exclude_lint,[])
        except click.ClickException:
            pass

    mock_method.assert_not_called()


@mock.patch.object(lint, '_verify_deckhand_render', return_value=[])
@mock.patch.object(lint, '_verify_no_unexpected_files', return_value=[])
def test_lint_warns_P001(*args):
    warn_lint = ['P001']
    config.set_primary_repo('../pegleg/site_yamls/deployment_files/')

    try:
        results = lint.full(False, [], warn_lint)
    except click.ClickException as e:
        pass
        # TODO: need to make sure expected error is in errors list
        # how do I change sorage_policy to cleartext so it will fail?


def test_lint_warns_P002():
    warn_lint = ['P002']
    config.set_primary_repo('../pegleg/site_yamls/deployment_files/')

    with mock.patch.object(lint,'_verify_deckhand_render') as mock_method:
        try:
            lint.full(False, [], warn_lint)
        except click.ClickException:
            pass

    mock_method.assert_called()


@mock.patch.object(lint, '_verify_deckhand_render', return_value=[])
def test_lint_warns_P003(*args):
    warn_lint = ['P003']
    config.set_primary_repo('../pegleg/site_yamls/deployment_files/')

    with mock.patch.object(lint,'_verify_no_unexpected_files') as mock_method:
        try:
            lint.full(False, [], warn_lint)
        except click.ClickException:
            pass

    mock_method.assert_called()
