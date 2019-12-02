# erpnext-rest-client
ERPNext REST API Client

### Login in
```python
from erpnext_client.query import ERPNextClient

erp_client = ERPNextClient(app.config["ERPNEXT_API_HOST"],
                           app.config["ERPNEXT_API_USERNAME"],
                           app.config["ERPNEXT_API_PASSWORD"])

if not erp_client.login():
    LOGGER.error("Login failed on ERP at {0} using username {1}".format(erp_client.host, erp_client.username))
else:
    LOGGER.info("Login OK on ERP at {0} using username {1}".format(erp_client.host, erp_client.username))
    
LOGGER.debug(erp_client.get_credentials())
```

### Listing items

```python
items = erp_client.query(ERPItem).list(erp_fields=["name", "description", "disabled", "item_code", "website_image"], filters=[["Item", "show_in_website", "=", "1"], ["Item", "is_sales_item", "=", True], ["Website Item Group", "item_group", "=", item_group]])
```

### Getting a single element

```python
item = erp_client.query(ERPItem).get(beer_slug, fields=["name", "slideshow", "description", "disabled", "item_code"], filters=[["Item", "show_in_website", "=", "1"], ["Item", "is_sales_item", "=", True]])
```
