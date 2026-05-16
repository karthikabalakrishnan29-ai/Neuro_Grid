class RootCauseAnalyzer:
    def analyze(self, anomaly_data, thresholds):
        """
        Features-a normal limits kooda compare panni 
        root cause-a kandupidippom.
        """
        reasons = []
        
        if anomaly_data['Voltage_V'] < thresholds['min_v']:
            reasons.append("Voltage Brownout (Under-voltage)")
        elif anomaly_data['Voltage_V'] > thresholds['max_v']:
            reasons.append("Voltage Surge (Over-voltage)")
            
        if abs(anomaly_data['Frequency_Hz'] - 50.0) > 0.5:
            reasons.append("Frequency Instability")
            
        if not reasons:
            reasons.append("Transient Noise / Unknown Spike")
            
        return reasons