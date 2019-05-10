# ch_wifi_monitor

WiFi speed monitoring via ClickHouse

## Setup

1. Install ClickHouse (e.g. via [docker](https://hub.docker.com/r/yandex/clickhouse-server))

    *If you are using Docker don't forget to bind port 8123 to localhost/192.168.99.100*

2. Create database (e.g. via [docker-client](https://hub.docker.com/r/yandex/clickhouse-server#connect-to-it-from-a-native-client)):

    ```
    CREATE DATABASE wifi;
    ``` 

    [Reference](https://clickhouse.yandex/docs/en/query_language/create/#create-database)
    
    
3. Setup database url via .env:

    ```
    DATABASE_URL = clickhouse://default:@192.168.99.100/wifi
    ```