# Purview Python #

## Description ##

This package is meant to act as a wrapper for the MSFT Purview (and Apache Atlas) APIs. It is currently in development by [Spydernaz](https://github.com/Spydernaz). To set up a development instance in Apache Atlas, you can see this repo [here]()

### Development Status ###

|Feature|Planned|WIP|Released|
|:---|:---:|:---:|:---:|
|Authenticate / Connect to APIs| :heavy_check_mark: |:heavy_check_mark:|:heavy_check_mark:|
|Get a Type (Entity)|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|
|Create a new Type (Entity)|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|
|Update an existing Type (Entity)|:heavy_check_mark:|:heavy_check_mark:||
|Get a Type (Others)|:heavy_check_mark:|||
|Create a new Type (Others)|:heavy_check_mark:|||
|Update an existing Type (Others)|:heavy_check_mark:|||
|Get an Entity (single element)|:heavy_check_mark:|||
|Get an Entity (with references)|:heavy_check_mark:|||
|Create a new Entity (single element)|:heavy_check_mark:|||
|Update an Existing Entity (single element)|:heavy_check_mark:|||
|Create a new Entity (with references)|:heavy_check_mark:|||
|Update an Existing Entity (with references)|:heavy_check_mark:|||


## Installation ##

This package runs on python3 and above. To install run

```sh
pip3 install purview_py
```

## Configuration ##

Describe the config Steps

## Example Usage ##

The follow code will connect to your purview instance and fetch the `hive_table` type. From here you could modify some details and then update your server as shown in the second part of this snippet

```python
import purview_py

# Your configuration
CLIENT_ID = __YOUR_CLIENT_ID__
CLIENT_SECRET = __YOUR_CLIENT_SECRET__
TENANT_ID = __YOUR_TENANT_ID__

resource =__YOUR_RESOURCE__

# Create a connection to your resource and a controller
conn = purview_py.PurviewConnection(resource, purview_py.TokenAuth(CLIENT_ID, CLIENT_SECRET, TENANT_ID))
c = purview_py.PurviewController()

# Fetch the hive_table type
t = purview_py.PurviewType.getTypeByName(conn, "hive_table")

# Add some new attributes to the type
t.name = "test_contract"

# Update the Type in Purview, its a type of lists but atm t is only a single object
c.create_new_types(conn, [t])

# You should now be able to get your new type(s)
t = purview_py.PurviewType.getTypeByName(conn, "contract_name")
print(f"You just created {t.name} with a GUID of {t.guid}")
```

## Docs ##

