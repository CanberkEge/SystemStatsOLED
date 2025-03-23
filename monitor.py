import psutil
import GPUtil
import requests
import time
import wmi
import json
import os

# Portu otomatik algılama
def get_base_url():
    config_path = "C:/ProgramData/SteelSeries/SteelSeries Engine 3/coreProps.json"
    try:
        with open(config_path, "r") as f:
            props = json.load(f)
            return f"http://{props['address']}"
    except:
        print("coreProps.json bulunamadı. Varsayılan port: 58042")
        return "http://127.0.0.1:58042"

BASE_URL = get_base_url()
print(f"BASE_URL: {BASE_URL}")

# Veri fonksiyonları
def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_cpu_temp():
    try:
        w = wmi.WMI(namespace="root\\OpenHardwareMonitor")
        for sensor in w.Sensor():
            if sensor.SensorType == 'Temperature' and 'CPU' in sensor.Name:
                return sensor.Value
        return None
    except Exception as e:
        print(f"CPU sıcaklığı alınamadı: {e}")
        return None

def get_gpu_usage():
    gpus = GPUtil.getGPUs()
    return gpus[0].load * 100 if gpus else None

def get_gpu_temp():
    gpus = GPUtil.getGPUs()
    return gpus[0].temperature if gpus else None

def get_ram_usage():
    ram = psutil.virtual_memory()
    return ram.used / (1024 ** 3)

TOTAL_RAM_GB = psutil.virtual_memory().total / (1024 ** 3)

# Oyun kaydı
def register_game():
    game_data = {"game": "SYSTEM_STATS", "game_display_name": "System Stats OLED", "icon_color_id": 1}
    response = requests.post(f"{BASE_URL}/game_metadata", json=game_data)
    print("Game Register Response:", response.status_code, response.text)

# Handler bağlama
def bind_handler(event_name, prefix, suffix):
    handler_data = {
        "game": "SYSTEM_STATS",
        "event": event_name,
        "handlers": [{
            "device-type": "screened",  # Tüm OLED cihazları
            "zone": "one",
            "mode": "screen",
            "datas": [{
                "has-text": True,
                "prefix": prefix,
                "suffix": suffix,
                "value": {"low": 0, "high": 100}
            }]
        }]
    }
    response = requests.post(f"{BASE_URL}/bind_game_event", json=handler_data)
    print(f"Bind {event_name} Response:", response.status_code, response.text)

# Event gönderme
def send_event(event_name, value):
    if value is not None:
        event_data = {"game": "SYSTEM_STATS", "event": event_name, "data": {"value": int(value)}}
        response = requests.post(f"{BASE_URL}/game_event", json=event_data)
        print(f"Send {event_name} Response:", response.status_code, response.text)

# Yapılandırma dosyasını oku
def load_config():
    config_file = "config.json"
    default_config = {
        "metrics": {
            "CPU_USAGE": True,
            "CPU_TEMP": True,
            "GPU_USAGE": True,
            "GPU_TEMP": True,
            "RAM_USAGE": True
        }
    }
    if not os.path.exists(config_file):
        with open(config_file, "w") as f:
            json.dump(default_config, f, indent=4)
        print("config.json oluşturuldu. Lütfen ayarları kontrol edin.")
        return default_config["metrics"]
    with open(config_file, "r") as f:
        return json.load(f)["metrics"]

# Veri listesi
all_metrics = [
    ("CPU_USAGE", "CPU: ", "%", get_cpu_usage),
    ("CPU_TEMP", "CPU Temp: ", "°C", get_cpu_temp),
    ("GPU_USAGE", "GPU: ", "%", get_gpu_usage),
    ("GPU_TEMP", "GPU Temp: ", "°C", get_gpu_temp),
    ("RAM_USAGE", "RAM: ", f"/{TOTAL_RAM_GB:.1f}GB", get_ram_usage)
]

# Başlatma
config = load_config()
active_metrics = [m for m in all_metrics if config.get(m[0], False)]

register_game()
for event_name, prefix, suffix, _ in active_metrics:
    bind_handler(event_name, prefix, suffix)

current_metric = 0
while True:
    event_name, prefix, suffix, get_func = active_metrics[current_metric]
    value = get_func()
    send_event(event_name, value)
    print(f"{prefix}{value:.1f}{suffix}")
    current_metric = (current_metric + 1) % len(active_metrics)
    time.sleep(7)