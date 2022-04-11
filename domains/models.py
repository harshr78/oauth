from django.db import models
from organization import models as OrganizationModels
from django.contrib.auth.models import User

# Create your models here.


class Domain(models.Model):
    Domain = models.CharField(max_length=1000)
    BelongsTo = models.ForeignKey(OrganizationModels.Organization,verbose_name="Organization", on_delete=models.CASCADE)
    RegisterBy = models.ForeignKey(User,verbose_name="User", on_delete=models.CASCADE)
    DateCreated = models.DateTimeField(auto_now_add=True)
    DateUpdated = models.DateTimeField(auto_now=True)
    Is_Active = models.BooleanField(default=True)

    def __str__(self):
        return self.Domain