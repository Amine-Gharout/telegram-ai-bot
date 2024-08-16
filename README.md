Intelligent Telegram Contact Bot,

This project utilizes the Telegram Bot API and Google Gemini API to create an intelligent Telegram contact capable of generating automated responses using AI.

Setup Instructions
Follow these steps to set up and run the bot:

1. Installing pachages:
- "ctrl" + 'R' and write "cmd'.
- Write 'pip install google-generativeai" and click enter, wait until the instalation complet.
- write 'pip install python-telegram-bot', enter, and wait.
  
2. Create a Telegram Bot
- Open Telegram and search for the @BotFather bot.
- Send the /newbot command and follow the prompts:
- Provide a name for your bot and press Enter.
- Provide a username for your bot and press Enter.
- After creating the bot, use the /token command to get your API token.

3. Obtain a Google Gemini API Key
- Go to "https://ai.google.dev/gemini-api".
- Click in "Get API key in Gooogle AI Studio".
- Click in "Get API key" and after that click "Create API key".
- Follow the clicks and select a project or create one.
- After that just copy the API key

4. Configure the Bot
- Open the files and replace placeholders(Comments) with your API tokens:
- Paste the Telegram bot token into the appropriate file.
- Paste the Google Gemini API key into the appropriate file.
- Check the mood settings in the 'gmini_api_app.py'.

5. Run the Bot
- Ensure that the configuration files and app.py are in the same directory.
- Run telegram_bot.py using a Python IDE like vscode or pycharm:

6. Interact with the Bot
- Search for your bot on Telegram using the username you provided.
- Start a chat with your bot to interact with it.

99. Troubleshooting:
- Verify that your API keys are correctly pasted and valid.
- Ensure that all required libraries are installed.
- Review any error messages for clues and consult the Telegram Bot API documentation and Google Gemini API documentation for more information.
