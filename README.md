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
   
4. Install dependencies

    ```
    poetry install
    ```
 
  
5. Create table with wifi metrics:

    ```
    poetry run python -m db
    ```
    
    This will create `wifi` table in `wifi` db
    
6. Run monitoring script:

    ```
    poetry run python -m main
    ```
    
    Script will measure wifi speed every hour and insert in to ClickHouse

7. Select inserted data:

    ```
    use wifi;
    select * from wifi;
    ```

    
## Used libs 

- [Speedtest-CLI](https://github.com/sivel/speedtest-cli) - to measure wifi speed
- [Delorian](https://github.com/myusuf3/delorean/) - to parse and localize datetime
- [ClickHouse SqlAlchemy](https://github.com/xzkostyan/clickhouse-sqlalchemy) - to insert data to CH
