import requests
from asgiref.sync import sync_to_async
from bs4 import BeautifulSoup
from data.config import TELEGRAM_API_BASE_URL
from aiogram.types import InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.enums.parse_mode import ParseMode
from loader import bot, db


async def telegram_parser(query: str):
    if query:
        response = requests.get(TELEGRAM_API_BASE_URL)
        soup = BeautifulSoup(response.content, 'html.parser')
        h4_elements = soup.find_all("h4")
        result = []
        for index, element in enumerate(h4_elements, start=1):
            has_method = await db.get_method_by_name(element.text)
            if query.lower() in element.text.lower() and has_method:
                result.append(
                    InlineQueryResultArticle(
                        id=str(index),
                        title=element.text,
                        input_message_content=InputTextMessageContent(
                            message_text=await get_message_text(element),
                            parse_mode=ParseMode.HTML,
                            disable_web_page_preview=True,
                        ),
                        description=element.find_next("p").text,
                        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                            [InlineKeyboardButton(text=str(element.text),
                                                  url=f"{TELEGRAM_API_BASE_URL}#{element.text.lower()}")]
                        ])
                    )
                )
        return result
    else:
        ads_result = []
        for ad in await db.get_ads_chats():
            chat_data = await bot.get_chat(ad.chat_id)
            ads_result.append(
                InlineQueryResultArticle(
                    id=str(chat_data.id),
                    title=str(chat_data.title),
                    input_message_content=InputTextMessageContent(
                        message_text=str(chat_data.invite_link),
                    ),
                    description=ad.description if ad.description else chat_data.description,
                )
            )
        return ads_result


async def get_message_text(element: BeautifulSoup):
    method = await db.get_method_by_name(element.text)
    if await sync_to_async(method.first)():
        fields = await db.get_fields_by_method(method.get("id"))
        fields = [field.get("name") for field in fields]
        content = f"{element.text}:\n\n"
        table = element.find_next("table")
        tbody = table.find("tbody")
        trs = tbody.find_all("tr")
        for index, tr in enumerate(trs, start=1):
            tags = tr.find_all("td")
            if str(tags[0])[4:-5] in fields:
                for tag in tags:
                    img_tags = tag.find_all("img")
                    for img_tag in img_tags:
                        alt_value = img_tag['alt']
                        img_tag.replace_with(alt_value)
                    code_tags = tag.find_all("code")
                    for code_tag in code_tags:
                        c_tag = str(code_tag.text).replace("<", "").replace(">", "")
                        code_tag.replace_with(c_tag)
                content += f"{index}. {' - '.join(tag.text for tag in tags)}\n"
        return content
    return f"<a href='{TELEGRAM_API_BASE_URL}#{element.text.lower()}'>{element.text}</a>"
