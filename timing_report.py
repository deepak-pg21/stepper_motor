#!/usr/bin/env python3
"""
Timing Report Generator for OpenLane Design Metrics
Extracts and displays comprehensive timing metrics from OpenLane reports
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

def format_timing_report(metrics):
    """Format and display timing report"""
    
    print("=" * 70)
    print("TIMING REPORT - STEPPER_CTRL DESIGN")
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
    
    # Clock Constraints
    print("CLOCK CONSTRAINTS:")
    print("-" * 70)
    clock_period = metrics.get('CLOCK_PERIOD', 'N/A')
    suggested_freq = metrics.get('suggested_clock_frequency', 'N/A')
    suggested_period = metrics.get('suggested_clock_period', 'N/A')
    
    print(f"Clock Period (ns):    {clock_period}")
    print(f"Max Frequency (MHz):  {suggested_freq}")
    print(f"Suggested Period:     {suggested_period} ns")
    print()
    
    # Critical Path Timing
    print("CRITICAL PATH TIMING:")
    print("-" * 70)
    crit_path = metrics.get('critical_path_ns', 'N/A')
    print(f"Critical Path (ns):   {crit_path}")
    
    try:
        crit_path_float = float(crit_path) if crit_path != 'N/A' else 0
        clock_period_float = float(clock_period) if clock_period != 'N/A' else 0
        if crit_path_float > 0 and clock_period_float > 0:
            slack_ns = clock_period_float - crit_path_float
            print(f"Slack (ns):           {slack_ns:.3f}")
            utilization = (crit_path_float / clock_period_float) * 100
            print(f"Path Utilization:     {utilization:.1f}%")
    except (ValueError, TypeError):
        pass
    print()
    
    # Worst Negative Slack
    print("SLACK ANALYSIS:")
    print("-" * 70)
    wns = metrics.get('wns', 'N/A')
    tns = metrics.get('tns', 'N/A')
    pl_wns = metrics.get('pl_wns', 'N/A')
    pl_tns = metrics.get('pl_tns', 'N/A')
    optimized_wns = metrics.get('optimized_wns', 'N/A')
    optimized_tns = metrics.get('optimized_tns', 'N/A')
    
    print("Post-Synthesis:")
    print(f"  WNS (Worst Neg Slack):  {wns} ns")
    print(f"  TNS (Total Neg Slack):  {tns} ns")
    print()
    print("Post-Placement:")
    print(f"  WNS:                    {pl_wns} ns")
    print(f"  TNS:                    {pl_tns} ns")
    print()
    print("Post-Optimization:")
    print(f"  WNS:                    {optimized_wns} ns")
    print(f"  TNS:                    {optimized_tns} ns")
    print()
    
    # Routing Timing
    print("ROUTING STAGE TIMING:")
    print("-" * 70)
    fastroute_wns = metrics.get('fastroute_wns', 'N/A')
    fastroute_tns = metrics.get('fastroute_tns', 'N/A')
    spef_wns = metrics.get('spef_wns', 'N/A')
    spef_tns = metrics.get('spef_tns', 'N/A')
    
    print(f"FastRoute WNS:        {fastroute_wns} ns")
    print(f"FastRoute TNS:        {fastroute_tns} ns")
    print(f"SPEF WNS:             {spef_wns} ns")
    print(f"SPEF TNS:             {spef_tns} ns")
    print()
    
    # Logic Depth
    print("LOGIC DEPTH:")
    print("-" * 70)
    level = metrics.get('level', 'N/A')
    print(f"Max Logic Levels:     {level}")
    print()
    
    # Circuit Complexity
    print("CIRCUIT COMPLEXITY:")
    print("-" * 70)
    inputs = metrics.get('inputs', 'N/A')
    outputs = metrics.get('outputs', 'N/A')
    cells_pre_abc = metrics.get('cells_pre_abc', 'N/A')
    synth_cells = metrics.get('synth_cell_count', 'N/A')
    
    print(f"Primary Inputs:       {inputs}")
    print(f"Primary Outputs:      {outputs}")
    print(f"Pre-ABC Cells:        {cells_pre_abc}")
    print(f"Synthesized Cells:    {synth_cells}")
    print()
    
    # Cell Types
    print("SEQUENTIAL ELEMENTS:")
    print("-" * 70)
    dff = metrics.get('DFF', 'N/A')
    print(f"Flip-Flops (DFF):     {dff}")
    print()
    
    # Memory Elements
    print("MEMORY ELEMENTS:")
    print("-" * 70)
    mem_count = metrics.get('memories_count', 'N/A')
    mem_bits = metrics.get('memory_bits', 'N/A')
    print(f"Memory Count:         {mem_count}")
    print(f"Memory Bits:          {mem_bits}")
    print()
    
    # Library Information
    print("=" * 70)
    print(f"Standard Cell Library: {metrics.get('STD_CELL_LIBRARY', 'N/A')}")
    print(f"Synthesis Strategy:    {metrics.get('SYNTH_STRATEGY', 'N/A')}")
    print("=" * 70)

def main():
    """Main function"""
    csv_file = "/workspaces/stepper_motor/reports/stepper_ctrl/metrics.csv"
    
    metrics = parse_metrics_csv(csv_file)
    
    if metrics:
        format_timing_report(metrics)
    else:
        print("No metrics found. Please run OpenLane flow first.")

if __name__ == "__main__":
    main()
