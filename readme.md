# Security POC

## Goals

[This POC](https://github.com/valhuber/security-poc) is intended to:

* Confirm approach to __role-based row authorization__, using SQLAlchemy [adding-global-where](https://docs.sqlalchemy.org/en/14/orm/session_events.html#adding-global-where-on-criteria) functionality.  See also [the examples](https://docs.sqlalchemy.org/en/14/orm/query.html#sqlalchemy.orm.with_loader_criteria).
     * Note using SQLAlchemy means that filters apply to all SAFRS and custom api access
     * Working quite well!
* Confirm whether the basic filtering capability __meets the requirements of 1 real-world app__
     * Once *certain* use case is *multi-tenent*
         * Each row is stamped with a `client_id`
         * User table identifies users' `client_id`
         * Enforced in `declare_security.py`:
     * Preliminary finding - first test case worked on real-world app

```python
Grant(  on_entity = models.Category,
        to_role = Roles.tenant,
        filter = models.Category.Id == Security.current_user().client_id)  # User table attributes
```

&nbsp;

This POC is _not_ meant to explore:

* Login Authentication (currently addressed with a place-holder stub)

* Interaction with SAFRS API handling (except to the extent SAFRS uses SQLAlchemy)

* System issues such as performance, caching, etc.

&nbsp;

## Setup and Test

To run:

1. Open [this repository](https://github.com/valhuber/security-poc) in codespaces

    * Takes about a minute; wait until the Ports tab shows up

2. Start the server, using the provided Launch Configuration

3. Issue this in the codespaces (_not_ your local machine) terminal window:

```
curl -X 'GET' \
'http://localhost:5656/api/CategoryTable/?fields%5BCategory%5D=Id%2CCategoryName%2CDescription&page%5Boffset%5D=0&page%5Blimit%5D=10&sort=id' -H 'accept: application/vnd.api+json' -H 'Content-Type: application/vnd.api+json'
```

&nbsp;

## Active Code

See `api_logic_server_run.py`, around line 400 >> `security/system/security_manager.py`.

To enable db-based security, activate line 10 in `security/system/security_manager.py.`

&nbsp;

## Declaring Logic

You can define filters for users' roles (role-based access control):

<figure><img src="https://github.com/valhuber/security-poc/blob/main/doc/images/declare-security.png?raw=true"></figure>

&nbsp;

## Installing Prototype on API Logic Projects

The truly daring can experiment with this on their own project:

1. Clone the [authentication-app](https://github.com/valhuber/authentication-app), and run the Admin App to create users (you'll need a venv, as usual)
2. Clone this, and from the clone..
2. Copy the security folder to your project
3. Merge in the changes from
    1. `api_logic_server_run.py`
    2. `config.py`
4. From the authentication-app, copy database/db.sqlite -> $project/security/authentication_provider/authentication_db.sqlite
    
&nbsp;

## Design Notes

<figure><img src="https://github.com/valhuber/security-poc/blob/main/doc/images/basic-design.png?raw=true"></figure>

<figure><img src="https://github.com/valhuber/security-poc/blob/main/doc/images/authentication-db.png?raw=true"></figure>

The Authentication Provider mechanism is currently this code in `security/system/security_manager.py`:

```python
# import security.authentication_provider.mem_auth_row as authentication_provider  # TODO: your provider here
import security.authentication_provider.db_auth as authentication_provider  # TODO: your provider here
```

&nbsp;

## Status

Now initially running, per [this support](https://github.com/sqlalchemy/sqlalchemy/discussions/8976), using the in-memory auth provider `security/authentication_provider/mem_auth_row.py.`

The db-based provider (`security/authentication_provider/db_auth.py`) is also running.

&nbsp;

