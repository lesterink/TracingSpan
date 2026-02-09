# test_tracingspan.py
"""
Tests for TracingSpan module.
"""

import unittest
from tracingspan import TracingSpan

class TestTracingSpan(unittest.TestCase):
    """Test cases for TracingSpan class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TracingSpan()
        self.assertIsInstance(instance, TracingSpan)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TracingSpan()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
