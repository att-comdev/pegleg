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

from __future__ import absolute_import
import tempfile

import pytest

from pegleg import config


@pytest.fixture()
def create_tmp_deployment_files(tmpdir):
    revision = "v1.0"
    site_types = ["cicd", "lab"]
    site_definitions = []
    fake_site_names = ["secrets", "software"]

    for site_type in site_types:
        site_definition = """
---
data:
  revision: %s
  site_type: %s
metadata:
  layeringDefinition: {abstract: false, layer: site}
  name: %s
  schema: metadata/Document/v1
  storagePolicy: cleartext
schema: pegleg/SiteDefinition/v1
...
""" % (revision, site_type, site_type)
        site_definitions.append(site_definition)

    p = tmpdir.mkdir("deployment_files")
    # Create global directory.
    g = p.mkdir("global")
    # Create global/common directory with global-common.yaml.
    g.mkdir("common").join("global-common.yaml").write("fake-global-common")
    # Create global/v1.0 directory with global-v1.0.yaml.
    g.mkdir(revision).join("global-%s.yaml" % revision).write(
        "fake-global-%s" % revision)

    # Create type directory.
    t = p.mkdir("type")
    # Create type/cicd and type/lab directories.
    for site_type in site_types:
        t1 = t.mkdir(site_type)
        # Create type/cicd/common/type-common.yaml.
        t1.mkdir("common").join("type-common.yaml").write("fake-type-common")
        # Create type/cicd/v1.0/type-v1.0.yaml.
        t1.mkdir(revision).join("type-%s.yaml" % revision).write(
            "fake-type-%s" % revision)

    s = p.mkdir("site")
    for idx, site_type in enumerate(site_types):
        site_name = fake_site_names[idx]
        # Create site directory and site/cicd.
        s1 = s.mkdir(site_type)
        s1.join("site-definition.yaml").write(site_definitions[idx])
        s1.mkdir(site_name).join("%s.yaml" % site_name).write(
            "fake-%s" % site_name)

    orig_primary_repo = config.get_primary_repo()
    config.set_primary_repo(str(tmpdir.listdir()[0]))

    yield

    config.set_primary_repo(orig_primary_repo)
