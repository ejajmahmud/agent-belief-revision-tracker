"""Tests for Belief Tracker."""
import unittest
from agent_belief_revision_tracker.core import BeliefRevisionTracker

class TestBeliefRevisionTracker(unittest.TestCase):
    def test_dependency_retraction(self):
        tms = BeliefRevisionTracker()
        tms.add_premise("p1", True)
        tms.add_premise("p2", True)
        tms.add_justification("c1", ["p1", "p2"])
        tms.add_justification("c2", ["c1"])
        
        self.assertTrue(tms.is_believed("c2"))
        tms.retract_premise("p1")
        self.assertFalse(tms.is_believed("c1"))
        self.assertFalse(tms.is_believed("c2"))
