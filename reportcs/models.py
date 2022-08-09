from django.db import models
from core import models as core_models
from report.services import run_stored_proc_report



def claim_history_query():
def sales_objectives_rate_query():
    data = run_stored_proc_report(
    )
    return {
        "data": data
    }



def services_performance_query(date_from=None, date_to=None):

def pregnant_woman_with_cs_query(date_from=None,date_to=None):
    queryset = ()

    return {"data": list(queryset)}



def insuree_without_photo_query(date_from=None, date_to=None):

def cpn1_with_cs_query(date_from=None,date_to=None):
    queryset = ()

    return {"data": list(queryset)}


def assisted_birth_with_cs_query():
    data = run_stored_proc_report()
    return {
        "data": data
    }


def health_facilities_query():

def mother_cpon_with_cs_query():
    data = run_stored_proc_report()
    return {
        "data": data
    }


def feedback_indicators_query():

def newborn_cpon_with_cs_query():

    data = run_stored_proc_report()
    return {
        "data": data
    }


def upload_enrolement_from_phone_query():

def complicated_birth_with_cs_query():
    data = run_stored_proc_report()
    return {
        "data": data
    }


def enrolement_officers_query():

def cesarienne_rate_query():

    data = run_stored_proc_report()
    return {
        "data": data
    }



def user_log_report_query():

def pregnant_woman_ref_rate_query():
    data = run_stored_proc_report()
    return {
        "data": data
    }

def user_log_report_query(user,date_from=None, date_to=None,action=None):
    data = run_stored_proc_report(
        "uspSSRSUserLogReport",
        FromDate = date_from,
        ToDate  = date_to,
        Action = action,
    )
    return {
        "data": data
    }

def invoice_per_fosa_query():

    data = run_stored_proc_report()
    return {
        "data": data
    }


def expired_policies_query():
    data = run_stored_proc_report()
    return {
        "data": data
    }


def periodic_paid_bills_query():
    data = run_stored_proc_report()
    return {
        "data": data
    }

def periodic_rejected_bills_query():
    data = run_stored_proc_report()
    return {
        "data": data
    }

def periodic_household_participation_query():
    data = run_stored_proc_report()
    return {
        "data": data
    }

def cs_sales_amount_query():
    data = run_stored_proc_report()
    return {
        "data": data
    }

def new_cs_per_month_query():
    data = run_stored_proc_report()
    return {
        "data": data
    }

def cs_in_use_query():
    data = run_stored_proc_report()
    return {
        "data": data
    }

def closed_cs_query():
    data = run_stored_proc_report()
    return {
        "data": data
    }

def medium_charge_on_beneficiary_query():
    data = run_stored_proc_report()
    return {
        "data": data
    }


