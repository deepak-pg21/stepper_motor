#!/usr/bin/env python3
"""
Power Report Generator for OpenLane Design Metrics
Extracts and displays comprehensive power metrics from OpenLane reports
"""

import csv
import os
from pathlib import Path

def parse_metrics_csv(csv_file):
    """Parse metrics.csv and return a dictionary of metrics"""
    metrics = {}
    
    if not os.path.exists(csv_file):
        print(f"Error: {csv_file} not found")
        return metrics
    
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            metrics = row
            break  # Get first row
    
    return metrics

def safe_float(value):
    """Safely convert value to float"""
    try:
        return float(value) if value and value != 'N/A' else 0.0
    except (ValueError, TypeError):
        return 0.0

def format_power_report(metrics):
    """Format and display power report"""
    
    print("=" * 70)
    print("POWER REPORT - STEPPER_CTRL DESIGN")
    print("=" * 70)
    print()
    
    # Design Information
    print("DESIGN INFORMATION:")
    print("-" * 70)
    print(f"Design Name:          {metrics.get('design_name', 'N/A')}")
    print(f"Config:               {metrics.get('config', 'N/A')}")
    print(f"Flow Status:          {metrics.get('flow_status', 'N/A')}")
    print(f"Total Runtime:        {metrics.get('total_runtime', 'N/A')}")
    print()
    
    # Slowest Corner (Maximum Power)
    print("SLOWEST CORNER (Maximum Power):")
    print("-" * 70)
    pow_slowest_internal = safe_float(metrics.get('power_slowest_internal_uW', 'N/A'))
    pow_slowest_switching = safe_float(metrics.get('power_slowest_switching_uW', 'N/A'))
    pow_slowest_leakage = safe_float(metrics.get('power_slowest_leakage_uW', 'N/A'))
    
    print(f"Internal Power:       {pow_slowest_internal:e} µW")
    print(f"Switching Power:      {pow_slowest_switching:e} µW")
    print(f"Leakage Power:        {pow_slowest_leakage:e} µW")
    
    pow_slowest_total = pow_slowest_internal + pow_slowest_switching + pow_slowest_leakage
    print(f"Total Power:          {pow_slowest_total:e} µW")
    print()
    
    # Typical Corner (Nominal Conditions)
    print("TYPICAL CORNER (Nominal Conditions):")
    print("-" * 70)
    pow_typical_internal = safe_float(metrics.get('power_typical_internal_uW', 'N/A'))
    pow_typical_switching = safe_float(metrics.get('power_typical_switching_uW', 'N/A'))
    pow_typical_leakage = safe_float(metrics.get('power_typical_leakage_uW', 'N/A'))
    
    print(f"Internal Power:       {pow_typical_internal:e} µW")
    print(f"Switching Power:      {pow_typical_switching:e} µW")
    print(f"Leakage Power:        {pow_typical_leakage:e} µW")
    
    pow_typical_total = pow_typical_internal + pow_typical_switching + pow_typical_leakage
    print(f"Total Power:          {pow_typical_total:e} µW")
    print()
    
    # Fastest Corner (Minimum Power)
    print("FASTEST CORNER (Minimum Power):")
    print("-" * 70)
    pow_fastest_internal = safe_float(metrics.get('power_fastest_internal_uW', 'N/A'))
    pow_fastest_switching = safe_float(metrics.get('power_fastest_switching_uW', 'N/A'))
    pow_fastest_leakage = safe_float(metrics.get('power_fastest_leakage_uW', 'N/A'))
    
    print(f"Internal Power:       {pow_fastest_internal:e} µW")
    print(f"Switching Power:      {pow_fastest_switching:e} µW")
    print(f"Leakage Power:        {pow_fastest_leakage:e} µW")
    
    pow_fastest_total = pow_fastest_internal + pow_fastest_switching + pow_fastest_leakage
    print(f"Total Power:          {pow_fastest_total:e} µW")
    print()
    
    # Power Breakdown
    print("POWER BREAKDOWN (Typical Corner):")
    print("-" * 70)
    if pow_typical_total > 0:
        internal_pct = (pow_typical_internal / pow_typical_total) * 100
        switching_pct = (pow_typical_switching / pow_typical_total) * 100
        leakage_pct = (pow_typical_leakage / pow_typical_total) * 100
        
        print(f"Internal:             {internal_pct:6.2f}% ({pow_typical_internal:e} µW)")
        print(f"Switching:            {switching_pct:6.2f}% ({pow_typical_switching:e} µW)")
        print(f"Leakage:              {leakage_pct:6.2f}% ({pow_typical_leakage:e} µW)")
    else:
        print("No power data available")
    print()
    
    # Corner Comparison
    print("CORNER COMPARISON:")
    print("-" * 70)
    print(f"Slowest Total:        {pow_slowest_total:e} µW (Reference: 100%)")
    if pow_slowest_total > 0:
        print(f"Typical Total:        {pow_typical_total:e} µW ({(pow_typical_total/pow_slowest_total)*100:.1f}% of slowest)")
        print(f"Fastest Total:        {pow_fastest_total:e} µW ({(pow_fastest_total/pow_slowest_total)*100:.1f}% of slowest)")
    print()
    
    # Leakage Analysis
    print("LEAKAGE ANALYSIS:")
    print("-" * 70)
    print(f"Slowest (Max):        {pow_slowest_leakage:e} µW")
    print(f"Typical:              {pow_typical_leakage:e} µW")
    print(f"Fastest (Min):        {pow_fastest_leakage:e} µW")
    
    if pow_slowest_leakage > 0:
        leakage_pct_slowest = (pow_slowest_leakage / pow_slowest_total) * 100
        print(f"Leakage % (Slowest):  {leakage_pct_slowest:.4f}% of total power")
    print()
    
    # Design Metrics for Power Context
    print("DESIGN METRICS (for context):")
    print("-" * 70)
    total_cells = safe_float(metrics.get('TotalCells', 'N/A'))
    core_area_um2 = safe_float(metrics.get('CoreArea_um^2', 'N/A'))
    clock_period = metrics.get('CLOCK_PERIOD', 'N/A')
    
    print(f"Total Cells:          {int(total_cells)}")
    print(f"Core Area:            {core_area_um2:,.0f} µm²")
    print(f"Clock Period:         {clock_period} ns")
    
    if core_area_um2 > 0 and pow_typical_total > 0:
        power_per_area = pow_typical_total / (core_area_um2 / 1e6)
        print(f"Power Density:        {power_per_area:.4e} µW/mm²")
    print()
    
    # Standard Cell Library
    print("=" * 70)
    print(f"Standard Cell Library: {metrics.get('STD_CELL_LIBRARY', 'N/A')}")
    print(f"Peak Memory Usage:     {metrics.get('Peak_Memory_Usage_MB', 'N/A')} MB")
    print("=" * 70)

def main():
    """Main function"""
    csv_file = "/workspaces/stepper_motor/reports/stepper_ctrl/metrics.csv"
    
    metrics = parse_metrics_csv(csv_file)
    
    if metrics:
        format_power_report(metrics)
    else:
        print("No metrics found. Please run OpenLane flow first.")

if __name__ == "__main__":
    main()
