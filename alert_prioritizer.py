class AlertPrioritizer:
    def categorize(self, anomaly_score, reasons):
        """
        Severity calculation based on number of issues
        """
        if any("Surge" in r for r in reasons) or len(reasons) > 2:
            return "CRITICAL", "Immediate Action Required: Shutdown recommended."
        
        if len(reasons) == 1:
            return "WARNING", "System monitoring required."
            
        return "INFO", "Minor deviation detected."