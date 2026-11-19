"""Core Truth Maintenance System (TMS) Belief Revision Tracker."""
from typing import Dict, List, Set, Optional

class BeliefNode:
    def __init__(self, node_id: str, is_premise: bool = False, is_active: bool = True):
        self.node_id = node_id
        self.is_premise = is_premise
        self.is_active = is_active
        self.justifications: List[Set[str]] = [] # list of antecedent premise sets

class BeliefRevisionTracker:
    def __init__(self):
        self.nodes: Dict[str, BeliefNode] = {}

    def add_premise(self, node_id: str, active: bool = True) -> BeliefNode:
        node = BeliefNode(node_id, is_premise=True, is_active=active)
        self.nodes[node_id] = node
        return node

    def add_justification(self, derived_id: str, antecedents: List[str]) -> BeliefNode:
        if derived_id not in self.nodes:
            self.nodes[derived_id] = BeliefNode(derived_id, is_premise=False)
        self.nodes[derived_id].justifications.append(set(antecedents))
        self._propagate()
        return self.nodes[derived_id]

    def retract_premise(self, premise_id: str):
        if premise_id in self.nodes and self.nodes[premise_id].is_premise:
            self.nodes[premise_id].is_active = False
            self._propagate()

    def _propagate(self):
        changed = True
        while changed:
            changed = False
            for node in self.nodes.values():
                if node.is_premise:
                    continue
                # Node is active if ANY justification has all antecedents active
                any_valid = False
                for just in node.justifications:
                    if all(self.nodes.get(ant) and self.nodes[ant].is_active for ant in just):
                        any_valid = True
                        break
                if node.is_active != any_valid:
                    node.is_active = any_valid
                    changed = True

    def is_believed(self, node_id: str) -> bool:
        return bool(self.nodes.get(node_id) and self.nodes[node_id].is_active)
