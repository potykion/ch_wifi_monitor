from typing import Dict

import speedtest

from ch_wifi_monitor.utils import format_date


def request_speed() -> speedtest.SpeedtestResults:
    s = speedtest.Speedtest()
    s.get_best_server()
    s.download()
    s.upload()
    return s.results


def format_speed(results: speedtest.SpeedtestResults) -> Dict:
    """
    See data/speed.json for example of {results}.json()
    """
    return dict(
        dt=format_date(results.timestamp),
        client_ip=results.client["ip"],
        download_speed=results.download,
        upload_speed=results.upload,
        ping=results.ping,
        bytes_sent=results.bytes_sent,
        bytes_received=results.bytes_received,
    )
