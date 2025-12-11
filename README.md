# Stepper Motor Controller - ASIC Design

A complete open-source ASIC design for stepper motor control using the Skywater 130nm PDK and OpenLane EDA flow.

## 📋 Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Quick Start](#quick-start)
- [Design Metrics](#design-metrics)
- [Repository Structure](#repository-structure)
- [Documentation](#documentation)
- [Design Flow](#design-flow)
- [Reports & Analysis](#reports--analysis)
- [Getting Started](#getting-started)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Overview

This repository contains a complete ASIC implementation of a stepper motor controller. The design is fully implemented using:

- **PDK**: Skywater 130nm (sky130_fd_sc_hd)
- **Flow**: OpenLane (open-source RTL-to-GDSII flow)
- **EDA Tools**: 
  - Synthesis: Yosys
  - Place & Route: OpenROAD
  - Verification: Magic (DRC/LVS)
  - Simulation: Verilator
- **Design Language**: Verilog HDL

The design demonstrates a complete modern semiconductor design flow from RTL to GDSII layout, suitable for educational purposes and practical chip design.

---

## ✨ Key Features

### Design Characteristics
- **Die Area**: 4,998 µm² (~0.005 mm²)
- **Core Area**: 2,953 µm² 
- **Total Cells**: 429 cells (134 logic cells + 295 utility cells)
- **Operating Frequency**: 50 MHz
- **Technology Node**: 130nm (Skywater PDK)

### Functional Features
- Full stepper motor control logic
- 27 primary inputs
- 30 primary outputs
- 24 flip-flops for sequential logic
- Maximum logic depth: 8 levels
- Zero design violations (clean DRC/LVS)

### Performance Metrics
- **Timing**: 1.26 ns critical path with 18.74 ns slack
- **Power**: ~0.0001314 µW (typical corner)
- **Utilization**: 54.05% (OpenDP)
- **Memory**: <1GB peak during flow
- **Runtime**: 1 minute 22 seconds (complete flow)

---

## 🚀 Quick Start

### View Design Reports

Generate comprehensive design analysis reports:

```bash
# Area report (die area, utilization, cell statistics)
python3 area_report.py

# Timing report (critical path, slack, clock constraints)
python3 timing_report.py

# Power report (internal, switching, leakage power)
python3 power_report.py
```

### Inspect Layout

View the final GDSII layout:

```bash
# GDS file location
gds/stepper_ctrl.gds

# View with KLayout (if installed)
klayout gds/stepper_ctrl.gds
```

### Review Configuration

Check the OpenLane flow configuration:

```bash
cat OpenLane/designs/stepper_ctrl/config.tcl
```

---

## 📊 Design Metrics

### Area Metrics
| Metric | Value |
|--------|-------|
| Die Area | 4,998 µm² |
| Core Area | 2,953 µm² |
| Aspect Ratio | 1:1 |
| Cell Density | ~32,412 cells/mm² |

### Cell Distribution
| Cell Type | Count | Purpose |
|-----------|-------|---------|
| Logic Cells | 134 | Functional logic |
| Decap Cells | 149 | Power decoupling |
| Welltap Cells | 44 | Well biasing |
| Fill Cells | 74 | Density compliance |
| **Total** | **429** | **All cells** |

### Gate-Level Statistics
| Gate Type | Count |
|-----------|-------|
| AND gates | 2 |
| NAND gates | 15 |
| OR gates | 38 |
| NOR gates | 1 |
| XOR gates | 23 |
| MUX | 2 |
| Flip-Flops | 24 |

### Timing Summary
| Parameter | Value |
|-----------|-------|
| Clock Period | 20.0 ns |
| Frequency | 50 MHz |
| Critical Path | 1.26 ns |
| Slack | 18.74 ns |
| Path Utilization | 6.3% |

### Power Summary (Typical)
| Component | Power |
|-----------|-------|
| Internal | 9.61e-05 µW (73.13%) |
| Switching | 3.53e-05 µW (26.86%) |
| Leakage | 1.11e-09 µW (0.00%) |
| **Total** | **0.0001314 µW** |

### Quality Metrics
| Check | Status |
|-------|--------|
| Routing Violations | 0 ✓ |
| Short Violations | 0 ✓ |
| Metal Spacing Violations | 0 ✓ |
| LVS Errors | 0 ✓ |
| DRC Violations | 0 ✓ |

---

## 📁 Repository Structure

```
stepper_motor/
├── README.md                    # This file - start here!
├── REPORTS_README.md            # Documentation for report generators
├── DESIGN.md                    # Detailed design specifications
├── FLOW.md                      # Design flow documentation
├── ARCHITECTURE.md              # Architecture and block diagrams
├── QUICKSTART.md                # Quick start guide
│
├── area_report.py               # Area analysis script
├── timing_report.py             # Timing analysis script
├── power_report.py              # Power analysis script
│
├── gds/
│   └── stepper_ctrl.gds         # Final GDSII layout
│
├── reports/
│   └── stepper_ctrl/
│       ├── metrics.csv          # Complete design metrics
│       ├── logs/                # OpenLane flow logs
│       └── signoff/             # Final verification reports
│
└── OpenLane/
    ├── designs/stepper_ctrl/    # Design configuration
    ├── configuration/           # Flow configuration files
    └── scripts/                 # EDA tool scripts
```

---

## 📚 Documentation

Comprehensive documentation is organized by topic:

### For First-Time Users
1. **[QUICKSTART.md](QUICKSTART.md)** - Get up and running in 5 minutes
2. **[DESIGN.md](DESIGN.md)** - Understand what the design does
3. **[ARCHITECTURE.md](ARCHITECTURE.md)** - Architecture overview and block diagrams

### For Detailed Learning
4. **[FLOW.md](FLOW.md)** - Complete design flow explanation
5. **[REPORTS_README.md](REPORTS_README.md)** - How to generate and understand reports

### For Implementation Details
- OpenLane configuration: `OpenLane/designs/stepper_ctrl/config.tcl`
- RTL source files: Check OpenLane/designs/stepper_ctrl/ directory
- Timing constraints: Review report outputs

---

## 🔄 Design Flow

```
RTL (Verilog)
    ↓
[SYNTHESIS] - Yosys
    ├─ Logic synthesis
    ├─ Optimization
    └─ Cell mapping
    ↓
Gate-Level Netlist
    ↓
[FLOORPLANNING] - OpenROAD
    ├─ Die size: 4,998 µm²
    ├─ Core area: 2,953 µm²
    └─ 50% core utilization
    ↓
[PLACEMENT] - OpenROAD
    ├─ 134 logic cells
    ├─ 295 utility cells
    └─ 54.05% utilization
    ↓
[ROUTING] - TritonRoute
    ├─ Wire length: 2,626 µm
    ├─ Via count: 1,027
    └─ 0 violations
    ↓
[VERIFICATION]
    ├─ DRC (Magic): PASS ✓
    ├─ LVS (Netgen): PASS ✓
    └─ Antenna checks: PASS ✓
    ↓
GDS-II Layout
    ↓
→ stepper_ctrl.gds (Ready for fabrication)
```

**Flow Status**: ✅ COMPLETED
**Total Runtime**: 1 minute 22 seconds
**Flow Configuration**: RUN_2025.12.11_08.03.01

---

## 📈 Reports & Analysis

### Automated Report Generation

Run analysis scripts to understand your design:

```bash
# Area report (die area, utilization, cells)
python3 area_report.py      # Die area, utilization, cells
python3 timing_report.py    # Timing paths, slack, frequency
python3 power_report.py     # Power dissipation analysis
```

### Report Contents

1. **Area Report** - Covers:
   - Die and core area metrics
   - Cell utilization percentages
   - Cell type breakdown
   - Gate-level statistics

2. **Timing Report** - Covers:
   - Clock constraints
   - Critical path analysis
   - Setup/hold timing
   - Logic depth and complexity

3. **Power Report** - Covers:
   - Power at different corners
   - Internal/switching/leakage breakdown
   - Power density
   - Temperature analysis

See [REPORTS_README.md](REPORTS_README.md) for detailed report documentation.

---

## 🎓 Getting Started

### Prerequisites
- Python 3.x (for report generation)
- Git (to clone repository)
- Optional: KLayout (to view GDS)

### Installation

```bash
# Clone the repository
git clone https://github.com/deepak-pg21/stepper_motor.git
cd stepper_motor

# Make scripts executable
chmod +x area_report.py timing_report.py power_report.py

# Generate reports
python3 area_report.py
```

### Next Steps

1. **Read the documentation** in order:
   - [QUICKSTART.md](QUICKSTART.md) (5 min read)
   - [DESIGN.md](DESIGN.md) (10 min read)
   - [ARCHITECTURE.md](ARCHITECTURE.md) (15 min read)

2. **Run the reports** to see actual metrics:
   ```bash
   python3 area_report.py
   python3 timing_report.py
   python3 power_report.py
   ```

3. **Explore the files**:
   - Check `reports/stepper_ctrl/metrics.csv` for complete data
   - View `gds/stepper_ctrl.gds` with KLayout
   - Read `OpenLane/designs/stepper_ctrl/config.tcl` for configuration

---

## 🏆 Design Highlights

✅ **Zero Violations** - Clean DRC/LVS verification
✅ **Fast Runtime** - Complete flow in <2 minutes
✅ **Low Power** - Optimized for minimal power dissipation
✅ **Good Timing** - 18.74 ns timing slack at 50 MHz
✅ **Compact Design** - ~0.005 mm² in 130nm technology
✅ **Production Ready** - GDS-II ready for fabrication

---

## 📝 File Summary

| File | Purpose |
|------|---------|
| `area_report.py` | Generate area analysis |
| `timing_report.py` | Generate timing analysis |
| `power_report.py` | Generate power analysis |
| `gds/stepper_ctrl.gds` | Final GDSII layout |
| `reports/stepper_ctrl/metrics.csv` | Complete metrics data |

---

## 🤝 Contributing

This is an educational design showcase. Contributions welcome!

Possible contributions:
- Additional documentation
- Report enhancements
- Flow improvements
- Results optimization
- Educational materials

---

## 📄 License

This project uses the Skywater 130nm PDK. Please refer to individual components for licensing details.

---

## 📞 Questions?

Refer to the documentation files for detailed information:
- **Quick questions?** → [QUICKSTART.md](QUICKSTART.md)
- **How does it work?** → [DESIGN.md](DESIGN.md)
- **Show me the design?** → [ARCHITECTURE.md](ARCHITECTURE.md)
- **How is it built?** → [FLOW.md](FLOW.md)
- **Generate reports?** → [REPORTS_README.md](REPORTS_README.md)

---

**Status**: ✅ Design Complete | **Last Updated**: December 11, 2025 | **Technology**: 130nm (sky130)