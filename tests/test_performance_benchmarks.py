"""
Performance benchmarks for the required domain system.

This module tests the performance impact of new parameter validation,
benchmarks various domain/context combinations, and ensures response
times remain acceptable.
"""

import time
import pytest
import statistics
from typing import List, Dict, Any
from divergent_thinking_mcp.divergent_mcp import DivergentThinkingServer
from divergent_thinking_mcp.validators import ThoughtValidator
from divergent_thinking_mcp.exceptions import ValidationError


class TestDomainValidationPerformance:
    """Test suite for domain validation performance."""
    
    def test_single_domain_validation_speed(self):
        """Test speed of validating a single domain."""
        domain = "artificial intelligence"
        
        # Warm up
        for _ in range(10):
            ThoughtValidator.validate_domain(domain)
        
        # Benchmark
        times = []
        for _ in range(1000):
            start = time.perf_counter()
            ThoughtValidator.validate_domain(domain)
            end = time.perf_counter()
            times.append(end - start)
        
        avg_time = statistics.mean(times)
        max_time = max(times)
        
        # Should be very fast (under 1ms average, under 5ms max)
        assert avg_time < 0.001, f"Average validation time too slow: {avg_time:.6f}s"
        assert max_time < 0.005, f"Max validation time too slow: {max_time:.6f}s"
        
        print(f"Domain validation - Avg: {avg_time:.6f}s, Max: {max_time:.6f}s")
    
    def test_all_domains_validation_speed(self):
        """Test speed of validating all 78 domains."""
        domains = list(ThoughtValidator.VALID_DOMAINS)
        
        # Warm up
        for domain in domains[:10]:
            ThoughtValidator.validate_domain(domain)
        
        # Benchmark all domains
        start = time.perf_counter()
        for domain in domains:
            ThoughtValidator.validate_domain(domain)
        end = time.perf_counter()
        
        total_time = end - start
        avg_per_domain = total_time / len(domains)
        
        # Should validate all 78 domains in under 100ms
        assert total_time < 0.1, f"Total validation time too slow: {total_time:.6f}s"
        assert avg_per_domain < 0.002, f"Average per domain too slow: {avg_per_domain:.6f}s"
        
        print(f"All domains validation - Total: {total_time:.6f}s, Avg per domain: {avg_per_domain:.6f}s")
    
    def test_invalid_domain_validation_speed(self):
        """Test speed of rejecting invalid domains."""
        invalid_domains = [
            "invalid_domain",
            "technology",
            "random text",
            "PRODUCT DESIGN",
            "mobile development"
        ]
        
        # Benchmark invalid domain validation
        times = []
        for domain in invalid_domains:
            for _ in range(100):  # Test each invalid domain 100 times
                start = time.perf_counter()
                try:
                    ThoughtValidator.validate_domain(domain)
                except ValidationError:
                    pass  # Expected
                end = time.perf_counter()
                times.append(end - start)
        
        avg_time = statistics.mean(times)
        max_time = max(times)
        
        # Invalid domain validation should also be fast
        assert avg_time < 0.001, f"Average invalid validation time too slow: {avg_time:.6f}s"
        assert max_time < 0.005, f"Max invalid validation time too slow: {max_time:.6f}s"
        
        print(f"Invalid domain validation - Avg: {avg_time:.6f}s, Max: {max_time:.6f}s")


class TestContextCreationPerformance:
    """Test suite for creativity context creation performance."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.server = DivergentThinkingServer()
    
    def test_minimal_context_creation_speed(self):
        """Test speed of creating context with minimal data."""
        thought_data = {"domain": "product design"}
        
        # Warm up
        for _ in range(10):
            self.server.create_creativity_context(thought_data)
        
        # Benchmark
        times = []
        for _ in range(1000):
            start = time.perf_counter()
            context = self.server.create_creativity_context(thought_data)
            end = time.perf_counter()
            times.append(end - start)
            
            # Verify context is created correctly
            assert context.domain == "product design"
        
        avg_time = statistics.mean(times)
        max_time = max(times)
        
        # Should be very fast (under 1ms average)
        assert avg_time < 0.001, f"Average context creation time too slow: {avg_time:.6f}s"
        assert max_time < 0.005, f"Max context creation time too slow: {max_time:.6f}s"
        
        print(f"Minimal context creation - Avg: {avg_time:.6f}s, Max: {max_time:.6f}s")
    
    def test_full_context_creation_speed(self):
        """Test speed of creating context with all parameters."""
        thought_data = {
            "domain": "artificial intelligence",
            "target_audience": "machine learning researchers",
            "time_period": "next 5 years",
            "resources": "high-performance computing, large datasets, expert team",
            "goals": "breakthrough accuracy, ethical AI, real-world deployment",
            "constraint": "must be explainable and transparent"
        }
        
        # Warm up
        for _ in range(10):
            self.server.create_creativity_context(thought_data)
        
        # Benchmark
        times = []
        for _ in range(500):
            start = time.perf_counter()
            context = self.server.create_creativity_context(thought_data)
            end = time.perf_counter()
            times.append(end - start)
            
            # Verify context is created correctly
            assert context.domain == "artificial intelligence"
            assert len(context.resources) == 3
            assert len(context.goals) == 3
        
        avg_time = statistics.mean(times)
        max_time = max(times)
        
        # Should still be fast even with full context (under 2ms average)
        assert avg_time < 0.002, f"Average full context creation time too slow: {avg_time:.6f}s"
        assert max_time < 0.01, f"Max full context creation time too slow: {max_time:.6f}s"
        
        print(f"Full context creation - Avg: {avg_time:.6f}s, Max: {max_time:.6f}s")
    
    def test_context_creation_with_different_domains(self):
        """Test context creation performance across different domains."""
        domains = [
            "product design", "artificial intelligence", "healthcare technology",
            "sustainable agriculture", "mobile app development", "cybersecurity",
            "e-commerce", "renewable energy", "educational technology", "urban transportation"
        ]
        
        times_by_domain = {}
        
        for domain in domains:
            thought_data = {
                "domain": domain,
                "target_audience": "professionals",
                "resources": "standard tools, experienced team",
                "goals": "innovation, efficiency"
            }
            
            # Benchmark this domain
            times = []
            for _ in range(100):
                start = time.perf_counter()
                context = self.server.create_creativity_context(thought_data)
                end = time.perf_counter()
                times.append(end - start)
                
                assert context.domain == domain
            
            times_by_domain[domain] = {
                'avg': statistics.mean(times),
                'max': max(times)
            }
        
        # Check that all domains perform similarly
        all_avg_times = [stats['avg'] for stats in times_by_domain.values()]
        all_max_times = [stats['max'] for stats in times_by_domain.values()]
        
        overall_avg = statistics.mean(all_avg_times)
        overall_max = max(all_max_times)
        
        assert overall_avg < 0.002, f"Overall average time too slow: {overall_avg:.6f}s"
        assert overall_max < 0.01, f"Overall max time too slow: {overall_max:.6f}s"
        
        # Check variance - no domain should be significantly slower
        avg_variance = statistics.variance(all_avg_times)
        assert avg_variance < 0.000001, f"Too much variance between domains: {avg_variance:.9f}"
        
        print(f"Cross-domain performance - Overall avg: {overall_avg:.6f}s, Max: {overall_max:.6f}s")


class TestValidationPerformance:
    """Test suite for comprehensive validation performance."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.server = DivergentThinkingServer()
    
    def test_thought_data_validation_speed(self):
        """Test speed of complete thought data validation."""
        thought_data = {
            "thought": "Create an innovative AI-powered healthcare solution",
            "thinking_method": "structured_process",
            "domain": "healthcare technology",
            "target_audience": "medical professionals",
            "time_period": "next 3 years",
            "resources": "cloud infrastructure, medical datasets, expert team",
            "goals": "improve patient outcomes, reduce costs, enhance efficiency",
            "thoughtNumber": 1,
            "totalThoughts": 3,
            "nextThoughtNeeded": True
        }
        
        # Warm up
        for _ in range(10):
            self.server.validate_thought_data(thought_data)
        
        # Benchmark
        times = []
        for _ in range(500):
            start = time.perf_counter()
            validated_data = self.server.validate_thought_data(thought_data)
            end = time.perf_counter()
            times.append(end - start)
            
            # Verify validation worked
            assert validated_data["domain"] == "healthcare technology"
            assert validated_data["thought"] == thought_data["thought"]
        
        avg_time = statistics.mean(times)
        max_time = max(times)
        
        # Complete validation should be fast (under 5ms average)
        assert avg_time < 0.005, f"Average validation time too slow: {avg_time:.6f}s"
        assert max_time < 0.02, f"Max validation time too slow: {max_time:.6f}s"
        
        print(f"Complete thought validation - Avg: {avg_time:.6f}s, Max: {max_time:.6f}s")
    
    def test_validation_error_performance(self):
        """Test performance when validation errors occur."""
        invalid_data_sets = [
            {"thought": "test", "thinking_method": "invalid_method", "domain": "product design"},
            {"thought": "test", "thinking_method": "structured_process", "domain": "invalid_domain"},
            {"thought": "", "thinking_method": "structured_process", "domain": "product design"},
            {"thinking_method": "structured_process", "domain": "product design"},  # Missing thought
        ]
        
        times = []
        error_count = 0
        
        for invalid_data in invalid_data_sets:
            for _ in range(100):
                start = time.perf_counter()
                try:
                    self.server.validate_thought_data(invalid_data)
                except ValidationError:
                    error_count += 1
                end = time.perf_counter()
                times.append(end - start)
        
        avg_time = statistics.mean(times)
        max_time = max(times)
        
        # Error handling should also be fast
        assert avg_time < 0.005, f"Average error handling time too slow: {avg_time:.6f}s"
        assert max_time < 0.02, f"Max error handling time too slow: {max_time:.6f}s"
        assert error_count > 0, "Expected validation errors to occur"
        
        print(f"Validation error handling - Avg: {avg_time:.6f}s, Max: {max_time:.6f}s, Errors: {error_count}")


class TestMemoryUsage:
    """Test suite for memory usage analysis."""
    
    def test_domain_validation_memory_efficiency(self):
        """Test that domain validation doesn't create excessive objects."""
        import gc
        import sys

        # Get baseline object count
        gc.collect()
        baseline_objects = len(gc.get_objects())

        # Perform many domain validations
        domains = list(ThoughtValidator.VALID_DOMAINS)
        for _ in range(100):  # Reduced iterations for simpler test
            for domain in domains:
                ThoughtValidator.validate_domain(domain)

        # Check object count after operations
        gc.collect()
        final_objects = len(gc.get_objects())
        object_increase = final_objects - baseline_objects

        # Object increase should be minimal (under 1000 new objects)
        assert object_increase < 1000, f"Too many new objects created: {object_increase}"

        print(f"Object count - Baseline: {baseline_objects}, "
              f"Final: {final_objects}, "
              f"Increase: {object_increase}")
    
    def test_context_creation_memory_efficiency(self):
        """Test that context creation doesn't create excessive objects."""
        import gc
        import sys

        server = DivergentThinkingServer()

        # Get baseline object count
        gc.collect()
        baseline_objects = len(gc.get_objects())

        # Create many contexts
        thought_data = {
            "domain": "artificial intelligence",
            "target_audience": "researchers",
            "resources": "computing resources, datasets",
            "goals": "innovation, efficiency"
        }

        contexts = []
        for _ in range(100):  # Reduced iterations for simpler test
            context = server.create_creativity_context(thought_data)
            contexts.append(context)

        # Check object count after operations
        gc.collect()
        final_objects = len(gc.get_objects())
        object_increase = final_objects - baseline_objects

        # Object increase should be reasonable (under 2000 new objects for 100 contexts)
        assert object_increase < 2000, f"Too many new objects created: {object_increase}"

        print(f"Context creation objects - Baseline: {baseline_objects}, "
              f"Final: {final_objects}, "
              f"Increase: {object_increase}")


class TestScalabilityBenchmarks:
    """Test suite for scalability under load."""
    
    def test_concurrent_domain_validation(self):
        """Test domain validation under concurrent load simulation."""
        import concurrent.futures
        import threading
        
        domains = list(ThoughtValidator.VALID_DOMAINS)
        results = []
        
        def validate_domains_batch():
            """Validate a batch of domains and measure time."""
            start = time.perf_counter()
            for domain in domains:
                ThoughtValidator.validate_domain(domain)
            end = time.perf_counter()
            return end - start
        
        # Simulate concurrent validation (10 threads)
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            futures = [executor.submit(validate_domains_batch) for _ in range(10)]
            for future in concurrent.futures.as_completed(futures):
                results.append(future.result())
        
        avg_batch_time = statistics.mean(results)
        max_batch_time = max(results)
        
        # Even under concurrent load, should be fast
        assert avg_batch_time < 0.5, f"Average batch time under load too slow: {avg_batch_time:.6f}s"
        assert max_batch_time < 1.0, f"Max batch time under load too slow: {max_batch_time:.6f}s"
        
        print(f"Concurrent validation - Avg batch: {avg_batch_time:.6f}s, Max batch: {max_batch_time:.6f}s")
