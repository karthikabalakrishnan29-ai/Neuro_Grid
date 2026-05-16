from utils.constants import GRID_FREQUENCY, NOMINAL_VOLTAGE

class StabilityMonitor:
    def check_stability(self, current_v, current_f):
        """Checks if grid is within +/- 5% of nominal values"""
        v_deviation = abs(current_v - NOMINAL_VOLTAGE) / NOMINAL_VOLTAGE
        f_deviation = abs(current_f - GRID_FREQUENCY) / GRID_FREQUENCY
        
        is_stable = v_deviation < 0.05 and f_deviation < 0.02
        status = "STABLE" if is_stable else "UNSTABLE"
        
        return {
            "status": status,
            "v_deviation": round(v_deviation * 100, 2),
            "f_deviation": round(f_deviation * 100, 2)
        }