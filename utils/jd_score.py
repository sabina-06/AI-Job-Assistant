from utils.skills import skill_list


def jd_score(matched, missing):

    total = len(matched) + len(missing)

    if total == 0:
        return 0

    return round((len(matched) / total) * 100, 2)
