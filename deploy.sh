#!/usr/bin/env bash

rsync -PazL static infoforcefeed.org:/var/www/arson.infoforcefeed.org/
rsync -PazL built/* infoforcefeed.org:/var/www/arson.infoforcefeed.org/
