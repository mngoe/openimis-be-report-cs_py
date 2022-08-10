from django.db import models
from core import models as core_models
from report.services import run_stored_proc_report
from claim.models import Claim

def cpn1_with_cs_query(date_from=None, date_to=None, **kwargs):
    if date_from:
        queryset = (
            Claim.objects.filter(validity_from__gte=date_from, validity_to__gte=date_to, count__code='CPN1').Count())
    return {"data": list(queryset)}

def cpn4_with_cs_query(date_from=None, date_to=None, **kwargs):
    queryset = ()
    return {"data": list(queryset)}

def assisted_birth_with_cs_query(date_from=None, date_to=None, **kwargs):
    queryset = ()
    return {"data": list(queryset)}

def mother_cpon_with_cs_query(date_from=None, date_to=None, **kwargs):
    queryset = ()
    return {"data": list(queryset)}

def newborn_cpon_with_cs_query(date_from=None, date_to=None, **kwargs):
    queryset = ()
    return {"data": list(queryset)}

def complicated_birth_with_cs_query(date_from=None, date_to=None, **kwargs):
    queryset = ()
    return {"data": list(queryset)}

def cesarienne_rate_query(date_from=None, date_to=None, **kwargs):
    queryset = ()
    return {"data": list(queryset)}

def pregnant_woman_ref_rate_query(date_from=None, date_to=None, **kwargs):
    queryset = ()
    return {"data": list(queryset)}

def invoice_per_fosa_query(date_from=None, date_to=None, **kwargs):
    queryset = ()
    return {"data": list(queryset)}

def expired_policies_query(date_from=None, date_to=None, **kwargs):
    queryset = ()
    return {"data": list(queryset)}

def periodic_paid_bills_query(date_from=None, date_to=None, **kwargs):
    queryset = ()
    return {"data": list(queryset)}

def periodic_rejected_bills_query(date_from=None, date_to=None, **kwargs):
    queryset = ()
    return {"data": list(queryset)}

def periodic_household_participation_query(date_from=None, date_to=None, **kwargs):
    queryset = ()
    return {"data": list(queryset)}

def cs_sales_amount_query(date_from=None, date_to=None, **kwargs):
    queryset = ()
    return {"data": list(queryset)}

def new_cs_per_month_query(date_from=None, date_to=None, **kwargs):
    queryset = ()
    return {"data": list(queryset)}

def cs_in_use_query(date_from=None, date_to=None, **kwargs):
    queryset = ()
    return {"data": list(queryset)}

def closed_cs_query(date_from=None, date_to=None, **kwargs):
    queryset = ()
    return {"data": list(queryset)}

def severe_malaria_cost_query(date_from=None, date_to=None, **kwargs):
    queryset = ()
    return {"data": list(queryset)}

