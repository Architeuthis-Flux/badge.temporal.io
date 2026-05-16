#include <stdlib.h>
#include <cstring>

#include "../../boops/BadgeBoops.h"
#include "../../identity/BadgeInfo.h"
#include "../../identity/BadgeUID.h"

#include "temporalbadge_runtime.h"

// ── Badge identity / boops ──────────────────────────────────────────────────

extern "C" const char *temporalbadge_runtime_my_uuid(void)
{
    return uid_hex;
}

namespace {
char *s_boops_cache = nullptr;
}

extern "C" const char *temporalbadge_runtime_boops(void)
{
    if (s_boops_cache)
    {
        free(s_boops_cache);
        s_boops_cache = nullptr;
    }
    size_t len = 0;
    s_boops_cache = BadgeBoops::readJson(&len);
    if (!s_boops_cache)
    {
        return "{\"pairings\":[]}";
    }
    return s_boops_cache;
}

extern "C" int temporalbadge_runtime_contact_get(const char *key,
                                                  char *buf,
                                                  size_t buf_cap)
{
    if (!key || !buf || buf_cap == 0)
    {
        return -1;
    }
    BadgeInfo::Fields info;
    BadgeInfo::getCurrent(info);

    const char *value = nullptr;
    if (strcmp(key, "name") == 0) value = info.name;
    else if (strcmp(key, "title") == 0) value = info.title;
    else if (strcmp(key, "company") == 0) value = info.company;
    else if (strcmp(key, "email") == 0) value = info.email;
    else if (strcmp(key, "website") == 0) value = info.website;
    else return -1;

    const size_t len = strlen(value);
    const size_t n = (len < buf_cap - 1) ? len : buf_cap - 1;
    memcpy(buf, value, n);
    buf[n] = '\0';
    return (int)n;
}

extern "C" int temporalbadge_runtime_contact_set(const char *key,
                                                  const char *value)
{
    if (!key || !value)
    {
        return -1;
    }

    BadgeInfo::Fields info;
    BadgeInfo::getCurrent(info);

    auto copy = [](char *dst, size_t cap, const char *src) {
        if (!dst || cap == 0) return;
        if (!src) src = "";
        strncpy(dst, src, cap - 1);
        dst[cap - 1] = '\0';
    };

    if (strcmp(key, "name") == 0) copy(info.name, sizeof(info.name), value);
    else if (strcmp(key, "title") == 0) copy(info.title, sizeof(info.title), value);
    else if (strcmp(key, "company") == 0) copy(info.company, sizeof(info.company), value);
    else if (strcmp(key, "email") == 0) copy(info.email, sizeof(info.email), value);
    else if (strcmp(key, "website") == 0) copy(info.website, sizeof(info.website), value);
    else return -1;

    if (!BadgeInfo::saveToFile(info))
    {
        return -1;
    }
    BadgeInfo::applyToGlobals(info);
    return 0;
}
