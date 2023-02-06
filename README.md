# Python Project Starter

## HowTo

Install dependencies and set up the virtual environment:

```bash
./ci/scripts/install_deps.sh
```

Start qPusher with a command like this:

```bash
qPusher \
  --APP_TOKEN $APP_TOKEN \
  --USER_KEY $USER_KEY \
  --BEGIN 9 \
  --END 19 \
  --PERIOD 1 \
  --QUESTIONS_DIR question_catalogue/BKA
```

User key and app token can be obtained from the your PushIT mobile app account.

---
