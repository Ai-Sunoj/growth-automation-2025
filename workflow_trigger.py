import time

def trigger_workflow(event):
    print(f"Triggering automation for: {event}")
    # Placeholder for actual logic (email, webhook, CRM update, etc.)
    time.sleep(1)
    print("✅ Workflow executed successfully.")

# Example event
trigger_workflow("New user signup via marketing campaign")
