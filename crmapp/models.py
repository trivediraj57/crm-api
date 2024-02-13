from django.db import models
from .master import MASDiv, MASUom, MASCat, MASLan, MASSlm

class CRMInv(models.Model):
    division = models.ForeignKey(MASDiv, models.PROTECT, db_column='IdDivInv', null=True)
    item_code = models.CharField(db_column='sItmCode', max_length=19, blank=True, null=True)
    tax_percent = models.DecimalField(max_digits=2, db_column='fTaxPerc', decimal_places=2, default='0.05')
    item_name = models.CharField(db_column='sDesc', max_length=50, blank=True, null=True)
    add_desc = models.CharField(db_column='sAddDesc', max_length=50, blank=True, null=True)
    primary_uom = models.ForeignKey(MASUom, models.DO_NOTHING, db_column='IDPrimUnit', blank=True, null=True)
    category1 = models.ForeignKey(MASCat, models.PROTECT, db_column='IdInvCat1', blank=True, null=True)
    category2 = models.ForeignKey(MASCat, models.PROTECT, related_name='invcat2', db_column='IdInvCat2', blank=True, null=True)
    category3 = models.ForeignKey(MASCat, models.PROTECT, related_name='invcat3', db_column='IdInvCat3', blank=True, null=True)
    gl_code = models.IntegerField(db_column='nGLCode', blank=True, null=True)
    current_stock = models.FloatField(db_column='fCurStk', blank=True, null=True)
    reserve_stock = models.FloatField(db_column='fResStk', blank=True, null=True)
    average_cost = models.FloatField(db_column='fCostAvg', blank=True, null=True)
    market_cost = models.FloatField(db_column='fCostMkt', blank=True, null=True)
    sell_price = models.FloatField(db_column='fSellPrice', blank=True, null=True)

    class Meta:
    #    managed = False
        db_table = 'CRMINV'
        verbose_name = 'a3.Product Master'


class CRMLed(models.Model):
    # contact = models.ForeignKey(CRMCnt, models.PROTECT, db_column='IdCnt', null=True, blank=True)
    first_name = models.CharField(db_column='sNameF', max_length=255, blank=True)
    last_name = models.CharField(db_column='sNameL', max_length=255, blank=True)
    email = models.EmailField(db_column='eEmail',  max_length=80, null=True, blank=True)
    phone = models.CharField(db_column='sPhone', max_length=20)
    language = models.ForeignKey(MASLan, models.PROTECT, db_column='IdLan', null=True, blank=True)
    STATUS_CHOICE = (('assigned', 'Assigned'),('in process', 'In Process'), ('converted', 'Converted'),
                     ('recycled', 'Recycled'),('closed', 'Closed'))
    lead_status = models.CharField(db_column='sLedStats', max_length=50, choices=STATUS_CHOICE, blank=True)
    # lead_source = models.ForeignKey('CRMEvt', models.PROTECT, db_column='IdEvt', null=True, blank=True) # From event
    pipeline = models.ForeignKey('CRMPil', models.PROTECT, db_column='IdPil', null=True, blank=True)
    city = models.CharField(db_column='sCity', max_length=40, blank=True)
    country = models.CharField(db_column='sCountry', max_length=40, blank=True)
    website = models.CharField(db_column='sWebsite', max_length=60, blank=True)
    description = models.TextField(db_column='tDesc', blank=True)
    assigned_to = models.ForeignKey(MASSlm, models.PROTECT, db_column='IdSlm', null=True, blank=True)
    opportunity_amount = models.IntegerField(db_column='nOppAmt', blank=True, null= True)
    generated_by = models.CharField(db_column='sGenBy', max_length=80, blank=True)
    created_on = models.DateTimeField(db_column='dCreatedOn', auto_now_add=True)
    enquiry_type = models.CharField(db_column='sEnqType', max_length=40, blank=True)
    IND_CHOICE = (("ADVERTISING", "ADVERTISING"),
                  ("REAL_ESTATE", "REAL_ESTATE"),
                  ("RETAIL", "RETAIL"),
                  ("AUTOMOTIVE", "AUTOMOTIVE"),
                  ("BANKING", "BANKING"),
                  ("CONTRACTING", "CONTRACTING"),
                  ("DISTRIBUTOR", "DISTRIBUTOR"),
                  ("SERVICES", "SERVICES"),
                  ("OTHERS", "OTHERS"))
    industry = models.CharField(db_column='sIndstry', max_length=20, choices=IND_CHOICE, blank=True)
    class Meta:
        db_table = 'CRMLED'
        verbose_name = 'b1.Lead'

    def __str__(self):
        return str(self.first_name) + str(self.last_name)

class CRMPil(models.Model):
    pipeline_name = models.CharField(db_column='sPilName', max_length=255)
    target_days = models.IntegerField(db_column='nAllwDur', default= 0)
    probability_percent = models.IntegerField(db_column='nProbPerc', default = 0)
    is_active = models.BooleanField(db_column='bIsActive', default=False)

    class Meta:
        db_table = 'CRMPIL'
        verbose_name = 'a4.Pipeline Setup'

    def __str__(self):
        return self.pipeline_name

class CRMOpp(models.Model):
    lead = models.ForeignKey(CRMLed, models.PROTECT, db_column='IdLed', null=True, blank=True)
    opportunity_name = models.CharField(db_column='sOppName', max_length=255)
    pipeline_stage = models.ForeignKey('CRMPil', models.PROTECT, db_column='IdPil', null=True, blank=True)
    CURRENCY_CHOICE = (('AED', 'AED'), ('EUR', 'EUR'), ('USD', 'USD'), ('GBP','GBP'))
    currency = models.CharField(db_column='sCurr', max_length=3, choices=CURRENCY_CHOICE, blank=True)
    amount = models.IntegerField(db_column='nAmt', blank=True, default = 0)
    probability = models.IntegerField(db_column='nProb',default=0)
    description = models.TextField(db_column='tDesc', blank=True)
    created_on = models.DateTimeField(db_column='dtCreatedOn', auto_now_add=True)
    target_date = models.DateField(db_column='dTrgtdte', blank=True, null=True)
    closed_on = models.DateField(db_column='dClosedOn', blank=True, null=True)

    class Meta:
        db_table = 'CRMOPP'
        verbose_name = 'b2.Opportunity'

    def __str__(self):
        return self.opportunity_name


class CRMTsk(models.Model):
    opportunity = models.ForeignKey(CRMOpp, models.PROTECT, db_column='IdOpp', null=True)
    lead = models.ForeignKey(CRMLed, models.PROTECT, db_column='IdLed', null=True)
    STATUS_CHOICES = (
        ("New", "New"),
        ("In Progress", "In Progress"),
        ("Completed", "Completed"),
    )
    PRIORITY_CHOICES = (("Low", "Low"), ("Medium", "Medium"), ("High", "High"))
    TASKTYPE_CHOICES = (
            ("call", "Call"),
            ("telephone call", "TelePhone Call"),
            ("email", "Email"),
            ("visit", "Visit"),
            ("meeting", "Meeting"),
            ("demo", "Demo"),
        )
    task_date = models.DateField(db_column='dTskDt', blank=True, null=True) #default current date
    task_type = models.CharField(db_column='sTskType',max_length=25, choices=TASKTYPE_CHOICES)
    task_notes = models.TextField(db_column='tTskNts', max_length=255)
    status = models.CharField(db_column='sStatus', max_length=25, choices=STATUS_CHOICES)
    priority = models.CharField(db_column='sPriorty', max_length=25, choices=PRIORITY_CHOICES)
    due_date = models.DateField(db_column='dduedt', blank=True, null=True)
    created_on = models.DateTimeField(db_column='dtCreatedOn', auto_now_add=True)

    class Meta:
        db_table = 'CRMTSK'
        verbose_name = 'b3.Task'

    def __str__(self):
        return self.task_type


