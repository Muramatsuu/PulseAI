# test_pulseai.py
"""
Tests for PulseAI module.
"""

import unittest
from pulseai import PulseAI

class TestPulseAI(unittest.TestCase):
    """Test cases for PulseAI class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PulseAI()
        self.assertIsInstance(instance, PulseAI)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PulseAI()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
