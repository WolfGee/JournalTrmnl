#!/usr/bin/env python3
import random
import json
import requests
import time
import schedule
from journal_prompts_dict import journal_prompts

TRMNL_WEBHOOK_URL = "YOUR-WEBHOOK-URL-HERE"

def get_random_prompt():
    prompt = random.choice(list(journal_prompts.keys()))
    category = journal_prompts[prompt]
    return prompt, category

def send_prompt_to_trmnl():
    try:
        prompt, category = get_random_prompt()
        
        payload = {
            "merge_variables": {
                "prompt": prompt,
                "category": category
            }
        }
        
        response = requests.post(TRMNL_WEBHOOK_URL, json=payload, timeout=10)
        
        if response.status_code == 200:
            print(f"Successfully sent prompt: {category}")
        else:
            print(f"Failed to send prompt. Status: {response.status_code}")
            
    except Exception as e:
        print(f"Error sending prompt: {e}")

def run_scheduler():
    schedule.every().day.at("07:00").do(send_prompt_to_trmnl)
    schedule.every().day.at("19:00").do(send_prompt_to_trmnl)
    
    print("Scheduler started. Sending prompts at 7:00 AM and 7:00 PM daily.")
    
    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == '__main__':
    send_prompt_to_trmnl()
    run_scheduler()