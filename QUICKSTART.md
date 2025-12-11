# Quick Start Guide - Stepper Motor Controller Design

Get up and running with this ASIC design in 5 minutes!

## 1️⃣ What Is This?

A complete chip design for stepper motor control in 130nm technology. It's a working example of modern ASIC design from RTL to fabrication-ready GDS.

## 2️⃣ What's Inside?

```
stepper_motor/
├── gds/stepper_ctrl.gds           ← Final chip layout (GDS-II format)
├── reports/stepper_ctrl/           ← Design metrics and reports
├── area_report.py                  ← Area analysis script
├── timing_report.py                ← Timing analysis script
├── power_report.py                 ← Power analysis script
└── README.md                       ← You are here
```

## 3️⃣ View the Metrics (30 seconds)

Run a quick report to see design stats:

```bash
# See area statistics
python3 area_report.py

# See timing information
python3 timing_report.py

# See power consumption
python3 power_report.py
```

## 4️⃣ Key Numbers

| Metric | Value |
|--------|-------|
| **Chip Size** | 4,998 µm² (about 0.005 mm²) |
| **Technology** | 130 nanometers |
| **Speed** | 50 MHz (50 million cycles/second) |
| **Power** | < 0.0002 µW |
| **Cells** | 429 (mix of logic, power, and filler) |
| **Status** | ✅ Complete & Verified |

## 5️⃣ View the Layout

The final chip design is in GDS-II format (industry standard):

```
gds/stepper_ctrl.gds
```

**To visualize it** (if KLayout is installed):
```bash
klayout gds/stepper_ctrl.gds
```

## 6️⃣ Understand the Design

Read these in order (each takes ~5-10 minutes):

1. **[DESIGN.md](DESIGN.md)** - What does it do?
2. **[ARCHITECTURE.md](ARCHITECTURE.md)** - How is it organized?
3. **[FLOW.md](FLOW.md)** - How was it made?

## 7️⃣ Complete Metrics

All design metrics are in CSV format:

```
reports/stepper_ctrl/metrics.csv
```

This includes:
- Cell counts (logic, decap, welltap, filler)
- Area and utilization
- Timing information
- Power figures
- Routing statistics
- Verification results

## 🎯 One-Line Summary

A **129-cell stepper motor controller** in **130nm technology** running at **50 MHz** with **zero violations** - ready for chip fabrication! ✨

---

## Common Questions

**Q: Can I modify this?**
A: Yes! The design is open-source. Check the main README for contribution guidelines.

**Q: How long to run the flow?**
A: About 1-2 minutes for a complete RTL-to-GDSII flow.

**Q: Is it actually working?**
A: Yes! Zero violations means it passed all design checks.

**Q: What's "130nm"?**
A: The minimum feature size. Smaller = more transistors per unit area.

---

**Next Step**: Read [DESIGN.md](DESIGN.md) to understand what this chip does!
