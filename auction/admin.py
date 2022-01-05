from django.contrib import admin
from auction.api.cart.models import CartUnit
from auction.api.order.models import Order
from auction.api.order_unit.models import OrderUnit
from auction.api.product.models import Product
from auction.api.bid.models import Bid
from auction.api.property.models import PropertyValue, Property
from auction.api.tag.models import Tag
from auction.api.unit.models import Unit, UnitImage
from auction.api.user.models import Seller
from .admin_models import UnitAdmin, ProductAdmin, UnitImageAdmin, OrderAdmin, OrderUnitAdmin, PropertyAdmin, \
    PropertyValueAdmin, BidAdmin

admin.site.register([Seller,
                     Tag])

admin.site.register(PropertyValue, PropertyValueAdmin)
admin.site.register(Property, PropertyAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(UnitImage, UnitImageAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderUnit, OrderUnitAdmin)
admin.site.register(Bid, BidAdmin)
