from django.db import models

# Create your models here.

class Report(models.Model):
    Id = models.AutoField(primary_key=True)
    Scope = models.CharField(max_length=50, blank=True, null=True)
    Category = models.TextField(blank=True, null=True)
    DataType = models.TextField(blank=True, null=True)
    Location = models.CharField(max_length=50, blank=True, null=True)
    TotalData = models.DecimalField(max_digits=100, decimal_places=2, blank=True, null=True)
    Emissions_t_of_CO2e = models.DecimalField(max_digits=100, decimal_places=2, blank=True, null=True)
    Scope_3_Indirect_Emissions = models.DecimalField(max_digits=100, decimal_places=2, blank=True, null=True)
    LifecycleEmissions = models.DecimalField(max_digits=100, decimal_places=2, blank=True, null=True)
    Floor_space_m2 = models.DecimalField(max_digits=100, decimal_places=2, blank=True, null=True)
    EmissionsIntensity = models.DecimalField(max_digits=100, decimal_places=2, blank=True, null=True)
    CO2Emissions = models.DecimalField(max_digits=100, decimal_places=2, blank=True, null=True)
    CH4Emissions = models.DecimalField(max_digits=100, decimal_places=2, blank=True, null=True)
    N2OEmissions = models.DecimalField(max_digits=100, decimal_places=2, blank=True, null=True)
    
    def __str__(self):
        return self.Scope




