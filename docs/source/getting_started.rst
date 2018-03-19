..
      Copyright 2018 AT&T Intellectual Property.
      All Rights Reserved.

      Licensed under the Apache License, Version 2.0 (the "License"); you may
      not use this file except in compliance with the License. You may obtain
      a copy of the License at

          http://www.apache.org/licenses/LICENSE-2.0

      Unless required by applicable law or agreed to in writing, software
      distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
      WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
      License for the specific language governing permissions and limitations
      under the License.

===============
Getting Started
===============

What is Pegleg?
---------------

Pegleg is a resource that can be used to:

* Create a single site document from artifacts.
* Validate site documents in relation to Deckhand's schema, layeringPolicy,
  etc. See (link to Deckhand validation stuff).

For more information on the documents that Pegleg works on see (link to artifacts)
and (link to authoring strategy)

Basic Usage
-----------

Before using Pegleg, you must install the required packages in src/bin/pegleg

.. code-block:: console

     pip3 install -r requirements.txt

Features
--------

Linting
~~~~~~~

Pegleg can lint documents and provide validation failures via the CLI. See
(link). It is assumed that all documents will go through linting prior to being
collected to create a site document.

Creating a Site Document
~~~~~~~~~~~~~~~~~~~~~~~~

Pegleg can take the artifact that contains all of the site information and
create a single .yaml file that is consumable by UCP.


All of Pegleg's features can be used through the CLI. See (link to cli) for more
information.
