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

To enable db-based security, activate line 10 in `security/security_sys.py.`

&nbsp;

## Declaring Logic

You can define filters for users' roles (role-based access control):

<figure><img src="https://github.com/valhuber/security-poc/blob/main/doc/images/declare-security.png?raw=true"></figure>

&nbsp;

## Design Notes

<figure><img src="https://github.com/valhuber/security-poc/blob/main/doc/images/basic-design.png?raw=true"></figure>

The provider mechanism is currently this code in `security/security_sys.py`:

```python
# import security.authentication_provider.mem_auth_row as authentication_provider  # TODO: your provider here
import security.authentication_provider.db_auth as authentication_provider  # TODO: your provider here
```

&nbsp;

## Status

Now initially running, per [this support](https://github.com/sqlalchemy/sqlalchemy/discussions/8976), using the in-memory auth provider `security/authentication_provider/mem_auth_row.py.`

The db-based provider (`security/authentication_provider/db_auth.py`) is also running.

&nbsp;

