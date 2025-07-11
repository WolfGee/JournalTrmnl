# TRMNL Journal Prompts Plugin Setup


1. **Install dependencies:**
   ```bash
   pip3 install -r requirements.txt
   ```

2. **Set up systemd service:**
   ```bash
   sudo cp trmnl-journal.service /etc/systemd/system/
   sudo systemctl daemon-reload
   sudo systemctl enable trmnl-journal
   sudo systemctl start trmnl-journal
   ```

3. **Check service status:**
   ```bash
   sudo systemctl status trmnl-journal
   ```

## TRMNL Plugin Configuration

1. **Create new private plugin** in TRMNL dashboard
2. **Set strategy to "Webhook"** 
3. **Use your Webhook in the trmnl_webhook_server.py**
4. **Copy the contents of `trmnl_markup_template.html`** into the Markup field

## How it works:
- Sends a prompt immediately when started
- Then sends new prompts twice daily at 7:00 AM and 7:00 PM
- Randomly selects from the prompts in journal_prompts_dict.py

## Test manually:
```bash
python3 trmnl_webhook_server.py
```