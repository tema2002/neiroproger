import subprocess
import time
import sys
import os
from datetime import datetime

# Путь к файлу логов
LOG_FILE = 'bot_runner_log.txt'

def log_error(message):
    """Записывает сообщение об ошибке в файл логов."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, 'a', encoding='utf-8') as log_file:
        log_file.write(f"{timestamp} - {message}\n")

def run_bot():
    while True:
        print("Starting the bot...")
        try:
            result = subprocess.run(['python3', 'telegram_bot_for_kids.py'], check=True, capture_output=True, text=True)
            if result.returncode != 0:
                error_message = f"Bot exited with return code {result.returncode}"
                print(error_message)
                log_error(error_message)
                if result.stderr:
                    log_error(f"Error output:\n{result.stderr}")
                time.sleep(10)  # Wait for 10 seconds before restarting
            else:
                print("Bot stopped normally")
                break
        except subprocess.CalledProcessError as e:
            error_message = f"Bot crashed with error: {e}"
            print(error_message, file=sys.stderr)
            log_error(error_message)
            if e.stderr:
                log_error(f"Error output:\n{e.stderr}")
            time.sleep(10)  # Wait for 10 seconds before restarting
        except KeyboardInterrupt:
            print("Received keyboard interrupt, stopping...")
            break
        except Exception as e:
            error_message = f"Unexpected error occurred: {e}"
            print(error_message, file=sys.stderr)
            log_error(error_message)
            time.sleep(10)  # Wait for 10 seconds before restarting

if __name__ == "__main__":
    run_bot()