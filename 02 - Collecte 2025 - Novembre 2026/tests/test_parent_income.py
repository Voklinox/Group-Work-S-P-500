import unittest
from src.reviewed import parent_income


def fact(tag, value):
    return {"value": value, "tag": tag, "period_start": "2025-01-01", "period_end": "2025-12-31",
            "accession": "a", "filed": "2026-02-01", "form": "10-K", "unit": "USD", "namespace": "us-gaap"}


def data(**tags):
    units = {t: {"units": {"USD": [dict(start="2025-01-01", end="2025-12-31", val=v, accn="a", form="10-K", filed="2026-02-01")]}} for t, v in tags.items()}
    return {"cik": 1, "facts": {"us-gaap": units}}


PERIOD = ("2025-01-01", "2025-12-31", "a")


class ParentIncomeTests(unittest.TestCase):
    def test_subtracts_noncontrolling_income_from_consolidated(self):
        d = data(NetIncomeLossAttributableToNoncontrollingInterest=3373)
        result, basis = parent_income(d, PERIOD, fact("ProfitLoss", 4357), [])
        self.assertEqual((result["value"], basis), (984, "computed_parent_minus_nci"))
        self.assertEqual([i["value"] for i in result["inputs"]], [4357, 3373])

    def test_keeps_consolidated_value_when_no_minority_income_is_tagged(self):
        result, basis = parent_income(data(), PERIOD, fact("ProfitLoss", 500), [])
        self.assertEqual((result["value"], basis), (500, "consolidated_no_nci_tagged"))

    def test_reviewed_mapping_takes_precedence(self):
        m = [dict(cik="0000000001", variable="net_income_usd", accession="a", period_start="2025-01-01", period_end="2025-12-31",
                  method="manual_report", tags=[], value=-745, label="x", reason="y", filed="2026-02-01", form="10-K")]
        d = data(NetIncomeLossAttributableToNoncontrollingInterest=1)
        result, basis = parent_income(d, PERIOD, fact("ProfitLoss", -738), m)
        self.assertEqual((result["value"], basis), (-745, "reviewed_report"))


if __name__ == "__main__":
    unittest.main()
