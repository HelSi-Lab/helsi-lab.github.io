"""Regression tests for the lab's BibTeX-to-Vancouver pipeline."""

import sys
import unittest
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).parent))

from plugins.bibtex import main
from vancouver import format_citations


class BibtexPipelineTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        config = yaml.safe_load(Path("_data/bibtex.yaml").read_text(encoding="utf-8"))[0]
        cls.citations = main(config)
        format_citations(cls.citations)
        cls.by_key = {citation["cite_key"]: citation for citation in cls.citations}

    def test_all_selected_entries_are_generated(self):
        self.assertEqual(len(self.citations), 10)
        self.assertEqual(len({citation["id"] for citation in self.citations}), 10)

    def test_vancouver_author_names_and_metadata(self):
        citation = self.by_key["Serin_campaign"]
        self.assertEqual(citation["authors"], ["**Lee S**", "Zabinsky ZB", "Liu S"])
        self.assertEqual(citation["journal"], "Health Care Manag Sci")
        self.assertEqual(citation["volume"], "28")
        self.assertEqual(citation["issue"], "1")
        self.assertEqual(citation["pages"], "84-98")
        self.assertEqual(citation["author_style"], "vancouver")

    def test_doi_urls_are_normalized(self):
        citation = self.by_key["Lee_AJPM"]
        self.assertEqual(citation["doi"], "10.1016/j.focus.2023.100155")
        self.assertEqual(citation["link"], "https://doi.org/10.1016/j.focus.2023.100155")

    def test_collective_author_is_not_abbreviated(self):
        citation = self.by_key["HPVSim"]
        self.assertIn("National Disease Modelling Consortium of India", citation["authors"])

    def test_blank_override_fields_are_removed(self):
        citation = self.by_key["Expl_calib"]
        self.assertNotIn("journal", citation)
        self.assertEqual(citation["status"], "Under review")


if __name__ == "__main__":
    unittest.main()
