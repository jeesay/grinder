#!/bin/bash

csplit -z pipeline_jobs.cpp -f relionjob_ /void\ RelionJob\:\:initialise/ '{*}'

