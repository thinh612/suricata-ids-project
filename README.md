# Suricata IDS Monitoring System

## 1. Overview
This project implements a Network Intrusion Detection System (IDS) using Suricata.
Alerts are ingested into PostgreSQL and visualized using Apache Superset.

## 2. Architecture

Attacker → Suricata → eve.json → Python Ingest → PostgreSQL → Superset Dashboard

## 3. Technologies Used
- Suricata IDS
- Python (psycopg2)
- PostgreSQL
- Apache Superset

## 4. Setup Instructions

### Step 1: Install Suricata
sudo apt install suricata

### Step 2: Enable eve.json
Configure suricata.yaml to enable eve-log output.

### Step 3: Run ingest script
python3 ingest/suricata_ingest.py

### Step 4: Connect Superset to PostgreSQL

## 5. Database Schema
See database/schema.sql

## 6. Sample Dashboard
Screenshots available in screenshots/ folder.

## Author
Tran Quoc Thinh
