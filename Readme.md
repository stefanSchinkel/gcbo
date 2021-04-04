# GCBO
[![Build Status](https://travis-ci.org/stefanSchinkel/gcbo.svg?branch=master)](https://travis-ci.org/stefanSchinkel/gcbo)

## About

gcbo (short for **g**it **c**lone **b**ranch **o**nly) is a small CLI tool to selectively clone a single branch from a git repository. I wanted it to be standalone and vanilla (ie not require any `pip install xyz` or so, even though [simple-term-menu](https://pypi.org/project/simple-term-menu/) is super nice). The name was chosen as it kinda resembles zsh shortcuts (such as `dco` for `docker-compose`)

So actually this is just a lot of boiler plate around 
```sh
git clone, -b, ${BRANCH}, --single-branch, ${REPO}, ${TARGET_DIR}
```
but it comes in handy as you don't have to remember how the branch was called, which I never do in particular as things like Jira decide on the full name of the branch and you'd have to update refs and search them first. To make matters even worse some (or at least I) have dozens of repos at github, gitlab, bitbucket, some private VCS instance and nearly as many ssh keys to use. I simply cannot be bothered to remember URLs, keypaths and the like. 

## Why

I am a big proponent of reviewing PRs on a clean slate. For small projects just changing the branch (as in `git checkout feature_123`) works well, but  larger projects often have multiple configs and/or some files not in VCS (think access key, .env files). Just changing to the branch to review and running (int) test might fail due to changes you overlooked or configs that are outdated or unexpectedly present. Even worse, the test may **pass** on the local machine but fail in CI  :scream_cat: (or even worse, production :scream_cat: :scream_cat: :scream_cat:).

## How
Just save [the main file](./gcbo) somewhere handy (`~/bin/gcbo` comes to mind) and save the [sample config](./.gcbo.json.sample) as `~/.gcbo.json` [be sure to mind the dot](https://xkcd.com/559/). Then you either `chmod u+x /path/to/gcbo` and run it,  or call it as  `python3 /path/to/gcbo`. The sample sets up to public git repos for you to try. 

In case you're trusting me<sup>[2](#myfootnote2)</sup> you can also just paste this in your Terminal. 
```sh
curl https://raw.githubusercontent.com/stefanSchinkel/gcbo/master/gcbo -o ~/bin/gcbo
curl https://raw.githubusercontent.com/stefanSchinkel/gcbo/master/.gcbo.json.sample -o ~/.gcbo.json
chmod u+x ~/bin/gcbo
```

## Requirements

Next to none:

 - python3.6+<sup>[2](#myfootnote2)</sup> on a *nix system 
 - git 

## Data structures

Only one to keep track of the repos locate in `${HOME}/.gcbo.json`. See [the sample file](./.gcbo.json.sample) that is rather self-explanatory (keys are ignored for now.)

## Todo
Things that need to be done, not necessarily in order

- [x] repo per arg
- [x] save repo passed per arg
- [ ] add repo when no config and none given as arg
- [x] sighandler for <kbd>Ctrl</kbd>+<kbd>c</kbd>
- [ ] "Go back" in menus
- [ ] honour ssh key 
- [ ] pass ssh key via -i option

<hr />
<a name="footnote1"><sup>1</sup></a>: But maybe you shouldn't trust stangers on the internet. 
<a name="footnote2"><sup>2<sup></a>: If you ask nicely, I might drop f-strings to support older python 3 versions too. 
