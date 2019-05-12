from typing import Dict

import speedtest

from ch_wifi_monitor.utils import dt_to_local


def request_speed() -> speedtest.SpeedtestResults:
    s = speedtest.Speedtest()
    s.get_best_server()
    s.download()
    s.upload()
    return s.results


def format_speed(results: speedtest.SpeedtestResults) -> Dict:
    """
    See speed.json for example {results}.json()
    """
    local_datetime = dt_to_local(results.timestamp)

    return dict(
        date=local_datetime.date(),
        hour=local_datetime.hour,
        minute=local_datetime.minute,
        client_ip=results.client["ip"],
        download_speed=results.download,
        upload_speed=results.upload,
        ping=results.ping,
        bytes_sent=results.bytes_sent,
        bytes_received=results.bytes_received,
    )
