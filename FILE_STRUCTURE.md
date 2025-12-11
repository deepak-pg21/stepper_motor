# File Structure and Organization

Complete guide to the repository organization and file descriptions.

## 📁 Repository Structure

```
stepper_motor/
│
├── 📄 README.md                     # Main project overview (start here!)
├── 📄 QUICKSTART.md                 # 5-minute quick start guide
├── 📄 DESIGN.md                     # Technical design specifications
├── 📄 ARCHITECTURE.md               # Architecture and block diagrams
├── 📄 FLOW.md                       # Complete RTL-to-GDS flow documentation
├── 📄 REPORTS_README.md             # Guide to report generation scripts
├── 📄 FILE_STRUCTURE.md             # This file
│
├── 🐍 Python Scripts (Report Generators)
│   ├── area_report.py               # Area and utilization analysis
│   ├── timing_report.py             # Timing and critical path analysis
│   └── power_report.py              # Power consumption analysis
│
├── 📂 gds/
│   └── stepper_ctrl.gds             # Final GDSII layout (production)
│
├── 📂 reports/
│   └── stepper_ctrl/
│       ├── metrics.csv              # Complete design metrics
│       ├── logs/                    # OpenLane flow execution logs
│       └── signoff/
│           └── 31-rcx_sta.checks.rpt # Final verification report
│
└── 📂 OpenLane/                     # OpenLane EDA Framework
    ├── flow.tcl                     # Main flow script
    ├── requirements.txt             # Python dependencies
    ├── Makefile                     # Build automation
    │
    ├── designs/stepper_ctrl/        # Design-specific files
    │   ├── config.tcl               # Flow configuration
    │   ├── sky130A_sky130_fd_sc_hd_config.tcl  # PDK config
    │   └── ...
    │
    ├── configuration/               # Global flow configurations
    │   ├── general.tcl
    │   ├── synthesis.tcl
    │   ├── floorplan.tcl
    │   ├── placement.tcl
    │   ├── routing.tcl
    │   ├── cts.tcl
    │   └── extraction.tcl
    │
    ├── scripts/                     # EDA tool scripts
    │   ├── synthesis/
    │   ├── placement/
    │   ├── routing/
    │   └── ...
    │
    ├── docker/                      # Docker configurations
    │   └── Dockerfile
    │
    └── dependencies/                # Tool dependencies
        └── tool.py
```

---

## 📚 Documentation Files

### Entry Points

#### **README.md** (Main Hub)
- **Purpose**: Complete project overview
- **Audience**: Everyone (first stop!)
- **Content**:
  - Project description
  - Key features and metrics
  - Quick links to other docs
  - How to generate reports
  - Design highlights
- **Read Time**: 10-15 minutes

#### **QUICKSTART.md** (Fast Track)
- **Purpose**: Get up and running quickly
- **Audience**: Impatient people! 😄
- **Content**:
  - What is this project?
  - How to run reports (30 seconds)
  - Key numbers
  - One-line summary
- **Read Time**: 5 minutes

### Detailed Documentation

#### **DESIGN.md** (Specifications)
- **Purpose**: Technical design details
- **Audience**: Engineers, technical reviewers
- **Content**:
  - Design specifications
  - Functional specifications
  - Interface specifications
  - Performance metrics
  - Operating conditions
  - Cell library information
- **Read Time**: 15-20 minutes

#### **ARCHITECTURE.md** (System Design)
- **Purpose**: Architecture and block diagrams
- **Audience**: System designers, students
- **Content**:
  - High-level architecture
  - Block diagrams
  - System interface
  - Control logic
  - Data paths
  - State management
  - Clock and power distribution
- **Read Time**: 20-25 minutes

#### **FLOW.md** (Design Process)
- **Purpose**: Complete design flow documentation
- **Audience**: Flow engineers, interested learners
- **Content**:
  - RTL-to-GDS flow overview
  - Detailed stage descriptions
  - Tools and technologies
  - Design metrics at each stage
  - Verification process
  - Quality assurance
- **Read Time**: 25-30 minutes

#### **REPORTS_README.md** (Analysis Tools)
- **Purpose**: Guide to report generation
- **Audience**: Anyone wanting design metrics
- **Content**:
  - How to run each report
  - What each report contains
  - Example output
  - Data source information
- **Read Time**: 10 minutes

#### **FILE_STRUCTURE.md** (This File)
- **Purpose**: Repository organization guide
- **Audience**: Project browsers
- **Content**:
  - Complete directory tree
  - File descriptions
  - Reading recommendations
  - How to find things

---

## 🐍 Python Report Scripts

### area_report.py
**Purpose**: Generate area and utilization analysis  
**Location**: `/workspaces/stepper_motor/area_report.py`

**Features**:
- Die and core area metrics
- Cell utilization statistics
- Cell type breakdown
- Gate-level distribution
- Routing metrics

**Usage**:
```bash
python3 area_report.py
```

**Output**: 
```
AREA METRICS:
----------------------------------------------------------------------
Die Area:             0.004998 mm²
Core Area:            2,953 µm²
...
```

### timing_report.py
**Purpose**: Generate timing analysis  
**Location**: `/workspaces/stepper_motor/timing_report.py`

**Features**:
- Clock constraints
- Critical path analysis
- Slack analysis
- Setup/hold times
- Logic depth metrics

**Usage**:
```bash
python3 timing_report.py
```

**Output**:
```
TIMING METRICS:
----------------------------------------------------------------------
Clock Period:         20.0 ns
Critical Path:        1.26 ns
Slack:                18.74 ns
...
```

### power_report.py
**Purpose**: Generate power consumption analysis  
**Location**: `/workspaces/stepper_motor/power_report.py`

**Features**:
- Power at multiple corners
- Internal/switching/leakage breakdown
- Power density analysis
- Temperature effects
- Power comparison

**Usage**:
```bash
python3 power_report.py
```

**Output**:
```
POWER ANALYSIS (Typical):
----------------------------------------------------------------------
Internal Power:       9.61e-05 µW
Switching Power:      3.53e-05 µW
Leakage Power:        1.11e-09 µW
Total Power:          1.314e-04 µW
...
```

---

## 📊 Results and Data Files

### metrics.csv
**Path**: `reports/stepper_ctrl/metrics.csv`  
**Format**: Comma-separated values  
**Size**: ~1 KB (single row, 100+ columns)

**Contains**:
- Area metrics (die area, core area, utilization)
- Cell counts (logic, decap, welltap, fill)
- Gate statistics (AND, OR, NAND, NOR, XOR, MUX, DFF)
- Timing information (clock period, critical path, slack)
- Power data (internal, switching, leakage)
- Routing statistics (wire length, via count)
- Verification results (DRC, LVS, antenna checks)
- Configuration parameters

**How to Read**:
```bash
# View as readable table
column -t -s, reports/stepper_ctrl/metrics.csv | head -1
```

### stepper_ctrl.gds
**Path**: `gds/stepper_ctrl.gds`  
**Format**: GDS-II (binary layout format)  
**Size**: ~2-5 MB

**Contains**:
- Complete chip layout
- All metal layers (6 levels)
- Via connections
- Cell placements
- 429 cell instances
- ~100,000 polygons

**How to View**:
```bash
# If KLayout is installed
klayout gds/stepper_ctrl.gds
```

**What It Shows**:
- Physical layout of all components
- Metal routing
- Via connections
- Final chip dimensions

### signoff Report
**Path**: `reports/stepper_ctrl/signoff/31-rcx_sta.checks.rpt`  
**Format**: Text report

**Contains**:
- Final timing analysis results
- Verification status
- Design rule check results
- Layout versus schematic results

---

## 📂 OpenLane Framework Structure

### Configuration Files

#### flow.tcl
**Purpose**: Main OpenLane flow controller  
**Controls**: Which stages run, flow configuration

#### designs/stepper_ctrl/config.tcl
**Purpose**: Design-specific parameters  
**Includes**:
```tcl
set ::env(DESIGN_NAME) "stepper_ctrl"
set ::env(CLOCK_PERIOD) "20.0"
set ::env(FP_CORE_UTIL) "50"
set ::env(SYNTH_STRATEGY) "AREA 0"
...
```

#### configuration/general.tcl
**Purpose**: Global settings for all stages

#### configuration/synthesis.tcl
**Purpose**: Yosys synthesis settings

#### configuration/floorplan.tcl
**Purpose**: Floorplanning parameters (die size, core area)

#### configuration/placement.tcl
**Purpose**: Placement optimization settings

#### configuration/routing.tcl
**Purpose**: Routing algorithm configuration

#### configuration/cts.tcl
**Purpose**: Clock tree synthesis settings

#### configuration/extraction.tcl
**Purpose**: Parasitic extraction settings

---

## 📋 Log Files

### reports/stepper_ctrl/logs/
**Contains**: Execution logs from each flow stage

**Typical Subdirectories**:
```
logs/
├── synthesis/          # Yosys synthesis logs
├── floorplan/          # Floorplanning logs
├── placement/          # Placement logs
├── routing/            # Routing logs
├── cts/                # Clock tree synthesis logs
├── verification/       # DRC/LVS logs
└── final/              # Final output logs
```

---

## 🔍 Finding Specific Information

### I want to...

**Understand what this project is**
→ Start with [README.md](README.md)

**Get started quickly**
→ Read [QUICKSTART.md](QUICKSTART.md)

**Learn design specifications**
→ Check [DESIGN.md](DESIGN.md)

**Understand the architecture**
→ Read [ARCHITECTURE.md](ARCHITECTURE.md)

**Learn about the design flow**
→ Check [FLOW.md](FLOW.md)

**Generate design reports**
→ See [REPORTS_README.md](REPORTS_README.md) or run:
```bash
python3 area_report.py
python3 timing_report.py
python3 power_report.py
```

**View the layout**
→ Open `gds/stepper_ctrl.gds` with KLayout

**Access raw metrics**
→ Check `reports/stepper_ctrl/metrics.csv`

**See final verification results**
→ Check `reports/stepper_ctrl/signoff/31-rcx_sta.checks.rpt`

**Modify the design**
→ Check OpenLane configuration in `OpenLane/designs/stepper_ctrl/`

---

## 📊 Reading Guide by Role

### For Students/Learners
1. [README.md](README.md) - Overview
2. [QUICKSTART.md](QUICKSTART.md) - Get hands-on
3. [DESIGN.md](DESIGN.md) - Learn specifications
4. [ARCHITECTURE.md](ARCHITECTURE.md) - Understand design
5. [FLOW.md](FLOW.md) - See complete process

**Total Time**: ~2 hours for complete understanding

### For Engineers/Reviewers
1. [DESIGN.md](DESIGN.md) - Technical specs
2. [ARCHITECTURE.md](ARCHITECTURE.md) - Design verification
3. [FLOW.md](FLOW.md) - Process validation
4. Run reports for metrics
5. Review GDS layout if needed

**Total Time**: ~1-2 hours for detailed review

### For Project Managers/Stakeholders
1. [README.md](README.md) - Project overview
2. [QUICKSTART.md](QUICKSTART.md) - Key metrics
3. Run reports for status
4. Review highlights section

**Total Time**: ~15 minutes for status check

---

## 🎯 Key Metrics Quick Reference

### Area Metrics
| Metric | Value |
|--------|-------|
| Die Area | 4,998 µm² |
| Core Area | 2,953 µm² |
| Total Cells | 429 |
| Utilization | 54.05% |

### Performance
| Metric | Value |
|--------|-------|
| Frequency | 50 MHz |
| Critical Path | 1.26 ns |
| Slack | 18.74 ns |
| Path Utilization | 6.3% |

### Quality
| Check | Result |
|-------|--------|
| DRC | PASS ✓ |
| LVS | PASS ✓ |
| Violations | 0 |

---

**Last Updated**: December 11, 2025  
**Technology**: Skywater 130nm (sky130_fd_sc_hd)  
**Status**: ✅ Complete and Verified
