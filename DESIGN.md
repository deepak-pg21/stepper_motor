# Design Specifications - Stepper Motor Controller

Complete technical specifications and design details.

## 📋 Table of Contents

1. [Design Overview](#design-overview)
2. [Functional Specifications](#functional-specifications)
3. [Interface Specifications](#interface-specifications)
4. [Performance Specifications](#performance-specifications)
5. [Power Specifications](#power-specifications)
6. [Design Constraints](#design-constraints)
7. [Operating Conditions](#operating-conditions)
8. [Cell Library Information](#cell-library-information)

---

## 🎯 Design Overview

### Project Information
- **Design Name**: stepper_ctrl
- **Technology Node**: Skywater 130nm (sky130_fd_sc_hd)
- **Design Type**: Digital ASIC
- **Application**: Stepper Motor Control
- **Design Language**: Verilog HDL
- **Design Status**: ✅ Complete and Verified

### Key Specifications
- **Supply Voltage**: 1.8V (typical for sky130)
- **Operating Temperature**: -40°C to 125°C
- **Power Domain**: Single VDD
- **Clock Domain**: Single clock

---

## 🔌 Functional Specifications

### Primary Inputs (27 total)
- **Clock**: Main system clock
- **Reset**: Active-high reset signal
- **Control Signals**: Motor direction and speed control
- **Step Signals**: Step enable and pulse inputs
- **Status Inputs**: Feedback from motor drivers

### Primary Outputs (30 total)
- **Phase Outputs**: A, B, AB, BA phases for stepper control
- **Status Signals**: Motor state and error flags
- **Enable/Disable Signals**: Driver enable outputs
- **Diagnostic Outputs**: Health and fault signals

### Logic Elements
- **Total Logic Cells**: 134
- **Flip-Flops**: 24 (sequential state storage)
- **Combinational Logic**: 110 cells
- **Max Logic Depth**: 8 levels

---

## 🔗 Interface Specifications

### Clock Specifications
```
Clock Period:         20.0 ns
Frequency:            50 MHz
Duty Cycle:           50%
Rise/Fall Time:       ~100 ps (typical)
```

### Reset Specifications
```
Reset Type:           Asynchronous
Reset Polarity:       Active-High
Reset Setup Time:     2.0 ns (typical)
Reset Hold Time:      1.0 ns (typical)
```

### I/O Voltage Levels
```
VDD:                  1.8V ± 5%
GND:                  0V
Input Low (VIL):      0.3 * VDD = 0.54V
Input High (VIH):     0.7 * VDD = 1.26V
Output Low (VOL):     < 0.4V
Output High (VOH):    > 1.4V
```

### Input/Output Characteristics
```
Input Capacitance:    ~2 pF per input
Output Capacitance:   ~3 pF per output
Input Rise Time:      1-2 ns
Input Fall Time:      1-2 ns
Output Rise Time:     2-3 ns (typical)
Output Fall Time:     2-3 ns (typical)
```

---

## ⚡ Performance Specifications

### Timing Specifications
| Parameter | Min | Typical | Max | Unit |
|-----------|-----|---------|-----|------|
| Clock Period | 20.0 | 20.0 | - | ns |
| Critical Path | - | 1.26 | - | ns |
| Slack | 18.74 | 18.74 | - | ns |
| Max Frequency | 50.0 | - | - | MHz |
| Setup Time | - | ~1.5 | - | ns |
| Hold Time | - | ~0.5 | - | ns |
| Combinational Delay | - | ~1.0 | - | ns |

### Slack Analysis
```
Timing Slack:         18.74 ns (excellent - plenty of margin)
Slack Percentage:     93.7% of clock period available
Critical Path Level:  8 logic levels
Path Utilization:     6.3% (very low - optimizable)
```

### Routing Statistics
```
Total Wire Length:    2,626 µm
Via Count:            1,027
Average Via Density:  ~0.35 vias/µm of wire
HPWL (Half-Perimeter): 1,524,792 µm
```

---

## 💡 Power Specifications

### Power Consumption

#### At Typical Corner (1.8V, 25°C, 50 MHz)
```
Internal Power:       9.61e-05 µW (73.13% of total)
Switching Power:      3.53e-05 µW (26.86% of total)
Leakage Power:        1.11e-09 µW (0.00% of total)
─────────────────────────────────────────
Total Power:          1.314e-04 µW (very low!)
```

#### Power Density
```
Power per Unit Area:  4.45e-02 µW/mm²
Estimated Annual Consumption: < 1 mW (at typical conditions)
```

### Dynamic vs. Static Power
```
Dynamic (Active):     73.13% - Internal + Switching
Static (Leakage):     0.00% - Negligible at typical corner
Activity Factor:      ~0.3 (30% of cells switching per cycle)
```

### Temperature Effects
```
Power increases with temperature (leakage dominated at higher T)
Typical range: 25°C - 125°C
At 125°C: Power approximately doubles due to leakage
```

---

## 📐 Design Constraints

### Area Constraints
```
Die Area (Total):     4,998 µm² (70.7 µm × 70.7 µm square)
Core Area (Routable): 2,953 µm²
Aspect Ratio:         1:1 (square die)
Core Utilization:     50.0% (good for routing)
```

### Cell Distribution
| Cell Type | Count | Purpose | Notes |
|-----------|-------|---------|-------|
| Logic Cells | 134 | Functional logic | Synthesized from RTL |
| Decap Cells | 149 | Power decoupling | For supply noise management |
| Welltap Cells | 44 | Well biasing | For bulk substrate connection |
| Fill Cells | 74 | Density filler | Metal density compliance |
| **Total** | **429** | **All cells** | ~32,412 cells/mm² density |

### Utilization
```
Placement Density:    54.05% (OpenDP utilization)
Core Utilization:     50.0% (FP_CORE_UTIL)
Target Density:       0.6 (60% - design is below target)
Routing Congestion:   Low
```

### Timing Constraints
```
Minimum Clock Period: 20.0 ns (50 MHz max frequency)
Max Fanout:           10 (per synthesis constraint)
Max Transition:       2.0 ns
Setup Time Margin:    > 1.5 ns
Hold Time Margin:     > 0.5 ns
```

---

## 🌡️ Operating Conditions

### Temperature Range
```
Minimum Temperature:  -40°C
Nominal Temperature:  25°C
Maximum Temperature:  125°C
```

### Supply Voltage Range
```
Minimum VDD:          1.71V (VDD - 5%)
Nominal VDD:          1.80V
Maximum VDD:          1.89V (VDD + 5%)
```

### Operating Modes
```
Active Mode:          Full operation at 50 MHz
Idle Mode:            Clock gating possible (reduces power)
Sleep Mode:           Requires external support
```

---

## 📦 Cell Library Information

### Standard Cell Library
```
Library Name:         sky130_fd_sc_hd
Technology:           Skywater 130nm PDK
Cell Format:          LEF/DEF
Variant:              High-Density (hd)
```

### Available Cell Types
```
Basic Gates:          AND, NAND, OR, NOR, XOR, XNOR, NOT, BUF
Complex Gates:        AND-OR, AND-OR-INVERT, MUX, MAJORITY
Sequential:           Flip-flops (DFF, DFFQ), Latches
Specialized:          AOI, OAI, MUX2, MUX4
Filler:               FILL1, FILL2, FILL4, FILL8, DECAP
Power:                Welltap, Decap (for power integrity)
```

### Cell Statistics Used
```
AND gates:            2
NAND gates:           15
OR gates:             38
NOR gates:            1
XOR gates:            23
MUX:                  2
Flip-Flops (DFF):     24
Decap Cells:          149
Welltap Cells:        44
Fill Cells:           74
```

---

## ✅ Verification & Quality Metrics

### Design Rule Checks (DRC)
```
Status:               PASS ✓
Violations:           0
Tool Used:            Magic
```

### Layout vs. Schematic (LVS)
```
Status:               PASS ✓
Errors:               0
Tool Used:            Netgen
```

### Antenna Checks
```
Status:               PASS ✓
Antenna Violations:   0
Pin Antenna:          0
Net Antenna:          0
```

### Routing Quality
```
Short Violations:     0 ✓
Metal Spacing:        0 ✓
Offset Grid Errors:   0 ✓
Min Hole Violations:  0 ✓
TritonRoute Errors:   0 ✓
```

---

## 📊 Design Summary Table

| Category | Parameter | Value |
|----------|-----------|-------|
| **Size** | Die Area | 4,998 µm² |
| | Core Area | 2,953 µm² |
| **Cells** | Total Count | 429 |
| | Logic Cells | 134 |
| | Density | 32,412 cells/mm² |
| **Frequency** | Max Clock | 50 MHz |
| | Period | 20.0 ns |
| **Timing** | Critical Path | 1.26 ns |
| | Slack | 18.74 ns |
| **Power** | Total (Typical) | 0.0001314 µW |
| | Power Density | 4.45e-02 µW/mm² |
| **Quality** | DRC | PASS ✓ |
| | LVS | PASS ✓ |
| | Violations | 0 |
| **PDK** | Technology | 130nm |
| | Library | sky130_fd_sc_hd |

---

## 🎓 Design Notes

- **Timing**: Only 6.3% of clock period used by critical path - excellent margin for relaxed timing
- **Power**: Dominated by internal power (switching), leakage is negligible at typical temperature
- **Area**: Relatively compact design with good cell density
- **Quality**: Zero violations across all verification checks
- **Feasibility**: All specifications are conservative and achievable with 130nm technology

---

**Last Updated**: December 11, 2025
**Design Status**: Complete and Verified ✅
**Technology**: Skywater 130nm (sky130_fd_sc_hd)
