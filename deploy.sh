#!/usr/bin/env bash

rsync -PazL built/* ${USER}@infoforcefeed.org:/var/www/arson/
