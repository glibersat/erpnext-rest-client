import requests

from .schemas import (
    ERPItemSchema,
    ERPItemPriceSchema,
    ERPItemGroupSchema,
    ERPSalesOrderSchema,
    ERPCustomerSchema,
    ERPUserSchema,
    ERPContactSchema,
    ERPContactEmailSchema,
    ERPContactPhoneSchema,
    ERPAddressSchema,
    ERPDynamicLinkSchema,
    ERPBinSchema,
    ERPJournalEntrySchema,
    ERPWebsiteSlideshow,
    ERPWebsiteSlideshowItem
)


class ERPResource:
    class DoesNotExist(Exception):
        """
        When an object isn't found on the server
        """
        pass

    def __init__(self, aERPNextClient):
        self.client = aERPNextClient

    def get(self, name, fields=[], filters=[]):
        try:
            response = self.client.get_resource(self.doctype, name, fields, filters)
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                raise self.DoesNotExist()
            else:
                e.response.raise_for_status()

        instance, errors = self.schema(strict=True).load(data=response.json()['data'])

        return instance

    def list(self, erp_fields=[], filters=[], schema_fields=None, parent=None, page_length=None):
        """
        Return a list of documents matching the given criterias
        """
        try:
            response = self.client.list_resource(self.doctype,
                                                 fields=erp_fields,
                                                 filters=filters,
                                                 parent=parent,
                                                 page_length=page_length)
        except requests.exceptions.HTTPError as e:
            print(e.response.text)
            e.response.raise_for_status()


        instances, errors = self.schema(partial=schema_fields,
                                        many=True).load(data=response.json()['data'])

        return instances

    def first(self, erp_fields=[], filters=[], schema_fields=None, parent=None):
        """
        Return first document matching criteras
        """
        documents = self.list(erp_fields, filters, schema_fields, parent)
        if len(documents) == 0:
            raise self.DoesNotExist

        return documents[0]

    def create(self, data):
        """
        Create a document of the current type with given data
        """
        try:
            response = self.client.create_resource(self.doctype, data)
        except requests.exceptions.HTTPError as e:
            e.response.raise_for_status()

        instance, errors = self.schema().load(data=response.json()['data'])

        return instance

    def update(self, name, data):
        """
        Update a document of the current type with given name and data
        """
        try:
            response = self.client.update_resource(self.doctype, name, data)
        except requests.exceptions.HTTPError as e:
            e.response.raise_for_status()

        return response



class ERPDynamicLink(ERPResource):
    doctype = "Dynamic Link"
    schema = ERPDynamicLinkSchema


class ERPItemPrice(ERPResource):
    doctype = "Item Price"
    schema = ERPItemPriceSchema


class ERPItem(ERPResource):
    doctype = "Item"
    schema = ERPItemSchema




class ERPBin(ERPResource):
    doctype = "Bin"
    schema = ERPBinSchema


class ERPItemGroup(ERPResource):
    doctype = "Item Group"
    schema = ERPItemGroupSchema


class ERPCustomer(ERPResource):
    doctype = "Customer"
    schema = ERPCustomerSchema


class ERPContact(ERPResource):
    doctype = "Contact"
    schema = ERPContactSchema

class ERPContactPhone(ERPResource):
    doctype = "Contact Phone"
    schema = ERPContactPhoneSchema

class ERPContactEmail(ERPResource):
    doctype = "Contact Email"
    schema = ERPContactEmailSchema


class ERPAddress(ERPResource):
    doctype = "Address"
    schema = ERPAddressSchema


class ERPSalesOrder(ERPResource):
    doctype = "Sales Order"
    schema = ERPSalesOrderSchema


class ERPUser(ERPResource):
    doctype = "User"
    schema = ERPUserSchema

class ERPJournalEntry(ERPResource):
    doctype = "Journal Entry"
    schema = ERPJournalEntrySchema


class ERPWebsiteSlideshow(ERPResource):
    doctype = "Website Slideshow"
    schema = ERPWebsiteSlideshow


class ERPWebsiteSlideshowItem(ERPResource):
    doctype = "Website Slideshow Item"
    schema = ERPWebsiteSlideshowItem


