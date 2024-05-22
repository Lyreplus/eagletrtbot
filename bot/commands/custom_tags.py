from telegram import Update
from telegram.ext import CallbackContext, Dispatcher, CommandHandler
from bot.commands.utils.airtable_utils import *


def tag_finder(tag):
    if not airtable_caches_updater():
        return "Mmm, non riesco a scaricare nuovi dati... riprova più tardi..."
    all_people_table_file = open(PEOPLE_TABLE_CACHE_FP)
    all_people_table = json.load(all_people_table_file)
    all_people_table_file.close()
    message = ""
    for person in all_people_table:
        rank = person.get("fields").get("Rank")
        if rank is not None and tag in rank:
            name = person.get("fields").get("@Telegram")
            active = person.get("fields").get("Status")
            if name is not None and active != "✖️ Inattivo":
                if name.startswith("@"):
                    message += name + " "
                else:
                    message += "@" + name + " "
    return message


def team_finder(team):
    if not airtable_caches_updater():
        return "Mmm, non riesco a scaricare nuovi dati... riprova più tardi..."
    all_people_table_file = open(PEOPLE_TABLE_CACHE_FP)
    all_people_table = json.load(all_people_table_file)
    all_people_table_file.close()
    message = ""
    for person in all_people_table:
        rank = person.get("fields").get("Team")
        if rank is not None and team in rank:
            name = person.get("fields").get("@Telegram")
            active = person.get("fields").get("Status")
            if name is not None and active != "✖️ Inattivo":
                if name.startswith("@"):
                    message += name + " "
                else:
                    message += "@" + name + " "
    return message

def custom_tag_ct(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(tag_finder("CT"), quote=True)


def custom_tag_drivers(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(tag_finder("DRIVER"), quote=True)


def custom_tag_pm(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(tag_finder("PM"), quote=True)

    
def custom_tag_hr(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(tag_finder("HR"), quote=True)
    

def custom_tag_sw(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(team_finder("SW"), quote=True)
    

def custom_tag_hw(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(team_finder("HW"), quote=True)

    
def custom_tag_cm(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(team_finder("CM"), quote=True)


def custom_tag_mgt(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(team_finder("MGT"), quote=True)
    

def custom_tag_mt(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(team_finder("MT"), quote=True)

    
def custom_tag_dmt(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(team_finder("DMT"), quote=True)



