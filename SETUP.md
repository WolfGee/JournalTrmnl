# TRMNL Journal Prompts Plugin Setup

## Raspberry Pi Setup

1. **Copy files to Raspberry Pi:**
   ```bash
   scp -r * pi@your-pi-ip:/home/pi/trmnl-journal/
   ```

2. **Install dependencies:**
   ```bash
   ssh pi@your-pi-ip
   cd /home/pi/trmnl-journal
   pip3 install -r requirements.txt
   ```

3. **Set up systemd service:**
   ```bash
   sudo cp trmnl-journal.service /etc/systemd/system/
   sudo systemctl daemon-reload
   sudo systemctl enable trmnl-journal
   sudo systemctl start trmnl-journal
   ```

4. **Check service status:**
   ```bash
   sudo systemctl status trmnl-journal
   ```

## TRMNL Plugin Configuration

1. **Create new private plugin** in TRMNL dashboard
2. **Set strategy to "Webhook"** 
3. **Your webhook URL is already configured in the script:** `https://usetrmnl.com/api/custom_plugins/98730d07-22b5-43dd-a49c-134981ccc0b1`
4. **Copy the contents of `trmnl_markup_template.html`** into the Markup field

## How it works:
- Sends a prompt immediately when started
- Then sends new prompts twice daily at 7:00 AM and 7:00 PM
- Randomly selects from your 90 journal prompts

## Test manually:
```bash
python3 trmnl_webhook_server.py
```