import unittest
from src.universe import reconcile, Constituents

class UniverseTests(unittest.TestCase):
    def test_keeps_both_tickers_but_one_issuer_and_applies_dated_event(self):
        rows=[dict(Symbol=s,Security="Alphabet Inc. (Class A)",CIK="1652044",**{"GICS Sector":"Communication Services"}) for s in ["GOOG","GOOGL"]]
        rows.append(dict(Symbol="SOLS",Security="Solstice",CIK="2064953",**{"GICS Sector":"Materials"}))
        issuers,changes,securities=reconcile(rows)
        self.assertEqual(securities,5)
        self.assertEqual(len(issuers),4)
        alphabet=next(r for r in issuers if r['cik']=='0001652044')
        self.assertEqual(alphabet['tickers'],'GOOG|GOOGL')
        self.assertNotIn('SOLS',[r['tickers'] for r in issuers])
        self.assertTrue(all(c['source_url'] and c['effective_date']=='2025-12-22' for c in changes))
        self.assertFalse(next(c for c in changes if c['ticker']=='LKQ')['applied'])

    def test_only_parses_constituents_not_subsequent_change_table(self):
        parser=Constituents()
        parser.feed('<table id="constituents"><tr><th>Symbol</th><th>CIK</th></tr><tr><td>ABC</td><td>123</td></tr></table><table><tr><td>WRONG</td></tr></table>')
        self.assertEqual(parser.rows,[['Symbol','CIK'],['ABC','123']])

    def test_rejects_conflicting_sectors_for_one_company(self):
        rows=[dict(Symbol=s,Security='X',CIK='1',**{'GICS Sector':sector}) for s,sector in [('X','A'),('Y','B')]]
        with self.assertRaises(ValueError): reconcile(rows)
