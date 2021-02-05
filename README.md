# No Join Bot

![NoJoin-Bot](https://socialify.git.ci/arnabsen1729/NoJoin-Bot/image?description=1&descriptionEditable=A%20simple%20telegram%20bot%20to%20get%20rid%20of%20annoying%20join%20messages&font=Raleway&forks=1&issues=1&language=1&owner=1&pattern=Overlapping%20Hexagons&pulls=1&stargazers=1&theme=Dark)

## Deploy in heroku

You can simply deploy to heroku with this Heroku Deploy button

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/arnabsen1729/NoJoin-Bot)

Or follow these steps:

- Login to heroku using `heroku login`
- Create a new application `heroku create`
- Make sure the procfile exists
- Push the contents to heroku `git push heroku master`
- Now move to the heroku dashboard and under settings > config vars; add the BOT_API_KEY
- Also make sure the worker is on
- For debugging purpose you can `heroku run python3 main.py` and `heroku logs`


## Future Scope

- [ ] Add menu option to enable and disable deletion of join messages
- [ ] Do the same for removal of members
- [ ] Make a clear option that will clear all the previous join messages


> To contribute, make an issue, fork the repo and make changes to a separate branch and make a PR. Thanks for your contribution
