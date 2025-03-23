# System Stats OLED

**System Stats OLED** is a lightweight application designed to display real-time system statistics on SteelSeries devices with OLED screens. Whether you own a Rival 710, Arctis Pro + GameDAC, or any other SteelSeries device with an OLED display, this tool lets you monitor your hardware performance with ease.

## Features
- **Real-Time Monitoring**: Displays CPU usage, CPU temperature, GPU usage, GPU temperature, and RAM usage.
- **Universal Compatibility**: Works with all SteelSeries OLED devices (e.g., Rival 700, Rival 710, Arctis Pro, Arctis Pro Wireless).
- **Customizable Metrics**: Choose which stats to display via a simple `config.json` file.
- **Automatic Port Detection**: Dynamically detects the SteelSeries Engine port from `coreProps.json`.
- **User-Friendly**: Available as a standalone `.exe` for easy use, or as a Python script for developers.
- **Error Handling**: Gracefully handles unavailable data (e.g., CPU temperature without OpenHardwareMonitor).

## Screenshots
*(Optional: Add screenshots of the OLED display showing stats here once available.)*

## Requirements
### General
- **Operating System**: Windows (tested on Windows 10/11; other OS support untested).
- **SteelSeries GG**: Must be installed and running for OLED integration.

### For Executable Version
- No additional software required beyond SteelSeries GG.

### For Source Code Version
- **Python**: Version 3.6 or higher.
- **Dependencies**:
  - `psutil`: For CPU and RAM stats.
  - `GPUtil`: For GPU stats.
  - `requests`: For communicating with SteelSeries Engine.
  - `wmi`: For CPU temperature via OpenHardwareMonitor (optional).
- **Optional**: [OpenHardwareMonitor](https://openhardwaremonitor.org/) for CPU temperature monitoring.

## Installation

### Option 1: Using the Executable (Recommended)
1. Download the latest `monitor.exe` from the [Releases](https://github.com/CanberkEge/SystemStatsOLED/releases) section.
2. Place `monitor.exe` in a folder of your choice (e.g., `C:\SystemStatsOLED`).
3. Double-click `monitor.exe` to run it.
   - A `config.json` file will be automatically created in the same folder on first run.

### Option 2: Running from Source
1. Clone or download this repository:
   ```bash
   git clone https://github.com/CanberkEge/SystemStatsOLED.git
   cd SystemStatsOLED
2. Install the required Python dependencies:
   ```bash
   pip install psutil gputil requests wmi
   ```
3. Run the script
```bash
python monitor.py
```
A config.json file will be generated in the working directory.

## Configuration

The application uses a config.json file to let you customize which stats are displayed. On first run, a default configuration is created:

```json
{
    "metrics": {
        "CPU_USAGE": true,
        "CPU_TEMP": true,
        "GPU_USAGE": true,
        "GPU_TEMP": true,
        "RAM_USAGE": true
    }
}
```

### Options
1. "CPU_USAGE": CPU usage percentage (e.g., "CPU: 23%").
2. "CPU_TEMP": CPU temperature in Celsius (e.g., "CPU Temp: 45°C").
3. "GPU_USAGE": GPU usage percentage (e.g., "GPU: 15%").
4. "GPU_TEMP": GPU temperature in Celsius (e.g., "GPU Temp: 50°C").
5. "RAM_USAGE": RAM usage in GB (e.g., "RAM: 8.5/31.9GB").

**Editing**: Open config.json in a text editor and set any metric to false to disable it. Save the file and restart the application.

## Usage

1. Ensure SteelSeries GG is running in the background.
2. Launch `monitor.exe` (or python `monitor.py` if using source).
3. The application will cycle through your selected metrics every 7 seconds on your SteelSeries OLED display.
4. Example output on OLED:
- "CPU: 23%"
- "CPU Temp: 45°C"
- "GPU: 15%"
- "GPU Temp: 50°C"
- "RAM: 8.5/31.9GB"

## Notes

- CPU Temperature: Requires OpenHardwareMonitor to be installed and running. If unavailable, the app will display "CPU Temp: Veri Yok" and continue with other metrics.
- GPU Stats: Requires a compatible GPU and drivers. If no GPU is detected, these metrics will show "Veri Yok".
- Performance: Minimal CPU and memory usage, designed to run unobtrusively in the background.

## Trobleshooting

- OLED Display Blank: Ensure SteelSeries GG is running and the correct port is detected (check terminal output for BASE_URL).
- Missing Stats: Verify config.json settings and ensure required software (e.g., OpenHardwareMonitor) is active.
- Errors: Run from source with python monitor.py to see detailed logs in the terminal.

## Building from Source

To create your own `.exe`:
   1. Install PyInstaller:
      ``bash
      pip install pyinstaller
      ``
   2. Build the executable:
      ``bash
      pyinstaller --onefile monitor.py``  
   3. Find `monitor.exe` in the `dist` folder.


## Contributing

Contributions are welcome! Here's how you can help:

1. Fork this repository.
2. Create a new branch (git checkout -b feature/your-feature).
3. Make your changes and commit (git commit -m "Add your feature").
4. Push to your fork (git push origin feature/your-feature).
5. Open a Pull Request on GitHub.

## License

This project is licensed under the  - feel free to use, modify, and distribute it.

## Contact

- Author: Canberk Ege Erden
- GitHub: CanberkEge
- Feedback: Open an issue on GitHub or reach out directly!

## Acknowledgements

Built with the `SteelSeries GameSense SDK`.
Thanks to the open-source community for libraries like `psutil` and `GPUtil`.