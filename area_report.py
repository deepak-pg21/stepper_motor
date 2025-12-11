#!/usr/bin/env python3
"""
Area Report Generator for OpenLane Design Metrics
Extracts and displays comprehensive area metrics from OpenLane reports
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

def format_area_report(metrics):
    """Format and display area report"""
    
    print("=" * 70)
    print("AREA REPORT - STEPPER_CTRL DESIGN")
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
    
    # Area Metrics
    print("AREA METRICS:")
    print("-" * 70)
    
    die_area_mm2 = float(metrics.get('DIEAREA_mm^2', 0)) if metrics.get('DIEAREA_mm^2') else 0
    core_area_um2 = float(metrics.get('CoreArea_um^2', 0)) if metrics.get('CoreArea_um^2') else 0
    core_area_mm2 = core_area_um2 / 1_000_000 if core_area_um2 else 0
    
    print(f"Die Area:             {die_area_mm2:.6f} mm²")
    print(f"Core Area:            {core_area_um2:,.0f} µm² ({core_area_mm2:.6f} mm²)")
    print(f"Die Area (µm²):       {die_area_mm2 * 1_000_000:,.0f} µm²")
    print()
    
    # Utilization
    print("UTILIZATION:")
    print("-" * 70)
    print(f"OpenDP Utilization:   {metrics.get('OpenDP_Util', 'N/A')}%")
    print(f"Final Utilization:    {metrics.get('Final_Util', 'N/A')}%")
    print(f"Core Utilization:     {metrics.get('FP_CORE_UTIL', 'N/A')}%")
    print(f"Target Density:       {metrics.get('PL_TARGET_DENSITY', 'N/A')}")
    print(f"Cell Per mm²:         {metrics.get('CellPer_mm^2', 'N/A')}")
    print()
    
    # Cell Information
    print("CELL STATISTICS:")
    print("-" * 70)
    print(f"Total Cells:          {metrics.get('TotalCells', 'N/A')}")
    print(f"Synth Cell Count:     {metrics.get('synth_cell_count', 'N/A')}")
    print(f"Decap Cells:          {metrics.get('DecapCells', 'N/A')}")
    print(f"Welltap Cells:        {metrics.get('WelltapCells', 'N/A')}")
    print(f"Diode Cells:          {metrics.get('DiodeCells', 'N/A')}")
    print(f"Fill Cells:           {metrics.get('FillCells', 'N/A')}")
    print()
    
    # Gate Count
    print("GATE COUNT:")
    print("-" * 70)
    print(f"AND gates:            {metrics.get('AND', 'N/A')}")
    print(f"NAND gates:           {metrics.get('NAND', 'N/A')}")
    print(f"OR gates:             {metrics.get('OR', 'N/A')}")
    print(f"NOR gates:            {metrics.get('NOR', 'N/A')}")
    print(f"XOR gates:            {metrics.get('XOR', 'N/A')}")
    print(f"MUX:                  {metrics.get('MUX', 'N/A')}")
    print(f"DFF (Flip-Flops):     {metrics.get('DFF', 'N/A')}")
    print()
    
    # Routing
    print("ROUTING METRICS:")
    print("-" * 70)
    print(f"Wire Length:          {metrics.get('wire_length', 'N/A')} µm")
    print(f"Via Count:            {metrics.get('vias', 'N/A')}")
    print(f"HPWL:                 {metrics.get('HPWL', 'N/A')} µm")
    print()
    
    # Timing
    print("TIMING METRICS:")
    print("-" * 70)
    print(f"Critical Path (ns):   {metrics.get('critical_path_ns', 'N/A')}")
    print(f"Clock Period (ns):    {metrics.get('CLOCK_PERIOD', 'N/A')}")
    print(f"Max Frequency (MHz):  {metrics.get('suggested_clock_frequency', 'N/A')}")
    print()
    
    # Violations
    print("VIOLATIONS:")
    print("-" * 70)
    print(f"tritonRoute Violations: {metrics.get('tritonRoute_violations', 'N/A')}")
    print(f"Short Violations:     {metrics.get('Short_violations', 'N/A')}")
    print(f"Metal Spacing Viol.:  {metrics.get('MetSpc_violations', 'N/A')}")
    print(f"LVS Errors:           {metrics.get('lvs_total_errors', 'N/A')}")
    print(f"Magic Violations:     {metrics.get('Magic_violations', 'N/A')}")
    print()
    
    # Power
    print("POWER ANALYSIS (Typical):")
    print("-" * 70)
    print(f"Internal Power:       {metrics.get('power_typical_internal_uW', 'N/A')} µW")
    print(f"Switching Power:      {metrics.get('power_typical_switching_uW', 'N/A')} µW")
    print(f"Leakage Power:        {metrics.get('power_typical_leakage_uW', 'N/A')} µW")
    print()
    
    # Floorplan
    print("FLOORPLAN:")
    print("-" * 70)
    print(f"Aspect Ratio:         {metrics.get('FP_ASPECT_RATIO', 'N/A')}")
    print(f"PDN H-Pitch:          {metrics.get('FP_PDN_HPITCH', 'N/A')}")
    print(f"PDN V-Pitch:          {metrics.get('FP_PDN_VPITCH', 'N/A')}")
    print()
    
    # Chip Summary
    print("=" * 70)
    print(f"Standard Cell Library: {metrics.get('STD_CELL_LIBRARY', 'N/A')}")
    print(f"Peak Memory Usage:     {metrics.get('Peak_Memory_Usage_MB', 'N/A')} MB")
    print("=" * 70)

def main():
    """Main function"""
    csv_file = "/workspaces/stepper_motor/reports/stepper_ctrl/metrics.csv"
    
    metrics = parse_metrics_csv(csv_file)
    
    if metrics:
        format_area_report(metrics)
    else:
        print("No metrics found. Please run OpenLane flow first.")

if __name__ == "__main__":
    main()
