from django.db import models


class ThinDevicesUnits(models.Model):
    STATUS_CHOICES = (
        (1, 'مخزنه'),
        (2, 'جارى العمل'),
        (3, 'انتهى العمل')
    )
    status = models.SmallIntegerField(null=True, blank=True, choices=STATUS_CHOICES)
    name = models.CharField(max_length=255, null=True, blank=True)
    total_devices = models.IntegerField(null=True, blank=True)
    devices_done = models.IntegerField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    short_name = models.CharField(max_length=255, null=True, blank=True)
    epg = models.CharField(max_length=255, null=True, blank=True)
    cdb = models.CharField(max_length=255, null=True, blank=True)
    category = models.CharField(max_length=255, null=True, blank=True)
    database_zone = models.CharField(max_length=255, null=True, blank=True)
    database_name = models.CharField(max_length=255, null=True, blank=True)

    @property
    def remain_devices(self):
        if self.devices_done is None:
            return self.total_devices
        else:
            return self.total_devices - self.devices_done

    def __str__(self):
        return self.name
