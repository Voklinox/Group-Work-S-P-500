import unittest
from src.governance import validate
from src.governance_catalogue import proxy_rows

def record(**changes):
    base=dict(publication_date='2025-05-13',board_size=13,independent_directors=12,board_leadership='No board chair',ceo_name='CEO',chair_name='',source_url='https://www.sec.gov/example',evidence=[{'note':'source checked'}],board_scope='incumbents',date_basis='proxy publication')
    return {**base,**changes}

class GovernanceTests(unittest.TestCase):
    def test_rejects_more_independent_members_than_board_members(self):
        with self.assertRaises(ValueError):validate(record(independent_directors=14))
    def test_rejects_2026_proxy_as_2025_measurement(self):
        with self.assertRaises(ValueError):validate(record(publication_date='2026-01-08'))
    def test_does_not_call_lead_director_a_chair(self):
        with self.assertRaises(ValueError):validate(record(chair_name='Lead director'))
        v=validate(record());self.assertEqual(v['board_leadership'],'No board chair')
        self.assertAlmostEqual(v['board_independence_reported_pct'],1200/13)
    def test_rejects_claimed_separation_for_same_person(self):
        with self.assertRaises(ValueError):validate(record(board_leadership='Separate CEO and chair',chair_name='CEO'))
    def test_requires_evidence_and_a_measurement_scope(self):
        with self.assertRaises(ValueError):validate(record(evidence=[]))
        with self.assertRaises(ValueError):validate(record(board_scope=''))
    def test_catalogue_recognises_information_statement_and_contested_proxy(self):
        f=dict(form=['DEF 14C','DEFC14A','DEFA14A','DEF 14A'],filingDate=['2025-03-01','2025-04-01','2025-04-02','2026-01-01'],accessionNumber=['a','b','c','d'],primaryDocument=['a.htm','b.htm','c.htm','d.htm'])
        rows=proxy_rows('0000000123',f,'catalogue')
        self.assertEqual([r['form'] for r in rows],['DEF 14C','DEFC14A'])
