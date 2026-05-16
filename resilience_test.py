class ResilienceTester:
    def calculate_score(self, recovery_time, unserved_energy):
        """
        Failure-kku apram system eppadi recovery aaguthu?
        """
        # Lower recovery time = Higher Resilience
        score = 100 - (recovery_time * 2) - (unserved_energy * 0.5)
        return max(0, score)