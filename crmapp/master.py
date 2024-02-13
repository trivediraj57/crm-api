from django.db import models


class MASDiv(models.Model):
    division_name = models.CharField(db_column="sBuName", max_length=60)


class MASUom(models.Model):  # Used in esIN, esPR, esWO, eTender only
    unit_of_measure = models.CharField(db_column="sUomName", max_length=5)
    MEASURE_CHOICE = (
        ("1", "Count"),
        ("2", "Area"),
        ("3", "Volume"),
        ("4", "Weight"),
        ("5", "Time"),
    )
    measure_type = models.CharField(
        db_column="sUomType", max_length=1, choices=MEASURE_CHOICE, default="1"
    )
    unit_desc = models.CharField(db_column="sDesc", max_length=25, blank=True)

    class Meta:
        db_table = "MASUOM"
        verbose_name = "d1.UoM Master"


class MASCat(models.Model):  # Category used in all modules
    category_code = models.IntegerField(db_column="nGrpNo", null=True)
    category_name = models.CharField(db_column="sGrpName", max_length=20, blank=True)
    system_code = models.CharField(
        db_column="sSysNo", max_length=2, blank=True, null=True
    )
    program_code = models.CharField(
        db_column="sPrgCode", max_length=8, blank=True, null=True
    )

    class Meta:
        #    managed = False
        db_table = "MASCAT"
        ordering = ["category_code"]
        verbose_name = "a8.Category Master"

    def __str__(self):
        return f"{self.category_code}"
    

class MASSlm(models.Model):
    first_name = models.CharField(db_column="sFrstNm", max_length=255)
    last_name = models.CharField(
        db_column="sLstNm", max_length=255, blank=True, null=True
    )
    mobile = models.CharField(db_column="sMobile", max_length=30, blank=True, null=True)
    telephone = models.CharField(
        db_column="stelephn", max_length=30, blank=True, null=True
    )
    email = models.EmailField(db_column="eEmail", max_length=255)

    class Meta:
        db_table = "MASSLM"
        verbose_name = "a6.Sales Person"

    def __str__(self):
        return f"{self.first_name} - {self.last_name }"
    

class MASLan(models.Model):
    language_name = models.CharField(db_column="sLanguage", max_length=40)

    class Meta:
        db_table = "MASLAN"
        verbose_name = "a9.Language"

    def __str__(self) -> str:
        return self.language_name
    