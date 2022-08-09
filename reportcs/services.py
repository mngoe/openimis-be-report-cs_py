from claim.models import Claim


def cs_report_cpn1_realisation(date_from, date_to, **kwargs):
    if date_from:
        queryset = (
            Claim.objects.filter(validity_from__gte=date_from, validity_to__gte=date_to, count__code='CPN1').Count())
    return {"data": list(queryset)}
