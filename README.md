
# SonOyuncu Auto Enchant

[![GitHub license](https://img.shields.io/github/license/affanatmaca/sonoyuncu-auto-enchant)](https://github.com/affanatmaca/sonoyuncu-auto-enchant/blob/main/LICENSE)

SonOyuncu Auto Enchant is a powerful automation tool designed for the Minecraft server "SonOyuncu." This tool automates the enchanting process in the game, allowing players to efficiently enchant their items with minimal manual effort.

## Features

- **Automated Enchanting**: Automatically enchant items such as pickaxes, shovels, axes, and more.
- **Resource Detection**: Detects required resources (e.g., lapis, books) on the screen and interacts with them.
- **Webhook Notifications**: Sends notifications via webhook for important events, such as successful enchantments.
- **Multiple Resolutions Support**: Compatible with different screen resolutions (1920x1080, 1366x768).
- **Customizable Settings**: Easily configure the tool for various enchanting options.

## Requirements

- Python 3.6+
- Required Python packages (listed in `requirements.txt`)
- Screen resolution support for 1920x1080 or 1366x768

## Installation

1. **Clone the Repository**

   \`\`\`bash
   git clone https://github.com/affanatmaca/sonoyuncu-auto-enchant.git
   cd sonoyuncu-auto-enchant
   \`\`\`

2. **Install the Requirements**

   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

3. **Run the Tool**

   \`\`\`bash
   python main.py
   \`\`\`

## Usage

1. **Start the Minecraft Client and Login to SonOyuncu Server.**
2. **Run the Tool and Follow On-Screen Instructions.**
3. **Monitor the Console for Real-Time Updates and Webhook Notifications.**

## Configuration

- **Webhook Settings**: Configure webhook settings in `webhook_settings.json` to receive notifications.
- **Screen Resolution**: Choose your screen resolution (1920x1080 or 1366x768) via the login screen's combo box.

## Example Code

Here are some snippets from the key modules:

### Main Automation Script (`main.py`)

\`\`\`python
import pyautogui as p
import keyboard
import time
import json
import requests

def lapiskoy():
    try:
        image_path = "images/lapis.png"
        location = pyautogui.locateOnScreen(image_path, confidence=0.99)
        if location is not None:
            pyautogui.moveTo(location)
            pyautogui.keyDown("shift")
            pyautogui.leftClick()
            pyautogui.keyUp("shift")
        else:
            print("Lapis bulunamadı.")
    except pyautogui.ImageNotFoundException:
        print("Lapis ekranda bulunamadı")
        
def otuzlevelgit():
    # Logic to move to level 30 enchanting area

def servetbas():
    # Logic to check and apply the 'Fortune' enchantment
    
def main():
    # Main logic to automate enchanting process

if __name__ == "__main__":
    main()
\`\`\`

### Webhook Notification Function

\`\`\`python
def webhook_mesaj_gonder(item_ismi, resim_url, aciklama):
    try:
        with open("webhook_settings.json", "r") as json_file:
            data = json.load(json_file)
            webhook_value = data.get("webhook", "")
            if webhook_value:
                embed = {
                    "title": item_ismi,
                    "description": aciklama,
                    "thumbnail": {"url": resim_url},
                    "color": 0x00FF00  # Açık yeşil renk
                }
                payload = {"content": "", "embeds": [embed]}
                headers = {"Content-Type": "application/json"}
                response = requests.post(webhook_value, data=json.dumps(payload), headers=headers)
                if response.status_code == 204:
                    print("Webhook'a embedli mesaj başarıyla gönderildi.")
                else:
                    print(f"Webhook'a mesaj gönderme başarısız. HTTP status code: {response.status_code}")
    except FileNotFoundError:
        print("webhook_settings.json dosyası bulunamadı.")
    except json.JSONDecodeError:
        print("webhook_settings.json dosyası okunurken hata oluştu.")
\`\`\`

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Contact

If you have any questions or need further assistance, feel free to open an issue or contact me via GitHub.

---

By [affanatmaca](https://github.com/affanatmaca)

Enjoy your enchanting journey in SonOyuncu! ✨
