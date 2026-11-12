import unittest
from src.financials import select_annual_period, select_fact, EvidenceError


def facts(*items):
    return {"facts": {"us-gaap": {"Revenues": {"units": {"USD": list(items)}}}}}


def annual(start, end, accession="first", filed="2026-02-01", value=100):
    return {"start": start, "end": end, "val": value, "accn": accession,
            "form": "10-K", "filed": filed, "fy": 2025, "fp": "FY"}


class FinancialEvidenceTests(unittest.TestCase):
    def test_uses_last_year_end_in_2025_not_fiscal_label(self):
        data = facts(annual("2024-01-29", "2025-01-26", filed="2025-02-26"),
                     annual("2025-01-27", "2026-01-25", filed="2026-02-25"))
        self.assertEqual(select_annual_period(data), ("2024-01-29", "2025-01-26", "first"))

    def test_does_not_add_overlapping_year_to_date_periods(self):
        data = facts(annual("2025-01-01", "2025-12-31"),
                     annual("2025-01-01", "2025-09-30", value=75))
        self.assertEqual(select_annual_period(data)[:2], ("2025-01-01", "2025-12-31"))

    def test_keeps_first_reported_version_and_does_not_mix_later_comparatives(self):
        first = annual("2025-01-01", "2025-12-31", filed="2026-02-01")
        later = annual("2025-01-01", "2025-12-31", accession="later", filed="2026-09-01", value=101)
        data = facts(later, first)
        period = select_annual_period(data)
        self.assertEqual(period[2], "first")
        selected = select_fact(data, ["Revenues"], period, "USD")
        self.assertEqual(selected["value"], 100)
        self.assertEqual(selected["accession"], "first")

    def test_rejects_conflicting_values_in_same_filing(self):
        first = annual("2025-01-01", "2025-12-31")
        other = {**first, "val": 999}
        data = facts(first, other)
        with self.assertRaises(EvidenceError):
            select_fact(data, ["Revenues"], select_annual_period(data), "USD")

    def test_52_53_week_year_closing_early_january_2026_counts_as_2025(self):
        data = facts(annual("2023-12-31", "2024-12-28", filed="2025-02-12"),
                     annual("2024-12-29", "2026-01-03", filed="2026-02-12"))
        self.assertEqual(select_annual_period(data)[:2], ("2024-12-29", "2026-01-03"))

    def test_year_closing_late_january_2026_does_not_count_as_2025(self):
        data = facts(annual("2024-02-04", "2025-02-01", filed="2025-03-20"),
                     annual("2025-02-02", "2026-01-31", filed="2026-03-20"))
        self.assertEqual(select_annual_period(data)[:2], ("2024-02-04", "2025-02-01"))

    def test_missing_value_stays_missing(self):
        data = facts(annual("2025-01-01", "2025-12-31"))
        self.assertIsNone(select_fact(data, ["Assets"], select_annual_period(data), "USD", instant=True))


if __name__ == "__main__":
    unittest.main()
