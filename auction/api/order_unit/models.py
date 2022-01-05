from django.db import models

from auction.api.order.models import Order
from auction.api.unit.models import Unit


class OrderUnit(models.Model):
    PENDING = 'PE'
    REJECTED = 'RE'
    COMPLETED = 'CO'
    STATUSES = (
        (PENDING, 'Pending'),
        (REJECTED, 'Rejected'),
        (COMPLETED, 'Completed'),
    )

    order = models.ForeignKey(to=Order, on_delete=models.CASCADE)
    unit = models.ForeignKey(to=Unit, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    unit_price = models.PositiveIntegerField()
    status = models.CharField(max_length=2, choices=STATUSES, default=PENDING)

    def __str__(self):
        return '{} pcs of {} by {}'.format(self.quantity, self.unit.product, self.order.name)
