from django.db import models
# Create your models here.


class Organization(models.Model):
    Name = models.CharField(max_length=50)
    Domain = models.CharField(max_length=255,unique=True,help_text="Do Not Use Prefix Like http:// Or https:")
    Location = models.CharField(max_length=500,blank=True,null=True)
    Email = models.EmailField(max_length=254)
    Number = models.CharField(max_length=10,help_text="Phone Number")
    Is_Active = models.BooleanField(default=True)


    def __str__(self):
        return self.Name
    


class Application(models.Model):
    Name = models.CharField(max_length=1000)
    BelongsTo = models.ForeignKey(Organization,verbose_name="Organization", on_delete=models.CASCADE)
    DateCreated = models.DateTimeField(auto_now_add=True)
    DateUpdated = models.DateTimeField(auto_now=True)
    Is_Active = models.BooleanField(default=True)

    def __str__(self):
        return self.Name


from apikey import models as APIKeysModel


class ApplicationAPIKeys(models.Model):
    Appication= models.OneToOneField(Application, on_delete=models.CASCADE)
    ApiKeys = models.ManyToManyField(APIKeysModel.ApiKey)

