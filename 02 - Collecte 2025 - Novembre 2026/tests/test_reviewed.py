import unittest
from src.reviewed import reviewed_fact

class ReviewedMappingTests(unittest.TestCase):
    def test_requires_exact_accession_and_period(self):
        data={'cik':123,'facts':{}}
        m={'cik':'0000000123','variable':'revenue_usd','accession':'first','period_start':'2025-01-01','period_end':'2025-12-31','method':'manual_report','value':42,'tags':[],'label':'Revenue','reason':'Source note','filed':'2026-02-01','form':'10-K'}
        self.assertIsNone(reviewed_fact(data,('2025-01-01','2025-12-31','other'),'revenue_usd',[m]))
        f=reviewed_fact(data,('2025-01-01','2025-12-31','first'),'revenue_usd',[m])
        self.assertEqual(f['value'],42)
        self.assertEqual(f['review']['reason'],'Source note')
