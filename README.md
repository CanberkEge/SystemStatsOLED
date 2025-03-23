# System Stats OLED

A simple application to display system stats (CPU, GPU, RAM) on SteelSeries OLED screens.

## Features
- Displays CPU usage, CPU temperature, GPU usage, GPU temperature, and RAM usage.
- Supports all SteelSeries OLED devices (e.g., Rival 710, Arctis Pro + GameDAC).
- Configurable via `config.json` to choose which metrics to show.
- Automatically detects SteelSeries Engine port.

## Requirements
- **Windows** (currently tested on Windows only).
- SteelSeries GG software installed and running.
- Python 3.x (if running from source) or use the pre-built `.exe`.
- **Optional**: [OpenHardwareMonitor](http://openhardwaremonitor.org/) for CPU temperature (if not installed, CPU_TEMP will show "Data Unavailable").

## Installation
1. **Using the Executable**:
   - Download `monitor.exe` from the [Releases](https://github.com/KULLANICI_ADIN/SystemStatsOLED/releases) section.
   - Place it in a folder and run it.
   - A `config.json` file will be created automatically.

2. **From Source**:
   - Install dependencies:
     ```bash
     pip install psutil gputil requests wmi