# Security POC

This is to confirm the [adding-global-where](https://docs.sqlalchemy.org/en/14/orm/session_events.html#adding-global-where-on-criteria) functionality.  See also [the examples](https://docs.sqlalchemy.org/en/14/orm/query.html#sqlalchemy.orm.with_loader_criteria).

## Setup and Test

To run:

1. Open [this repository](https://github.com/valhuber/security-poc) in codespaces

    * Takes about a minute; wait until the Ports tab shows up

2. Start the server, using the provided Launch Configuration

3. Issue this in the codespaces (_not_ your local machine) terminal window:

```
curl -X 'GET' \
'http://localhost:5656/api/Category/?fields%5BCategory%5D=Id%2CCategoryName%2CDescription&page%5Boffset%5D=0&page%5Blimit%5D=10&sort=id' -H 'accept: application/vnd.api+json' -H 'Content-Type: application/vnd.api+json'
```

&nbsp;

## Active Code

See `api_logic_server_run.py`, around line 400 >> `security/security_sys.py`.

&nbsp;

## Design Notes

<figure><img src="https://github.com/valhuber/security-poc/blob/main/doc/images/basic-design.png?raw=true"></figure>



&nbsp;

## Status

Now initally running, per [this support](https://github.com/sqlalchemy/sqlalchemy/discussions/8976).

&nbsp;

----
> Standard API Logic Server readme follows (ignore)

&nbsp;


# Tutorial Setup

OK, your project is created and open.  You must _Establish Your Python Environment_ to run the Tutorial.

1.  Execute the __Setup and Run__ procedure below, then 
2. [Open the Tutorial](Tutorial.md)

The standard API Logic Project Readme is included, below.

&nbsp;

---

&nbsp;

&nbsp;
# Readme - API Logic Project

This API Logic Project was created by the API Logic Server with the `ApiLogicServer create` command.  

Edit / extend this readme as desired.

&nbsp;&nbsp;

# Setup and Run

To run your project, the system requires various runtime systems for data access, api, and logic.  These are [included with API Logic Server](https://valhuber.github.io/ApiLogicServer/Architecture-What-Is/).  So, to run your project:

1.  __Establish your Python Environment__ to activate these runtime systems
    * Choose the __either__ the _Local Install_ __or__ the _Docker_ approach below, then 
2. __Run__


&nbsp;

## Establish Your Python Environment - Local Install

You `requirements.txt` has already been created, so...

```bash title="Install API Logic Server in a Virtual Environment"
python -m venv venv                        # may require python3 -m venv venv
venv\Scripts\activate                      # mac/linux: source venv/bin/activate
python -m pip install -r requirements.txt  # accept "new Virtual environment"
```

Notes:

* See also the `venv_setup` directory in this API Logic Project.

* If using SqlServer, install `pyodbc`.  Not required for docker-based projects.  For local installs, see the [Quick Start](https://valhuber.github.io/ApiLogicServer/Install-pyodbc/).

&nbsp;

## Establish Your Python Environment - Docker

Your runtime systems are part of Dev Container, which you probably activated when you [opened the project](https://valhuber.github.io/ApiLogicServer/IDE-Execute/).  If you did not accept the "Open in Container" option when you started VSCode, use __View > Command Palette > Remote-Containers: Reopen in Container__.

&nbsp;

## Run

To run your project:

* **Start the API**, either by __IDE launch configurations__ (see below), or by command line: `python api_logic_server_run.py`.

* **Open the Admin App -** either

    * Open your Browser at [http://localhost:5656](http://localhost:5656), or 
    
    * Open in VSCode's Simple Browser (as shown below):

        1. Click __View > Command__ to open the Command Palette
            * Enter command: `Simple Browser: Show`
            * Specify the URL: `http://localhost:5656`
        2. Explore the swagger - open another simple Browser with URL `http://localhost:5656/api` 
            * Note: you can drag windows to arrange your viewing area

<figure><img src="https://github.com/valhuber/apilogicserver/wiki/images/ui-admin/run-admin-app.png?raw=true"></figure>

&nbsp;&nbsp;

# Project Information

| About                    | Info                               |
|:-------------------------|:-----------------------------------|
| Created                  | December 11, 2022 08:31:58                      |
| API Logic Server Version | 6.04.05           |
| Created in directory     | ../../servers/ApiLogicProject |
| API Name                 | api          |

&nbsp;&nbsp;


# Key Technologies

API Logic Server is based on the projects shown below.
Consult their documentation for important information.

### SARFS JSON:API Server

[SAFRS: Python OpenAPI & JSON:API Framework](https://github.com/thomaxxl/safrs)

SAFRS is an acronym for SqlAlchemy Flask-Restful Swagger.
The purpose of this framework is to help python developers create
a self-documenting JSON API for sqlalchemy database objects and relationships.

These objects are serialized to JSON and 
created, retrieved, updated and deleted through the JSON API.
Optionally, custom resource object methods can be exposed and invoked using JSON.

Class and method descriptions and examples can be provided
in yaml syntax in the code comments.

The description is parsed and shown in the swagger web interface.
The result is an easy-to-use
swagger/OpenAPI and JSON:API compliant API implementation.

### LogicBank

[Transaction Logic for SQLAlchemy Object Models](https://valhuber.github.io/ApiLogicServer/Logic-Why/)

Use Logic Bank to govern SQLAlchemy update transaction logic - 
multi-table derivations, constraints, and actions such as sending mail or messages. Logic consists of _both:_

*   **Rules - 40X** more concise using a spreadsheet-like paradigm, and

*   **Python - control and extensibility,** using standard tools and techniques

Logic Bank is based on SQLAlchemy - it handles `before_flush` events to enforce your logic.
Your logic therefore applies to any SQLAlchemy-based access - JSON:Api, Admin App, etc.


### SQLAlchemy

[Object Relational Mapping for Python](https://docs.sqlalchemy.org/en/13/).

SQLAlchemy provides Python-friendly database access for Python.

It is used by JSON:Api, Logic Bank, and the Admin App.

SQLAlchemy processing is based on Python `model` classes,
created automatically by API Logic Server from your database,
and saved in the `database` directory.



### Admin App

This generated project also contains a React Admin app:
* Multi-page - including page transitions to "drill down"
* Multi-table - master / details (with tab sheets)
* Intelligent layout - favorite fields first, predictive joins, etc
* Logic Aware - updates are monitored by business logic

&nbsp;&nbsp;

# Project Structure
This project was created with the following directory structure:

| Directory | Usage                         | Key Customization File             | Typical Customization                                                                 |
|:-------------- |:------------------------------|:-----------------------------------|:--------------------------------------------------------------------------------------|
| ```api``` | JSON:API                      | ```api/customize_api.py```         | Add new end points / services                                                         |
| ```database``` | SQLAlchemy Data Model Classes | ```database/customize_models.py``` | Add derived attributes, and relationships missing in the schema                       |
| ```logic``` | Transactional Logic           | ```logic/declare_logic.py```       | Declare multi-table derivations, constraints, and events such as send mail / messages |
| ```ui``` | Admin App                     | ```ui/admin/admin.yaml```          | Control field display - order, captions etc.                                          |
| ```tests``` | Behave Test Suite              | ```tests/api_logic_server_behave/features```          | Declare and implement [Behave Tests](https://valhuber.github.io/ApiLogicServer/Behave/)                                          |
&nbsp;

### Key Customization File - Typical Customization

In the table above, the _Key Customization Files_ are created as stubs, intended for you to add customizations that extend
the created API, Logic and Web App.  Since they are separate files, the project can be
[rebuilt](https://valhuber.github.io/ApiLogicServer/Project-Rebuild/) (e.g., synchronized with a revised schema), preserving your customizations.

Please see the ```nw``` sample for examples of typical customizations.
