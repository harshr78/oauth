from django.db import models
from organization import models as OrganizationModels


# Create your models here.
class ApiKey(models.Model):
    Key = models.CharField(max_length=1000)
    BelongsTo = models.ForeignKey(OrganizationModels.Application,verbose_name="Application", on_delete=models.CASCADE)
    DateCreated = models.DateTimeField(auto_now_add=True)
    DateUpdated = models.DateTimeField(auto_now=True)
    Is_Active = models.BooleanField(default=True)
    BlackListed = models.BooleanField(default=False)
    def __str__(self):
        return self.Key



