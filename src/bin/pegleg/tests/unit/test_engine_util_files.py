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

from pegleg import config
from pegleg.engine.util import files

def test_no_non_yamls():
    # Non YAML has been added to the directory
    config.set_primary_repo('../pegleg/site_yamls/')
    results = files.all()
    # make sure only YAML files are returned
    for i in results:
        assert i.endswith('.yaml')
