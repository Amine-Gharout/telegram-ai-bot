Intelligent Telegram Contact Bot,

This project utilizes the Telegram Bot API and Google Gemini API to create an intelligent Telegram contact capable of generating automated responses using AI.

Setup Instructions
Follow these steps to set up and run the bot:

1. Create a Telegram Bot
- Open Telegram and search for the @BotFather bot.
- Send the /newbot command and follow the prompts:
- Provide a name for your bot and press Enter.
- Provide a username for your bot and press Enter.
- After creating the bot, use the /token command to get your API token.

3. Obtain a Google Gemini API Key
- Go to the Google Cloud Console.
- Create a new project or select an existing project.
- Navigate to the APIs & Services section and enable the Google Gemini API.
- Generate an API key for Google Gemini.

4. Configure the Bot
- Open the files and replace placeholders with your API tokens:
- Paste the Telegram bot token into the appropriate file.
- Paste the Google Gemini API key into the appropriate file.

6. Run the Bot
- Ensure that the configuration files and app.py are in the same directory.
- Run telegram_bot.py using Python:

7. Interact with the Bot
- Search for your bot on Telegram using the username you provided.
- Start a chat with your bot to interact with it.

Troubleshooting:
If you encounter any issues, check the following:
-Verify that your API keys are correctly pasted and valid.
-Ensure that all required libraries are installed.
-Review any error messages for clues and consult the Telegram Bot API documentation and Google Gemini API documentation for more information.
