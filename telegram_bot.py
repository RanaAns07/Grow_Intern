from telegram import Update
from telegram.ext import MessageHandler, ContextTypes, filters, CommandHandler, Application
from typing import final
from response import Response
import response



token:final = '7969728161:AAEgWpoZAffocECXv_4IbBnTRGHgIL0K_Tk'
username:final = '@Ans_007_bot'

# Execute Commands
async def start_command(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! This is a Bot by Ans Mustafa.")
async def help_command(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("How would i help you?")
async def custom_command(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("This is a Custom Command")

#Handle Response
def handle_response(text:str)-> str:
    input_text:str = text.lower()
    Response = response.Response()
    response_text: str = Response.answers(input_text)
    return response_text

async def message_type(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Extract message type and text
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f"User ({update.message.chat.id}) in {message_type}: {text}")

    # Check if it's a group message
    if message_type == 'group':
        if username in text:
            new_text: str = text.replace(username, '').strip()
            response: str = handle_response(new_text)
        else:
            return  # Ignore messages that don't mention the bot
    else:
        # Handle private messages
        response: str = handle_response(text)

    # Send response
    print('Bot:', response)
    await update.message.reply_text(response)

    
async def error_handler(update:Update, context:ContextTypes.DEFAULT_TYPE):
    print(f'upadte {update} caused an error {context.error}')
        
    
if __name__ == '__main__':
    app = Application.builder().token(token).build()
    
    #Command handler
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', start_command))
    app.add_handler(CommandHandler('custom', start_command))
    
    #Message_Handler
    app.add_handler(MessageHandler(filters.TEXT, message_type))
    
    #error_Handler
    app.add_error_handler(error_handler)
    #polling
    print('polling....')
    app.run_polling(poll_interval=3)
