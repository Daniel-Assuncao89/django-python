import re

url = input("URL: ").strip()
# url_base = "https://twitter.com/"
# username = url.replace(url_base, "")
# username = url.removeprefix(url_base)
# -------------------------------------
# re.sub(pattern, repl, string, count=0, flags=0)
# username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
# print(f"Username: {username}")

if matches := re.search(r"^https?://(?:www\.)?twitter\.com/(\w+)$", url, re.IGNORECASE):
    print(f"Username:", matches.group(1))
