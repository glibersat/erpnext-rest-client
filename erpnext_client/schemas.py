from marshmallow import Schema, fields


class ERPDocument(Schema):
    """
    Base ERPNext Document
    """

    name = fields.String()
    status = fields.String()

    def __eq__(self, other):
        return self.name == other.name and type(self) == type(other)


class ERPUserSchema(ERPDocument):
    email = fields.Email(load_from="email")
    first_name = fields.String(load_from="first_name")
    last_name = fields.String(load_from="last_name")


class ERPItemSchema(ERPDocument):
    code = fields.String(load_from="item_code")
    name = fields.String(load_from="item_name")
    disabled = fields.Boolean(load_from="disabled")
    description_html = fields.String(load_from="description")
    website_long_description_html = fields.String(load_from="web_long_description")
    website_warehouse = fields.String(load_from="website_warehouse")
    price = fields.Float(load_from="standard_rate")
    total_projected_qty = fields.Float(load_from="total_projected_qty")
    thumbnail = fields.String()
    website_image = fields.String()
    slideshow = fields.String()
    has_variants = fields.Boolean(load_from="has_variants")
    variants = fields.Nested("ERPItemSchema", many=True)
    website_specifications = fields.Nested(
        "ERPItemWebsiteSpecificationSchema",
        many=True,
        load_from="website_specifications",
    )


class ERPItemPriceSchema(ERPDocument):
    item_code = fields.String(load_from="item_code")
    item_name = fields.String(load_from="item_name")
    currency = fields.String(load_from="currency")
    price_list_rate = fields.Float(load_from="price_list_rate")


class ERPPaymentEntrySchema(ERPDocument):
    payment_type = fields.String(load_from="payment_type")
    mode_of_payment = fields.String(load_from="mode_of_payment")


class ERPBinSchema(ERPDocument):
    """
    A Bin is a stock status for a given item in a given warehouse
    """

    item_code = fields.String(load_from="item_code")
    name = fields.String(load_from="item_name")
    warehouse = fields.String(load_from="warehouse")
    reserved_qty = fields.Float(load_from="reserved_qty")
    actual_qty = fields.Float(load_from="actual_qty")
    ordered_qty = fields.Float(load_from="ordered_qty")
    indented_qty = fields.Float(load_from="indented_qty")
    planned_qty = fields.Float(load_from="planned_qty")
    projected_qty = fields.Float(load_from="projected_qty")


class ERPItemGroupSchema(ERPDocument):
    name = fields.String(load_from="name")


class ERPCustomerSchema(ERPDocument):
    email = fields.Email(load_from="email")
    primary_address = fields.String(load_from="primary_address")
    mobile_no = fields.String(load_from="mobile_no")
    customer_group = fields.String(load_from="customer_group")


class ERPContactPhoneSchema(ERPDocument):
    phone = fields.String(load_from="phone")
    is_primary_phone = fields.Boolean(load_from="is_primary_phone")
    is_primary_mobile_no = fields.Boolean(load_from="is_primary_mobile_no")


class ERPContactEmailSchema(ERPDocument):
    email = fields.String(load_from="email_id")
    is_primary = fields.Boolean(load_from="is_primary")


class ERPContactSchema(ERPDocument):
    email = fields.Email(load_from="email_id")
    first_name = fields.String(load_from="first_name")
    last_name = fields.String(load_from="last_name")
    mobile_no = fields.String(load_from="mobile_no")
    phone_nos = fields.Nested("ERPContactPhoneSchema", load_from="phone_nos", many=True)
    email_ids = fields.Nested("ERPContactEmailSchema", load_from="email_ids", many=True)


class ERPAddressSchema(ERPDocument):
    title = fields.String(load_from="address_title")
    address_type = fields.String(load_from="address_type")
    address_line1 = fields.String(load_from="address_line1")
    address_line2 = fields.String(load_from="address_line2")
    pincode = fields.String(load_from="pincode", allow_none=True)
    city = fields.String(load_from="city")
    country = fields.String(load_from="country")


class ERPDynamicLinkSchema(ERPDocument):
    """
    Dynamic Link between two documents
    """

    link_name = fields.String(load_from="link_name")
    parent = fields.String(load_from="parent")
    parent_type = fields.String(load_from="parenttype")


class ERPSalesOrderItemSchema(ERPDocument):
    item_code = fields.String()
    item_name = fields.String()
    item_group = fields.String()
    description = fields.String()
    warehouse = fields.String()
    quantity = fields.Int(load_from="qty")
    rate = fields.Float()
    amount = fields.Float(load_from="net_amount")
    image = fields.String(load_from="image")
    projected_qty = fields.Int(load_from="projected_qty")


class ERPJournalEntrySchema(ERPDocument):
    voucher_type = fields.String()


class ERPSalesOrderTaxes(ERPDocument):
    name = fields.String()
    description = fields.String()
    tax_amount = fields.Float(load_from="tax_amount")


class ERPShippingRuleSchema(ERPDocument):
    pass


class ERPSalesOrderSchema(ERPDocument):
    date = fields.Date(load_from="transaction_date")
    title = fields.Str()
    customer = fields.Str()
    total = fields.Float(load_from="total")
    amount_total = fields.Float(load_from="grand_total")
    items = fields.Nested(ERPSalesOrderItemSchema, many=True)
    taxes = fields.Nested(ERPSalesOrderTaxes, many=True)
    shipping_rule = fields.Str()


class ERPItemWebsiteSpecificationSchema(ERPDocument):
    """
    A key:value pair for adding attributes to items for the website
    """

    label = fields.Str()
    description = fields.String()


class ERPWebsiteSlideshowItem(ERPDocument):
    image = fields.String()
    description = fields.String()
    heading = fields.String(load_from="heading")


class ERPWebsiteSlideshow(ERPDocument):
    slideshow_items = fields.Nested("ERPWebsiteSlideshowItem", many=True)


class ERPDeliveryNoteSchema(ERPDocument):
    customer = fields.Str()
    customer_name = fields.Str()
    customer_group = fields.String(load_from="customer_group")
    shipping_address = fields.String(load_from="shipping_address")


class ERPDeliveryStopSchema(ERPDocument):
    customer_address = fields.String()
    contact = fields.String()
    address = fields.String()
    estimated_arrival = fields.String()
    distance = fields.Int()
    lat = fields.Float()
    lng = fields.Float()


class ERPDeliveryTripSchema(ERPDocument):
    total_distance = fields.Float()
    departure_time = fields.String()

    stops = fields.Nested(
        "ERPDeliveryStopSchema", load_from="delivery_stops", many=True
    )
