def paginate_inline_results(results, current_offset):
    offset = int(current_offset)
    max_length = 50
    next_offset = ''

    if not offset:
        if len(results) > max_length:
            next_offset = max_length
            results = results[:max_length]
    elif len(results) > offset:
        if len(results) > offset + max_length:
            next_offset = offset + max_length
        results = results[offset:offset + max_length]

    return {
        "results": results,
        "next_offset": str(next_offset),
        "cache_time": 10
    }
