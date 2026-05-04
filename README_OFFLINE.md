# HXN GUI - Offline Mode

## Overview

The HXN GUI now supports an **offline mode** for testing and development without requiring access to beamline hardware. This is useful for:
- Testing the GUI during pixi environment setup
- Development work away from the beamline
- Training and demonstrations
- Debugging GUI issues

## Running in Offline Mode

### Using Pixi (Recommended)

```bash
pixi run hxn-gui-offline
```

### Using Python Directly

```bash
python src/hxn-gui/hxn_gui_v3.py --offline
```

## What Gets Mocked in Offline Mode

- **EPICS connections**: All `caget()` and `caput()` calls return simulated values
- **Motor objects**: Mock motors (zpssx, zpssy, zpssz, dssx, dssy, dssz) with position tracking
- **Detector objects**: Simulated detector configurations
- **Process Variables (PVs)**: Returns reasonable default values for ion chambers, pressures, statuses, etc.
- **Configuration files**: Uses local `default_plot_elems.json` for XRF element lists

## Differences from Online Mode

In offline mode:
- No actual hardware connections are made
- Motor movements are simulated (positions update instantly)
- PV readings show consistent dummy values with small random variations
- Configuration files fall back to local defaults
- Bluesky RunEngine (RE) checks are bypassed

## Files Added for Offline Support

- `src/hxn-gui/mock_epics.py` - Mock EPICS implementation
- `src/hxn-gui/default_plot_elems.json` - Default XRF element configuration
- `README_OFFLINE.md` - This file

## Development Notes

The offline mode is controlled by the `--offline` command-line flag, which sets the global `OFFLINE_MODE` variable. This variable is checked throughout the code to:
- Import mock modules instead of real EPICS
- Skip hardware-dependent operations
- Use fallback configuration files
- Bypass beamline-specific checks

## Switching Between Modes

- **Offline (testing)**: Use `--offline` flag or `pixi run hxn-gui-offline`
- **Online (beamline)**: Run without the `--offline` flag from the beamline IPython environment

The same codebase supports both modes seamlessly.
