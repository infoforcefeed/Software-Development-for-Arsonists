#!/usr/bin/env bash

rsync -PazL built/* quinlan@infoforcefeed.org:/var/www/arson/
