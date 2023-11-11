from aiogram import Router, types
from utils import telegram, inline_queries
from loader import db

router = Router()


@router.inline_query()
async def search_limit(inline_query: types.InlineQuery):
    current_offset = inline_query.offset if inline_query.offset else 0
    result = await telegram.telegram_parser(inline_query.query)
    if len(result) == len(await db.get_ads_chats()):
        await inline_query.answer(result, cache_time=0)
    else:
        await inline_query.answer(
            **inline_queries.paginate_inline_results(results=result, current_offset=current_offset)
        )
