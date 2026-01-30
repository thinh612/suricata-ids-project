import json
import psycopg2

conn = psycopg2.connect(
    host="192.168.64.1",   # IP Mac
    database="suricata",
    user="suriuser",
    password="suripass"
)

cur = conn.cursor()

with open("/var/log/suricata/eve.json", "r") as f:
    for line in f:
        try:
            log = json.loads(line)
        except json.JSONDecodeError:
            continue

        if log.get("event_type") == "alert":
            cur.execute("""
                INSERT INTO suricata_alerts
                (timestamp, src_ip, dest_ip, src_port, dest_port,
                 protocol, signature, category, severity, event_type, raw_json)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """, (
                log.get("timestamp"),
                log.get("src_ip"),
                log.get("dest_ip"),
                log.get("src_port"),
                log.get("dest_port"),
                log.get("proto"),
                log["alert"].get("signature"),
                log["alert"].get("category"),
                log["alert"].get("severity"),
                log.get("event_type"),
                json.dumps(log)
            ))

            conn.commit()

print("Suricata ingest running...")
