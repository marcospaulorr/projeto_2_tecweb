from django.db import models

class StockData(models.Model):
    date = models.DateField()
    open = models.DecimalField(max_digits=10, decimal_places=2)
    high = models.DecimalField(max_digits=10, decimal_places=2)
    low = models.DecimalField(max_digits=10, decimal_places=2)
    close = models.DecimalField(max_digits=10, decimal_places=2)
    volume = models.BigIntegerField()

    class Meta:
        app_label = 'notes'

    def __str__(self):
        return f"{self.date} - Open: {self.open}, Close: {self.close}"
