# Python Project Starter

## HowTo

Install dependencies and set up the virtual environment:

```bash
./ci/scripts/install_deps.sh
```

Start qPusher with a command like this:

```bash
qPusher \
--APP_TOKEN <app_token> \
--USER_KEY <user_key> \
--BEGIN 9 \
--END 19 \
--PERIOD 1 \
--QUESTIONS_DIR question_catalogue/BKA
```

User key and app token can be obtained from the your PushIT mobile app account.

---
