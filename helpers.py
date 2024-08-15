from datetime import datetime, timedelta, timezone


def convert_datetime_str_to_utc(datetime_str):
    decimal_index = datetime_str.find(".")
    if decimal_index != -1:
        # Ensure only 3 digits after the decimal point for milliseconds
        datetime_str = datetime_str[: decimal_index + 4]

    return datetime.fromisoformat(datetime_str).replace(tzinfo=timezone.utc)


def format_duration(seconds):
    message = ""
    duration_td = timedelta(seconds=seconds)
    days, day_remainder = divmod(duration_td.total_seconds(), 86400)
    hours, remainder = divmod(day_remainder, 3600)
    minutes, seconds = divmod(remainder, 60)

    if days:
        message = f"{int(days)} hari "

    if hours:
        message = message + f"{int(hours)} jam "

    if minutes:
        message = message + f"{int(minutes)} menit "

    if seconds:
        message = message + f"{int(seconds)} detik"
    return message


def remove_query_id_from_tg_web_data(tg_web_data):
    data_to_be_splitted = tg_web_data
    splitted_original_data = data_to_be_splitted.split("&")
    return "&".join(splitted_original_data[1:])


def mapping_role_color(role):
    if role == "admin":
        role = f"<lg>{role}</lg>"
    elif role == "premium":
        role = f"<lc>{role}</lc>"

    return role


def populate_not_started_tasks(tasks: list):
    not_started_tasks = []
    for task in tasks:
        if task.get("title") == "Promo":
            continue
        sub_tasks = task.get("tasks")
        for sub_task in sub_tasks:
            if (
                sub_task.get("status") == "NOT_STARTED"
                and sub_task.get("socialSubscription", {}).get("openInTelegram") is not True
                and sub_task.get("isHidden") is not True
            ):
                temp_task = {
                    "task_id": sub_task.get("id"),
                    "task_title": sub_task.get('title'),
                }
                not_started_tasks.append(temp_task)
    return not_started_tasks


def populate_not_claimed_tasks(tasks: list):
    not_claimed_tasks = []
    for task in tasks:
        if task.get("title") == "Promo":
            continue
        sub_tasks = task.get("tasks")
        for sub_task in sub_tasks:
            if sub_task.get("status") == "READY_FOR_CLAIM":
                temp_task = {
                    "task_id": sub_task.get("id"),
                    "task_title": sub_task.get('title'),
                }
                not_claimed_tasks.append(temp_task)
    return not_claimed_tasks
